import os
import re

DIR = r"c:\Users\HP ZBOOK\Downloads\Golden eagle\redesign"
CSS_FILE = os.path.join(DIR, "styles.css")

with open(CSS_FILE, "r", encoding="utf-8") as f:
    css = f.read()

# 1. Fix the nav-switch triangle on mobile to be a perfect corner triangle again
# I previously set it to width: 55px; height: 110px; padding-left: 10px;
bad_switch = r'\.nav-switch\s*\{\s*width:\s*55px;\s*height:\s*110px;\s*padding-left:\s*10px;\s*\}'
good_switch = """    .nav-switch {
        width: 70px;
        height: 70px;
        padding: 15px 0 0 15px; /* align hamburger to top-left corner */
        align-items: flex-start;
        justify-content: flex-start;
    }"""
css = re.sub(bad_switch, good_switch, css)

# Fix the nav-switch-inner so it stays intact
bad_inner = r'\.nav-switch-inner\s*\{\s*width:\s*20px;\s*height:\s*16px;\s*\}'
good_inner = """    .nav-switch-inner {
        width: 22px;
        height: 18px;
    }"""
css = re.sub(bad_inner, good_inner, css)


# 2. Hide map dots on mobile to prevent clutter and overlapping the stacked boxes
css += """
@media (max-width: 991px) {
    /* Cache les points dorés sur mobile car ils chevauchent les cases blanches empilées */
    .map-dot {
        display: none !important;
    }
}
"""

with open(CSS_FILE, "w", encoding="utf-8") as f:
    f.write(css)

print("Mobile visuals (triangle and map dots) fixed.")
