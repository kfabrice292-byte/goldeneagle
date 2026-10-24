import os
import re

DIR = r"c:\Users\HP ZBOOK\Downloads\Golden eagle\redesign"

def run():
    # 1. Read index.html
    with open(os.path.join(DIR, "index.html"), "r", encoding="utf-8") as f:
        idx = f.read()
        
    # First, let's fix the # links in index.html in Python memory
    # We will replace the whole nav-menu-links block with properly typed links
    new_nav_links = """<div class="nav-menu-links">
            <div class="nav-box">
                <h4>À PROPOS DE GOLDEN EAGLE</h4>
                <ul>
                    <li><a href="about.html">Notre Entreprise</a></li>
                    <li><a href="about.html#presence">Présence Globale</a></li>
                    <li><a href="services.html">Technologie & R&D</a></li>
                    <li><a href="about.html#brand">Notre Marque</a></li>
                </ul>
            </div>
            <div class="nav-box">
                <h4>INDUSTRIES & SOLUTIONS</h4>
                <ul>
                    <li><a href="products.html">Explosifs Civils</a></li>
                    <li><a href="services.html">Forage & Minage</a></li>
                    <li><a href="products.html#mmu">Unités Mobiles MMU</a></li>
                    <li><a href="services.html#consultation">Ingénierie & Conseil</a></li>
                </ul>
            </div>
            <div class="nav-box">
                <h4>NOTRE ENGAGEMENT</h4>
                <ul>
                    <li><a href="about.html#safety">Culture de la Sécurité</a></li>
                    <li><a href="about.html#people">Passion pour les Hommes</a></li>
                    <li><a href="about.html#ethics">Comportement Éthique</a></li>
                    <li><a href="about.html#environment">Protection de l'Environnement</a></li>
                </ul>
            </div>
            <div class="nav-box">
                <h4>PRODUITS & COTATIONS</h4>
                <ul>
                    <li><a href="products.html">Catalogue d'Explosifs</a></li>
                    <li><a href="products.html">Boosters & Détonateurs</a></li>
                    <li><a href="products.html">Demande de Cotation</a></li>
                    <li><a href="contact.html">Support Artificiers</a></li>
                </ul>
            </div>
        </div>"""
        
    idx = re.sub(r'<div class="nav-menu-links">.*?</div>\s*</div>\s*</nav>', new_nav_links + '\n    </nav>', idx, flags=re.DOTALL)
    
    # Also fix footer links in memory
    new_footer_links = """<footer class="footer">
        <div class="container">
            <div class="footer-grid">
                <div>
                    <h4>À PROPOS DE GOLDEN EAGLE</h4>
                    <ul>
                        <li><a href="about.html">Notre entreprise</a></li>
                        <li><a href="about.html#presence">Présence globale</a></li>
                        <li><a href="services.html">Technologie</a></li>
                        <li><a href="about.html#brand">Notre marque</a></li>
                    </ul>
                </div>
                <div>
                    <h4>INDUSTRIES & SOLUTIONS</h4>
                    <ul>
                        <li><a href="products.html">Explosifs Civils</a></li>
                        <li><a href="services.html">Forage & Minage</a></li>
                        <li><a href="services.html#topographie">Etudes & Modélisation</a></li>
                    </ul>
                </div>
                <div>
                    <h4>NOTRE ENGAGEMENT</h4>
                    <ul>
                        <li><a href="about.html#safety">Culture de la sécurité</a></li>
                        <li><a href="about.html#people">Passion pour les hommes</a></li>
                        <li><a href="about.html#environment">Environnement</a></li>
                    </ul>
                </div>
                <div>
                    <img src="assets/web_829_logo_logo.png" alt="Golden Eagle" style="width: 150px; filter: brightness(0) invert(1); margin-bottom: 20px;">
                    <p>Une entreprise de référence spécialisée dans le forage et le minage civil.</p>
                </div>
            </div>
            <div class="footer-bottom">
                <div>&copy; 2026 Golden Eagle SARL. Tous droits réservés.</div>
                <div>
                    <a href="about.html" style="color:var(--gray-text); margin-right: 15px;">Mentions légales</a>
                    <a href="about.html" style="color:var(--gray-text);">Politique de confidentialité</a>
                </div>
            </div>
        </div>
    </footer>"""
    
    idx = re.sub(r'<footer class="footer">.*?</footer>', new_footer_links, idx, flags=re.DOTALL)
    
    # Save back index.html
    with open(os.path.join(DIR, "index.html"), "w", encoding="utf-8") as f:
        f.write(idx)
        
    # Extract the full top section (from after body tag to before main/page-header)
    top_section_match = re.search(r'(<div class="nav-sidebar">.*?</header>)', idx, re.DOTALL)
    top_section = top_section_match.group(1)
    
    # Apply to other pages
    pages = ["about.html", "services.html", "products.html", "contact.html"]
    
    for page in pages:
        page_path = os.path.join(DIR, page)
        if not os.path.exists(page_path):
            continue
        with open(page_path, "r", encoding="utf-8") as f:
            content = f.read()
            
        # Replace top part (everything between <body class="..."> and <section class="page-header"> or similar)
        content = re.sub(r'(<body[^>]*>).*?(<section class="page-header">|<section class="about-content-section)', r'\1\n\n' + top_section.replace('\\', '\\\\') + r'\n\n\2', content, flags=re.DOTALL)
        
        # Replace footer part
        content = re.sub(r'<footer .*?</footer>', new_footer_links.replace('\\', '\\\\'), content, flags=re.DOTALL)
        
        with open(page_path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Updated {page}")

run()
