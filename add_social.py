import os
import re

html_files = []
for root, _, files in os.walk(r'c:\Users\HP ZBOOK\Downloads\Golden eagle\redesign'):
    for f in files:
        if f.endswith('.html'):
            html_files.append(os.path.join(root, f))

social_html = """
                    <div class="social-links">
                        <a href="https://web.facebook.com/melveen11" target="_blank" class="social-link" title="Facebook"><i class="fab fa-facebook-f"></i></a>
                    </div>"""

pattern = re.compile(r'(<p class="footer-desc">.*?</p>)', re.DOTALL)

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if '<div class="social-links">' not in content:
        new_content = pattern.sub(r'\1' + social_html, content)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {filepath}")
