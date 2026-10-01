import os
import re

base_dir = r"c:\Users\HP ZBOOK\Downloads\Golden eagle\redesign"

# 1. Update navigation in all HTML files
html_files = [f for f in os.listdir(base_dir) if f.endswith('.html')]
en_html_files = [f for f in os.listdir(os.path.join(base_dir, 'en')) if f.endswith('.html')]

# We'll create products.html and en/products.html based on services.html and en/services.html

fr_nav_link = '<li><a href="services.html" class="nav-link">Nos Services</a></li>'
fr_nav_link_active = '<li><a href="services.html" class="nav-link active">Nos Services</a></li>'
fr_new_nav_link = '<li><a href="products.html" class="nav-link">Produits & Équipements</a></li>'

en_nav_link = '<li><a href="services.html" class="nav-link">Our Services</a></li>'
en_nav_link_active = '<li><a href="services.html" class="nav-link active">Our Services</a></li>'
en_new_nav_link = '<li><a href="products.html" class="nav-link">Products & Equipment</a></li>'

fr_footer_link = '<li><a href="services.html">Nos Services</a></li>'
fr_new_footer_link = '<li><a href="products.html">Produits & Équipements</a></li>'

en_footer_link = '<li><a href="services.html">Our Services</a></li>'
en_new_footer_link = '<li><a href="products.html">Products & Equipment</a></li>'

def update_file(filepath, nav, nav_active, new_nav, footer, new_footer):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if new_nav not in content:
        # replace nav link
        content = content.replace(nav, nav + '\n                    ' + new_nav)
        content = content.replace(nav_active, nav_active + '\n                    ' + new_nav)
        # replace footer link
        content = content.replace(footer, footer + '\n                        ' + new_footer)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {filepath}")

for f in html_files:
    update_file(os.path.join(base_dir, f), fr_nav_link, fr_nav_link_active, fr_new_nav_link, fr_footer_link, fr_new_footer_link)

for f in en_html_files:
    update_file(os.path.join(base_dir, 'en', f), en_nav_link, en_nav_link_active, en_new_nav_link, en_footer_link, en_new_footer_link)
