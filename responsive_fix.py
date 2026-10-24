import os

DIR = r"c:\Users\HP ZBOOK\Downloads\Golden eagle\redesign"
CSS_FILE = os.path.join(DIR, "styles.css")

responsive_css = """
/* ==========================================================================
   RESPONSIVENESS & MOBILE ADAPTABILITY
   ========================================================================== */

/* --- Typography & Hero Sections --- */
@media (max-width: 991px) {
    .hero-tagline {
        font-size: 2.5rem !important;
        padding: 0 20px;
    }
    .head-top h2 {
        font-size: 1.2rem;
        padding: 0 20px;
    }
    .page-intro {
        padding: 60px 20px 40px;
    }
    .page-intro h2 {
        font-size: 2.2rem;
    }
}

@media (max-width: 576px) {
    .hero-tagline {
        font-size: 2rem !important;
    }
    .page-intro h2 {
        font-size: 1.8rem;
    }
    .btn {
        padding: 10px 20px;
        font-size: 0.85rem;
    }
}

/* --- Alternating Image/Text Blocks (destacados) --- */
@media (max-width: 991px) {
    .destacados-img-text {
        flex-direction: column !important;
    }
    .destacados-img {
        width: 100% !important;
        height: 300px;
    }
    .destacados-img.order-2 {
        order: 1 !important;
    }
    .destacados-content {
        width: 100% !important;
        padding: 40px 30px !important;
    }
    .destacados-content.order-1 {
        order: 2 !important;
    }
}

/* --- Navigation & Menu --- */
@media (max-width: 991px) {
    .nav-sidebar {
        width: 60px;
    }
    .nav-switch {
        width: 60px;
        height: 60px;
    }
    .nav-menu {
        padding-left: 60px;
    }
    .nav-menu-links {
        flex-direction: column;
        gap: 30px;
        padding: 30px 20px;
        overflow-y: auto;
        height: calc(100vh - 80px);
    }
    .nav-menu-top {
        padding: 15px 20px;
        flex-direction: column;
        gap: 15px;
    }
    .top-search-white, .top-search-color {
        display: none;
    }
}

/* --- Premium Grids & Cards --- */
@media (max-width: 768px) {
    .premium-grid {
        grid-template-columns: 1fr;
        padding: 0 20px 60px;
    }
    .card-img {
        height: 220px;
    }
    .card-content {
        padding: 30px 20px;
    }
}

/* --- Map & Global Presence --- */
@media (max-width: 991px) {
    .mapa-filtre {
        flex-direction: column;
        gap: 15px;
        align-items: center;
        margin-bottom: 30px;
    }
    .mapa-container {
        height: 300px;
    }
    .map-dot:hover .tooltip {
        transform: translateX(-50%) translateY(20px);
        font-size: 0.7rem;
    }
    .cifras-lista {
        position: relative;
        bottom: 0;
        flex-direction: column;
        align-items: center;
        gap: 20px;
        margin-top: 20px;
    }
    .cifra-box {
        width: 90%;
        max-width: 300px;
        padding: 15px 20px;
    }
    .cifra-box .cifra {
        font-size: 2.5rem;
    }
    .mapa-home {
        padding-bottom: 80px;
    }
}

/* --- Slider & Related Items (News) --- */
@media (max-width: 768px) {
    .mod-slider .slide-texto {
        position: relative;
        width: 100%;
        padding: 40px 20px;
        background: rgba(0,0,0,0.8);
    }
    .mod-slider .slide-content {
        flex-direction: column;
    }
    .lista-contenido {
        grid-template-columns: 1fr;
    }
    .lista-contenido li img {
        height: 200px;
    }
}

/* --- Footer --- */
@media (max-width: 991px) {
    .footer-grid {
        grid-template-columns: 1fr 1fr;
        gap: 40px;
    }
}
@media (max-width: 576px) {
    .footer-grid {
        grid-template-columns: 1fr;
        text-align: center;
    }
    .footer-bottom {
        flex-direction: column;
        gap: 20px;
        text-align: center;
    }
}
"""

def run():
    with open(CSS_FILE, "a", encoding="utf-8") as f:
        f.write("\n" + responsive_css)
    print("Responsiveness rules successfully appended to styles.css.")

if __name__ == "__main__":
    run()
