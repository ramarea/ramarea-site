import os

BASE = "/sessions/sharp-quirky-davinci/mnt/outputs/ramarea-site"

# ── shared pieces ──────────────────────────────────────────────────────────────

CSS = """
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,600;0,700;1,400&family=Inter:wght@300;400;500&display=swap" rel="stylesheet"/>
<style>
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0}
:root{
  --purple-deep:#1a0a2e;--purple-mid:#2d1254;--purple-light:#4a1f8c;
  --gold:#c9a84c;--gold-light:#e8c96a;--white:#f5f0ea;--text-muted:#b8a9c9;
}
html{scroll-behavior:smooth}
body{font-family:'Inter',sans-serif;background:var(--purple-deep);color:var(--white);min-height:100vh}

/* NAV */
nav{position:fixed;top:0;left:0;right:0;z-index:100;display:flex;align-items:center;
  justify-content:space-between;padding:1.25rem 3rem;
  background:rgba(26,10,46,0.92);backdrop-filter:blur(12px);
  border-bottom:1px solid rgba(201,168,76,0.15)}
.nav-logo{font-family:'Cormorant Garamond',serif;font-size:1.5rem;font-weight:700;
  color:var(--gold);letter-spacing:.12em;text-decoration:none}
.nav-links{display:flex;align-items:center;gap:2.5rem;list-style:none}
.nav-links a{font-size:.78rem;font-weight:500;letter-spacing:.18em;text-transform:uppercase;
  color:var(--white);text-decoration:none;opacity:.8;transition:opacity .2s,color .2s}
.nav-links a:hover{opacity:1;color:var(--gold-light)}
.nav-cta{color:var(--purple-deep)!important;background:var(--gold);
  padding:.55rem 1.4rem;border-radius:2px;opacity:1!important;transition:background .2s!important}
.nav-cta:hover{background:var(--gold-light)!important}

/* PAGE HERO */
.page-hero{padding:9rem 3rem 5rem;background:linear-gradient(135deg,var(--purple-mid) 0%,var(--purple-deep) 100%);
  border-bottom:1px solid rgba(201,168,76,0.12)}
.page-eyebrow{font-size:.65rem;letter-spacing:.3em;text-transform:uppercase;color:var(--gold);margin-bottom:1rem}
.page-title{font-family:'Cormorant Garamond',serif;font-size:clamp(2.5rem,6vw,5rem);
  font-weight:700;line-height:1;color:var(--white);margin-bottom:1.25rem}
.page-subtitle{font-size:1.05rem;font-weight:300;line-height:1.7;color:var(--text-muted);max-width:580px}
.page-subtitle em{color:var(--gold-light);font-style:italic}

/* CONTENT */
.content{max-width:1100px;margin:0 auto;padding:5rem 3rem}
.content-narrow{max-width:720px;margin:0 auto;padding:5rem 3rem}
.section-label{font-size:.65rem;letter-spacing:.3em;text-transform:uppercase;color:var(--gold);margin-bottom:1rem}
.gold-rule{width:48px;height:1px;background:var(--gold);opacity:.5;margin-bottom:2rem}
h2.section-heading{font-family:'Cormorant Garamond',serif;font-size:clamp(1.8rem,3vw,2.5rem);
  font-weight:600;color:var(--white);margin-bottom:1.5rem}
h3.sub-heading{font-family:'Cormorant Garamond',serif;font-size:1.5rem;
  font-weight:600;color:var(--gold);margin:2.5rem 0 .75rem}
p.body-text{font-size:.95rem;line-height:1.85;color:var(--text-muted);font-weight:300;margin-bottom:1.25rem}
.body-text a{color:var(--gold);text-decoration:none}
.body-text a:hover{text-decoration:underline}

/* CARDS GRID */
.cards-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(280px,1fr));gap:1.5rem;margin:2.5rem 0}
.card{display:block;border:1px solid rgba(201,168,76,.18);border-radius:4px;
  padding:2rem;text-decoration:none;background:rgba(201,168,76,.03);
  transition:border-color .25s,transform .25s}
.card:hover{border-color:var(--gold);transform:translateY(-3px)}
.card-label{font-size:.6rem;letter-spacing:.25em;text-transform:uppercase;color:var(--gold);margin-bottom:.6rem}
.card-title{font-family:'Cormorant Garamond',serif;font-size:1.4rem;font-weight:600;
  color:var(--white);margin-bottom:.6rem}
.card-desc{font-size:.82rem;line-height:1.6;color:var(--text-muted);font-weight:300}

/* PILLAR CARDS */
.pillars-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(220px,1fr));gap:1.25rem;margin:2.5rem 0}
.pillar{border:1px solid rgba(201,168,76,.2);border-radius:4px;padding:2rem;
  background:rgba(201,168,76,.03);transition:border-color .25s}
.pillar:hover{border-color:var(--gold)}
.pillar-title{font-family:'Cormorant Garamond',serif;font-size:1.3rem;
  font-weight:700;color:var(--gold);margin-bottom:.75rem}
.pillar ul{padding-left:1.2rem;color:var(--text-muted);font-size:.85rem;line-height:1.75;font-weight:300}

/* IMAGE PLACEHOLDER */
.img-placeholder{background:rgba(201,168,76,.06);border:1px dashed rgba(201,168,76,.3);
  border-radius:4px;display:flex;flex-direction:column;align-items:center;justify-content:center;
  padding:3rem 1.5rem;text-align:center;color:var(--text-muted);font-size:.8rem;gap:.5rem;margin:1.5rem 0}
.img-placeholder span{font-size:1.5rem;opacity:.4}

/* PHOTO GRID */
.photo-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(240px,1fr));gap:1rem;margin:2rem 0}
.photo-item .img-placeholder{margin:0;aspect-ratio:4/3}
.photo-caption{font-size:.75rem;color:var(--text-muted);margin-top:.5rem;text-align:center}

/* BACK LINK */
.back-link{display:inline-flex;align-items:center;gap:.6rem;font-size:.72rem;
  letter-spacing:.2em;text-transform:uppercase;color:var(--gold);text-decoration:none;
  border:1px solid rgba(201,168,76,.3);padding:.65rem 1.25rem;border-radius:2px;
  margin-top:3rem;transition:border-color .2s,background .2s}
.back-link:hover{border-color:var(--gold);background:rgba(201,168,76,.08)}

/* QUOTE BLOCK */
.quote-block{border-left:2px solid var(--gold);padding:1.5rem 2rem;margin:2.5rem 0;
  background:rgba(201,168,76,.04)}
.quote-block p{font-family:'Cormorant Garamond',serif;font-size:1.25rem;
  font-style:italic;color:var(--white);line-height:1.6;margin-bottom:.5rem}
.quote-block cite{font-size:.72rem;letter-spacing:.2em;text-transform:uppercase;color:var(--gold)}

/* BTN */
.btn-primary{display:inline-block;font-size:.72rem;font-weight:500;letter-spacing:.2em;
  text-transform:uppercase;color:var(--purple-deep);background:var(--gold);
  padding:.85rem 2rem;border-radius:2px;text-decoration:none;transition:background .2s}
.btn-primary:hover{background:var(--gold-light)}

/* FOOTER */
footer{background:#0f0620;border-top:1px solid rgba(201,168,76,.1);padding:3rem;
  display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:1.5rem}
.footer-brand{font-family:'Cormorant Garamond',serif;font-size:1.2rem;
  font-weight:700;color:var(--gold);letter-spacing:.1em}
.footer-nav{display:flex;gap:2rem;list-style:none}
.footer-nav a{font-size:.7rem;letter-spacing:.2em;text-transform:uppercase;
  color:var(--text-muted);text-decoration:none;transition:color .2s}
.footer-nav a:hover{color:var(--gold)}
.footer-copy{font-size:.7rem;color:var(--text-muted);opacity:.6}

/* RESPONSIVE */
@media(max-width:768px){
  nav{padding:1rem 1.5rem}.nav-links{gap:1.25rem}.nav-cta{display:none}
  .page-hero,.content,.content-narrow{padding-left:1.5rem;padding-right:1.5rem}
  footer{flex-direction:column;align-items:flex-start;padding:2rem 1.5rem}
  .cards-grid{grid-template-columns:1fr}
}
</style>
"""

def nav():
    return """
<nav>
  <a href="/" class="nav-logo">RAMAREA</a>
  <ul class="nav-links">
    <li><a href="/live/">Live</a></li>
    <li><a href="/play/">Play</a></li>
    <li><a href="/work/">Work</a></li>
    <li><a href="/live/community/" class="nav-cta">Connect</a></li>
  </ul>
</nav>"""

def footer():
    return """
<footer>
  <span class="footer-brand">RAMAREA</span>
  <ul class="footer-nav">
    <li><a href="/live/">Live</a></li>
    <li><a href="/play/">Play</a></li>
    <li><a href="/work/">Work</a></li>
  </ul>
  <span class="footer-copy">&copy; 2026 Tumisang Ikefuna-Ramarea</span>
</footer>"""

def page(title, meta_title, body):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width,initial-scale=1.0"/>
<title>{meta_title} — RAMAREA</title>
{CSS}
</head>
<body>
{nav()}
{body}
{footer()}
</body>
</html>"""

def img_ph(label="Image — replace with your photo"):
    return f'<div class="img-placeholder"><span>🖼</span>{label}</div>'

# ── pages ──────────────────────────────────────────────────────────────────────

pages = {}

# ── LIVE ──────────────────────────────────────────────────────────────────────
pages["live/index.html"] = page("Live","Live",f"""
<div class="page-hero">
  <p class="page-eyebrow">Live</p>
  <h1 class="page-title">Learning Important<br>Values Everyday</h1>
  <p class="page-subtitle">Welcome to the &ldquo;LIVE&rdquo; section. An acronym that succinctly summarises the ongoing project that is my life.</p>
</div>
<div class="content">
  <div class="cards-grid">
    <a href="/live/values-and-pillars/" class="card">
      <p class="card-label">01</p>
      <h2 class="card-title">Values &amp; Pillars</h2>
      <p class="card-desc">Five core values — Growth, Ubuntu, Creativity, Curiosity, Excellence — and the four pillars that structure my life.</p>
    </a>
    <a href="/live/blog/" class="card">
      <p class="card-label">02</p>
      <h2 class="card-title">Blog: My 31 Cents</h2>
      <p class="card-desc">Writing is how I ensure I engage with the world and remain an active participant in its conversations.</p>
    </a>
    <a href="/live/my-story/" class="card">
      <p class="card-label">03</p>
      <h2 class="card-title">My Story</h2>
      <p class="card-desc">Celebrating the myth of Tumisang Ramarea — written in the third person to underscore the pseudo-celebrity status I have in my home village.</p>
    </a>
    <a href="/live/community/" class="card">
      <p class="card-label">04</p>
      <h2 class="card-title">My Tribe</h2>
      <p class="card-desc">Ubuntu — I am because you are. This section celebrates the communities and individuals who shaped me.</p>
    </a>
    <a href="/live/travel/" class="card">
      <p class="card-label">05</p>
      <h2 class="card-title">My Travels</h2>
      <p class="card-desc">From the Kalahari to Costa Rica to Stanford and beyond — travel has taught me so much and challenged every value I hold.</p>
    </a>
  </div>
  <a href="/" class="back-link">&larr; Return to Homepage</a>
</div>""")

# ── VALUES & PILLARS ───────────────────────────────────────────────────────────
pages["live/values-and-pillars/index.html"] = page("Values & Pillars","Values & Pillars",f"""
<div class="page-hero">
  <p class="page-eyebrow">Live &rarr; Values &amp; Pillars</p>
  <h1 class="page-title">Values &amp; Pillars</h1>
  <p class="page-subtitle">Over the years I have come to define five core values to govern my life, and four pillars that structure my strategy for living it.</p>
</div>
<div class="content-narrow">
  <p class="section-label">Core Values</p>
  <div class="gold-rule"></div>
  <p class="body-text">After a long and iterative process of introspection, I have come to define 5 values that I live by: <strong style="color:var(--white)">Growth, Ubuntu, Creativity, Curiosity, and Excellence.</strong></p>
  {img_ph("Values mind-map — replace with your image")}

  <p class="section-label" style="margin-top:3rem">Life Pillars</p>
  <div class="gold-rule"></div>
  <p class="body-text">My current strategy towards this life game is organised around 4 essential pillars:</p>
  {img_ph("Pillars diagram — replace with your image")}

  <h2 class="section-heading" style="margin-top:3rem">Guiding Pillars of Ramarea&rsquo;s Life Plan</h2>

  <div class="pillars-grid">
    <div class="pillar">
      <h3 class="pillar-title">Personal Development</h3>
      <ul>
        <li>Lead a healthful life sustained by a nutritious diet, active lifestyle, and sufficient rest.</li>
        <li>Cultivate consciousness through intentional, ongoing reflection.</li>
        <li>Be intentional about learning, especially outside the formal education system.</li>
      </ul>
    </div>
    <div class="pillar">
      <h3 class="pillar-title">Meaningful Communities</h3>
      <ul>
        <li>Develop and sustain meaningful relationships characterised by mutual commitment to spiritual growth.</li>
        <li>Actively advance the marginalised communities to which I have pledged my service.</li>
        <li>Be mindful of the privileges I bring into interactions with others.</li>
      </ul>
    </div>
    <div class="pillar">
      <h3 class="pillar-title">Professional Excellence</h3>
      <ul>
        <li>Pursue work that enables me to help people and organisations make better decisions.</li>
        <li>Continuously equip myself with the skills needed to excel at the work I do.</li>
        <li>Be a man of my word, producing quality work within the shortest time possible.</li>
      </ul>
    </div>
    <div class="pillar">
      <h3 class="pillar-title">Financial Sustainability</h3>
      <ul>
        <li>Have prudent cash flow management — balancing present enjoyment with future security.</li>
        <li>Ethically develop and manage a diversified investment portfolio.</li>
        <li>Commit at least a tenth of after-tax income towards the advancement of marginalised groups.</li>
      </ul>
    </div>
  </div>
  <a href="/live/" class="back-link">&larr; Return to Live</a>
</div>""")

# ── MY STORY ──────────────────────────────────────────────────────────────────
pages["live/my-story/index.html"] = page("My Story","My Story — The Man and The Myth",f"""
<div class="page-hero">
  <p class="page-eyebrow">Live &rarr; My Story</p>
  <h1 class="page-title">The Man &amp;<br>The Myth</h1>
  <p class="page-subtitle">&ldquo;In my 20+ years of working with students, Tumisang is clearly among one the best I have been associated with.&rdquo; &mdash; Brian Cabbab</p>
</div>
<div class="content-narrow">
  <p class="body-text">The world should have known that there was something special about this Tumisang Ramarea kid. This section is dedicated to celebrating that myth — written in the third person to underscore the pseudo-celebrity status he holds in his home village.</p>

  {img_ph("Early life photos — replace with your images")}

  <h3 class="sub-heading">2000 — Learning to Read</h3>
  <p class="body-text">In the year 2000, Ramarea was taught to read, write, and count by one of his older brothers as his first school experience. He continued his academic domination at Mookami Junior Secondary School, where he was the undisputed top student.</p>

  {img_ph("School photos — replace with your images")}

  <h3 class="sub-heading">Senior Secondary — Against the Odds</h3>
  <p class="body-text">Ramarea entered senior secondary school with the odds stacked against him. Having made peace with his fate at Seepapitso, he turned it into his own success story — rising through the ranks to become one of the school&rsquo;s standout students.</p>

  {img_ph("Secondary school photos — replace with your images")}

  <h3 class="sub-heading">UWC &amp; The World</h3>
  <p class="body-text">Failing to get 48 points meant Ramarea&rsquo;s dream of studying abroad had momentarily gone down the drain. But destiny had other plans. He arrived in Costa Rica a month later than his peers, after navigating a difficult visa process, and the journey that followed changed everything.</p>

  {img_ph("UWC Costa Rica photos — replace with your images")}

  <h3 class="sub-heading">Stanford</h3>
  <p class="body-text">Stanford! Never has this young man been in a place filled with so much privilege and so much opportunity. Upon arrival, he was suddenly faced with new identities — and learned to navigate them all with grace.</p>
  <p class="body-text">He spent summers in Sri Lanka studying Community Health, and as he looks forward, he can&rsquo;t help but marvel at the story of the kid from the village who made it this far.</p>

  {img_ph("Stanford photos — replace with your images")}

  <h2 class="section-heading" style="margin-top:3rem">Life in Decades</h2>
  <p class="body-text">If I were to ever follow through on my plans to write my autobiography, I would have the following structure:</p>

  <div class="cards-grid">
    <div class="card">
      <p class="card-label">1994–2000</p>
      <h3 class="card-title">Genesis</h3>
      <p class="card-desc">The very first 6 years — the period I know least about, yet which shaped everything that followed.</p>
    </div>
    <div class="card">
      <p class="card-label">2001–2012</p>
      <h3 class="card-title">Socialisis</h3>
      <p class="card-desc">Childhood into adolescence. The journey from a small village in Botswana into the wider world.</p>
    </div>
    <div class="card">
      <p class="card-label">2013–2020</p>
      <h3 class="card-title">Metamorphosis</h3>
      <p class="card-desc">Transition into adulthood away from home — Costa Rica, Stanford, and everything in between.</p>
    </div>
    <div class="card">
      <p class="card-label">2021–2030</p>
      <h3 class="card-title">Symbiosis</h3>
      <p class="card-desc">I am in the middle of living these years — exploring what it means to give back as much as I have received.</p>
    </div>
  </div>

  <a href="/live/news/" class="btn-primary" style="margin-right:1rem">News About Ramarea</a>
  <a href="/live/" class="back-link" style="margin-top:1rem">&larr; Return to Live</a>
</div>""")

# ── COMMUNITY ─────────────────────────────────────────────────────────────────
pages["live/community/index.html"] = page("Community","My Tribe",f"""
<div class="page-hero">
  <p class="page-eyebrow">Live &rarr; My Tribe</p>
  <h1 class="page-title">Community</h1>
  <p class="page-subtitle">&ldquo;Ubuntu — <em>I am because you are.</em>&rdquo;</p>
</div>
<div class="content">
  <p class="body-text">The secret to the successes I have had thus far in life is in the community of people who have opened doors, offered hands, and believed before I believed in myself. This section of my website celebrates them.</p>

  <div class="cards-grid">
    <a href="/live/community/gratitude-wall/" class="card">
      <p class="card-label">Community</p>
      <h2 class="card-title">Gratitude Wall</h2>
      <p class="card-desc">A non-exhaustive list of people for whom I hold a depth of gratitude — updated continuously.</p>
    </a>
    <a href="/live/community/memorial-wall/" class="card">
      <p class="card-label">Community</p>
      <h2 class="card-title">Memorial Wall</h2>
      <p class="card-desc">Celebrating the lives of those spirits that once touched my life but no longer walk in physical form amongst us.</p>
    </a>
    <a href="/live/community/resources/" class="card">
      <p class="card-label">Community</p>
      <h2 class="card-title">Community Resources</h2>
      <p class="card-desc">A repository of opportunities and resources for the communities I serve — currently under construction.</p>
    </a>
  </div>

  <h2 class="section-heading" style="margin-top:3rem">Bots 57 in Los Angeles</h2>
  <p class="body-text">Over the last few years, I have become something of a community builder for Africans in California. Bringing people together across distance and difference is one of the things I love most.</p>
  <p class="body-text"><a href="https://botswanaindependence.com/usa-celebration-los-angeles-california" target="_blank" rel="noopener">Checkout the Event Page &rarr;</a></p>
  {img_ph("Community event photos — replace with your images")}

  <a href="/live/" class="back-link">&larr; Return to Live</a>
</div>""")

# ── TRAVEL ────────────────────────────────────────────────────────────────────
pages["live/travel/index.html"] = page("Travel","My Travels",f"""
<div class="page-hero">
  <p class="page-eyebrow">Live &rarr; My Travels</p>
  <h1 class="page-title">Travel</h1>
  <p class="page-subtitle">&ldquo;I am not the same, having seen the moon shine on the other side of the world.&rdquo; &mdash; Mary Anne Radmacher</p>
</div>
<div class="content">
  <p class="body-text">I have always loved traveling to new places. They always give one more perspective and expand their capacity to dream. Later in school, I would sign up for every club and travelled the width and breadth of Botswana before eventually the world.</p>

  <h2 class="section-heading">Recent Travels</h2>
  <div class="photo-grid">
    <div class="photo-item">{img_ph("Joshua Tree NP, California — Feb 2025")}<p class="photo-caption">Joshua Tree National Park, California — February 2025</p></div>
    <div class="photo-item">{img_ph("Botswana — Dec 2024")}<p class="photo-caption">Botswana — December 2024</p></div>
    <div class="photo-item">{img_ph("Virginia — Dec 2024")}<p class="photo-caption">Virginia — December 2024</p></div>
    <div class="photo-item">{img_ph("Los Cabos, Mexico — Dec 2024")}<p class="photo-caption">Los Cabos, Mexico — December 2024</p></div>
    <div class="photo-item">{img_ph("SF Bay Area — Oct 2024")}<p class="photo-caption">San Francisco Bay Area — October 2024</p></div>
    <div class="photo-item">{img_ph("Virginia — Aug 2024")}<p class="photo-caption">Virginia — August 2024</p></div>
    <div class="photo-item">{img_ph("Virginia — Apr 2024")}<p class="photo-caption">Virginia — April 2024</p></div>
    <div class="photo-item">{img_ph("SF Bay Area — Jan 2024")}<p class="photo-caption">San Francisco Bay Area — January 2024</p></div>
    <div class="photo-item">{img_ph("Botswana — Dec 2023")}<p class="photo-caption">Botswana — December 2023</p></div>
    <div class="photo-item">{img_ph("Napa Valley — May 2023")}<p class="photo-caption">Napa Valley, California — May 2023</p></div>
    <div class="photo-item">{img_ph("Joshua Tree — Apr 2023")}<p class="photo-caption">Joshua Tree National Park — April 2023</p></div>
  </div>

  <h2 class="section-heading" style="margin-top:3rem">My Travel Stats</h2>
  <p class="body-text">Excluding the countries I have lived in for a non-trivial amount of time (Botswana, the United States, and Costa Rica), I have visited countries across Africa, Europe, Asia, and the Americas.</p>
  <p class="body-text">Excluding my home state of California, I have been to 16 US states: Ohio, Texas, Arizona, New Mexico, Nevada, Virginia, Maryland, New York, Massachusetts, and more.</p>
  {img_ph("World map / travel stats — replace with your image")}

  <div class="cards-grid" style="margin-top:2rem">
    <a href="/live/travel/pre-2023-travels/" class="card">
      <p class="card-label">Archive</p>
      <h3 class="card-title">Travels Before 2023</h3>
      <p class="card-desc">A full record of trips from before 2023.</p>
    </a>
    <a href="/live/travel/pre-2019-travels/" class="card">
      <p class="card-label">Archive</p>
      <h3 class="card-title">Travels Before 2019</h3>
      <p class="card-desc">A full record of trips from before 2019.</p>
    </a>
    <a href="/live/travel/places/" class="card">
      <p class="card-label">Gallery</p>
      <h3 class="card-title">Places Exhibit</h3>
      <p class="card-desc">Photography from places around the world.</p>
    </a>
  </div>

  <a href="/live/" class="back-link">&larr; Return to Live</a>
</div>""")

# ── BLOG ──────────────────────────────────────────────────────────────────────
pages["live/blog/index.html"] = page("Blog","Blog: My 31 Cents",f"""
<div class="page-hero">
  <p class="page-eyebrow">Live &rarr; Blog</p>
  <h1 class="page-title">Blog:<br>My 31 Cents</h1>
  <p class="page-subtitle">As far as I can remember, I have always loved to write and journal. Writing is one way I ensure I engage with the world and remain an active participant in its conversations.</p>
</div>
<div class="content">
  <div class="quote-block">
    <p>Disclaimer: The opinions and positions expressed in any of the blog articles are guaranteed only as of that date. Views may evolve.</p>
  </div>
  <p class="body-text">Blog posts coming soon — replace this section with links to your articles as you migrate them.</p>
  <div class="cards-grid">
    <div class="card">
      <p class="card-label">Article</p>
      <h3 class="card-title">Blog Post Title</h3>
      <p class="card-desc">Add your blog posts here by duplicating this card and linking to each article.</p>
    </div>
  </div>
  <a href="/live/" class="back-link">&larr; Return to Live</a>
</div>""")

# ── PLAY ──────────────────────────────────────────────────────────────────────
pages["play/index.html"] = page("Play","Play",f"""
<div class="page-hero">
  <p class="page-eyebrow">Play</p>
  <h1 class="page-title">Pursuing Leisure<br>for Youthfulness</h1>
  <p class="page-subtitle">&ldquo;The unbearable weight of massive talent&rdquo; is a perfect description of my life. I refuse to contain it — writing, displaying creativity, and doing a lot of fun stuff.</p>
</div>
<div class="content">
  <p class="body-text">I perform in public, embarrass myself with my two left feet, and play with my voice. This section is dedicated to celebrating that.</p>
  <div class="cards-grid">
    <a href="/play/write/" class="card">
      <p class="card-label">01</p>
      <h2 class="card-title">Write</h2>
      <p class="card-desc">Literary pursuits — poetry, short stories, essays, and the full breadth of my storytelling.</p>
    </a>
    <a href="/play/show/" class="card">
      <p class="card-label">02</p>
      <h2 class="card-title">Show</h2>
      <p class="card-desc">Doodles, photography, and photo shoots — a picture is a poem without words.</p>
    </a>
    <a href="/play/do/" class="card">
      <p class="card-label">03</p>
      <h2 class="card-title">Do</h2>
      <p class="card-desc">Dance, performing arts, speaking, music, podcast, and cooking — living this life to the fullest.</p>
    </a>
  </div>
  <a href="/" class="back-link">&larr; Return to Homepage</a>
</div>""")

# ── WRITE ─────────────────────────────────────────────────────────────────────
pages["play/write/index.html"] = page("Write","My Creative Writing",f"""
<div class="page-hero">
  <p class="page-eyebrow">Play &rarr; Write</p>
  <h1 class="page-title">Write</h1>
  <p class="page-subtitle">&ldquo;You can always edit a bad page. You can&rsquo;t edit a blank page.&rdquo; &mdash; Jodi Picoult</p>
</div>
<div class="content">
  <p class="body-text">This section is dedicated to my literary pursuits. I consider myself a storyteller and poet — here you will find a collection of my creative writing.</p>
  <div class="cards-grid">
    <a href="/play/write/and-finally-it-rained-in-california/" class="card">
      <p class="card-label">Essay</p>
      <h3 class="card-title">&hellip;and Finally it Rained in California!</h3>
      <p class="card-desc">A reflection on California, drought, and what it means to wait for relief.</p>
    </a>
    <a href="/play/write/homeless/" class="card">
      <p class="card-label">Story</p>
      <h3 class="card-title">Homeless</h3>
      <p class="card-desc">A piece exploring belonging, displacement, and what home truly means.</p>
    </a>
    <a href="/play/write/a-thousand-lifetimes/" class="card">
      <p class="card-label">Poetry</p>
      <h3 class="card-title">A Thousand Lifetimes</h3>
      <p class="card-desc">Meditations on the many lives one person can live within a single lifetime.</p>
    </a>
    <a href="/play/write/tragic-endings/" class="card">
      <p class="card-label">Story</p>
      <h3 class="card-title">Tragic Endings</h3>
      <p class="card-desc">On the endings that shape us — and what we carry forward from them.</p>
    </a>
    <a href="/play/write/just-talking/" class="card">
      <p class="card-label">Essay</p>
      <h3 class="card-title">Just Talking</h3>
      <p class="card-desc">Conversations with myself — and perhaps with you.</p>
    </a>
    <a href="/play/write/take-off/" class="card">
      <p class="card-label">Poetry</p>
      <h3 class="card-title">Take Off</h3>
      <p class="card-desc">The feeling of departure — airports, dreams, and the courage to leave.</p>
    </a>
    <a href="/play/write/se-ileng-se-a-bo-se-ile/" class="card">
      <p class="card-label">Poetry</p>
      <h3 class="card-title">Se Ileng Se a bo Se Ile</h3>
      <p class="card-desc">A poem in Setswana about what was and what remains.</p>
    </a>
    <a href="/play/write/lehuma-leswe/" class="card">
      <p class="card-label">Essay</p>
      <h3 class="card-title">Lehuma Leswe</h3>
      <p class="card-desc">On poverty, survival, and the complicated relationship with money.</p>
    </a>
    <a href="/play/write/fa-le-phirima/" class="card">
      <p class="card-label">Poetry</p>
      <h3 class="card-title">Fa Le Phirima</h3>
      <p class="card-desc">When the sun sets — an ode to endings and the beauty of dusk.</p>
    </a>
    <a href="/play/write/mma-pelo/" class="card">
      <p class="card-label">Story</p>
      <h3 class="card-title">Mma Pelo</h3>
      <p class="card-desc">A story of a woman who embodies the heart of a community.</p>
    </a>
    <a href="/play/write/collection-of-old-stories/" class="card">
      <p class="card-label">Collection</p>
      <h3 class="card-title">Collection of Old Stories</h3>
      <p class="card-desc">An archive of earlier work — stories that trace the arc of my writing life.</p>
    </a>
    <a href="http://poemhunter.com/tumisang-ramarea/" target="_blank" rel="noopener" class="card">
      <p class="card-label">External</p>
      <h3 class="card-title">Poetry on PoemHunter</h3>
      <p class="card-desc">My published poems available on PoemHunter.com.</p>
    </a>
  </div>
  <a href="/play/" class="back-link">&larr; Return to Play</a>
</div>""")

# ── SHOW ──────────────────────────────────────────────────────────────────────
pages["play/show/index.html"] = page("Show","My Visual Creations",f"""
<div class="page-hero">
  <p class="page-eyebrow">Play &rarr; Show</p>
  <h1 class="page-title">Show</h1>
  <p class="page-subtitle">&ldquo;A picture is a poem without words.&rdquo; &mdash; Horace</p>
</div>
<div class="content">
  <p class="body-text">This section is dedicated to my doodles and photography — where I share with the world what I see through my lens and what flows from my pen.</p>

  <h2 class="section-heading">Doodles</h2>
  <div class="cards-grid">
    <a href="/play/show/doodles/" class="card">
      <p class="card-label">Art</p>
      <h3 class="card-title">Doodles</h3>
      <p class="card-desc">A collage of illustrations and doodles — from moving across California to African spirituality.</p>
    </a>
  </div>

  <h2 class="section-heading" style="margin-top:2.5rem">Photography</h2>
  <p class="body-text">I bought myself a Fujifilm X-A2 to congratulate myself on successfully finishing my undergraduate journey at Stanford. Here is what I have captured since.</p>
  <div class="cards-grid">
    <a href="/play/show/flowers/" class="card"><p class="card-label">Photography</p><h3 class="card-title">Flowers</h3><p class="card-desc">A celebration of colour and life in Malibu and beyond.</p></a>
    <a href="/play/show/kgalagadi-a-dry-paradise/" class="card"><p class="card-label">Photography</p><h3 class="card-title">Kgalagadi: A Dry Paradise</h3><p class="card-desc">The Kalahari desert captured in all its austere beauty.</p></a>
    <a href="/play/show/sunset-to-sunrise/" class="card"><p class="card-label">Photography</p><h3 class="card-title">Sunset to Sunrise</h3><p class="card-desc">The golden hours — from the Maldives to California.</p></a>
  </div>

  <h2 class="section-heading" style="margin-top:2.5rem">Model in Photo Shoots</h2>
  <div class="cards-grid">
    <a href="/play/show/linkedin-headshot-spring-2019/" class="card"><p class="card-label">Photo Shoot</p><h3 class="card-title">LinkedIn Headshot Spring 2019</h3><p class="card-desc"></p></a>
    <a href="/play/show/june-2018-photo-shoot-in-botswana/" class="card"><p class="card-label">Photo Shoot</p><h3 class="card-title">June 2018 Photoshoot in Botswana</h3><p class="card-desc"></p></a>
    <a href="/play/show/spring-photo-shoot-2018/" class="card"><p class="card-label">Photo Shoot</p><h3 class="card-title">Spring Photo Shoot 2018</h3><p class="card-desc"></p></a>
    <a href="/play/show/african-cultural-fashion-show-2017/" class="card"><p class="card-label">Photo Shoot</p><h3 class="card-title">African Cultural Fashion Show 2017</h3><p class="card-desc"></p></a>
    <a href="/play/show/stanford-125-portraits-project-2016/" class="card"><p class="card-label">Photo Shoot</p><h3 class="card-title">Stanford 125 Portraits Project 2016</h3><p class="card-desc"></p></a>
    <a href="/play/show/poster-boy/" class="card"><p class="card-label">Photo Shoot</p><h3 class="card-title">Poster Boy</h3><p class="card-desc"></p></a>
  </div>
  <a href="/play/" class="back-link">&larr; Return to Play</a>
</div>""")

# ── DO ────────────────────────────────────────────────────────────────────────
pages["play/do/index.html"] = page("Do","My Artistic Performances",f"""
<div class="page-hero">
  <p class="page-eyebrow">Play &rarr; Do</p>
  <h1 class="page-title">Do</h1>
  <p class="page-subtitle">&ldquo;I&rsquo;m having fun. I&rsquo;m being myself. I&rsquo;m doing what I love. That&rsquo;s all that matters.&rdquo; &mdash; James Charles</p>
</div>
<div class="content">
  <p class="body-text">My aim is to live this life to the fullest. I recognise that I am not particularly talented at a lot of things — and that is okay — but I refuse to let that stop me from doing them anyway.</p>
  <div class="cards-grid">
    <a href="/play/do/dance/" class="card">
      <p class="card-label">Performance</p>
      <h2 class="card-title">Dance</h2>
      <p class="card-desc">Two left feet and all — dancing in Lokgwabe and wherever else the music takes me.</p>
    </a>
    <a href="/play/do/performing-arts/" class="card">
      <p class="card-label">Performance</p>
      <h2 class="card-title">Performing Arts</h2>
      <p class="card-desc">Acting on stage at Stanford and UWC Costa Rica — West Side Story and beyond.</p>
    </a>
    <a href="/play/do/speaking/" class="card">
      <p class="card-label">Performance</p>
      <h2 class="card-title">Speaking</h2>
      <p class="card-desc">From Kigali to TEDx stages — using my voice to move ideas and people.</p>
    </a>
    <a href="/play/do/music/" class="card">
      <p class="card-label">Creative</p>
      <h2 class="card-title">Music</h2>
      <p class="card-desc">Playing with sound and song — at the Gaborone bus rank and everywhere in between.</p>
    </a>
    <a href="/play/do/moremogolo/" class="card">
      <p class="card-label">Podcast</p>
      <h2 class="card-title">Moremogolo Podcast</h2>
      <p class="card-desc">Season 1 of my podcast — conversations about growth, community, and African futures.</p>
    </a>
    <a href="/play/do/cooking/" class="card">
      <p class="card-label">Creative</p>
      <h2 class="card-title">Cooking</h2>
      <p class="card-desc">Delicious food — one of the greatest expressions of love and culture there is.</p>
    </a>
  </div>
  <a href="/play/" class="back-link">&larr; Return to Play</a>
</div>""")

# ── WORK ──────────────────────────────────────────────────────────────────────
pages["work/index.html"] = page("Work","Work",f"""
<div class="page-hero">
  <p class="page-eyebrow">Work</p>
  <h1 class="page-title">Welding Opportunities<br>from Resources &amp; Knowledge</h1>
  <p class="page-subtitle">My professional and entrepreneurial journey — where passion, expertise, and purpose intersect.</p>
</div>
<div class="content">
  <div class="cards-grid">
    <a href="/work/education/" class="card">
      <p class="card-label">01</p>
      <h2 class="card-title">Education</h2>
      <p class="card-desc">PSLE, JCE, BGCSE, IB, BS, MS — the academic journey from Botswana to Stanford, fuelled by insatiable curiosity.</p>
    </a>
    <a href="/work/portfolio/" class="card">
      <p class="card-label">02</p>
      <h2 class="card-title">Work Portfolio</h2>
      <p class="card-desc">Product Management at Krikey AI, Teaching Assistant at Stanford, EdTech Operator — transforming research into meaningful technology.</p>
    </a>
    <a href="/work/entrepreneurship/" class="card">
      <p class="card-label">03</p>
      <h2 class="card-title">Entrepreneurship</h2>
      <p class="card-desc">Dryve Africa, RaMCash Corp, The Halidon Committee — building ventures from a place of deep conviction.</p>
    </a>
    <a href="/work/social-responsibility/" class="card">
      <p class="card-label">04</p>
      <h2 class="card-title">Social Responsibility</h2>
      <p class="card-desc">United World Colleges, MasterCard Foundation Scholars, Tsoga Africa — giving back is not optional, it is essential.</p>
    </a>
  </div>
  <a href="/work/catalyzing-impact/" class="btn-primary" style="margin-top:1rem;display:inline-block">Read My Work Narrative</a>
  <br>
  <a href="/" class="back-link">&larr; Return to Homepage</a>
</div>""")

# ── EDUCATION ─────────────────────────────────────────────────────────────────
pages["work/education/index.html"] = page("Education","Education",f"""
<div class="page-hero">
  <p class="page-eyebrow">Work &rarr; Education</p>
  <h1 class="page-title">Education</h1>
  <p class="page-subtitle">Thanks to my insatiable curiosity, I am forever a student in the school of life.</p>
</div>
<div class="content-narrow">
  <p class="body-text">I was very fortunate to have received a world-class education. My gratitude knows no bounds for my educators.</p>
  <p class="body-text">My full name, with my academic accolades: <strong style="color:var(--white)">Tumisang Ikefuna-Ramarea, PSLE, JCE, BGCSE, IB, BS, MS.</strong></p>

  <div class="cards-grid" style="margin-top:2.5rem">
    <a href="/work/education/uwc-costa-rica/" class="card">
      <p class="card-label">2013–2015</p>
      <h2 class="card-title">UWC Costa Rica</h2>
      <p class="card-desc">International Baccalaureate — where the world opened up and everything changed.</p>
    </a>
    <a href="/work/education/stanford/" class="card">
      <p class="card-label">2015–2021</p>
      <h2 class="card-title">Stanford University</h2>
      <p class="card-desc">BS and MS in Management Science &amp; Engineering — never has a place held so much privilege and so much opportunity.</p>
    </a>
  </div>

  <p class="body-text" style="margin-top:2rem">Academic credentials listed chronologically: Primary School Leaving Examination (PSLE), Junior Certificate Examination (JCE), Botswana General Certificate of Secondary Education (BGCSE), International Baccalaureate (IB), Bachelor of Science (BS), Master of Science (MS).</p>

  <a href="/work/" class="back-link">&larr; Return to Work</a>
</div>""")

# ── PORTFOLIO ─────────────────────────────────────────────────────────────────
pages["work/portfolio/index.html"] = page("Portfolio","Professional Portfolio",f"""
<div class="page-hero">
  <p class="page-eyebrow">Work &rarr; Portfolio</p>
  <h1 class="page-title">Professional<br>Portfolio</h1>
  <p class="page-subtitle">Transforming cutting-edge research into technologies that meaningfully improve people&rsquo;s lives.</p>
</div>
<div class="content-narrow">
  <p class="body-text">My interest in building &ldquo;new&rdquo; technologies also includes indigenous technologies and knowledge systems — I believe the future belongs to those who bridge both.</p>

  <h3 class="sub-heading">Product Manager — Krikey AI</h3>
  <p class="body-text">I have over 4 years of experience as a Product Manager at <a href="https://www.krikey.ai/" target="_blank" rel="noopener">Krikey AI</a>, spanning three product domains:</p>
  <div class="cards-grid">
    <div class="card"><p class="card-label">AI</p><h3 class="card-title">Generative AI PM</h3><p class="card-desc">Leading product development on AI-powered 3D animation tools.</p></div>
    <div class="card"><p class="card-label">Web3</p><h3 class="card-title">Crypto Web3 Gaming PM</h3><p class="card-desc">Building at the intersection of gaming and blockchain.</p></div>
    <div class="card"><p class="card-label">Mobile</p><h3 class="card-title">Mobile AR Experiences PM</h3><p class="card-desc">Augmented reality mobile experiences for global audiences.</p></div>
  </div>

  <h3 class="sub-heading">Teaching Assistant — Stanford</h3>
  <p class="body-text">Twice I have worked as a Teaching Assistant. First in 2013, when I helped teach students across Botswana. Then at Stanford, where I TA&rsquo;d for Accounting for Managers and Entrepreneurs.</p>
  <div class="cards-grid">
    <div class="card"><p class="card-label">Stanford</p><h3 class="card-title">Accounting for Managers TA</h3><p class="card-desc">Teaching MBA-level accounting concepts to undergraduate students.</p></div>
    <div class="card"><p class="card-label">Botswana</p><h3 class="card-title">UCMAS Mindmapping TA</h3><p class="card-desc">Mnemonic techniques and mindmapping for students across Botswana.</p></div>
  </div>
  <p class="body-text"><a href="https://explorecourses.stanford.edu/instructor/ramarea" target="_blank" rel="noopener">View Stanford instructor profile &rarr;</a></p>

  <h3 class="sub-heading">Education Technology Operator — Stanford</h3>
  <p class="body-text">I started as Studio Operator for the Stanford Center for Professional Development, eventually rising to Lead Student Ed-Tech Operator — supporting the infrastructure that powers Stanford&rsquo;s online education.</p>
  {img_ph("Ed-Tech role photo — replace with your image")}

  <a href="/work/" class="back-link">&larr; Return to Work</a>
</div>""")

# ── ENTREPRENEURSHIP ──────────────────────────────────────────────────────────
pages["work/entrepreneurship/index.html"] = page("Entrepreneurship","Entrepreneurial Endeavors",f"""
<div class="page-hero">
  <p class="page-eyebrow">Work &rarr; Entrepreneurship</p>
  <h1 class="page-title">Entrepreneurship</h1>
  <p class="page-subtitle">Studying Management Science and Engineering at Stanford, it is not hard to see how one can be drawn to building things.</p>
</div>
<div class="content">
  <h2 class="section-heading">Entrepreneurial Experiences</h2>
  <div class="cards-grid">
    <a href="/work/entrepreneurship/dryve-africa/" class="card">
      <p class="card-label">2019–2020</p>
      <h2 class="card-title">Dryve Africa</h2>
      <p class="card-desc">A mobility startup aimed at expanding access to reliable transportation across Africa.</p>
    </a>
    <a href="/work/entrepreneurship/ramcash-corporation/" class="card">
      <p class="card-label">2010–2012</p>
      <h2 class="card-title">RaMCash Corp</h2>
      <p class="card-desc">An early entrepreneurial venture that taught me the fundamentals of business and resourcefulness.</p>
    </a>
    <a href="/work/entrepreneurship/halidon-committee/" class="card">
      <p class="card-label">2011–2012</p>
      <h2 class="card-title">The Halidon Committee</h2>
      <p class="card-desc">A student-led initiative focused on community and economic empowerment.</p>
    </a>
    <a href="/work/entrepreneurship/group-food-committee/" class="card">
      <p class="card-label">2007</p>
      <h2 class="card-title">Group Food Committee</h2>
      <p class="card-desc">An early experiment in organising collective resources for shared benefit.</p>
    </a>
  </div>

  <h2 class="section-heading" style="margin-top:2.5rem">Other Gigs</h2>
  <p class="body-text">Although these are what my mentor Tim would call side hustles, they represent an important part of my entrepreneurial education — learning to create value from whatever resources are at hand.</p>

  <a href="/work/" class="back-link">&larr; Return to Work</a>
</div>""")

# ── SOCIAL RESPONSIBILITY ──────────────────────────────────────────────────────
pages["work/social-responsibility/index.html"] = page("Social Responsibility","Social Responsibility",f"""
<div class="page-hero">
  <p class="page-eyebrow">Work &rarr; Social Responsibility</p>
  <h1 class="page-title">Social<br>Responsibility</h1>
  <p class="page-subtitle">Social responsibility is an integral part of good citizenship — especially as we live in a world of profound and growing inequality.</p>
</div>
<div class="content">
  <div class="cards-grid">
    <a href="/work/social-responsibility/united-world-colleges/" class="card">
      <p class="card-label">Education</p>
      <h2 class="card-title">United World Colleges</h2>
      <p class="card-desc">Supporting UWC&rsquo;s mission to make education a force to unite people, nations, and cultures for peace.</p>
    </a>
    <a href="/work/social-responsibility/stanford-seed-internship-program/" class="card">
      <p class="card-label">Economic Dev.</p>
      <h2 class="card-title">Tsoga Africa via Stanford SEED</h2>
      <p class="card-desc">Using the Stanford Seed Internship Program to support African economic development.</p>
    </a>
    <a href="/work/social-responsibility/mastercard-foundation-scholars-program/" class="card">
      <p class="card-label">Scholarships</p>
      <h2 class="card-title">MasterCard Foundation Scholars</h2>
      <p class="card-desc">Advancing access to higher education for talented young Africans with financial need.</p>
    </a>
    <a href="/live/community/memorial-wall/batho-madigele/" class="card">
      <p class="card-label">Memory</p>
      <h2 class="card-title">In Memory of Batho Madigele</h2>
      <p class="card-desc">Education give-back initiatives honoring a life that mattered deeply.</p>
    </a>
    <a href="/work/social-responsibility/organic-naturals-skincare/" class="card">
      <p class="card-label">Business</p>
      <h2 class="card-title">Organic Naturals Skincare Botswana</h2>
      <p class="card-desc">Supporting an African skincare business rooted in natural ingredients and community.</p>
    </a>
    <a href="/work/social-responsibility/the-voice-of-africa-botswana/" class="card">
      <p class="card-label">Media</p>
      <h2 class="card-title">The Voice of Africa Botswana</h2>
      <p class="card-desc">Amplifying African voices and stories that deserve to be heard.</p>
    </a>
    <a href="/work/social-responsibility/stars-revealed/" class="card">
      <p class="card-label">Youth</p>
      <h2 class="card-title">Stars Revealed</h2>
      <p class="card-desc">A youth development initiative uncovering the potential in young people.</p>
    </a>
    <a href="/work/social-responsibility/costa-rican-international-model-united-nations-leadership-network/" class="card">
      <p class="card-label">Leadership</p>
      <h2 class="card-title">Costa Rican International MUN</h2>
      <p class="card-desc">Building the next generation of global leaders through Model United Nations.</p>
    </a>
  </div>
  <a href="/work/" class="back-link">&larr; Return to Work</a>
</div>""")

# ── WRITE ALL FILES ────────────────────────────────────────────────────────────
for path, html in pages.items():
    full_path = os.path.join(BASE, path)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, "w") as f:
        f.write(html)

# Copy homepage
import shutil
shutil.copy("/sessions/sharp-quirky-davinci/mnt/outputs/ramarea-homepage.html",
            os.path.join(BASE, "index.html"))

print(f"Built {len(pages)+1} pages")
for p in sorted(pages.keys()):
    print(f"  ✓ {p}")
print(f"  ✓ index.html")
