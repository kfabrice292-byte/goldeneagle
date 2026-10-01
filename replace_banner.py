import os
import re

html_files = []
for root, _, files in os.walk(r'c:\Users\HP ZBOOK\Downloads\Golden eagle\redesign'):
    for f in files:
        if f.endswith('.html') and f != 'index.html':
            html_files.append(os.path.join(root, f))

# Pattern to capture the entire page-header section and extract the h1 content for SEO
pattern = re.compile(r'<section class="page-header">\s*<div class="container">\s*<h1 class="page-title">(.*?)</h1>.*?</div>\s*</section>', re.DOTALL)

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if the page has a .page-header
    if '<section class="page-header">' in content:
        # Determine image path based on whether file is in 'en' or not
        img_src = 'assets/bande-annonce.png'
        if 'en' in os.path.split(os.path.dirname(filepath))[1]:
            img_src = '../assets/bande-annonce.png'
            
        def replacement(match):
            h1_text = match.group(1)
            return f"""<section class="promo-header">
        <h1 class="sr-only">{h1_text}</h1>
        <img src="{img_src}" alt="SAMAO 2026 - Golden Eagle" class="promo-banner-img">
    </section>"""
            
        new_content = pattern.sub(replacement, content)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {filepath}")
