import os
import re

DIR = r"c:\Users\HP ZBOOK\Downloads\Golden eagle\redesign"
CSS_FILE = os.path.join(DIR, "styles.css")

with open(CSS_FILE, "r", encoding="utf-8") as f:
    css = f.read()

# 1. Remove the malicious old .nav-menu override on mobile
bad_nav_menu_regex = r'\.nav-menu\s*\{\s*position:\s*absolute;\s*top:\s*100%;\s*left:\s*0;\s*width:\s*100%;\s*\}'
css = re.sub(bad_nav_menu_regex, "", css)

# 2. Make sure .head-top is position: absolute on all screen sizes so it overlays the hero image
# We'll just append an !important override to the bottom of the file
css += """
/* FORCE HEADER TO OVERLAY HERO ON MOBILE */
.head-top {
    position: absolute !important;
    top: 0 !important;
    left: 0 !important;
    right: 0 !important;
    z-index: 1000 !important;
    background: transparent !important; /* Fix white background issue on mobile */
}

/* Ensure the gold overlay menu stays fixed to the viewport when opened */
@media (max-width: 991px) {
    .nav-menu {
        position: fixed !important;
        top: 0 !important;
        height: 100vh !important;
    }
}
"""

with open(CSS_FILE, "w", encoding="utf-8") as f:
    f.write(css)

print("CSS Fixed: Old nav-menu override removed, header forced absolute.")
