import os
import re

base_dir = r"c:\Users\HP ZBOOK\Downloads\Golden eagle\redesign"
en_dir = os.path.join(base_dir, "en")
os.makedirs(en_dir, exist_ok=True)

files = ["index.html", "about.html", "services.html", "products.html", "contact.html"]

# 1. Update French files to point to English equivalents
for fn in files:
    fp = os.path.join(base_dir, fn)
    with open(fp, "r", encoding="utf-8") as f:
        html = f.read()

    # Nav menu english link
    html = re.sub(
        r'<li><a href="[^"]*">english</a></li>',
        f'<li><a href="en/{fn}">ENGLISH</a></li>',
        html,
        flags=re.IGNORECASE,
    )
    html = re.sub(
        r'<li><a href="[^"]*">ENGLISH</a></li>',
        f'<li><a href="en/{fn}">ENGLISH</a></li>',
        html,
    )

    # Top header english link
    html = re.sub(
        r'<li><a href="[^"]*" style="color: var\(--gray-dark\);">ENGLISH</a></li>',
        f'<li><a href="en/{fn}" style="color: var(--gray-dark);">ENGLISH</a></li>',
        html,
    )

    # Search links
    html = html.replace('<li><a href="#"><i class="fas fa-search"></i></a></li>', '<li><a href="products.html" title="Rechercher des produits"><i class="fas fa-search"></i></a></li>')
    html = html.replace('<li><a href="#" style="color: var(--gray-dark);"><i class="fas fa-search"></i></a></li>', '<li><a href="products.html" style="color: var(--gray-dark);" title="Rechercher des produits"><i class="fas fa-search"></i></a></li>')

    with open(fp, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"[FR] Updated {fn}")

# Common translation dictionaries for the English pages
common_translations = [
    # HTML Lang
    ('<html lang="fr">', '<html lang="en">'),
    
    # Asset paths
    ('href="styles.css"', 'href="../styles.css"'),
    ('href="assets/', 'href="../assets/'),
    ('src="assets/', 'src="../assets/'),
    ('src="script.js"', 'src="../script.js"'),
    ('src="firebase-public.js"', 'src="../firebase-public.js"'),
    ('src="firebase-config.js"', 'src="../firebase-config.js"'),
    ("url('assets/", "url('../assets/"),
    
    # Nav bar links to French
    ('<li><a href="en/index.html">ENGLISH</a></li>', '<li><a href="../index.html">FRANÇAIS</a></li>'),
    ('<li><a href="en/about.html">ENGLISH</a></li>', '<li><a href="../about.html">FRANÇAIS</a></li>'),
    ('<li><a href="en/services.html">ENGLISH</a></li>', '<li><a href="../services.html">FRANÇAIS</a></li>'),
    ('<li><a href="en/products.html">ENGLISH</a></li>', '<li><a href="../products.html">FRANÇAIS</a></li>'),
    ('<li><a href="en/contact.html">ENGLISH</a></li>', '<li><a href="../contact.html">FRANÇAIS</a></li>'),
    
    ('style="color: var(--gray-dark);">ENGLISH</a>', 'style="color: var(--gray-dark);">FRANÇAIS</a>'),
    ('href="en/index.html"', 'href="../index.html"'),
    ('href="en/about.html"', 'href="../about.html"'),
    ('href="en/services.html"', 'href="../services.html"'),
    ('href="en/products.html"', 'href="../products.html"'),
    ('href="en/contact.html"', 'href="../contact.html"'),
    
    # Overlay Menu Navigation
    ('title="Menu de navigation"', 'title="Main Navigation Menu"'),
    ('<h4>À PROPOS DE GOLDEN EAGLE</h4>', '<h4>ABOUT GOLDEN EAGLE</h4>'),
    ('<li><a href="about.html">Notre Entreprise</a></li>', '<li><a href="about.html">Our Company</a></li>'),
    ('<li><a href="about.html#presence">Présence Globale</a></li>', '<li><a href="about.html#presence">Global Presence</a></li>'),
    ('<li><a href="services.html">Technologie & R&D</a></li>', '<li><a href="services.html">Technology & R&D</a></li>'),
    ('<li><a href="about.html#brand">Notre Marque</a></li>', '<li><a href="about.html#brand">Our Brand</a></li>'),
    
    ('<h4>INDUSTRIES & SOLUTIONS</h4>', '<h4>INDUSTRIES & SOLUTIONS</h4>'),
    ('<li><a href="products.html">Explosifs Civils</a></li>', '<li><a href="products.html">Civil Explosives</a></li>'),
    ('<li><a href="services.html">Forage & Minage</a></li>', '<li><a href="services.html">Drilling & Blasting</a></li>'),
    ('<li><a href="products.html#mmu">Unités Mobiles MMU</a></li>', '<li><a href="products.html#mmu">Mobile Units (MMU)</a></li>'),
    ('<li><a href="services.html#consultation">Ingénierie & Conseil</a></li>', '<li><a href="services.html#consultation">Engineering & Consulting</a></li>'),
    
    ('<h4>NOTRE ENGAGEMENT</h4>', '<h4>OUR COMMITMENT</h4>'),
    ('<li><a href="about.html#safety">Culture de la Sécurité</a></li>', '<li><a href="about.html#safety">Safety Culture</a></li>'),
    ('<li><a href="about.html#people">Passion pour les Hommes</a></li>', '<li><a href="about.html#people">Passion for People</a></li>'),
    ('<li><a href="about.html#ethics">Comportement Éthique</a></li>', '<li><a href="about.html#ethics">Ethical Behavior</a></li>'),
    ('<li><a href="about.html#environment">Protection de l\'Environnement</a></li>', '<li><a href="about.html#environment">Environmental Protection</a></li>'),
    
    ('<h4>PRODUITS & COTATIONS</h4>', '<h4>PRODUCTS & QUOTATIONS</h4>'),
    ('<li><a href="products.html">Catalogue d\'Explosifs</a></li>', '<li><a href="products.html">Explosives Catalog</a></li>'),
    ('<li><a href="products.html">Boosters & Détonateurs</a></li>', '<li><a href="products.html">Boosters & Detonators</a></li>'),
    ('<li><a href="products.html">Demande de Cotation</a></li>', '<li><a href="products.html">Request a Quote</a></li>'),
    ('<li><a href="contact.html">Support Artificiers</a></li>', '<li><a href="contact.html">Blaster Support</a></li>'),
    
    # Common Footer
    ('<li><a href="about.html">Notre entreprise</a></li>', '<li><a href="about.html">Our company</a></li>'),
    ('<li><a href="about.html#presence">Présence globale</a></li>', '<li><a href="about.html#presence">Global presence</a></li>'),
    ('<li><a href="services.html">Technologie</a></li>', '<li><a href="services.html">Technology</a></li>'),
    ('<li><a href="about.html#brand">Notre marque</a></li>', '<li><a href="about.html#brand">Our brand</a></li>'),
    ('<li><a href="services.html#topographie">Etudes & Modélisation</a></li>', '<li><a href="services.html#topographie">Surveys & Modeling</a></li>'),
    ('<li><a href="about.html#safety">Culture de la sécurité</a></li>', '<li><a href="about.html#safety">Safety culture</a></li>'),
    ('<li><a href="about.html#people">Passion pour les hommes</a></li>', '<li><a href="about.html#people">Passion for people</a></li>'),
    ('<li><a href="about.html#environment">Environnement</a></li>', '<li><a href="about.html#environment">Environment</a></li>'),
    ('<p>Une entreprise de référence spécialisée dans le forage et le minage civil.</p>', '<p>A leading reference company specialized in civil drilling and blasting operations.</p>'),
    ('<div>&copy; 2026 Golden Eagle SARL. Tous droits réservés.</div>', '<div>&copy; 2026 Golden Eagle SARL. All rights reserved.</div>'),
    ('Mentions légales', 'Legal Notice'),
    ('Politique de confidentialité', 'Privacy Policy'),
]

# Page specific translations
page_translations = {
    "index.html": [
        ('<h2>Une entreprise de référence spécialisée dans les matériaux énergétiques</h2>', '<h2>A leading reference specialized in energetic materials & precision blasting</h2>'),
        ('>À PROPOS DE GOLDEN EAGLE<', '>ABOUT GOLDEN EAGLE<'),
        ('<h2>L\'avenir du minage est ici</h2>', '<h2>The Future of Mining is Here</h2>'),
        ('<p>Faites passer votre exploitation au niveau supérieur avec notre combinaison de produits, de technologies d\'ingénierie, d\'outils numériques et de notre expertise en matière de forage et de dynamitage.</p>', '<p>Take your mining operations to the next level with our advanced portfolio of energetic materials, engineering technologies, digital blast design tools, and precision shotfiring expertise.</p>'),
        ('>EN SAVOIR PLUS<', '>LEARN MORE<'),
        ('<h2>Minage durable</h2>', '<h2>Sustainable Mining</h2>'),
        ('<h1>Présence Globale</h1>', '<h1>Regional Footprint</h1>'),
        ('CHOISISSEZ UN TYPE D\'IMPLANTATION', 'SELECT FACILITY TYPE'),
        ('>Golden Eagle<', '>All Locations<'),
        ('>Bases Opérationnelles<', '>Operational Bases<'),
        ('>Unités Mobiles MMU<', '>Mobile Units (MMU)<'),
        ('Ouagadougou, Burkina Faso (Base Principale)', 'Ouagadougou, Burkina Faso (Headquarters)'),
        ('Bamako, Mali (Base)', 'Bamako, Mali (Regional Base)'),
        ('Site Minier, Niger (Unité MMU)', 'Mining Site, Niger (MMU Unit)'),
        ('Site Minier, Sénégal (Unité MMU)', 'Mining Site, Senegal (MMU Unit)'),
        ('Abidjan, Côte d\'Ivoire (Base)', 'Abidjan, Ivory Coast (Operations Base)'),
        ('<p>bases en<br>+2 pays</p>', '<p>bases across<br>+2 countries</p>'),
        ('<p>Opérations dans<br>pays</p>', '<p>operations in<br>countries</p>'),
        ('<p>Tirs<br>sécurisés</p>', '<p>Zero-incident<br>blasts</p>'),
        ('>IMPLANTATIONS RÉGIONALES<', '>REGIONAL OPERATIONS<'),
        ('<h2 class="white">Technologie</h2>', '<h2 class="white">Technology & R&D</h2>'),
        ('<p class="white">Notre <strong>plateforme technologique de matériaux énergétiques</strong> intègre les connaissances les plus avancées de l\'industrie. À travers notre <strong>écosystème d\'innovation</strong>, auquel participent tous les domaines clés de l\'entreprise, nous travaillons chaque jour dans le seul but de développer de nouveaux produits et solutions qui maximisent la <strong>création de valeur pour nos clients</strong>.</p>', '<p class="white">Our <strong>energetic materials technology platform</strong> integrates the industry\'s most advanced chemical and mining knowledge. Through our <strong>innovation ecosystem</strong>, engaging every technical division, we strive daily to deliver cutting-edge blasting solutions that maximize <strong>value creation for our clients</strong>.</p>'),
        ('Plateforme de premier ordre', 'World-Class Platform'),
        ('<h2 class="gray">Nos Hommes</h2>', '<h2 class="gray">Our People</h2>'),
        ('<p class="gray">Nous sommes une entreprise <strong>régionale, multiculturelle</strong> et <strong>diverse</strong>. Rejoignez les professionnels qui forment Golden Eagle pour <strong>générer un véritable impact</strong> et <strong>vivre des aventures uniques</strong>.</p>', '<p class="gray">We are a <strong>regional, multicultural</strong>, and <strong>diverse</strong> enterprise. Join the professionals who make up Golden Eagle to <strong>drive real industrial impact</strong> and <strong>experience unique operational challenges</strong>.</p>'),
        ('>Pourquoi VOUS<', '>Why Join Us<'),
        ('<h2 class="white">Sécurité</h2>', '<h2 class="white">Safety Culture</h2>'),
        ('<p class="white">Nous croyons que la <strong>Culture de la Sécurité</strong> est un <strong>mode de vie</strong>.<br><br>Golden Eagle s\'engage quotidiennement à maintenir un environnement de travail sûr, sans compromis sur la qualité ou l\'intégrité de nos équipes et de l\'environnement.</p>', '<p class="white">We believe that a <strong>Culture of Safety</strong> is a <strong>way of life</strong>.<br><br>Golden Eagle is unconditionally committed to maintaining a safe work environment on every bench, without compromise on quality, team wellbeing, or the environment.</p>'),
        ('Actualités & Insights', 'News & Insights'),
        ('Déploiement d\'une nouvelle flotte de transport spécialisé', 'Deployment of a new specialized transport fleet'),
        ('Un pas de plus vers l\'autonomie logistique et la sécurisation de l\'approvisionnement en matériaux sensibles.', 'Another step toward logistical autonomy and secure supply of sensitive materials.'),
        ('Atelier pratique et certification des artificiers', 'Practical workshop and shotfirer certification'),
        ('Le renforcement continu des capacités de nos collaborateurs reste notre priorité absolue.', 'Continuous capacity building for our workforce remains our top priority.'),
        ('Dynamitage de précision en milieu contraint', 'Precision blasting in constrained environments'),
        ('Comment nos équipes d\'ingénierie ont optimisé la fragmentation tout en réduisant les vibrations.', 'How our engineering teams optimized rock fragmentation while mitigating vibration.'),
        ('>VOIR TOUT<', '>VIEW ALL<'),
    ],
    "about.html": [
        ('NOTRE ENTREPRISE', 'OUR COMPANY'),
        ('Zéro Incident', 'Zero Incident'),
        ('<span class="page-intro-category">À PROPOS DE NOUS</span>', '<span class="page-intro-category">ABOUT US</span>'),
        ('<h2>L\'Excellence comme Standard</h2>', '<h2>Excellence as a Standard</h2>'),
        ('<p>Golden Eagle est une entreprise de référence dans la région ouest-africaine. Notre mission est d\'accroître durablement la productivité et la sécurité de l\'industrie extractive grâce à l\'ingénierie appliquée.</p>', '<p>Golden Eagle is a leading reference company across West Africa. Our mission is to sustainably increase mining and quarry productivity and safety through applied engineering.</p>'),
        ('<h2 class="white">Expertise de Terrain</h2>', '<h2 class="white">Field Expertise</h2>'),
        ('<p class="white">GOLDEN EAGLE est spécialisée dans le forage, la fabrication, la fourniture d\'explosifs et les services de dynamitage de haute précision.<br><br>Dans le souci constant de répondre aux exigences HSE, nous fournissons des études techniques approfondies d\'évaluation des risques.</p>', '<p class="white">GOLDEN EAGLE specializes in drilling, manufacturing, supplying explosives, and high-precision blasting services.<br><br>With an unwavering commitment to HSE standards, we provide thorough technical risk assessments for every bench.</p>'),
        ('<h2 class="gray">Vision Stratégique</h2>', '<h2 class="gray">Strategic Vision</h2>'),
        ('<p class="gray">Accroître durablement la productivité et la sécurité des exploitants miniers et carriers en Afrique de l\'Ouest.<br><br>Notre Direction s\'appuie sur une équipe d\'ingénieurs et d\'artificiers chevronnés, recrutés selon des critères d\'exigence rigoureux.</p>', '<p class="gray">Sustainably maximize the productivity and safety of mining and quarry operators throughout West Africa.<br><br>Our executive leadership relies on a certified team of engineers and seasoned shotfirers selected to the highest industry standards.</p>'),
        ('<h3>Zéro Incident</h3>', '<h3>Zero Incident</h3>'),
        ('<p style="color:var(--gray-text);">La sécurité est notre ligne directrice absolue dans chaque intervention et manipulation pyrotechnique.</p>', '<p style="color:var(--gray-text);">Safety is our non-negotiable benchmark in every pyrotechnic handling and field operation.</p>'),
        ('<h3>Respect de l\'Environnement</h3>', '<h3>Environmental Respect</h3>'),
        ('<p style="color:var(--gray-text);">Minimisation rigoureuse des vibrations, du bruit et de la poussière lors de nos plans de tir.</p>', '<p style="color:var(--gray-text);">Strict minimization of ground vibrations, air blast, and flyrock during every firing sequence.</p>'),
        ('<h3>Capital Humain</h3>', '<h3>Human Capital</h3>'),
        ('<p style="color:var(--gray-text);">Formation continue de nos équipes locales pour garantir l\'autonomie et le transfert de compétences.</p>', '<p style="color:var(--gray-text);">Ongoing training of local talent to foster operational independence and skills transfer.</p>'),
    ],
    "services.html": [
        ('<h1 class="hero-tagline" style="font-size: 3.5rem;">NOS SERVICES</h1>', '<h1 class="hero-tagline" style="font-size: 3.5rem;">OUR SERVICES</h1>'),
        ('<span class="page-intro-category">INGÉNIERIE DE PRÉCISION</span>', '<span class="page-intro-category">PRECISION ENGINEERING</span>'),
        ('<h2>Expertise Technique & Opérationnelle</h2>', '<h2>Technical & Operational Expertise</h2>'),
        ('<p>Notre équipe d\'ingénieurs déploie une approche scientifique pour la conception de vos plans de tirs, l\'audit de vos résultats et la modélisation 3D de vos gisements.</p>', '<p>Our engineering team applies a rigorous scientific approach to computerized blast design, fragmentation audits, and 3D deposit modeling.</p>'),
        ('<span class="card-badge">FORAGE</span>', '<span class="card-badge">DRILLING</span>'),
        ('<h3>Forage & Dynamitage</h3>', '<h3>Drilling & Blasting</h3>'),
        ('<p>Conception de plans de tir informatisés pour maximiser la fragmentation tout en contrôlant rigoureusement les vibrations et les projections.</p>', '<p>Computerized blast patterns engineered to maximize rock fragmentation while strictly controlling ground vibrations and flyrock.</p>'),
        ('Solliciter une étude <i class="fas fa-arrow-right"></i>', 'Request a Study <i class="fas fa-arrow-right"></i>'),
        ('<span class="card-badge">MODÉLISATION</span>', '<span class="card-badge">MODELING</span>'),
        ('<h3>Topographie & Drones 3D</h3>', '<h3>Topography & 3D Drones</h3>'),
        ('<p>Relevés photogrammétriques par drone et modélisation des fronts de taille pour calculer avec précision les volumes de matériaux abattus.</p>', '<p>Drone photogrammetry and bench face scanning to accurately compute rock volume, burden profiling, and muckpile distribution.</p>'),
        ('Découvrir le service <i class="fas fa-arrow-right"></i>', 'Explore Service <i class="fas fa-arrow-right"></i>'),
        ('<span class="card-badge">CONSEIL</span>', '<span class="card-badge">CONSULTING</span>'),
        ('<h3>Audit & Formation</h3>', '<h3>Audit & Training</h3>'),
        ('<p>Évaluation de la fragmentation, optimisation des coûts d\'extraction et formations pratiques dispensées par nos experts internationaux.</p>', '<p>Fragmentation analysis, extraction cost optimization, and certified practical training delivered by international experts.</p>'),
        ('Planifier un audit <i class="fas fa-arrow-right"></i>', 'Schedule an Audit <i class="fas fa-arrow-right"></i>'),
        ('<h2>Prêt à optimiser vos rendements ?</h2>', '<h2>Ready to optimize your yields?</h2>'),
        ('<p>Nos experts sont à votre disposition pour réaliser un audit complet de vos chantiers actuels ou futurs.</p>', '<p>Our technical team is ready to conduct a full operational audit of your current and future mining sites.</p>'),
        ('>CONTACTEZ-NOUS DÈS AUJOURD\'HUI<', '>CONTACT US TODAY<'),
    ],
    "products.html": [
        ('PRODUITS & ÉQUIPEMENTS', 'PRODUCTS & EQUIPMENT'),
        ('<h1 class="hero-tagline" style="font-size: 3.5rem;">NOS PRODUITS</h1>', '<h1 class="hero-tagline" style="font-size: 3.5rem;">PRODUCTS & EQUIPMENT</h1>'),
        ('<span class="page-intro-category">GAMME INDUSTRIELLE</span>', '<span class="page-intro-category">INDUSTRIAL RANGE</span>'),
        ('<h2>Solutions d\'Abattage Haute Performance</h2>', '<h2>High-Performance Blasting Solutions</h2>'),
        ('<p>Fabrication in-situ et distribution de matières énergétiques formulées selon les plus hauts standards de sécurité HSE. Notre flotte d\'équipements spécialisés est conçue pour fiabiliser et rentabiliser vos opérations d\'abattage à ciel ouvert.</p>', '<p>In-situ manufacturing and supply of energetic materials adhering to the highest HSE safety benchmarks. Our specialized fleet guarantees reliable and cost-effective open-pit blasting.</p>'),
        ('<span class="card-badge">VRAC & MATRICES</span>', '<span class="card-badge">BULK & MATRICES</span>'),
        ('<h3>Nitrate d\'Ammonium PPAN</h3>', '<h3>PPAN Ammonium Nitrate</h3>'),
        ('<p>Substance granulée poreuse haute pureté (> 99.2%) pour la fabrication d\'ANFO et le dopage d\'émulsions lourdes en carrière et mine d\'or.</p>', '<p>High-purity porous prilled substance (> 99.2%) for ANFO production and heavy emulsion doping in quarries and gold mines.</p>'),
        ('Demander une cotation <i class="fas fa-arrow-right"></i>', 'Request a Quote <i class="fas fa-arrow-right"></i>'),
        ('<span class="card-badge">HAUTE VÉLOCITÉ</span>', '<span class="card-badge">HIGH VELOCITY</span>'),
        ('<h3>Boosters Pentolite</h3>', '<h3>Pentolite Boosters</h3>'),
        ('<p>Charges relais haute densité garantissant une vitesse de détonation supérieure à 7 500 m/s pour l\'amorçage fiable des émulsions insensibles.</p>', '<p>High-density booster charges ensuring detonation velocity above 7,500 m/s for reliable initiation of insensitive bulk emulsions.</p>'),
        ('<span class="card-badge">UNITÉ MOBILE</span>', '<span class="card-badge">MOBILE UNIT</span>'),
        ('<h3>Camions MMU Tout-Terrain</h3>', '<h3>All-Terrain MMU Trucks</h3>'),
        ('<p>Unités mobiles lourdes de fabrication continue d\'émulsion en vrac avec pompage mécanisé et sensibilisation chimique directe.</p>', '<p>Heavy-duty mobile units for on-bench continuous bulk emulsion manufacturing, mechanized delivery, and chemical gassing.</p>'),
        ('Réserver une unité <i class="fas fa-arrow-right"></i>', 'Book a Unit <i class="fas fa-arrow-right"></i>'),
        ('<h2 class="white">Stations GPS RTK & Drones</h2>', '<h2 class="white">RTK GPS Stations & Drones</h2>'),
        ('<p class="white">Équipements topographiques différentiels pour l\'implantation millimétrique des trous de mine, le relevé de front et le calcul de volume.<br><br>Drones photogrammétriques durcis pour mine et logiciels de calcul de cubatures inclus.</p>', '<p class="white">Differential topographic equipment for millimetric borehole staking, bench surveys, and volume calculation.<br><br>Rugged mining photogrammetry drones and volumetric modeling software included.</p>'),
        ('>Commander du Matériel<', '>Inquire About Equipment<'),
    ],
    "contact.html": [
        ('<h1 class="hero-tagline" style="font-size: 3rem;">CONTACTEZ-NOUS</h1>', '<h1 class="hero-tagline" style="font-size: 3rem;">CONTACT US</h1>'),
        ('<h2 class="white">Siège & Opérations</h2>', '<h2 class="white">Headquarters & Operations</h2>'),
        ('Envoyer un email', 'Send an Email'),
        ('Parlons de votre projet', 'Let\'s Discuss Your Project'),
        ('Nos équipes d\'experts sont à votre disposition pour étudier vos besoins en dynamitage, forage et fourniture d\'explosifs civils en Afrique de l\'Ouest.', 'Our expert engineering teams are at your disposal to analyze your blasting, drilling, and civil explosives supply requirements across West Africa.'),
        ('Siège Social :', 'Head Office:'),
        ('Email :', 'Email:'),
        ('Téléphone :', 'Phone:'),
        ('Nom complet *', 'Full Name *'),
        ('Email professionnel *', 'Business Email *'),
        ('Sujet', 'Subject'),
        ('<option value="Demande de devis">Demande de devis</option>', '<option value="Quote Request">Request a Quote</option>'),
        ('<option value="Partenariat">Partenariat / Fourniture</option>', '<option value="Partnership">Partnership / Supply</option>'),
        ('<option value="Recrutement">Recrutement</option>', '<option value="Careers">Careers</option>'),
        ('<option value="Autre">Autre demande</option>', '<option value="Other">Other Inquiry</option>'),
        ('Message *', 'Detailed Message *'),
        ('ENVOYER LE MESSAGE', 'SEND MESSAGE'),
        ('Nous vous répondrons sous 24h ouvrées.', 'We will respond within 24 business hours.'),
    ],
}

# 2. Generate English pages
for fn in files:
    src_fp = os.path.join(base_dir, fn)
    dst_fp = os.path.join(en_dir, fn)
    with open(src_fp, "r", encoding="utf-8") as f:
        html = f.read()

    # Apply common replacements
    for src, dst in common_translations:
        html = html.replace(src, dst)

    # Apply page-specific replacements
    if fn in page_translations:
        for src, dst in page_translations[fn]:
            html = html.replace(src, dst)

    with open(dst_fp, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"[EN] Generated en/{fn}")

print("\n--- ALL PAGES SYNCED AND TRANSLATED SUCCESSFULLY! ---")
