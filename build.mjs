#!/usr/bin/env node
/**
 * Build: embed party_plan.json (the single source of truth) into the
 * <script id="party-data"> fallback block of index.html.
 *
 * index.html renders from a live fetch() of party_plan.json, but keeps a
 * verbatim embedded copy so the page also works when opened via file://
 * (double-click), where fetch() is blocked by the opaque-origin CORS rule.
 * This script regenerates that copy from the JSON so the two never drift.
 *
 * Usage:  node build.mjs        (or: npm run build)
 * Exit code is non-zero if the JSON is malformed or the block can't be found.
 */
import { readFileSync, writeFileSync } from "node:fs";
import { fileURLToPath } from "node:url";
import { dirname, join } from "node:path";

const root = dirname(fileURLToPath(import.meta.url));
const DATA = join(root, "party_plan.json");
const HTML = join(root, "index.html");
const MARKER = 'id="party-data">';

function fail(msg) {
  console.error("build: " + msg);
  process.exit(1);
}

// 1. Read + validate the data — fail loudly rather than embed broken JSON.
const rawFile = readFileSync(DATA, "utf8").replace(/^﻿/, "").replace(/\s+$/, "");
try {
  JSON.parse(rawFile);
} catch (e) {
  fail("party_plan.json is not valid JSON: " + e.message);
}

// 2. Splice it into the data block, matching index.html's line-ending style
//    so the embedded copy stays byte-for-byte identical to the JSON file.
const html = readFileSync(HTML, "utf8");
const crlf = html.includes("\r\n");
const nl = crlf ? "\r\n" : "\n";
const json = crlf ? rawFile.replace(/\r?\n/g, "\r\n") : rawFile.replace(/\r\n/g, "\n");

const mi = html.indexOf(MARKER); // first hit is the real tag (line ~345), before the escaped one in data_model
if (mi < 0) fail('could not find the <script id="party-data"> block in index.html');
const jsonStart = html.indexOf("{", mi + MARKER.length);
const closeIdx = html.indexOf("</script>", jsonStart); // JSON carries no literal </script>
if (jsonStart < 0 || closeIdx < 0) fail("could not locate the embedded JSON bounds in index.html");

const next = html.slice(0, jsonStart) + json + nl + "    " + html.slice(closeIdx);

if (next === html) {
  console.log("build: index.html already in sync (" + json.length + " data bytes)");
} else {
  writeFileSync(HTML, next);
  console.log("build: embedded party_plan.json → index.html (" + json.length + " data bytes)");
}
