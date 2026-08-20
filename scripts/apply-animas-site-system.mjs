#!/usr/bin/env node

import { readdir, readFile, writeFile } from "node:fs/promises";
import { fileURLToPath } from "node:url";
import path from "node:path";

const SCRIPT_DIR = path.dirname(fileURLToPath(import.meta.url));
const ROOT = path.resolve(SCRIPT_DIR, "..");
const SHARED_STYLESHEET = "/assets/animas-site.css?v=20260819c";
const ROOT_PAGES = [
  "index.html",
  "case-studies.html",
  "chartstead.html",
  "how-it-works.html",
  "masthead.html",
  "pip.html",
  "resume.html",
  "solutions.html",
  "tools.html",
];

function familyFor(relativePath) {
  if (relativePath === "index.html") return "animas-home";
  if (relativePath === "resume.html") return "animas-resume";
  if (["chartstead.html", "masthead.html", "pip.html"].includes(relativePath)) return "animas-product";
  if (relativePath === "blog/index.html") return "animas-blog-index";
  if (relativePath.startsWith("blog/")) return "animas-article";
  return "animas-page";
}

function transformUtilityToken(token) {
  const parts = token.split(":");
  let base = parts.pop();
  const prefix = parts.length ? `${parts.join(":")}:` : "";

  if (
    base === "rounded" ||
    base.startsWith("rounded-") ||
    base === "shadow" ||
    base.startsWith("shadow-") ||
    base.includes("gradient") ||
    base.startsWith("bg-gradient-") ||
    base.startsWith("from-") ||
    base.startsWith("via-") ||
    base.startsWith("to-")
  ) {
    return "";
  }

  const accent = base.match(/^(text|bg|border)-(amber|teal|emerald|rose|cyan)-(\d{2,3})(\/\d+)?$/);
  if (accent) {
    const [, property, , shade, alpha = ""] = accent;
    if (property === "text") base = `text-brand-600${alpha}`;
    if (property === "border") base = `border-brand-200${alpha}`;
    if (property === "bg") base = `bg-brand-${Number(shade) <= 100 ? shade : "600"}${alpha}`;
  }

  if (/^bg-\[#(?:dfe8d7|f4f1e8|e8eef2)\]$/i.test(base)) {
    base = "bg-[#edf4f6]";
  }

  return `${prefix}${base}`;
}

function transformClasses(source) {
  return source.replace(/class="([^"]*)"/g, (_match, value) => {
    const tokens = value
      .split(/\s+/)
      .filter(Boolean)
      .map(transformUtilityToken)
      .filter(Boolean);
    return `class="${tokens.join(" ")}"`;
  });
}

function addShellClasses(source, family) {
  return source.replace(/<body class="([^"]*)">/, (_match, value) => {
    const tokens = new Set(value.split(/\s+/).filter(Boolean));
    tokens.add("animas-site");
    tokens.add(family);
    return `<body class="${[...tokens].join(" ")}">`;
  });
}

function addSharedStylesheet(source) {
  if (/href="\/assets\/animas-site\.css(?:\?[^\"]*)?"/.test(source)) {
    return source.replace(
      /href="\/assets\/animas-site\.css(?:\?[^\"]*)?"/,
      `href="${SHARED_STYLESHEET}"`,
    );
  }
  return source.replace(
    /\n<\/head>/,
    `\n    <link rel="stylesheet" href="${SHARED_STYLESHEET}">\n</head>`,
  );
}

function addMonoFont(source) {
  if (source.includes("family=JetBrains+Mono")) return source;
  return source.replace(
    /(&family=Inter:wght@400;500;600)(?=&display=swap)/,
    "$1&family=JetBrains+Mono:wght@500;600",
  );
}

async function transformPage(relativePath) {
  const absolutePath = path.join(ROOT, relativePath);
  const original = await readFile(absolutePath, "utf8");
  let updated = transformClasses(original);
  updated = addShellClasses(updated, familyFor(relativePath));
  updated = addMonoFont(updated);
  updated = addSharedStylesheet(updated);
  if (updated !== original) await writeFile(absolutePath, updated, "utf8");
  process.stdout.write(`${relativePath}\n`);
}

const blogPages = (await readdir(path.join(ROOT, "blog")))
  .filter((name) => name.endsWith(".html"))
  .sort()
  .map((name) => `blog/${name}`);

for (const relativePath of [...ROOT_PAGES, ...blogPages]) {
  await transformPage(relativePath);
}
