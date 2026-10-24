import os

DIR = r"c:\Users\HP ZBOOK\Downloads\Golden eagle\redesign"
CSS_FILE = os.path.join(DIR, "styles.css")

mobile_fixes = """
/* ==========================================================================
   FINAL MOBILE FIXES (OVERFLOWS & SPACING)
   ========================================================================== */

/* Fix horizontal scroll issues completely */
html, body {
    overflow-x: hidden;
    width: 100%;
}

@media (max-width: 991px) {
    /* Header padding */
    .head-top {
        padding: 10px 15px !important;
    }
    
    /* Map Container needs to grow on mobile to fit the stacked boxes */
    .mapa-container {
        height: auto !important;
        min-height: 350px;
        padding-bottom: 40px; /* Space for boxes inside */
    }
    
    /* Make the boxes fit properly */
    .cifras-lista {
        position: relative !important;
        bottom: auto !important;
        flex-direction: column !important;
        align-items: center;
        gap: 20px;
        margin-top: 50px;
    }
    
    .cifra-box {
        width: 100% !important;
        max-width: 280px;
    }
    
    .mapa-home {
        padding-bottom: 60px !important;
    }

    /* Fix image and text block alignments for AOS */
    .destacados-img-text {
        overflow: hidden; /* prevents fade-right from breaking layout */
    }
    
    /* Formspree Contact Form Mobile */
    form {
        padding: 20px !important;
    }
}
"""

with open(CSS_FILE, "a", encoding="utf-8") as f:
    f.write("\n" + mobile_fixes)

print("Final mobile fixes appended to CSS.")
