import os
import re

DIR = r"c:\Users\HP ZBOOK\Downloads\Golden eagle\redesign"
CSS_FILE = os.path.join(DIR, "styles.css")

with open(CSS_FILE, "r", encoding="utf-8") as f:
    css = f.read()

# Replace the broken media query
target = """    .nav-sidebar {
        width: 60px;
    }
    .nav-switch {
        width: 60px;
        height: 60px;
    }
    .nav-menu {
        padding-left: 60px;
    }"""

replacement = """    .nav-sidebar {
        width: auto;
    }
    .nav-switch {
        width: 55px;
        height: 110px;
        padding-left: 10px;
    }
    .nav-switch-inner {
        width: 20px;
        height: 16px;
    }
    .nav-switch.active .nav-switch-line:nth-child(1) {
        transform: translateY(7px) rotate(45deg);
    }
    .nav-switch.active .nav-switch-line:nth-child(3) {
        transform: translateY(-7px) rotate(-45deg);
    }
    .nav-menu {
        padding-left: 55px;
    }"""

# Use a flexible regex to handle \r\n vs \n spaces
target_regex = r'\.nav-sidebar\s*\{\s*width:\s*60px;\s*\}\s*\.nav-switch\s*\{\s*width:\s*60px;\s*height:\s*60px;\s*\}\s*\.nav-menu\s*\{\s*padding-left:\s*60px;\s*\}'
css = re.sub(target_regex, replacement, css)

with open(CSS_FILE, "w", encoding="utf-8") as f:
    f.write(css)

print("Mobile nav successfully fixed.")
