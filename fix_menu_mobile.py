import os
import re

DIR = r"c:\Users\HP ZBOOK\Downloads\Golden eagle\redesign"

# 1. Update script.js to close menu on link click
script_path = os.path.join(DIR, "script.js")
with open(script_path, "r", encoding="utf-8") as f:
    script = f.read()

menu_close_logic = """
    if (navSwitch && navMenu) {
        navSwitch.addEventListener("click", () => {
            navSwitch.classList.toggle("active");
            navMenu.classList.toggle("active");
        });
        
        // Close menu when a link is clicked (especially important for mobile and anchor links)
        const navLinks = navMenu.querySelectorAll("a");
        navLinks.forEach(link => {
            link.addEventListener("click", () => {
                navSwitch.classList.remove("active");
                navMenu.classList.remove("active");
            });
        });
    }
"""
script = re.sub(r'if \(navSwitch && navMenu\) \{.*?\n    \}', menu_close_logic.strip(), script, flags=re.DOTALL)

with open(script_path, "w", encoding="utf-8") as f:
    f.write(script)


# 2. Update styles.css to fix nested scrolling on mobile menu
css_path = os.path.join(DIR, "styles.css")
with open(css_path, "r", encoding="utf-8") as f:
    css = f.read()

# The bad CSS block:
#     .nav-menu-links {
#         flex-direction: column;
#         gap: 30px;
#         padding: 30px 20px;
#         overflow-y: auto;
#         height: calc(100vh - 80px);
#     }

bad_css_regex = r'\.nav-menu-links\s*\{\s*flex-direction:\s*column;\s*gap:\s*30px;\s*padding:\s*30px 20px;\s*overflow-y:\s*auto;\s*height:\s*calc\(100vh - 80px\);\s*\}'
good_css = """    .nav-menu-links {
        flex-direction: column;
        gap: 20px;
        padding: 20px 20px 80px 10px;
        overflow-y: visible;
        height: auto;
    }"""
    
css = re.sub(bad_css_regex, good_css, css)

# Make sure the top logo is smaller so the menu header isn't too tall
css = css.replace(
    ".nav-menu-top .logo-white img {\n    max-width: 250px;\n}",
    ".nav-menu-top .logo-white img {\n    max-width: 200px;\n}"
)

# And make sure .nav-menu doesn't have clipping issues
# Let's add a safe padding bottom to .nav-menu itself
css += """
@media (max-width: 991px) {
    .nav-menu {
        padding-bottom: 50px;
    }
    /* Ensure the toggle button is easy to tap by increasing touch target implicitly */
    .nav-switch {
        cursor: pointer;
        touch-action: manipulation;
    }
}
"""

with open(css_path, "w", encoding="utf-8") as f:
    f.write(css)

print("Mobile menu fixed: auto-close on click, and double-scroll bug removed.")
