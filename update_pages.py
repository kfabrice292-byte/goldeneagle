import os

DIR = r"c:\Users\HP ZBOOK\Downloads\Golden eagle\redesign"

with open(os.path.join(DIR, "index.html"), "r", encoding="utf-8") as f:
    index_html = f.read()

# Using string splitting to extract precisely
# Nav Sidebar
nav_sidebar_start = index_html.find('<!-- MAXAM Left Nav Switch (Triangle) -->')
nav_sidebar_end = index_html.find('<!-- The actual menu (hidden by default) -->')
nav_sidebar = index_html[nav_sidebar_start:nav_sidebar_end]

# Overlay Menu
overlay_start = index_html.find('<!-- The actual menu (hidden by default) -->')
overlay_end = index_html.find('<!-- Header -->')
overlay_menu = index_html[overlay_start:overlay_end]

# Header
header_start = index_html.find('<!-- Header -->')
header_end = index_html.find('<main class="main">')
header = index_html[header_start:header_end]

# Footer
footer_start = index_html.find('<footer class="footer">')
footer_end = index_html.find('<script src="script.js"></script>')
footer = index_html[footer_start:footer_end]

print("Extracted components.")

# Apply to other pages
pages = ["about.html", "services.html", "products.html", "contact.html"]

for page in pages:
    page_path = os.path.join(DIR, page)
    if not os.path.exists(page_path):
        continue
    with open(page_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Nav Sidebar replacing
    old_nav_start = content.find('<!-- 1. MAXAM Signature Corner Gold Triangle Menu Trigger -->')
    old_nav_end = content.find('<!-- 2. MAXAM Fullscreen Overlay Navigation Menu -->')
    if old_nav_start != -1 and old_nav_end != -1:
        content = content[:old_nav_start] + nav_sidebar + content[old_nav_end:]
        
    # Overlay Menu replacing
    old_over_start = content.find('<!-- 2. MAXAM Fullscreen Overlay Navigation Menu -->')
    old_over_end = content.find('<!-- 3. Top Header Bar')
    if old_over_start != -1 and old_over_end != -1:
        content = content[:old_over_start] + overlay_menu + content[old_over_end:]
        
    # Header replacing
    old_head_start = content.find('<!-- 3. Top Header Bar')
    old_head_end = content.find('<!-- 4. Page Header Banner -->')
    if old_head_start != -1 and old_head_end != -1:
        content = content[:old_head_start] + header + content[old_head_end:]
        
    # Footer replacing
    old_foot_start = content.find('<!-- 8. MAXAM Corporate Footer -->')
    if old_foot_start == -1:
        old_foot_start = content.find('<!-- 7. MAXAM Corporate Footer -->')
    if old_foot_start == -1:
        old_foot_start = content.find('<!-- MAXAM Corporate Footer -->')
        
    old_foot_end = content.find('<!-- Scripts -->')
    if old_foot_end == -1:
        old_foot_end = content.find('<script')
        
    if old_foot_start != -1 and old_foot_end != -1:
        content = content[:old_foot_start] + footer + content[old_foot_end:]
        
    with open(page_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Updated {page}")

# Merge old CSS for specific pages into styles.css
try:
    with open(os.path.join(DIR, "old_styles.css"), "r", encoding="utf-16") as f:
        old_css = f.read()
except UnicodeDecodeError:
    with open(os.path.join(DIR, "old_styles.css"), "r", encoding="utf-8") as f:
        old_css = f.read()

page_header_idx = old_css.find(".page-header")
if page_header_idx != -1:
    start_idx = old_css.rfind("/*", 0, page_header_idx)
    if start_idx == -1:
        start_idx = page_header_idx
    append_css = old_css[start_idx:]
    with open(os.path.join(DIR, "styles.css"), "a", encoding="utf-8") as f:
        f.write("\n\n/* === RECOVERED PAGE STYLES === */\n")
        f.write(append_css)
    print("Appended page styles to styles.css")
else:
    print("Could not find .page-header in old_styles.css")
