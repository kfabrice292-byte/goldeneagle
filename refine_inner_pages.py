import os

DIR = r"c:\Users\HP ZBOOK\Downloads\Golden eagle\redesign"

css_additions = """
/* === INNER PAGES PREMIUM DESIGN === */
.hero-inner {
    height: 50vh !important;
}
.page-intro {
    padding: 100px 20px 60px;
    text-align: center;
    max-width: 900px;
    margin: 0 auto;
}
.page-intro-category {
    color: var(--gold);
    font-weight: 700;
    letter-spacing: 2px;
    text-transform: uppercase;
    font-size: 0.9rem;
    display: block;
    margin-bottom: 15px;
}
.page-intro h2 {
    font-size: 2.8rem;
    color: var(--gray-dark);
    margin-bottom: 20px;
    line-height: 1.2;
}
.page-intro p {
    font-size: 1.15rem;
    color: var(--gray-text);
    line-height: 1.8;
}
.gold-line {
    width: 60px;
    height: 4px;
    background-color: var(--gold);
    margin: 30px auto;
}
.premium-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
    gap: 40px;
    padding: 0 5% 100px;
    max-width: 1400px;
    margin: 0 auto;
}
.premium-card {
    background: #fff;
    box-shadow: 0 15px 40px rgba(0,0,0,0.06);
    transition: transform 0.4s ease, box-shadow 0.4s ease;
    border-radius: 4px;
    overflow: hidden;
}
.premium-card:hover {
    transform: translateY(-10px);
    box-shadow: 0 25px 50px rgba(0,0,0,0.1);
}
.card-img {
    height: 280px;
    overflow: hidden;
    position: relative;
}
.card-img img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    transition: transform 0.6s ease;
}
.premium-card:hover .card-img img {
    transform: scale(1.08);
}
.card-badge {
    position: absolute;
    top: 20px;
    left: 20px;
    background: var(--gold);
    color: #fff;
    padding: 5px 15px;
    font-size: 0.8rem;
    font-weight: bold;
    letter-spacing: 1px;
    z-index: 2;
}
.card-content {
    padding: 40px 30px;
}
.card-content h3 {
    font-size: 1.6rem;
    margin-bottom: 15px;
    color: var(--gray-dark);
}
.card-content p {
    color: var(--gray-text);
    margin-bottom: 25px;
    line-height: 1.7;
}
.card-link {
    color: var(--gold);
    font-weight: 700;
    text-transform: uppercase;
    text-decoration: none;
    font-size: 0.9rem;
    letter-spacing: 1px;
    display: inline-flex;
    align-items: center;
    transition: color 0.3s;
}
.card-link i {
    margin-left: 8px;
    transition: transform 0.3s;
}
.card-link:hover {
    color: var(--gray-dark);
}
.card-link:hover i {
    transform: translateX(5px);
}
.cta-banner {
    background: var(--gray-dark);
    color: #fff;
    text-align: center;
    padding: 80px 20px;
}
.cta-banner h2 {
    font-size: 2.5rem;
    margin-bottom: 20px;
}
.cta-banner p {
    font-size: 1.1rem;
    opacity: 0.8;
    max-width: 600px;
    margin: 0 auto 40px;
    line-height: 1.6;
}
"""

with open(os.path.join(DIR, "styles.css"), "a", encoding="utf-8") as f:
    f.write(css_additions)

def read_file(name):
    with open(os.path.join(DIR, name), "r", encoding="utf-8") as f:
        return f.read()

index_html = read_file("index.html")
top_part = index_html[:index_html.find('<main class="main">') + len('<main class="main">')]
bottom_part = index_html[index_html.find('</main>'):]

# PRODUCTS HTML
products_html = f"""
        <section class="head-top hero-inner">
            <div class="video-background">
                <img src="assets/citerne.jpg" style="width:100%; height:100%; object-fit:cover;">
                <div class="hero-overlay"></div>
            </div>
            <div class="head-top-content">
                <h1 class="hero-tagline" style="font-size: 3.5rem;">PRODUITS & ÉQUIPEMENTS</h1>
            </div>
        </section>

        <section class="page-intro">
            <span class="page-intro-category">GAMME INDUSTRIELLE</span>
            <h2>Solutions d'Abattage Haute Performance</h2>
            <div class="gold-line"></div>
            <p>Fabrication in-situ et distribution de matières énergétiques formulées selon les plus hauts standards de sécurité HSE. Notre flotte d'équipements spécialisés est conçue pour fiabiliser et rentabiliser vos opérations d'abattage à ciel ouvert.</p>
        </section>

        <section class="premium-grid">
            <div class="premium-card">
                <div class="card-img">
                    <span class="card-badge">VRAC & MATRICES</span>
                    <img src="assets/citerne.jpg" alt="Nitrate d'Ammonium PPAN">
                </div>
                <div class="card-content">
                    <h3>Nitrate d'Ammonium PPAN</h3>
                    <p>Substance granulée poreuse haute pureté (> 99.2%) pour la fabrication d'ANFO et le dopage d'émulsions lourdes en carrière et mine d'or.</p>
                    <a href="contact.html?prod=ppan" class="card-link">Demander une cotation <i class="fas fa-arrow-right"></i></a>
                </div>
            </div>

            <div class="premium-card">
                <div class="card-img">
                    <span class="card-badge">HAUTE VÉLOCITÉ</span>
                    <img src="assets/IMG-20260909-WA0019.jpg" alt="Boosters Pentolite">
                </div>
                <div class="card-content">
                    <h3>Boosters Pentolite</h3>
                    <p>Charges relais haute densité garantissant une vitesse de détonation supérieure à 7 500 m/s pour l'amorçage fiable des émulsions insensibles.</p>
                    <a href="contact.html?prod=boosters" class="card-link">Demander une cotation <i class="fas fa-arrow-right"></i></a>
                </div>
            </div>

            <div class="premium-card">
                <div class="card-img">
                    <span class="card-badge">UNITÉ MOBILE</span>
                    <img src="assets/WhatsApp Image 2026-09-09 at 13.03.41.jpeg" alt="Camions MMU Tout-Terrain">
                </div>
                <div class="card-content">
                    <h3>Camions MMU Tout-Terrain</h3>
                    <p>Unités mobiles lourdes de fabrication continue d'émulsion en vrac avec pompage mécanisé et sensibilisation chimique directe.</p>
                    <a href="contact.html?prod=mmu" class="card-link">Réserver une unité <i class="fas fa-arrow-right"></i></a>
                </div>
            </div>
        </section>

        <div class="destacados-img-text bg-gray-70">
            <div class="destacados-img">
                <img src="assets/topographie-gps.jpg" alt="Géomatique">
            </div>
            <div class="destacados-content bg-dark">
                <h2 class="white">Stations GPS RTK & Drones</h2>
                <p class="white">Équipements topographiques différentiels pour l'implantation millimétrique des trous de mine, le relevé de front et le calcul de volume.<br><br>Drones photogrammétriques durcis pour mine et logiciels de calcul de cubatures inclus.</p>
                <a href="contact.html" class="btn btn-gold">Commander du Matériel</a>
            </div>
        </div>
"""

# SERVICES HTML
services_html = f"""
        <section class="head-top hero-inner">
            <div class="video-background">
                <img src="assets/Camion-de-dynamitage-1024x768.jpeg" style="width:100%; height:100%; object-fit:cover; transform: scaleX(-1);">
                <div class="hero-overlay"></div>
            </div>
            <div class="head-top-content">
                <h1 class="hero-tagline" style="font-size: 3.5rem;">NOS SERVICES</h1>
            </div>
        </section>

        <section class="page-intro">
            <span class="page-intro-category">INGÉNIERIE DE PRÉCISION</span>
            <h2>Expertise Technique & Opérationnelle</h2>
            <div class="gold-line"></div>
            <p>Notre équipe d'ingénieurs déploie une approche scientifique pour la conception de vos plans de tirs, l'audit de vos résultats et la modélisation 3D de vos gisements.</p>
        </section>

        <section class="premium-grid">
            <div class="premium-card">
                <div class="card-img">
                    <span class="card-badge">FORAGE</span>
                    <img src="assets/Camion-de-dynamitage-1024x768.jpeg" alt="Forage et Minage">
                </div>
                <div class="card-content">
                    <h3>Forage & Dynamitage</h3>
                    <p>Conception de plans de tir informatisés pour maximiser la fragmentation tout en contrôlant rigoureusement les vibrations et les projections.</p>
                    <a href="contact.html" class="card-link">Solliciter une étude <i class="fas fa-arrow-right"></i></a>
                </div>
            </div>

            <div class="premium-card">
                <div class="card-img">
                    <span class="card-badge">MODÉLISATION</span>
                    <img src="assets/topographie-gps.jpg" alt="Topographie et Drones 3D">
                </div>
                <div class="card-content">
                    <h3>Topographie & Drones 3D</h3>
                    <p>Relevés photogrammétriques par drone et modélisation des fronts de taille pour calculer avec précision les volumes de matériaux abattus.</p>
                    <a href="contact.html" class="card-link">Découvrir le service <i class="fas fa-arrow-right"></i></a>
                </div>
            </div>

            <div class="premium-card">
                <div class="card-img">
                    <span class="card-badge">CONSEIL</span>
                    <img src="assets/formation.jpg" alt="Audit et Formation">
                </div>
                <div class="card-content">
                    <h3>Audit & Formation</h3>
                    <p>Évaluation de la fragmentation, optimisation des coûts d'extraction et formations pratiques dispensées par nos experts internationaux.</p>
                    <a href="contact.html" class="card-link">Planifier un audit <i class="fas fa-arrow-right"></i></a>
                </div>
            </div>
        </section>
        
        <section class="cta-banner">
            <h2>Prêt à optimiser vos rendements ?</h2>
            <p>Nos experts sont à votre disposition pour réaliser un audit complet de vos chantiers actuels ou futurs.</p>
            <a href="contact.html" class="btn btn-gold">CONTACTEZ-NOUS DÈS AUJOURD'HUI</a>
        </section>
"""

# ABOUT HTML
about_html = f"""
        <section class="head-top hero-inner">
            <div class="video-background">
                <img src="assets/qui sommes nous bande.jpg" style="width:100%; height:100%; object-fit:cover;">
                <div class="hero-overlay"></div>
            </div>
            <div class="head-top-content">
                <h1 class="hero-tagline" style="font-size: 3.5rem;">NOTRE ENTREPRISE</h1>
            </div>
        </section>

        <section class="page-intro">
            <span class="page-intro-category">À PROPOS DE NOUS</span>
            <h2>L'Excellence comme Standard</h2>
            <div class="gold-line"></div>
            <p>Golden Eagle est une entreprise de référence dans la région ouest-africaine. Notre mission est d'accroître durablement la productivité et la sécurité de l'industrie extractive grâce à l'ingénierie appliquée.</p>
        </section>

        <div class="destacados-img-text bg-gray-70">
            <div class="destacados-img">
                <img src="assets/IMG-20260909-WA0019.jpg" alt="Historique">
            </div>
            <div class="destacados-content bg-dark">
                <h2 class="white">Expertise de Terrain</h2>
                <p class="white">GOLDEN EAGLE est spécialisée dans le forage, la fabrication, la fourniture d'explosifs et les services de dynamitage de haute précision.<br><br>Dans le souci constant de répondre aux exigences HSE, nous fournissons des études techniques approfondies d'évaluation des risques.</p>
            </div>
        </div>

        <div class="destacados-img-text">
            <div class="destacados-img order-2">
                <img src="assets/equipe-golden-eagle-1024x768.jpeg" alt="Vision">
            </div>
            <div class="destacados-content bg-light order-1">
                <h2 class="gray">Vision Stratégique</h2>
                <p class="gray">Accroître durablement la productivité et la sécurité des exploitants miniers et carriers en Afrique de l'Ouest.<br><br>Notre Direction s'appuie sur une équipe d'ingénieurs et d'artificiers chevronnés, recrutés selon des critères d'exigence rigoureux.</p>
            </div>
        </div>
        
        <section class="premium-grid" style="padding-top:80px;">
            <div class="premium-card" style="text-align:center; padding:40px;">
                <i class="fas fa-shield-alt" style="font-size: 3rem; color: var(--gold); margin-bottom:20px;"></i>
                <h3 style="margin-bottom:15px;">Zéro Incident</h3>
                <p style="color:var(--gray-text);">La sécurité est notre ligne directrice absolue dans chaque intervention et manipulation pyrotechnique.</p>
            </div>
            <div class="premium-card" style="text-align:center; padding:40px;">
                <i class="fas fa-leaf" style="font-size: 3rem; color: var(--gold); margin-bottom:20px;"></i>
                <h3 style="margin-bottom:15px;">Respect de l'Environnement</h3>
                <p style="color:var(--gray-text);">Minimisation rigoureuse des vibrations, du bruit et de la poussière lors de nos plans de tir.</p>
            </div>
            <div class="premium-card" style="text-align:center; padding:40px;">
                <i class="fas fa-users" style="font-size: 3rem; color: var(--gold); margin-bottom:20px;"></i>
                <h3 style="margin-bottom:15px;">Capital Humain</h3>
                <p style="color:var(--gray-text);">Formation continue de nos équipes locales pour garantir l'autonomie et le transfert de compétences.</p>
            </div>
        </section>
"""

with open(os.path.join(DIR, "products.html"), "w", encoding="utf-8") as f:
    f.write(top_part + products_html + bottom_part)
with open(os.path.join(DIR, "services.html"), "w", encoding="utf-8") as f:
    f.write(top_part + services_html + bottom_part)
with open(os.path.join(DIR, "about.html"), "w", encoding="utf-8") as f:
    f.write(top_part + about_html + bottom_part)
