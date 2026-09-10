// Scrapes title + self-text body from BG3 Reddit posts via old.reddit.com HTML.
// No Playwright needed — old.reddit serves static HTML that curl/fetch can read.
const fs = require("fs");
const path = require("path");
const { execFileSync } = require("child_process");

const DIR = __dirname;
const links = fs.readFileSync(path.join(DIR, "links.txt"), "utf8")
  .split(/\r?\n/).map(l => l.trim()).filter(Boolean);

const UA = "Mozilla/5.0 (X11; Linux x86_64; rv:120.0) Gecko/20100101 Firefox/120.0";

function decode(s) {
  return s
    .replace(/&lt;/g, "<").replace(/&gt;/g, ">")
    .replace(/&quot;/g, '"').replace(/&#39;/g, "'").replace(/&#x200B;/g, "")
    .replace(/&nbsp;/g, " ").replace(/&amp;/g, "&");
}

function htmlToText(html) {
  return decode(
    html
      .replace(/<\/(p|div|li|h[1-6]|blockquote|pre|tr)>/gi, "\n")
      .replace(/<br\s*\/?>/gi, "\n")
      .replace(/<li[^>]*>/gi, "- ")
      .replace(/<[^>]+>/g, "")
  ).replace(/\n{3,}/g, "\n\n").replace(/[ \t]+\n/g, "\n").trim();
}

function fetchHtml(url) {
  return execFileSync("curl", ["-sL", "-A", UA, url], { maxBuffer: 50 * 1024 * 1024 }).toString();
}

const results = [];
for (const url of links) {
  const m = url.match(/reddit\.com\/r\/([^/]+)\/comments\/([^/]+)\/([^/?]*)/);
  const subreddit = m ? m[1] : "";
  const id = m ? m[2] : url;
  const slug = m ? m[3] : id;
  const oldUrl = url.replace(/^https:\/\/www\.reddit\.com/, "https://old.reddit.com");

  let title = "", body = "", author = "", ok = false, note = "";
  try {
    const html = fetchHtml(oldUrl);
    if (/class=theme-beta/.test(html) && html.length < 250000 && !/commentarea/.test(html)) {
      note = "blocked (bot-check page)";
    } else {
      const og = html.match(/<meta property="og:title" content="([^"]*)"/);
      const t = html.match(/<title>([\s\S]*?)<\/title>/);
      title = decode(og ? og[1] : (t ? t[1].replace(/\s*:\s*[^:]*$/, "") : ""));

      const am = html.match(/data-author="([^"]*)"/);
      author = am ? am[1] : "";

      // The post lives between #siteTable and .commentarea. The sidebar (.side)
      // renders earlier in source order, so scope to this window to avoid it.
      const start = html.indexOf('id="siteTable"');
      const end = html.indexOf("commentarea");
      const region = start >= 0 ? html.slice(start, end > start ? end : undefined) : html;
      const bm = region.match(/<div class="usertext-body[^"]*"[^>]*>\s*<div class="md">([\s\S]*?)<\/div>\s*<\/div>/);
      body = bm ? htmlToText(bm[1]) : "";
      ok = !!title;
    }
  } catch (e) {
    note = "error: " + e.message;
  }

  const out = { url, subreddit, id, title, author, body, note };
  const file = path.join(DIR, `${id}_${slug}`.slice(0, 80) + ".json");
  fs.writeFileSync(file, JSON.stringify(out, null, 2), "utf8");
  results.push({ id, ok, len: body.length, title: title.slice(0, 60), note });
  console.log(`${ok ? "OK " : "!! "} ${id}  body=${String(body.length).padStart(5)}  ${title.slice(0, 55)}${note ? "  [" + note + "]" : ""}`);
}

fs.writeFileSync(path.join(DIR, "_summary.json"), JSON.stringify(results, null, 2), "utf8");
console.log(`\nDone: ${results.filter(r => r.ok).length}/${results.length} succeeded.`);
