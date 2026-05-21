# Personal Website — Dr. Liam Ning

Static personal site hosted on GitHub Pages at `https://csningli.github.io` (custom domain: `csningli.com`).

## File Structure

```
.
├── index.html              # Homepage: bio, social links, blog list
├── blogs.json              # Blog metadata registry (loaded by JS)
├── rss.xml                 # RSS 2.0 feed
├── CNAME                   # Custom domain: csningli.com
├── blogs/                  # Individual blog post HTML files
│   └── 20260515-vlm.html
└── .gitignore
```

## How to Add a Blog Post

Adding a post requires **three coordinated changes**:

### 1. Create the blog HTML file

Create `blogs/YYYYMMDD-slug.html`. Use the existing post as a template. The file must include:

- Standard HTML5 document structure
- Same `<style>` block as existing posts (or copy from `blogs/20260515-vlm.html`)
- `<a href="/" class="back">&larr; Back</a>` at the top of `<body>`
- `<h1>` for the post title
- `<div class="date">Month DD, YYYY</div>` for the date
- Body content in `<p>` and `<h2>` elements

### 2. Register the post in `blogs.json`

Append a new object to the JSON array:

```json
{
  "file": "YYYYMMDD-slug",
  "title": "Post Title",
  "date": "YYYY-MM-DD"
}
```

- `file`: basename of the HTML file (without `.html`)
- `title`: displayed in the blog list on the homepage
- `date`: ISO 8601 date; used for sorting (newest first)

### 3. Add an RSS `<item>` in `rss.xml`

Insert a new `<item>` inside `<channel>`, **above** existing items so newest is first:

```xml
<item>
  <title>Post Title</title>
  <link>https://csningli.github.io/blogs/YYYYMMDD-slug.html</link>
  <guid>https://csningli.github.io/blogs/YYYYMMDD-slug.html</guid>
  <pubDate>Day, DD Mon YYYY 00:00:00 GMT</pubDate>
  <description>One-line summary of the post.</description>
</item>
```

Update `<lastBuildDate>` to match the newest post's `pubDate`.

## How to Update Homepage Info

Edit `index.html` directly:

- **Name / title**: change the `<h1>` text (line ~273)
- **Social links**: modify `href` attributes inside the `<nav>` grid. Each link is an `<a class="link-node">` with an inline SVG icon
- **AI directive**: the text in `<p class="directive">` at the bottom of `.wrapper`
- **Page metadata**: update `<title>` and `<meta name="description">` in `<head>`

The blog list is **auto-populated** by JavaScript fetching `blogs.json`, so do not edit it manually.

## Conventions

- Blog filenames: `YYYYMMDD-{slug}.html`, lowercase, kebab-case slug
- Dates in `blogs.json`: `YYYY-MM-DD` (ISO 8601)
- Dates in RSS: `RFC 822` format, e.g. `Fri, 15 May 2026 00:00:00 GMT`
- All posts use the same minimal CSS (defined inline in each HTML file)
- No build step; commit raw HTML/JSON/XML directly
