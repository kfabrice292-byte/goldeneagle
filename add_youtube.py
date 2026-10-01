import os
import re

html_files = []
for root, _, files in os.walk(r'c:\Users\HP ZBOOK\Downloads\Golden eagle\redesign'):
    for f in files:
        if f.endswith('.html'):
            html_files.append(os.path.join(root, f))

youtube_html = '\n                        <a href="https://youtube.com/@goldeneaglesarl8811?si=srrhVOIYyCaGlpf0" target="_blank" class="social-link" title="YouTube"><i class="fab fa-youtube"></i></a>'

pattern = re.compile(r'(<a href="https://www.linkedin.com/company/godeneagle"[^>]*><i class="fab fa-linkedin-in"></i></a>)')

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if 'fa-youtube' not in content:
        new_content = pattern.sub(r'\1' + youtube_html, content)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {filepath}")
