#!/usr/bin/env node
/**
 * Renders cv.html -> Abir_Khan_CV.pdf (A4) and verifies it fits ONE page.
 * With --src/--out, renders any other page in this repo the same way.
 *
 * The one-page rule is a hard requirement for this application, so it is
 * enforced here rather than eyeballed: the script measures the natural
 * content height, compares it against the A4 box, and exits non-zero with
 * a millimetre-accurate overflow figure when it does not fit.
 *
 *   node build.mjs            build + check
 *   node build.mjs --png      also write a preview PNG for visual QA
 *   node build.mjs --src=cover-letter.html --out=Abir_Khan_Cover_Letter.pdf
 */

import { chromium } from 'playwright';
import { pathToFileURL } from 'node:url';
import { writeFile } from 'node:fs/promises';
import path from 'node:path';

const ROOT = path.dirname(new URL(import.meta.url).pathname);

// Defaults build the CV. --src/--out point the same pipeline at the cover
// letter, which shares the template and so wants the same one-page check.
const arg = (name, fallback) => {
  const hit = process.argv.find((a) => a.startsWith(`--${name}=`));
  return hit ? hit.slice(name.length + 3) : fallback;
};
const SRC     = path.join(ROOT, arg('src', 'cv.html'));
const PDF_OUT = path.join(ROOT, arg('out', 'Abir_Khan_CV.pdf'));
const PNG_OUT = path.join(ROOT, arg('png', 'preview.png'));

const A4_H_MM  = 297;
const MM_PER_PX = 25.4 / 96;          // CSS px -> mm at the 96dpi print base

const wantPng = process.argv.includes('--png');

// Honour a pre-installed Chromium when the pinned Playwright revision is not
// downloadable (sandboxes, offline CI). Falls back to Playwright's own build.
const browser = await chromium.launch(
  process.env.CHROMIUM_PATH ? { executablePath: process.env.CHROMIUM_PATH } : {}
);
const page = await browser.newPage({
  viewport: { width: 794, height: 1123 },   // A4 @96dpi
  deviceScaleFactor: 2,
});

await page.goto(pathToFileURL(SRC).href, { waitUntil: 'load' });
await page.emulateMedia({ media: 'print' });
await page.evaluate(() => document.fonts.ready);

/* ---- measure natural content height (min-height defeats scrollHeight) ---- */
const metrics = await page.evaluate(() => {
  const el = document.querySelector('.page');
  const prev = el.style.minHeight;
  el.style.minHeight = '0';
  void el.offsetHeight;                     // force reflow
  const contentPx = el.getBoundingClientRect().height;
  el.style.minHeight = prev;
  void el.offsetHeight;
  // Placeholders are written as «like this» in the markup; also honour an
  // explicit .todo class. Counting the text is what actually catches an
  // unfilled field, which a class-only check silently misses.
  const guillemets = (document.body.innerText.match(/\u00ab[^\u00bb]*\u00bb/g) || []).length;
  const todos = guillemets + document.querySelectorAll('.todo').length;
  return { contentPx, todos };
});

const contentMm = metrics.contentPx * MM_PER_PX;
const fits      = contentMm <= A4_H_MM + 0.5;   // 0.5mm rounding tolerance
const deltaMm   = Math.abs(contentMm - A4_H_MM);

await page.pdf({
  path: PDF_OUT,
  width: '210mm',          // exact A4. format:'A4' rounds to 210.23 x 297.35mm
  height: '297mm',         // in Chromium, which a print shop can flag.
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

if (fits) {
  console.log(`  ${pad('one page')} \x1b[32mOK\x1b[0m — ${deltaMm.toFixed(1)} mm headroom left`);
} else {
  console.log(`  ${pad('one page')} \x1b[31mOVERFLOW\x1b[0m — ${deltaMm.toFixed(1)} mm too tall`);
}

if (metrics.todos > 0) {
  console.log(`  ${pad('placeholders')} \x1b[33m${metrics.todos} unfilled\x1b[0m — not ready to send`);
} else {
  console.log(`  ${pad('placeholders')} \x1b[32mnone\x1b[0m`);
}
console.log('');

if (!fits) {
  console.error('Trim content, or reduce --fs-base / --lh / section margins in cv.html.');
  process.exit(1);
}
