#!/usr/bin/env node
/**
 * Renders cover-letter.html -> Abir_Hilal_Khan_Cover_Letter.pdf (A4),
 * verifies it fits ONE page, and counts unfilled «placeholders».
 *
 * Logos are optional. Any <img> in .logos whose file is missing is
 * removed before render, and the strip is hidden if none survive, so
 * the letterhead is correct with two logos, one, or none. Drop
 * assets/logo-nova.png and/or assets/logo-allianz.png in and rerun.
 *
 *   node build-letter.mjs          build + check
 *   node build-letter.mjs --png    also write a preview PNG
 */

import { chromium } from 'playwright';
import { pathToFileURL } from 'node:url';
import { existsSync } from 'node:fs';
import path from 'node:path';

const ROOT    = path.dirname(new URL(import.meta.url).pathname);
const SRC     = path.join(ROOT, 'cover-letter.html');
const PDF_OUT = path.join(ROOT, 'Abir_Hilal_Khan_Cover_Letter.pdf');
const PNG_OUT = path.join(ROOT, 'preview-letter.png');

const A4_H_MM   = 297;
const MM_PER_PX = 25.4 / 96;

const wantPng = process.argv.includes('--png');

const browser = await chromium.launch();
const page = await browser.newPage({
  viewport: { width: 794, height: 1123 },
  deviceScaleFactor: 2,
});

await page.goto(pathToFileURL(SRC).href, { waitUntil: 'load' });

/* ---- drop logo <img>s whose file is not on disk -------------------- */
const wanted = await page.$$eval('.logos img', els => els.map(e => e.getAttribute('src')));
const missing = wanted.filter(src => !existsSync(path.join(ROOT, src)));
const present = wanted.filter(src => existsSync(path.join(ROOT, src)));

await page.evaluate((missingSrcs) => {
  for (const src of missingSrcs) {
    const el = document.querySelector(`.logos img[src="${src}"]`);
    if (el) el.remove();
  }
  const strip = document.querySelector('.logos');
  if (strip && strip.querySelectorAll('img').length === 0) strip.remove();
}, missing);

await page.emulateMedia({ media: 'print' });
await page.evaluate(() => document.fonts.ready);
if (present.length) await page.evaluate(() => Promise.all(
  [...document.images].filter(i => !i.complete).map(i => i.decode().catch(() => {}))
));

/* ---- measure natural content height -------------------------------- */
const metrics = await page.evaluate(() => {
  const el = document.querySelector('.page');
  const prev = el.style.minHeight;
  el.style.minHeight = '0';
  void el.offsetHeight;
  const contentPx = el.getBoundingClientRect().height;
  el.style.minHeight = prev;
  void el.offsetHeight;
  const todos = (document.body.innerText.match(/«[^»]*»/g) || []).length;
  const words = document.body.innerText.trim().split(/\s+/).length;
  return { contentPx, todos, words };
});

const contentMm = metrics.contentPx * MM_PER_PX;
const fits      = contentMm <= A4_H_MM + 0.5;
const deltaMm   = Math.abs(contentMm - A4_H_MM);

await page.pdf({
  path: PDF_OUT,
  width: '210mm',
  height: '297mm',
  printBackground: true,
  margin: { top: '0', right: '0', bottom: '0', left: '0' },
});

if (wantPng) {
  await page.emulateMedia({ media: 'screen' });
  const el = await page.$('.page');
  await el.screenshot({ path: PNG_OUT });
}

await browser.close();

/* ---------------------------- report ---------------------------- */
const pad = (s) => String(s).padEnd(15);
console.log('');
console.log(`  ${pad('output')} ${path.relative(process.cwd(), PDF_OUT)}`);
console.log(`  ${pad('content height')} ${contentMm.toFixed(1)} mm  of  ${A4_H_MM} mm (A4)`);
console.log(`  ${pad('words')} ${metrics.words}`);

if (fits) {
  console.log(`  ${pad('one page')} \x1b[32mOK\x1b[0m — ${deltaMm.toFixed(1)} mm headroom left`);
} else {
  console.log(`  ${pad('one page')} \x1b[31mOVERFLOW\x1b[0m — ${deltaMm.toFixed(1)} mm too tall`);
}

console.log(`  ${pad('logos')} ${present.length ? present.map(s => path.basename(s)).join(', ')
                                                : '\x1b[33mnone found\x1b[0m — add assets/logo-nova.png, assets/logo-allianz.png'}`);

if (metrics.todos > 0) {
  console.log(`  ${pad('placeholders')} \x1b[33m${metrics.todos} unfilled\x1b[0m — not ready to send`);
} else {
  console.log(`  ${pad('placeholders')} \x1b[32mnone\x1b[0m`);
}
console.log('');

if (!fits) {
  console.error('Trim content, or reduce --fs-base / --lh in cover-letter.html.');
  process.exit(1);
}
