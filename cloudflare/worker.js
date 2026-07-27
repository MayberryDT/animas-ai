const EXACT_REWRITES = new Map([
  ["/calculator", "/calculator/index.html"],
  ["/intake", "/intake/index.html"],
  ["/audit", "/audit/index.html"],
  ["/scorecard", "/scorecard/index.html"],
  ["/resume", "/resume.html"],
]);

const SECURITY_HEADERS = {
  "Content-Security-Policy": "frame-ancestors 'self'",
  "Referrer-Policy": "strict-origin-when-cross-origin",
  "Strict-Transport-Security": "max-age=31536000; includeSubDomains; preload",
  "X-Content-Type-Options": "nosniff",
  "X-Frame-Options": "SAMEORIGIN",
  "X-XSS-Protection": "1; mode=block",
};

function rewritePath(pathname) {
  const exact = EXACT_REWRITES.get(pathname);
  if (exact) return exact;

  if (/^\/blog\/[^/.]+$/.test(pathname)) {
    return `${pathname}.html`;
  }

  return pathname;
}

function withSecurityHeaders(response) {
  const headers = new Headers(response.headers);
  for (const [name, value] of Object.entries(SECURITY_HEADERS)) {
    headers.set(name, value);
  }
  return new Response(response.body, {
    status: response.status,
    statusText: response.statusText,
    headers,
  });
}

export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    const rewrittenPath = rewritePath(url.pathname);

    if (rewrittenPath !== url.pathname) {
      url.pathname = rewrittenPath;
      request = new Request(url, request);
    }

    return withSecurityHeaders(await env.ASSETS.fetch(request));
  },
};
