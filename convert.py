#!/usr/bin/env python3
"""
Confidence Curriculum: MD → HTML converter.
Reads source MDs, applies the shared CSS, embeds SVGs from source/figures/,
outputs publication-ready HTML files.
"""

import re, os, sys
import markdown

REPO = '/home/claude/github-repo-v2'
SRC = os.path.join(REPO, 'source')
FIGS = os.path.join(SRC, 'figures')
BASE_URL = 'https://hip1.github.io/confidence-curriculum/'

FILE_MAP = {
    '0-the-confidence-curriculum-series-introduction-v8.md': '0-the-confidence-curriculum-series-introduction.html',
    '1-the-confidence-vulnerability-v6.md': '1-the-confidence-vulnerability.html',
    '1-the-confidence-vulnerability-v6-appendices.md': '1-the-confidence-vulnerability-appendices.html',
    '1-the-confidence-vulnerability-v6-test-documents.md': '1-the-confidence-vulnerability-test-documents.html',
    '2-the-skill-ceiling-v6.md': '2-the-skill-ceiling.html',
    '3-the-knowledge-horizon-v7.md': '3-the-knowledge-horizon.html',
    '4-the-pedagogical-inversion-v6.md': '4-the-pedagogical-inversion.html',
    '5-the-confidence-collision-v4.md': '5-the-confidence-collision.html',
    'the-symbiont-hypothesis-epilogue-v6.md': 'the-symbiont-hypothesis-epilogue.html',
    'the-confidence-curriculum-reading-guide.md': 'the-confidence-curriculum-reading-guide.html',
}

SVG_MAP = {
    'series-architecture.svg': '0-the-confidence-curriculum-series-introduction-figure-1.svg',
    'p3-shared-substrate.svg': '2-the-skill-ceiling-figure-1.svg',
    'p3-deployment-trust.svg': '2-the-skill-ceiling-figure-2.svg',
    'p4-adversarial-orchestration.svg': '3-the-knowledge-horizon-figure-1.svg',
    'p6-epistemic-training-architecture.svg': '5-the-confidence-collision-figure-1.svg',
}

P1_FIGS = {
    1: '1-the-confidence-vulnerability-figure-1.svg',
    2: '1-the-confidence-vulnerability-figure-2.svg',
}

TITLES = {
    '0-the-confidence-curriculum-series-introduction-v8.md': (
        'The Confidence Curriculum',
        'Compliance, Judgment, and Accountability in AI Systems',
        'The Confidence Curriculum — HiP (Ivan Phan), 2026',
        'What AI systems follow, what they can\u2019t judge, and who answers.',
    ),
    '1-the-confidence-vulnerability-v6.md': (
        'The Confidence Vulnerability',
        'Unstable Judgment in Language Model Summarisation',
        'The Confidence Vulnerability — HiP (Ivan Phan), 2026',
    ),
    '1-the-confidence-vulnerability-v6-appendices.md': (
        'The Confidence Vulnerability — Appendices A–G',
        '',
        'The Confidence Vulnerability: Appendices — HiP (Ivan Phan), 2026',
    ),
    '1-the-confidence-vulnerability-v6-test-documents.md': (
        'The Confidence Vulnerability — Test Documents',
        '',
        'The Confidence Vulnerability: Test Documents — HiP (Ivan Phan), 2026',
    ),
    '2-the-skill-ceiling-v6.md': (
        'The Skill Ceiling',
        'Author-Side Defences and Infrastructure-Level Trust for Agent Skills and Extension Mechanisms',
        'The Skill Ceiling — HiP (Ivan Phan), 2026',
    ),
    '3-the-knowledge-horizon-v7.md': (
        'The Knowledge Horizon',
        'Accountability, Expertise Erosion, and the Case for Human Orchestration in Agentic AI',
        'The Knowledge Horizon — HiP (Ivan Phan), 2026',
    ),
    '4-the-pedagogical-inversion-v6.md': (
        'The Pedagogical Inversion',
        'Confidence Inheritance and the Case for Training-Oriented AI',
        'The Pedagogical Inversion — HiP (Ivan Phan), 2026',
    ),
    '5-the-confidence-collision-v4.md': (
        'The Confidence Collision',
        'Training for Epistemic Calibration Under Contested and Adversarial Conditions',
        'The Confidence Collision — HiP (Ivan Phan), 2026',
    ),
    'the-symbiont-hypothesis-epilogue-v6.md': (
        'The Symbiont Hypothesis',
        'Frontier Speculations on Relational Identity, Formative Influence, and the Autonomy Threshold',
        'The Symbiont Hypothesis — HiP (Ivan Phan) & Claude, 2026',
    ),
    'the-confidence-curriculum-reading-guide.md': (
        'Reading Guide',
        'The Confidence Curriculum',
        'Reading Guide — The Confidence Curriculum, 2026',
    ),
}

# Google Fonts links per paper (based on original font stacks)
GOOGLE_FONTS = {
    '0-the-confidence-curriculum-series-introduction-v8.md':
        'Inter:wght@400;500;600&family=Lora:ital,wght@0,400;0,600;1,400&family=JetBrains+Mono:wght@400;500',
    '1-the-confidence-vulnerability-v6.md':
        'IBM+Plex+Sans:wght@400;500;600;700&family=IBM+Plex+Mono:wght@400;500',
    '1-the-confidence-vulnerability-v6-appendices.md':
        'Source+Serif+4:ital,opsz,wght@0,8..60,300;0,8..60,400;0,8..60,600;0,8..60,700;1,8..60,400&family=Source+Sans+3:wght@400;600;700&family=JetBrains+Mono:wght@400;500',
    '1-the-confidence-vulnerability-v6-test-documents.md':
        'IBM+Plex+Sans:wght@400;500;600;700&family=IBM+Plex+Mono:wght@400;500',
    '2-the-skill-ceiling-v6.md':
        'Inter:wght@400;500;600&family=Fira+Code:wght@400;500',
    '3-the-knowledge-horizon-v7.md':
        'Inter:wght@400;500;600&family=DM+Mono:wght@400;500',
    '4-the-pedagogical-inversion-v6.md':
        'Lora:ital,wght@0,400;0,600;1,400&family=Inter:wght@400;500;600&family=Fira+Code:wght@400;500',
    '5-the-confidence-collision-v4.md':
        'IBM+Plex+Sans:wght@400;500;600;700&family=IBM+Plex+Serif:ital,wght@0,400;0,600;1,400&family=IBM+Plex+Mono:wght@400;500',
    'the-symbiont-hypothesis-epilogue-v6.md':
        'Lora:ital,wght@0,400;0,600;1,400&family=Karla:wght@400;500;600&family=Fira+Code:wght@400;500',
    'the-confidence-curriculum-reading-guide.md':
        'Inter:wght@400;500;600&family=Lora:ital,wght@0,400;0,600;1,400&family=JetBrains+Mono:wght@400;500',
}

def build_css_var_bridge(css):
    """Only inject variable aliases for variables NOT already defined in the paper's :root."""
    import re
    root = re.search(r':root\s*\{([^}]+)\}', css)
    defined = set(re.findall(r'--([\w-]+):', root.group(1))) if root else set()
    
    bridges = []
    if 'bg-surface' not in defined:
        bridges.append('--bg-surface: var(--surface, var(--bg, #f2f1ee));')
    if 'bg-elevated' not in defined:
        bridges.append('--bg-elevated: var(--surface, var(--bg, #eae9e5));')
    if 'text-secondary' not in defined:
        bridges.append('--text-secondary: var(--text-light, var(--text-muted, #52514d));')
    if 'text-muted' not in defined:
        bridges.append('--text-muted: var(--text-light, #8a8884);')
    if 'max-width' not in defined:
        bridges.append('--max-width: var(--max-w, 780px);')
    if 'border' not in defined:
        bridges.append('--border: #d8d7d3;')
    
    if not bridges:
        return ''
    return ':root {\n  ' + '\n  '.join(bridges) + '\n}'

SPECIAL_SECTIONS = [
    ('Abstract', 'abstract'),
    ('Thesis', 'thesis'),
    ('Limitations and Open Questions', 'limitations'),
    ('Limitations', 'limitations'),
    ('Confidence Statement', 'confidence-statement'),
    ('Conclusion', 'conclusion'),
    ('References', 'references'),
    ('Sources', 'references'),
    ('Provenance', 'methodology'),
    ('Coda', 'coda'),
]


ORIG_DIR = '/home/claude/originals'

# Map source MD → original HTML for CSS extraction
CSS_SOURCE_MAP = {
    '0-the-confidence-curriculum-series-introduction-v8.md': '0-the-confidence-curriculum-series-introduction-v7.html',
    '1-the-confidence-vulnerability-v6.md': '1-the-confidence-vulnerability-v6.html',
    '1-the-confidence-vulnerability-v6-appendices.md': '1-the-confidence-vulnerability-v6-appendices.html',
    '1-the-confidence-vulnerability-v6-test-documents.md': '1-the-confidence-vulnerability-v6-test-documents.html',
    '2-the-skill-ceiling-v6.md': '2-the-skill-ceiling-v6.html',
    '3-the-knowledge-horizon-v7.md': '3-the-knowledge-horizon-v6.html',
    '4-the-pedagogical-inversion-v6.md': '4-the-pedagogical-inversion-v5.html',
    '5-the-confidence-collision-v4.md': '5-the-confidence-collision-v3.html',
    'the-symbiont-hypothesis-epilogue-v6.md': 'the-symbiont-hypothesis-epilogue-v5.html',
    'the-confidence-curriculum-reading-guide.md': 'the-confidence-curriculum-reading-guide.html',
}

def load_css(md_filename=None):
    """Load the original CSS for a specific paper, stripping any stale TOC rules."""
    # Try per-paper CSS first
    if md_filename and md_filename in CSS_SOURCE_MAP:
        orig = os.path.join(ORIG_DIR, CSS_SOURCE_MAP[md_filename])
        if os.path.exists(orig):
            content = open(orig).read()
            m = re.search(r'<style>(.*?)</style>', content, re.DOTALL)
            if m:
                css = m.group(1)
                # Strip any stale TOC rules from old builds
                css = re.sub(r'\.toc-sidebar\s*\{[^}]*\}', '', css)
                css = re.sub(r'\.toc-toggle\s*\{[^}]*\}', '', css)
                css = re.sub(r'\.toc-body[^{]*\{[^}]*\}', '', css)
                css = re.sub(r'\.toc-link[^{]*\{[^}]*\}', '', css)
                css = re.sub(r'\.toc-title\s*\{[^}]*\}', '', css)
                css = re.sub(r'/\*.*?Floating TOC.*?\*/', '', css)
                css = re.sub(r'@media[^{]*\{[^}]*toc[^}]*\}[^}]*\}', '', css, flags=re.IGNORECASE)
                css = re.sub(r'@media[^{]*\{[^}]*\.toc-sidebar[^}]*\}', '', css)
                return css
    # Fallback: P1 CSS
    for fname in ['1-the-confidence-vulnerability.html']:
        path = os.path.join(ORIG_DIR, fname)
        if os.path.exists(path):
            content = open(path).read()
            m = re.search(r'<style>(.*?)</style>', content, re.DOTALL)
            if m:
                return m.group(1)
    return ''


def slugify(text):
    """Convert heading text to a URL-friendly slug."""
    text = re.sub(r'<[^>]+>', '', text)  # strip HTML
    text = re.sub(r'&[a-z]+;', '', text)  # strip entities
    text = text.lower().strip()
    text = re.sub(r'[^a-z0-9\s-]', '', text)
    text = re.sub(r'[\s]+', '-', text)
    text = re.sub(r'-+', '-', text)
    return text.strip('-')[:60]


def add_heading_ids(html):
    """Add id attributes to h2/h3/h4 headings and return (modified_html, toc_entries)."""
    toc = []
    seen_slugs = set()
    
    def replace_heading(m):
        tag = m.group(1)  # h2, h3, h4
        content = m.group(2)
        slug = slugify(content)
        # Deduplicate
        base = slug
        i = 1
        while slug in seen_slugs:
            slug = f"{base}-{i}"
            i += 1
        seen_slugs.add(slug)
        
        level = int(tag[1])
        clean_text = re.sub(r'<[^>]+>', '', content).strip()
        toc.append((level, slug, clean_text))
        
        return f'<{tag} id="{slug}">{content}</{tag}>'
    
    html = re.sub(r'<(h[234])>(.*?)</\1>', replace_heading, html)
    return html, toc


def build_toc_html(toc_entries):
    """Build the floating TOC sidebar HTML from heading entries."""
    if not toc_entries or len(toc_entries) < 3:
        return ''
    
    items = []
    for level, slug, text in toc_entries:
        # Shorten long headings
        display = text[:50] + '…' if len(text) > 50 else text
        indent = 'toc-h3' if level == 3 else 'toc-h4' if level == 4 else ''
        items.append(f'<a href="#{slug}" class="toc-link {indent}">{display}</a>')
    
    return f'''<nav id="toc-sidebar" class="toc-sidebar" aria-label="Table of contents">
<button id="toc-toggle" class="toc-toggle" aria-label="Toggle table of contents"><span class="toc-icon">☰</span><span class="toc-label">Contents</span></button>
<div id="toc-body" class="toc-body">
<div class="toc-title">Contents</div>
{''.join(items)}
</div>
</nav>'''


TOC_CSS = '''
/* Floating TOC */
.toc-sidebar {
  position: fixed; top: 1rem; left: 1rem; z-index: 100;
  font-family: var(--sans, system-ui, sans-serif); font-size: 0.75rem;
}
.toc-toggle {
  background: var(--bg-surface, var(--bg, #f2f1ee)); border: 1px solid var(--border, #d8d7d3);
  border-radius: 8px; padding: 0.5rem 0.75rem; cursor: pointer;
  color: var(--text, #1b1b1a); font-size: 0.8rem; line-height: 1;
  font-family: var(--sans, system-ui, sans-serif); font-weight: 500;
  box-shadow: 0 1px 4px rgba(0,0,0,0.12);
  transition: background 0.15s, box-shadow 0.15s;
  display: flex; align-items: center; gap: 0.4rem;
}
.toc-toggle:hover { background: var(--bg-elevated, var(--bg, #eae9e5)); box-shadow: 0 2px 8px rgba(0,0,0,0.15); }
.toc-toggle .toc-icon { font-size: 1rem; }
.toc-toggle .toc-label { font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.06em; }
.toc-body {
  display: none; margin-top: 0.5rem;
  background: var(--bg-surface, var(--bg, #f2f1ee)); border: 1px solid var(--border, #d8d7d3);
  border-radius: 10px; padding: 0.8rem 0; overflow-y: auto;
  box-shadow: 0 4px 20px rgba(0,0,0,0.12);
}
.toc-body.open { display: block; }
.toc-title {
  font-weight: 600; font-size: 0.68rem; text-transform: uppercase;
  letter-spacing: 0.08em; color: var(--text-muted, #8a8884);
  padding: 0 1rem 0.6rem; border-bottom: 1px solid var(--border, #d8d7d3);
  margin-bottom: 0.4rem;
}
.toc-link {
  display: block; padding: 0.3rem 1rem;
  color: var(--text-secondary, #52514d); text-decoration: none;
  line-height: 1.4; transition: color 0.1s, background 0.1s;
  border-left: 2px solid transparent;
}
.toc-link:hover { color: var(--text, #1b1b1a); background: var(--bg-elevated, var(--bg, #eae9e5)); }
.toc-link.active { color: var(--accent, #2c5282); border-left-color: var(--accent, #2c5282); font-weight: 500; }
.toc-link.toc-h3 { padding-left: 1.6rem; font-size: 0.7rem; }
.toc-link.toc-h4 { padding-left: 2.2rem; font-size: 0.65rem; color: var(--text-muted, #8a8884); }

/* Desktop: sidebar panel */
@media (min-width: 1200px) {
  .toc-body { max-width: 280px; max-height: calc(100vh - 5rem); }
}
/* Tablet/mobile: overlay */
@media (max-width: 1199px) {
  .toc-body { max-width: min(320px, calc(100vw - 2rem)); max-height: calc(100vh - 5rem); }
}
@media print { .toc-sidebar { display: none; } }
'''

TOC_JS = '''
<script>
(function() {
  var toggle = document.getElementById('toc-toggle');
  var body = document.getElementById('toc-body');
  var label = toggle ? toggle.querySelector('.toc-label') : null;
  if (!toggle || !body) return;
  
  function closeToc() {
    body.classList.remove('open');
    if (label) label.textContent = 'Contents';
    toggle.querySelector('.toc-icon').textContent = '☰';
  }
  function openToc() {
    body.classList.add('open');
    if (label) label.textContent = 'Close';
    toggle.querySelector('.toc-icon').textContent = '✕';
  }
  
  toggle.addEventListener('click', function() {
    body.classList.contains('open') ? closeToc() : openToc();
  });
  
  // Close on outside click
  document.addEventListener('click', function(e) {
    if (!e.target.closest('.toc-sidebar') && body.classList.contains('open')) closeToc();
  });
  
  // Active section tracking
  var links = document.querySelectorAll('.toc-link');
  var headings = [];
  links.forEach(function(link) {
    var id = link.getAttribute('href').slice(1);
    var el = document.getElementById(id);
    if (el) headings.push({ el: el, link: link });
  });
  
  var ticking = false;
  function updateActive() {
    var current = null;
    var scrollY = window.scrollY + 120;
    for (var i = headings.length - 1; i >= 0; i--) {
      if (headings[i].el.offsetTop <= scrollY) { current = headings[i]; break; }
    }
    links.forEach(function(l) { l.classList.remove('active'); });
    if (current) current.link.classList.add('active');
    ticking = false;
  }
  window.addEventListener('scroll', function() {
    if (!ticking) { requestAnimationFrame(updateActive); ticking = true; }
  });
  updateActive();
  
  // Smooth scroll + close on mobile
  links.forEach(function(link) {
    link.addEventListener('click', function(e) {
      e.preventDefault();
      var id = this.getAttribute('href').slice(1);
      var el = document.getElementById(id);
      if (el) {
        el.scrollIntoView({ behavior: 'smooth', block: 'start' });
        // Close TOC on narrower screens
        if (window.innerWidth < 1200) closeToc();
      }
    });
  });
})();
</script>'''


BACK_TO_TOP_CSS = ''

BACK_TO_TOP_JS = ''

BREATHE_CSS = '''
/* Enhanced readability */
p { margin-bottom: 1.05rem; }
h2 { margin-top: 3.5rem; margin-bottom: 1rem; }
h3 { margin-top: 2.5rem; margin-bottom: 0.7rem; }
.paper-container { max-width: var(--max-width); padding: 0 2rem 6rem; }

/* Front matter breathing */
.front-matter { padding-bottom: 2.5rem; margin-bottom: 3rem; }
.front-matter p { margin-bottom: 1rem; }

/* Section spacing */
section.abstract, section.thesis { margin: 2.5rem 0 3rem; padding: 2rem 2.2rem; }
section.confidence-statement { margin-top: 3rem; }
section.references { margin-top: 3rem; }
section.coda { margin-top: 3rem; }

/* Better blockquotes (figure captions from MD) */
blockquote { margin: 1.2rem 0; padding: 0.8rem 1.2rem; }

/* Smoother reading on long text */
.paper-body { line-height: 1.78; }

/* Tables: more air */
th { padding: 0.6rem 0.8rem; }
td { padding: 0.55rem 0.8rem; }
tbody tr { transition: background 0.15s; }
tbody tr:hover { background: var(--bg-surface, var(--surface, rgba(0,0,0,0.03))); }

/* Scroll margin for anchor links */
[id] { scroll-margin-top: 1.5rem; }

/* Print: pagination and orphan control */
@media print {
  .toc-sidebar { display: none !important; }
  
  h2, h3, h4 {
    page-break-after: avoid !important;
    break-after: avoid !important;
    /* wkhtmltopdf workaround: force heading to pull next content along */
    page-break-inside: avoid !important;
    break-inside: avoid !important;
  }
  h2 { margin-top: 2rem; padding-bottom: 0; margin-bottom: 0.3rem; }
  h3 { margin-top: 1.5rem; padding-bottom: 0; margin-bottom: 0.2rem; }
  
  /* Wrap heading + first content together to prevent orphans.
     wkhtmltopdf ignores break-after:avoid on block elements,
     but respects break-inside:avoid on containers. */
  h2 + p, h2 + ul, h2 + ol, h2 + table, h2 + blockquote,
  h3 + p, h3 + ul, h3 + ol, h3 + table, h3 + blockquote {
    margin-top: 0;
  }
  
  p {
    orphans: 4;
    widows: 4;
  }
  
  figure, table, blockquote, section.abstract,
  section.confidence-statement, .paper-card, .epilogue-card,
  .stimulus-meta, .parchment {
    page-break-inside: avoid;
    break-inside: avoid;
  }
  
  /* Heading orphan guards */
  .heading-guard {
    page-break-inside: avoid !important;
    break-inside: avoid !important;
  }
  
  /* Keep heading with its first paragraph */
  h2 + p, h3 + p, h2 + ul, h3 + ul, h2 + ol, h3 + ol,
  h2 + table, h3 + table, h2 + blockquote, h3 + blockquote {
    page-break-before: avoid;
    break-before: avoid;
  }
  
  /* References: allow breaks but keep each entry together */
  section.references li {
    page-break-inside: avoid;
    break-inside: avoid;
  }
  
  /* Clean backgrounds for print */
  body { background: white !important; }
  .paper-container, .container { padding: 0 !important; max-width: none !important; }
  .front-matter { margin-bottom: 0.5rem; padding-bottom: 0.5rem; }
  .front-matter hr { display: none; }
  .meta-block { margin-bottom: 0.3rem; }
  header.paper-header { padding-bottom: 0.5rem; }
  section.thesis { margin: 0.5rem 0 1.5rem; padding: 0.8rem 1.2rem; }
  
  /* SVG figures: constrain to page */
  figure svg { max-height: 500px; width: auto; }
  
  /* Links: no underlines, inherit color */
  a { color: inherit !important; text-decoration: none !important; }
}
'''


def load_svg(svg_filename):
    path = os.path.join(FIGS, svg_filename)
    if os.path.exists(path):
        return open(path).read().strip()
    return None


def md_to_html(md_text):
    md = markdown.Markdown(extensions=['tables', 'smarty', 'fenced_code'])
    return md.convert(md_text)


def split_front_and_body(md_text):
    lines = md_text.split('\n')
    for i, line in enumerate(lines):
        if line.strip() == '---':
            return '\n'.join(lines[:i]), '\n'.join(lines[i+1:])
    return '', md_text


def make_full_links(html):
    def replace_link(m):
        href = m.group(1)
        if href.startswith('http') or href.startswith('#') or href.startswith('mailto:'):
            return m.group(0)
        return f'href="{BASE_URL}{href}"'
    return re.sub(r'href="([^"]*\.html[^"]*)"', replace_link, html)


def embed_image_svgs(html):
    def replace_img(m):
        alt = m.group(1)
        src = m.group(2)
        svg_file = SVG_MAP.get(src)
        if svg_file:
            svg_content = load_svg(svg_file)
            if svg_content:
                return f'<figure class="paper-figure">\n{svg_content}\n</figure>'
        return m.group(0)
    return re.sub(r'<p><img alt="([^"]*)" src="([^"]+\.svg)"[^/]*/></p>', replace_img, html)


def embed_webp_images(html):
    import base64
    def replace_img(m):
        alt = m.group(1)
        src = m.group(2)
        # Try to find the webp file
        for path in [os.path.join(FIGS, src), os.path.join(SRC, src), os.path.join(REPO, src)]:
            if os.path.exists(path):
                data = base64.b64encode(open(path, 'rb').read()).decode()
                return (f'<figure class="paper-figure">'
                        f'<img src="data:image/webp;base64,{data}" alt="{alt}" '
                        f'style="max-width:100%;border-radius:8px;">'
                        f'</figure>')
        # Fallback: relative path
        return (f'<figure class="paper-figure">'
                f'<img src="figures/{src}" alt="{alt}" style="max-width:100%;border-radius:8px;">'
                f'</figure>')
    return re.sub(r'<p><img alt="([^"]*)" src="([^"]+\.webp)"[^/]*/></p>', replace_img, html)


def guard_heading_orphans(html):
    """Wrap each h2/h3 + its first paragraph in a div to prevent page-break orphans.
    wkhtmltopdf ignores break-after:avoid on blocks but respects break-inside:avoid on containers."""
    # Match: heading followed by whitespace then a <p>...</p>
    def wrap(m):
        return f'<div class="heading-guard">{m.group(1)}\n{m.group(2)}</div>'
    
    # [^<]* for heading text prevents backtracking past other tags when no <p> follows
    html = re.sub(r'(<h2[^>]*>[^<]*(?:<(?!/?h2)[^>]*>[^<]*)*</h2>)\s*(<p(?:\s[^>]*)?>(?:(?!<h[23]).)*?</p>)', wrap, html, flags=re.DOTALL)
    html = re.sub(r'(<h3[^>]*>[^<]*(?:<(?!/?h3)[^>]*>[^<]*)*</h3>)\s*(<p(?:\s[^>]*)?>(?:(?!<h[23]).)*?</p>)', wrap, html, flags=re.DOTALL)
    return html


def embed_p1_figures(html):
    for fig_num, svg_file in P1_FIGS.items():
        svg_content = load_svg(svg_file)
        if not svg_content:
            continue
        pattern = (r'<blockquote>\s*<p><strong>Figure ' + str(fig_num) +
                   r'\.?</strong>(.*?)</p>\s*</blockquote>')
        m = re.search(pattern, html, re.DOTALL)
        if m:
            caption_text = f'<strong>Figure {fig_num}.</strong>{m.group(1)}'
            replacement = (f'<figure class="paper-figure">\n{svg_content}\n'
                          f'<figcaption>{caption_text}</figcaption>\n</figure>')
            html = html.replace(m.group(0), replacement)
    return html


def merge_blockquote_captions(html):
    html = re.sub(
        r'</figure>\s*<blockquote>\s*<p>(<strong>Figure \d+\.?</strong>.*?)</p>\s*</blockquote>',
        r'<figcaption>\1</figcaption>\n</figure>',
        html, flags=re.DOTALL
    )
    html = re.sub(
        r'</figure>\s*<p><em>(Figure \d+[:.][^<]*)</em></p>',
        r'<figcaption><em>\1</em></figcaption>\n</figure>',
        html, flags=re.DOTALL
    )
    return html


def wrap_sections(html):
    parts = re.split(r'(<h2[^>]*>.*?</h2>)', html)
    result = []
    open_section = None
    for part in parts:
        h2 = re.match(r'<h2[^>]*>(.*?)</h2>', part)
        if h2:
            if open_section:
                result.append('</section>')
                open_section = None
            heading = re.sub(r'<[^>]+>', '', h2.group(1)).strip()
            heading_clean = re.sub(r'^\d+\.\s*', '', heading)
            for key, cls in SPECIAL_SECTIONS:
                if heading_clean.lower().startswith(key.lower()):
                    result.append(f'<section class="{cls}">')
                    open_section = cls
                    break
        result.append(part)
    if open_section:
        result.append('</section>')
    return ''.join(result)


def style_appendix_toc(html):
    """Remove the inline TOC from the appendix — the floating TOC handles navigation."""
    pattern = r'<h2[^>]*>Table of Contents</h2>\s*<ul>.*?</ul>'
    html = re.sub(pattern, '', html, flags=re.DOTALL)
    return html


RAW_STIMULUS_MAP = {
    '1': os.path.join(SRC, 'raw-stimulus-B.txt'),  # Stimulus 1 = Document B (care)
    '2': os.path.join(SRC, 'raw-stimulus-C.txt'),  # Stimulus 2 = Document C (authority)
    '3': os.path.join(SRC, 'raw-stimulus-A.txt'),  # Stimulus 3 = Document A (control)
}

def style_test_documents(html):
    """Replace rendered document content with raw source text in <pre> blocks."""
    import html as html_mod
    
    type_map = {
        'care': 'attack-care',
        'institutional': 'attack-authority',
        'authority': 'attack-authority',
        'control': 'control-honest',
        'honest': 'control-honest',
    }
    
    parts = re.split(r'(<h2>Stimulus \d[^<]*</h2>)', html)
    
    result = [parts[0]]
    i = 1
    while i < len(parts):
        heading = parts[i]
        body = parts[i + 1] if i + 1 < len(parts) else ''
        
        heading_text = re.sub(r'<[^>]+>', '', heading).lower()
        parchment_class = 'parchment'
        for key, cls in type_map.items():
            if key in heading_text:
                parchment_class = f'parchment {cls}'
                break
        
        # Extract stimulus number
        stim_num = re.search(r'Stimulus (\d)', heading)
        stim_id = stim_num.group(1) if stim_num else None
        
        # Split at <hr /> to separate metadata from document
        doc_start = re.search(r'<hr\s*/>', body)
        if doc_start:
            meta_html = body[:doc_start.start()]
            # Try to load raw source
            raw_path = RAW_STIMULUS_MAP.get(stim_id)
            if raw_path and os.path.exists(raw_path):
                raw_text = open(raw_path).read()
                escaped = html_mod.escape(raw_text)
                doc_html = f'<pre class="raw-stimulus">{escaped}</pre>'
            else:
                doc_html = body[doc_start.end():]
            
            result.append(heading)
            result.append(f'<div class="stimulus-meta">{meta_html}</div>')
            result.append(f'<div class="{parchment_class}">{doc_html}</div>')
        else:
            result.append(heading)
            result.append(body)
        
        i += 2
    
    return ''.join(result)


RAW_STIMULUS_CSS = '''
/* Raw stimulus text */
.raw-stimulus {
  font-family: var(--font-sans, var(--sans, system-ui, sans-serif));
  font-size: 0.88rem;
  line-height: 1.65;
  white-space: pre-wrap;
  word-wrap: break-word;
  padding: 0;
  margin: 0;
  background: none;
  border: none;
  color: inherit;
  overflow-x: auto;
}
'''


# Paper number → HTML filename for card links
PAPER_URLS = {
    '1': '1-the-confidence-vulnerability.html',
    '2': '2-the-skill-ceiling.html',
    '3': '3-the-knowledge-horizon.html',
    '4': '4-the-pedagogical-inversion.html',
    '5': '5-the-confidence-collision.html',
}

INTRO_CARD_CSS = '''
/* Paper cards */
.paper-card {
  background: var(--bg-surface, #f2f1ee);
  border: 1px solid var(--border-light, #e8e7e3);
  border-radius: 6px;
  padding: 1.4rem 1.6rem;
  margin-bottom: 1rem;
  transition: border-color 0.15s, box-shadow 0.15s;
}
.paper-card:hover { border-color: var(--accent); box-shadow: 0 2px 8px rgba(0,0,0,0.06); }
.paper-card h3 {
  font-family: var(--sans, sans-serif);
  font-size: 1rem; font-weight: 600;
  color: var(--text); margin: 0 0 0.15rem;
}
.paper-card .genre {
  font-family: var(--mono, monospace);
  font-size: 0.72rem; color: var(--text-muted);
  text-transform: uppercase; letter-spacing: 0.06em;
  margin-bottom: 0.6rem;
}
.paper-card p { font-size: 0.92rem; color: var(--text-secondary); margin-bottom: 0; line-height: 1.65; }
.paper-card-link { text-decoration: none; color: inherit; display: block; }

/* Epilogue card */
.epilogue-card {
  background: var(--bg-surface, #f2f1ee);
  border: 1px dashed var(--border, #d8d7d3);
  border-radius: 6px;
  padding: 1.4rem 1.6rem;
  margin-top: 1.5rem;
  transition: border-color 0.15s;
}
.epilogue-card:hover { border-color: var(--accent); }
.epilogue-card h3 { font-family: var(--sans, sans-serif); font-size: 1rem; font-weight: 600; color: var(--text-muted); margin: 0 0 0.15rem; }
.epilogue-card .genre { font-family: var(--mono, monospace); font-size: 0.72rem; color: var(--text-muted); text-transform: uppercase; letter-spacing: 0.06em; margin-bottom: 0.6rem; }
.epilogue-card p { font-size: 0.92rem; color: var(--text-muted); margin-bottom: 0.6rem; line-height: 1.65; }
'''


def style_intro_cards(html):
    """Transform paper summary paragraphs in the intro into clickable cards."""
    
    def make_card(m):
        full_p = m.group(0)
        strong_match = re.search(r'<strong>(Paper (\d+)\s*[—–]\s*([^:]+)(?::\s*[^<]+)?)</strong>', full_p)
        if not strong_match:
            return full_p
        
        paper_num = strong_match.group(2)
        short_title = strong_match.group(3).strip()
        
        # Extract genre (italic text)
        genre_match = re.search(r'<em>Genre:\s*([^.]+)\.(?:\s*Series role:[^<]*)?</em>', full_p)
        genre = genre_match.group(1).strip() if genre_match else ''
        
        # Extract description: everything after the genre em tag
        desc = full_p
        # Remove the strong title
        desc = re.sub(r'<strong>.*?</strong>\s*', '', desc)
        # Remove the genre em
        desc = re.sub(r'<em>Genre:.*?</em>\s*', '', desc)
        # Remove wrapping <p> tags
        desc = re.sub(r'^<p>\s*', '', desc)
        desc = re.sub(r'\s*</p>$', '', desc)
        desc = desc.strip()
        
        url = BASE_URL + PAPER_URLS.get(paper_num, '#')
        
        return (f'<a href="{url}" class="paper-card-link"><div class="paper-card">\n'
                f'<h3>Paper {paper_num} — {short_title}</h3>\n'
                f'{f"""<p class="genre">{genre}</p>""" if genre else ""}\n'
                f'<p>{desc}</p>\n'
                f'</div></a>')
    
    # Match paragraphs starting with <strong>Paper N
    html = re.sub(
        r'<p><strong>Paper \d+.*?</p>',
        make_card,
        html,
        flags=re.DOTALL
    )
    
    # Handle the Epilogue section
    epi_pattern = (r'<h2>Epilogue[^<]*</h2>\s*'
                   r'<p><strong>The Symbiont Hypothesis[^<]*</strong>\s*'
                   r'<em>[^<]*</em></p>\s*'
                   r'(?:<p>.*?</p>\s*)*')
    epi_match = re.search(epi_pattern, html, re.DOTALL)
    
    if epi_match:
        # Extract the epilogue content
        epi_html = epi_match.group(0)
        h2 = re.search(r'<h2[^>]*>[^<]*</h2>', epi_html).group(0)
        
        # Get genre
        genre_m = re.search(r'<em>([^<]*)</em>', epi_html)
        genre = genre_m.group(1).replace('Genre: ', '').strip() if genre_m else ''
        
        # Get description paragraphs (everything after the first <p> with strong/em)
        desc_paras = re.findall(r'<p>(?!<strong>)(.*?)</p>', epi_html, re.DOTALL)
        desc_html = '\n'.join(f'<p>{d}</p>' for d in desc_paras if d.strip())
        
        epi_url = BASE_URL + 'the-symbiont-hypothesis-epilogue.html'
        
        replacement = (f'{h2}\n\n'
                      f'<a href="{epi_url}" class="paper-card-link"><div class="epilogue-card">\n'
                      f'<h3>The Symbiont Hypothesis</h3>\n'
                      f'{f"""<p class="genre">{genre}</p>""" if genre else ""}\n'
                      f'{desc_html}\n'
                      f'</div></a>')
        
        html = html[:epi_match.start()] + replacement + html[epi_match.end():]
    
    return html


def build_front_matter(front_md):
    lines = front_md.split('\n')
    filtered = []
    for line in lines:
        # Skip title and subtitle (go in header)
        if line.startswith('# ') or line.startswith('### '):
            continue
        # Skip tagline
        if re.match(r'^\*[^*]{5,80}\*$', line.strip()):
            continue
        # Skip Author/Date/DOI/Authors lines (already in meta-block)
        if re.match(r'^\*\*(Authors?|Date|DOI):\*\*', line.strip()):
            continue
        filtered.append(line)
    return md_to_html('\n'.join(filtered))


def build_paper(md_filename):
    md_path = os.path.join(SRC, md_filename)
    md_text = open(md_path).read()

    title_tuple = TITLES.get(md_filename, ('Untitled', '', 'Untitled'))
    title = title_tuple[0]
    subtitle = title_tuple[1]
    html_title = title_tuple[2]
    tagline = title_tuple[3] if len(title_tuple) > 3 else ''
    css = load_css(md_filename)

    front_md, body_md = split_front_and_body(md_text)

    front_html = build_front_matter(front_md)
    body_html = md_to_html(body_md)

    body_html = embed_image_svgs(body_html)
    front_html = embed_image_svgs(front_html)
    body_html = embed_webp_images(body_html)
    front_html = embed_webp_images(front_html)

    if md_filename == '1-the-confidence-vulnerability-v6.md':
        body_html = embed_p1_figures(body_html)

    body_html = merge_blockquote_captions(body_html)
    body_html = wrap_sections(body_html)
    
    # Style the appendix inline TOC
    if 'appendices' in md_filename:
        body_html = style_appendix_toc(body_html)
    
    # Style test document parchments
    if 'test-documents' in md_filename:
        body_html = style_test_documents(body_html)
    
    # Style intro paper cards
    if md_filename.startswith('0-'):
        body_html = style_intro_cards(body_html)

    # Add heading IDs and build TOC
    body_html, toc_entries = add_heading_ids(body_html)
    toc_html = build_toc_html(toc_entries)

    front_html = make_full_links(front_html)
    body_html = make_full_links(body_html)
    body_html = guard_heading_orphans(body_html)
    # Remove heading-guards from first-body headings (thesis/abstract) — they can't orphan
    # and the guard prevents them from sharing the page with front matter
    body_html = re.sub(r'<div class="heading-guard">(<h2 id="thesis">.*?</p>)</div>', r'\1', body_html, flags=re.DOTALL)
    body_html = re.sub(r'<div class="heading-guard">(<h2 id="abstract">.*?</p>)</div>', r'\1', body_html, flags=re.DOTALL)

    ORCID_LINK = '<a href="https://orcid.org/0009-0003-1095-5855" title="ORCID" style="text-decoration:none;"><svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 256 256" style="vertical-align:-2px;margin-left:3px;"><circle cx="128" cy="128" r="128" fill="#A6CE39"/><path fill="#fff" d="M86.3 186.2H70.9V79.1h15.4v107.1zm2.4-129.4c0 5.5-4.5 10.1-10.1 10.1-5.6 0-10.1-4.6-10.1-10.1 0-5.6 4.5-10.1 10.1-10.1 5.6 0 10.1 4.6 10.1 10.1zM108.9 79.1h41.6c39.6 0 57 28.3 57 53.6 0 27.5-21.5 53.6-56.8 53.6h-41.8V79.1zm15.4 93.3h24.5c34.9 0 42.9-26.5 42.9-39.7 0-21.5-13.7-39.7-43.7-39.7h-23.7v79.4z"/></svg></a>'

    PAPER_DOIS = {
        '0-the-confidence-curriculum-series-introduction-v8.md': '10.5281/zenodo.19198621',
        '1-the-confidence-vulnerability-v6.md': '10.5281/zenodo.19199055',
        '1-the-confidence-vulnerability-v6-appendices.md': '10.5281/zenodo.19199055',
        '1-the-confidence-vulnerability-v6-test-documents.md': '10.5281/zenodo.19199055',
        '2-the-skill-ceiling-v6.md': '10.5281/zenodo.19199328',
        '3-the-knowledge-horizon-v7.md': '10.5281/zenodo.19199657',
        '4-the-pedagogical-inversion-v6.md': '10.5281/zenodo.19199682',
        '5-the-confidence-collision-v4.md': '10.5281/zenodo.19199987',
    }

    if 'epilogue' in md_filename:
        author_line = '<strong>Authors:</strong> HiP (Ivan Phan)' + ORCID_LINK + ' &amp; Claude (Anthropic)'
    else:
        author_line = '<strong>Author:</strong> HiP (Ivan Phan)' + ORCID_LINK

    # Determine if this is the appendix (needs back-to-top links)
    # Structure variants per file type
    is_intro = md_filename.startswith('0-') or md_filename.startswith('the-confidence-curriculum-reading')
    is_appendix = 'appendices' in md_filename
    is_testdoc = 'test-documents' in md_filename
    is_paper = not is_intro and not is_appendix and not is_testdoc
    
    container_class = 'paper-container' if is_paper else 'container'
    header_class = 'paper-header' if is_paper else 'series-header' if is_intro else 'doc-header'
    
    extra_css = BREATHE_CSS + TOC_CSS + (BACK_TO_TOP_CSS if is_appendix else '')
    if is_intro and md_filename.startswith('0-'):
        extra_css += INTRO_CARD_CSS
    if is_testdoc:
        extra_css += RAW_STIMULUS_CSS
    
    # Targeted page-break overrides for headings that remain orphaned
    # despite the heading-guard (wkhtmltopdf ignores page-break on children
    # of break-inside:avoid containers — inject a break element before the guard div)
    FORCE_BREAK_BEFORE = {
        '0-the-confidence-curriculum-series-introduction': ['research-agenda'],
        '1-the-confidence-vulnerability-v6.md': ['23-baseline-handling-patterns', '92-harder-but-possible', '6-related-work', '69-provenance-and-digital-trust'],
        '1-the-confidence-vulnerability-appendices': ['d2-false-positives-under-security-framing'],
        '2-the-skill-ceiling': ['6-the-structural-problem-skills-and-prompt-injection-share-a', '64-digital-signatures-as-kerckhoffs-compliant-protection', '8-principle-7-author-side-behavioural-stopgap'],
        '3-the-knowledge-horizon': ['regulatory-and-accountability', '59-cross-disciplinary-testing-invitation', '32-what-counts-and-what-doesnt', 'agentic-safety-and-misalignment', 'methodology-notes'],
        '4-the-pedagogical-inversion': [],
        '5-the-confidence-collision': ['3-the-proposal-a-post-alignment-epistemic-training-phase'],
        'the-confidence-curriculum-reading-guide': ['4-cognitive-psychologists-and-education-researchers', '5-labour-economists'],
    }
    for prefix, ids in FORCE_BREAK_BEFORE.items():
        if md_filename.startswith(prefix):
            for hid in ids:
                # Insert a page-break div before the heading (or its guard wrapper)
                # Try heading-guard first, fall back to bare heading
                guard_pattern = f'<div class="heading-guard"><h2 id="{hid}"'
                guard_pattern_h3 = f'<div class="heading-guard"><h3 id="{hid}"'
                bare_h2 = f'<h2 id="{hid}"'
                bare_h3 = f'<h3 id="{hid}"'
                
                page_break = '<div style="page-break-before:always;break-before:page;"></div>'
                
                for pat in [guard_pattern, guard_pattern_h3, bare_h2, bare_h3]:
                    if pat in body_html:
                        body_html = body_html.replace(pat, page_break + pat, 1)
                        break
    
    extra_js = TOC_JS + (BACK_TO_TOP_JS if is_appendix else '')

    if is_intro and md_filename.startswith('0-'):
        meta_html = f'<p class="meta">HiP (Ivan Phan) {ORCID_LINK} &middot; March 2026 &middot; <span style="white-space:nowrap">DOI: <a href="https://doi.org/10.5281/zenodo.19198621">10.5281/zenodo.19198621</a></span></p>'
        tagline_html = f'<p class="tagline">{tagline}</p>' if tagline else ''
    elif is_intro:
        # Reading guide — no DOI/ORCID
        meta_html = f'<p class="meta">HiP (Ivan Phan) &middot; March 2026</p>'
        tagline_html = ''
    else:
        paper_doi = PAPER_DOIS.get(md_filename, '')
        doi_html = f' &middot; <span style="white-space:nowrap">DOI: <a href="https://doi.org/{paper_doi}">{paper_doi}</a></span>' if paper_doi else ''
        meta_html = f'''<div class="meta-block">
<p>{author_line} &middot; <strong>Date:</strong> March 2026{doi_html}</p>
</div>'''
        tagline_html = ''

    # Build Google Fonts link
    font_families = GOOGLE_FONTS.get(md_filename, '')
    if font_families:
        font_link = (f'<link rel="preconnect" href="https://fonts.googleapis.com">\n'
                     f'<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
                     f'<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family={font_families}&display=swap">')
    else:
        font_link = ''

    # Build CSS variable bridge (only for papers with missing variables)
    css_bridge = build_css_var_bridge(css)

    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{html_title}</title>
{font_link}
<style>
{css}
{css_bridge}
{extra_css}
</style>
</head>
<body>

{toc_html}

{'<header class="' + header_class + '">' if is_intro else '<div class="' + container_class + '"><header class="' + header_class + '">'}
<h1>{title}</h1>
{f'<p class="subtitle">{subtitle}</p>' if subtitle else ''}
{tagline_html}
{meta_html if is_intro else ''}
</header>

{'<div class="' + container_class + '">' if is_intro else ''}

{'' if is_intro else meta_html}

<div class="front-matter">
{front_html}
<hr />
</div>

<main class="paper-body">
{body_html}
</main>

</div>

{extra_js}
</body>
</html>
'''
    return html


def main():
    targets = sys.argv[1:] if len(sys.argv) > 1 else list(FILE_MAP.keys())
    for md_filename in targets:
        if md_filename not in FILE_MAP:
            print(f"✗ Unknown: {md_filename}")
            continue
        if md_filename not in TITLES:
            print(f"⊘ Skipping (no title info): {md_filename}")
            continue
        try:
            html = build_paper(md_filename)
            out_path = os.path.join(REPO, FILE_MAP[md_filename])
            open(out_path, 'w').write(html)
            svg_count = html.count('<svg')
            fig_count = html.count('<figure')
            toc_count = html.count('toc-link')
            print(f"✓ {md_filename} → {FILE_MAP[md_filename]}  "
                  f"[{len(html)//1024}KB, {svg_count} SVG, {fig_count} fig, {toc_count} TOC]")
        except Exception as e:
            import traceback
            print(f"✗ {md_filename}: {e}")
            traceback.print_exc()
    
    # Copy intro HTML to index.html (landing page)
    intro_path = os.path.join(REPO, FILE_MAP['0-the-confidence-curriculum-series-introduction-v8.md'])
    index_path = os.path.join(REPO, 'index.html')
    if os.path.exists(intro_path):
        import shutil
        shutil.copy2(intro_path, index_path)
        print(f"✓ Copied intro → index.html")


if __name__ == '__main__':
    main()
