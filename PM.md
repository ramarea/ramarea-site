# ramarea.com — Migration Product Management Doc

*A living document tracking the migration and build of ramarea.com — what was decided, what was built, and what comes next.*

**Project:** Migration from Google Sites (`sites.google.com/view/ramarea`) to a custom static site at `ramarea.com`, hosted on GitHub Pages.  
**Status:** In Progress  
**Last updated:** July 2026

---

## Objective

Replace the Google Sites presence with a fully custom-coded, self-owned personal site — improving design control, performance, SEO, and long-term portability — while preserving all existing content.

---

## Principles

- Content fidelity: all migrated content reproduces the original source accurately, without paraphrasing
- Static HTML only: no build system, no JS framework, no CMS dependency
- Git as source of truth: all changes tracked in version control and reviewed before being applied
- Owner-led: the site owner reviews and approves all changes and handles all publishing

---

## Architecture

```
ramarea.com/
├── live/          Stories, blog, values, travel, community, my story
│   ├── blog/      70 posts (2018–2024)
│   ├── my-story/
│   ├── community/ Gratitude wall, memorial wall, resources
│   ├── values-and-pillars/
│   └── travel/
├── play/          Creative work
│   ├── write/     11 poems and short stories
│   ├── show/      Photography galleries
│   └── do/        Music, dance, cooking, performing arts, speaking
├── work/          Professional
│   ├── portfolio/
│   ├── education/
│   ├── entrepreneurship/
│   └── social-responsibility/
└── connect/       Social links + community card
```

**Fonts:** Cormorant Garamond (serif/display) + Inter (sans), loaded async from Google Fonts  
**Images:** All assets in WebP format (converted from PNG/JPG originals)

---

## Site Stats (as of July 2026)

| Metric | Value |
|---|---|
| Total HTML pages | 140 |
| Blog posts | 70 |
| Poetry / writing pages | 11 |
| WebP images | 167 |
| Image assets size | 23.1 MB (down from 74.9 MB) |

---

## Milestones

### ✅ Phase 1 — Foundation (June 2026)
- Custom domain `ramarea.com` live on GitHub Pages
- Homepage with hero, bio, section cards, footer
- Section hubs: Live, Play, Work
- CNAME, robots.txt, sitemap.xml

### ✅ Phase 2 — Content Migration (June–July 2026)
- 70 blog posts migrated from Google Sites
- 11 poetry / writing pages
- Photography galleries (show/)
- Work sub-pages: portfolio, education, entrepreneurship, social responsibility
- Community pages: gratitude wall, memorial wall, resources
- Travel section structure
- My Story page — long-form autobiographical page with verbatim text, photo grid placeholders, Life in Decades card tiles
- Connect page — social links (LinkedIn, Facebook, X, YouTube, TikTok, PoemHunter) + community card

### ✅ Phase 3 — Polish & Performance (July 2026)
- All images converted to WebP (70% file size reduction, 51.7 MB saved)
- Non-blocking Google Fonts (media="print" async pattern + preconnect)
- Hero image preloaded
- `<main>` landmark on homepage
- Footer contrast fix for accessibility
- Announcement bar: Edge Model FIFA World Cup 2026 results (26/32, 81%)

### ✅ Phase 4 — SEO Foundation (July 2026)
- Canonical tags: double-slash bug fixed on hub pages, 52 new canonical tags added (full coverage across 140 pages)
- Open Graph + Twitter Card meta tags on all 140 pages
- Meta descriptions: added to connect, my-story, portfolio; CSV maintained for all pages
- Person schema: `sameAs` added linking all social profiles
- `index.html` back-links cleaned up
- Version control hygiene: `.gitignore` established for local working files and archived assets

---

## In Progress

- **Inner page performance:** non-blocking font loading, `<main>` landmark, and footer contrast fix applied to homepage only — needs to propagate to inner page templates
- **around-the-grapevine:** `/live/my-story/around-the-grapevine/` exists as a placeholder; content not yet built

---

## Backlog

### Content migration — stub pages (24 pages)

These pages exist in the site structure and are linked from nav/section hubs, but contain placeholder body text sourced from the original Google Sites. Each needs its content replaced with the real content from the source.

**Live**

| Page | Path |
|---|---|
| Community hub | `live/community/` |
| Memorial Wall | `live/community/memorial-wall/` |
| Resources | `live/community/resources/` |
| News About Ramarea | `live/my-story/around-the-grapevine/` |
| Travel: Inbound | `live/travel/inbound/` |
| Travel: Places | `live/travel/places/` |
| Travel Blog | `live/travel/travel-blog/` |

**Play**

| Page | Path |
|---|---|
| Cooking | `play/do/cooking/` |
| Dance | `play/do/dance/` |
| Moremogolo | `play/do/moremogolo/` |
| Music | `play/do/music/` |

**Work**

| Page | Path |
|---|---|
| Stanford | `work/education/stanford/` |
| UWC Costa Rica | `work/education/uwc-costa-rica/` |
| Dryve Africa | `work/entrepreneurship/dryve-africa/` |
| Group Food Committee | `work/entrepreneurship/group-food-committee/` |
| Halidon Committee | `work/entrepreneurship/halidon-committee/` |
| RamCash Corporation | `work/entrepreneurship/ramcash-corporation/` |
| CRIMUN Leadership Network | `work/social-responsibility/costa-rican-international-model-united-nations-leadership-network/` |
| Mastercard Foundation Scholars Program | `work/social-responsibility/mastercard-foundation-scholars-program/` |
| Organic Naturals Skincare | `work/social-responsibility/organic-naturals-skincare/` |
| Stanford SEED Internship Program | `work/social-responsibility/stanford-seed-internship-program/` |
| Stars Revealed | `work/social-responsibility/stars-revealed/` |
| The Voice of Africa Botswana | `work/social-responsibility/the-voice-of-africa-botswana/` |
| United World Colleges | `work/social-responsibility/united-world-colleges/` |

### Other backlog items

| Item | Notes |
|---|---|
| `/live/my-story/` images | Replace ~57 photo placeholder divs with real images once assets are available |
| `/live/values-and-pillars/` | Page exists; content not yet migrated |
| Alt text pass | Add descriptive alt text to all `<img>` tags once photo placeholders are replaced with real images. My Story (~40 images) and play/show galleries are priority. Portfolio already has alt text — use as standard. |
| Inner page templates: non-blocking fonts | Apply `media="print"` async font pattern to all inner pages |
| Inner page templates: `<main>` landmark | Apply to all inner pages for accessibility |
| Inner page templates: footer contrast | Apply `color:#7a6d8e` fix to all inner pages |
| Meta descriptions for remaining pages | ~52 pages currently use fallback site description for OG tags; write per-page descriptions for high-traffic pages |
| Blog: resume publishing | Last post August 2024; even occasional posts improve crawl frequency |

---

## Off-Site Actions (owner)

- Add `ramarea.com` link to LinkedIn Featured section
- Add personal site link to Stanford profile
- Update any guest interview bio links (e.g. avthar.com) to point to ramarea.com
- These directly improve name-search ranking for "Tumisang Ramarea" / "Tumisang Ikefuna-Ramarea"

---

## Technical Decisions Log

| Decision | Rationale |
|---|---|
| Static HTML, no build system | Simplicity, portability, no build toolchain to maintain |
| GitHub Pages | Free hosting, git-native, custom domain support |
| WebP for all images | 70% average size reduction vs PNG/JPG originals |
| Non-blocking Google Fonts | Eliminates render-blocking resource; PageSpeed desktop 99, mobile 92 |
| `display=swap` + preconnect | Prevents invisible text during font load |
| `og:image` defaults to homepage hero | Consistent brand image for social previews until per-page images are set |
| Name standard: "Tumisang Ikefuna-Ramarea" for new content | Legacy content ("Tumisang Ramarea") preserved as-is; new copy uses full name |
| Owner handles all git operations | No automated commits or pushes from tooling |

## Standards & Conventions

| Convention | Detail |
|---|---|
| Name — legacy content | "Tumisang Ramarea" — preserved as-is across existing blog posts and previously published copy |
| Name — new content | "Tumisang Ikefuna-Ramarea" — used in all new meta descriptions, schema data, and site copy |
| Source of truth for titles & descriptions | `meta_descriptions.csv` in the project root |

---

## Design System

| Token | Value | Usage |
|---|---|---|
| `--purple-deep` | `#1a0a2e` | Page background, nav, announcement bar |
| `--purple-mid` | `#2d1254` | Section backgrounds, hero gradients |
| `--purple-light` | `#4a1f8c` | Accent gradients |
| `--gold` | `#c9a84c` | Primary brand accent, CTAs, borders |
| `--gold-light` | `#e8c96a` | Hover states |
| `--white` | `#f5f0ea` | Body text, headings |
| `--text-muted` | `#b8a9c9` | Secondary text, subtitles |
