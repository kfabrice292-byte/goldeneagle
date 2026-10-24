import os

DIR = r"c:\Users\HP ZBOOK\Downloads\Golden eagle\redesign"

def read_file(name):
    with open(os.path.join(DIR, name), "r", encoding="utf-8") as f:
        return f.read()

index_html = read_file("index.html")

top_part = index_html[:index_html.find('<main class="main">') + len('<main class="main">')]
bottom_part = index_html[index_html.find('</main>'):]

# 1. Rebuild about.html
about_content = f"""
        <section class="head-top" style="height: 60vh;">
            <div class="video-background">
                <img src="assets/qui sommes nous bande.jpg" style="width:100%; height:100%; object-fit:cover;">
                <div class="hero-overlay"></div>
            </div>
            <div class="head-top-content">
                <h1 class="hero-tagline" style="font-size: 3rem;">NOTRE ENTREPRISE</h1>
            </div>
        </section>

        <div class="destacados-img-text bg-gray-70">
            <div class="destacados-img">
                <img src="assets/IMG-20260909-WA0019.jpg" alt="Historique">
            </div>
            <div class="destacados-content bg-dark">
                <h2 class="white">Expertise & Capital Humain</h2>
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

        <div class="destacados-img-text bg-gray-70">
            <div class="destacados-img">
                <img src="assets/IMG-20260909-WA0017.jpg" alt="Sécurité">
            </div>
            <div class="destacados-content bg-dark">
                <h2 class="white">Sécurité Zéro Incident</h2>
                <p class="white">Le partage du capital d'expériences accumulées, la transmission des valeurs de rigueur et la priorité absolue accordée à la vie humaine constituent le socle de chaque intervention.<br><br>Nos procédures respectent scrupuleusement les législations environnementales.</p>
            </div>
        </div>
"""

with open(os.path.join(DIR, "about.html"), "w", encoding="utf-8") as f:
    f.write(top_part + about_content + bottom_part)

# 2. Rebuild services.html
services_content = f"""
        <section class="head-top" style="height: 60vh;">
            <div class="video-background">
                <img src="assets/Camion-de-dynamitage-1024x768.jpeg" style="width:100%; height:100%; object-fit:cover;">
                <div class="hero-overlay"></div>
            </div>
            <div class="head-top-content">
                <h1 class="hero-tagline" style="font-size: 3rem;">NOS SERVICES</h1>
            </div>
        </section>

        <div class="destacados-img-text bg-gray-70">
            <div class="destacados-img">
                <img src="assets/Camion-de-dynamitage-1024x768.jpeg" alt="Forage">
            </div>
            <div class="destacados-content bg-dark">
                <h2 class="white">Forage & Dynamitage</h2>
                <p class="white">Nous concevons et réalisons des plans de tir informatisés pour maximiser la fragmentation rocheuse tout en contrôlant rigoureusement les vibrations et les projections.<br><br>Étude géomécanique, mailles de forage optimisées, amorçage électrique et non-électrique.</p>
            </div>
        </div>

        <div class="destacados-img-text">
            <div class="destacados-img order-2">
                <img src="assets/topographie-gps.jpg" alt="Topographie">
            </div>
            <div class="destacados-content bg-light order-1">
                <h2 class="gray">Topographie & Drones 3D</h2>
                <p class="gray">Nos géomètres équipés de stations totales robotisées, de récepteurs GPS RTK différentiels et de drones photogrammétriques modélisent les fronts de carrière.<br><br>Calculs précis de cubatures abattues et réconciliation géologique des volumes.</p>
            </div>
        </div>

        <div class="destacados-img-text bg-gray-70">
            <div class="destacados-img">
                <img src="assets/formation.jpg" alt="Formation">
            </div>
            <div class="destacados-content bg-dark">
                <h2 class="white">Audit & Formation</h2>
                <p class="white">Nos ingénieurs seniors évaluent périodiquement les résultats de fragmentation. Ces audits permettent de réduire le coût global d'extraction.<br><br>Modules de formation pratique dispensés par des professionnels chevronnés du secteur minier.</p>
            </div>
        </div>
"""

with open(os.path.join(DIR, "services.html"), "w", encoding="utf-8") as f:
    f.write(top_part + services_content + bottom_part)

# 3. Rebuild products.html
products_content = f"""
        <section class="head-top" style="height: 60vh;">
            <div class="video-background">
                <img src="assets/citerne.jpg" style="width:100%; height:100%; object-fit:cover;">
                <div class="hero-overlay"></div>
            </div>
            <div class="head-top-content">
                <h1 class="hero-tagline" style="font-size: 3rem;">PRODUITS & ÉQUIPEMENTS</h1>
            </div>
        </section>

        <div class="destacados-img-text bg-gray-70">
            <div class="destacados-img">
                <img src="assets/citerne.jpg" alt="Vrac">
            </div>
            <div class="destacados-content bg-dark">
                <h2 class="white">Explosifs Civils</h2>
                <p class="white">Fabrication in-situ, livraison et fourniture de substances explosives civiles certifiées.<br><br>Nitrate d'Ammonium poreux PPAN, Matrice d'émulsion S100. Haute capacité de rétention et rendement énergétique constant pour vos opérations.</p>
            </div>
        </div>

        <div class="destacados-img-text">
            <div class="destacados-img order-2">
                <img src="assets/IMG-20260909-WA0019.jpg" alt="Boosters">
            </div>
            <div class="destacados-content bg-light order-1">
                <h2 class="gray">Systèmes d'Amorçage</h2>
                <p class="gray">Boosters Pentolite & Magnum garantissant une vitesse de détonation supérieure à 7 500 m/s.<br><br>Détonateurs électriques instantanés, micro-retards et cordeaux détonants souples pour un amorçage séquentiel parfaitement synchronisé.</p>
            </div>
        </div>

        <div class="destacados-img-text bg-gray-70">
            <div class="destacados-img">
                <img src="assets/WhatsApp Image 2026-09-09 at 13.03.41.jpeg" alt="MMU">
            </div>
            <div class="destacados-content bg-dark">
                <h2 class="white">Unités Mobiles MMU</h2>
                <p class="white">Camions MMU Tout-Terrain pour la fabrication continue d'émulsion en vrac avec pompage mécanisé.<br><br>Débit de pompage haute cadence et sensibilisation chimique directe au fond du trou pour une sécurité maximale.</p>
            </div>
        </div>
"""

with open(os.path.join(DIR, "products.html"), "w", encoding="utf-8") as f:
    f.write(top_part + products_content + bottom_part)

# 4. Rebuild contact.html
contact_content = f"""
        <section class="head-top" style="height: 60vh;">
            <div class="video-background">
                <img src="assets/pano_360_quarry.jpg" style="width:100%; height:100%; object-fit:cover;">
                <div class="hero-overlay"></div>
            </div>
            <div class="head-top-content">
                <h1 class="hero-tagline" style="font-size: 3rem;">CONTACTEZ-NOUS</h1>
            </div>
        </section>

        <div class="destacados-img-text bg-gray-70">
            <div class="destacados-img">
                <!-- Using a map embedded in the image slot for a cool maxam-like contact layout -->
                <iframe src="https://www.google.com/maps/embed?pb=!1m14!1m8!1m3!1d3715.1831933952803!2d-1.4961490631103516!3d12.322710990905762!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0xe2ebf14577d1983%3A0x1dc63d8550fe63f6!2sGolden%20Eagle!5e1!3m2!1sfr!2sbf!4v1789991535924!5m2!1sfr!2sbf" width="100%" height="100%" style="border:0; min-height:400px; filter: grayscale(50%);" allowfullscreen="" loading="lazy"></iframe>
            </div>
            <div class="destacados-content bg-dark">
                <h2 class="white">Siège & Opérations</h2>
                <p class="white" style="margin-bottom:15px;"><i class="fas fa-map-marker-alt" style="color:var(--gold); margin-right:10px;"></i> Ouaga 2000, Secteur 53, Ouagadougou, Burkina Faso</p>
                <p class="white" style="margin-bottom:15px;"><i class="fas fa-phone-alt" style="color:var(--gold); margin-right:10px;"></i> (+226) 25 37 53 33</p>
                <p class="white" style="margin-bottom:30px;"><i class="fas fa-envelope" style="color:var(--gold); margin-right:10px;"></i> info@goldeneaglebf.com</p>
                <a href="mailto:info@goldeneaglebf.com" class="btn btn-gold">Envoyer un email</a>
            </div>
        </div>
"""

with open(os.path.join(DIR, "contact.html"), "w", encoding="utf-8") as f:
    f.write(top_part + contact_content + bottom_part)

print("All inner pages completely rebuilt using pure MAXAM layout components.")
