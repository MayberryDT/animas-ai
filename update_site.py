import os
from bs4 import BeautifulSoup

files = [
    'index.html', 'solutions.html', 'case-studies.html', 
    'how-it-works.html', 'engagement-model.html', 'infrastructure.html'
]

cta_text_indicators = ["call", "get started", "deploy", "contact", "initialize", "schedule", "talk", "book"]

pages = {
    'Home': 'index.html',
    'Solutions': 'solutions.html',
    'Case Studies': 'case-studies.html',
    'How it Works': 'how-it-works.html',
    'Engagement': 'engagement-model.html',
    'Infrastructure': 'infrastructure.html'
}

def extract_copy(soup, title):
    md = f"# {title}\n\n"
    for tag in soup.find_all(['h1', 'h2', 'h3', 'h4', 'p', 'li']):
        text = tag.get_text(" ", strip=True)
        if not text: continue
        if 'ANIMAS AI' in text and tag.name == 'div': continue # skip logo
        if tag.name == 'h1': md += f"## {text}\n"
        elif tag.name == 'h2': md += f"### {text}\n"
        elif tag.name == 'h3': md += f"#### {text}\n"
        elif tag.name == 'p': md += f"{text}\n\n"
        elif tag.name == 'li': md += f"- {text}\n"
    return md

cta_link = "#book-a-call"
copywriting = []

for filename in files:
    if not os.path.exists(filename): continue
    with open(filename, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f, 'html.parser')
    
    # Extract copy
    page_title = soup.title.string if soup.title else filename.replace('.html', '').title()
    copywriting.append(extract_copy(soup, page_title))
    
    # Logo Link
    logo = soup.find(string=lambda t: t and t.strip() == 'ANIMAS AI')
    if logo and logo.parent:
        p = logo.parent
        if p.name != 'a':
            p.name = 'a'
            p['href'] = 'index.html'
            p.string = 'ANIMAS AI'
    
    # Nav Links
    nav = soup.find('nav')
    if nav:
        nav_links_container = None
        for div in nav.find_all('div'):
            classes = div.get('class', [])
            if 'hidden' in classes and 'md:flex' in classes:
                nav_links_container = div
                break
        
        if nav_links_container:
            nav_links_container.clear()
            for name, url in pages.items():
                if name == 'Home': continue
                a = soup.new_tag('a', href=url)
                a['class'] = "text-neutral-400 font-medium hover:text-indigo-300 transition-colors duration-300 font-label text-sm uppercase tracking-wider"
                a.string = name
                nav_links_container.append(a)
    
    # CTAs
    for btn in soup.find_all('button'):
        text = btn.get_text(strip=True).lower()
        if any(ind in text for ind in cta_text_indicators) or "book" in text:
            btn.name = 'a'
            btn['href'] = cta_link
    
    for a in soup.find_all('a'):
        text = a.get_text(strip=True).lower()
        if any(ind in text for ind in cta_text_indicators) or "book" in text:
            a['href'] = cta_link

    # Generic href="#" buttons which might be CTAs
    for a in soup.find_all('a'):
        if a.get('href') == '#' and a.get('class'):
            classes = ' '.join(a['class'])
            if 'px-' in classes and 'py-' in classes and 'bg-gradient' in classes:
                a['href'] = cta_link
                
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(str(soup))

# Write the artifact separately
with open('/tmp/copywriting_extracted.md', 'w', encoding='utf-8') as f:
    f.write('\n\n---\n\n'.join(copywriting))

print("Done")
