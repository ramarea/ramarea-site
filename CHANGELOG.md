# CHANGELOG — ramarea.com Migration

All significant changes made during the migration from Google Sites to the custom static site at `ramarea.com`.

---

## [Phase 4 — SEO Foundation] — July 2026

### SEO audit
- Commissioned and reviewed a full SEO audit of ramarea.com; assessed all recommendations against the live site and prioritised action items

### Canonical tags
- Fixed a URL formatting bug causing doubled trailing slashes on the three main hub pages (`/live/`, `/play/`, `/work/`)
- Added canonical tags to 52 pages that had none; site now has full canonical coverage across all 140 pages

### Social sharing
- Added Open Graph and Twitter Card tags to all 140 pages, enabling branded link previews when shared on LinkedIn, X, Facebook, TikTok, and other platforms

### Meta descriptions
- Wrote and added meta descriptions to `/connect/`, `/live/my-story/`, and `/work/portfolio/`

### Structured data
- Updated Person schema on the homepage to include `sameAs` links to all social profiles, strengthening entity recognition for "Tumisang Ikefuna-Ramarea" in search

### Link cleanup
- Fixed "Return to Homepage" links on the three main section hubs to use clean root URLs

### Version control hygiene
- `.gitignore` established to exclude local working files and archived assets from the repository

---

## [Phase 3 — Polish & Performance] — July 2026

### Image optimisation
- Converted all site images to WebP format — 70% reduction in total image weight (51.7 MB saved across 167 images)
- Hero image updated to *my-cup-runneth-over*

### Page performance
- Optimised font loading to eliminate render-blocking resources; preloaded the hero image for faster initial paint
- PageSpeed scores: 99 (desktop) / 92 (mobile)

### Accessibility
- Added semantic landmark structure to the homepage
- Improved footer text contrast to meet WCAG standards

### Announcement bar
- Added a fixed announcement bar highlighting the Edge Model's FIFA World Cup 2026 performance (26/32, 81%), linking to edgemodel.tech
- Mobile-responsive with an abbreviated version of the text on small screens

---

## [Phase 2 — Content Migration] — June–July 2026

### Connect page
- Launched `/connect/` — a dedicated page with links to all social platforms (LinkedIn, Facebook, X, YouTube, TikTok, PoemHunter) and a card linking to the community pages
- Updated the Connect call-to-action across all site pages to point to the new destination

### My Story
- Completed the long-form autobiographical page at `/live/my-story/` with verbatim text from the original source, photo placeholders, and Life in Decades card tiles

### Navigation fix
- Fixed the "Read My Story" homepage button to link directly to `/live/my-story/` rather than via a redirect, improving SEO link equity

### Blog
- 70 blog posts (2018–2024) migrated from Google Sites, each with a cover image and meta description

### Writing
- 11 poetry and short fiction pages migrated under `/play/write/`, including works in English and Setswana

### Photography
- Gallery pages built under `/play/show/` covering doodles, flowers, Kgalagadi, performance photography, headshots, Stanford portraits, fashion shows, and photo shoots

### Work section
- Professional portfolio, education, entrepreneurship, and social responsibility pages built under `/work/`

### Community pages
- Gratitude wall, memorial wall, and resources pages built under `/live/community/`

---

## [Phase 1 — Foundation] — June 2026

### Site setup
- GitHub repository created; GitHub Pages enabled on custom domain `ramarea.com`
- `robots.txt` and `sitemap.xml` established
- Design system defined: colour tokens, type scale (Cormorant Garamond + Inter), and reusable component patterns

### Homepage
- Hero, bio, section cards (Live, Play, Work), connect section, and footer
- Structured data added: WebSite, Person, and BreadcrumbList schemas

### Section hubs
- Live, Play, and Work hub pages built with sub-section navigation cards

### Favicon
- `favicon.ico`, SVG, and PNG variants added
