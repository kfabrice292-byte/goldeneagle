import os

path = r'c:\Users\HP ZBOOK\Downloads\Golden eagle\redesign\en'

translations = {
    # Head and paths
    'href="styles.css"': 'href="../styles.css"',
    'src="assets/': 'src="../assets/',
    'href="assets/': 'href="../assets/',
    'src="script.js"': 'src="../script.js"',
    
    # Nav
    '<a href="index.html" class="nav-link active">Accueil</a>': '<a href="index.html" class="nav-link active">Home</a>',
    '<a href="index.html" class="nav-link">Accueil</a>': '<a href="index.html" class="nav-link">Home</a>',
    '<a href="services.html" class="nav-link active">Nos Services</a>': '<a href="services.html" class="nav-link active">Our Services</a>',
    '<a href="services.html" class="nav-link">Nos Services</a>': '<a href="services.html" class="nav-link">Our Services</a>',
    '<a href="about.html" class="nav-link active">Qui sommes-nous?</a>': '<a href="about.html" class="nav-link active">About Us</a>',
    '<a href="about.html" class="nav-link">Qui sommes-nous?</a>': '<a href="about.html" class="nav-link">About Us</a>',
    '<a href="contact.html" class="nav-link active btn-header">Contactez-nous</a>': '<a href="contact.html" class="nav-link active btn-header">Contact Us</a>',
    '<a href="contact.html" class="nav-link btn-header">Contactez-nous</a>': '<a href="contact.html" class="nav-link btn-header">Contact Us</a>',
    
    # Lang Switcher
    '<a href="index.html" class="active">FR</a> | <a href="en/index.html">EN</a>': '<a href="../index.html">FR</a> | <a href="index.html" class="active">EN</a>',
    '<a href="about.html" class="active">FR</a> | <a href="en/about.html">EN</a>': '<a href="../about.html">FR</a> | <a href="about.html" class="active">EN</a>',
    '<a href="services.html" class="active">FR</a> | <a href="en/services.html">EN</a>': '<a href="../services.html">FR</a> | <a href="services.html" class="active">EN</a>',
    '<a href="contact.html" class="active">FR</a> | <a href="en/contact.html">EN</a>': '<a href="../contact.html">FR</a> | <a href="contact.html" class="active">EN</a>',
    
    # Common Footer
    'GOLDEN EAGLE SARL est spécialisée dans le forage, la fabrication, la fourniture d\'explosifs et les services de dynamitage.': 'GOLDEN EAGLE SARL specializes in drilling, manufacturing, supplying explosives, and blasting services.',
    'Navigation': 'Navigation',
    'Accueil': 'Home',
    'Nos Services': 'Our Services',
    'Qui sommes-nous ?': 'About Us',
    'Contact': 'Contact',
    'Contact Info': 'Contact Info',
    'Siège Social & Adresse Postale': 'Head Office & Postal Address',
    'Restez informé de nos dernières actualités sur le terrain.': 'Stay informed of our latest news in the field.',
    'Votre adresse email': 'Your email address',
    'Tous droits réservés.': 'All rights reserved.',
    'Horaires : Lundi-Vendredi, 08h00-16h00': 'Hours: Monday-Friday, 08:00-16:00',
    
    # index.html specific
    'L\'Expertise Absolue en Forage & Dynamitage': 'The Absolute Expertise in Drilling & Blasting',
    '« Majestueux – Minutieux – Précis – Vivace »': '"Majestic – Meticulous – Precise – Vivacious"',
    'Découvrir notre histoire': 'Discover our history',
    'Bienvenue chez': 'Welcome to',
    'Renforcer les capacités des entreprises burkinabè à travers les expériences capitalisées de nos ingénieurs.': 'Strengthening the capabilities of Burkinabe companies through the capitalized experiences of our engineers.',
    'Nous sommes une entreprise spécialisée dans le forage, le dynamitage, la fabrication et fourniture de substances explosives. Dans le souci de répondre aux exigences internationales, nous accompagnons nos clients en leur fournissant des études d\'évaluation des risques et une sécurité infaillible sur chaque chantier.': 'We are a company specialized in drilling, blasting, manufacturing, and supplying explosive substances. In order to meet international requirements, we support our clients by providing risk assessment studies and infallible safety on every site.',
    'Golden Eagle a mis tous les moyens nécessaires à la bonne marche de ses activités et ses atouts sont : La santé, sécurité et l’environnement, la vivacité, l’expertise, et un capital humain dynamique et professionnel.': 'Golden Eagle has provided all the necessary means for the smooth running of its activities and its assets are: Health, safety and environment, vivacity, expertise, and a dynamic and professional human capital.',
    'Nos Valeurs Fondamentales': 'Our Core Values',
    'Majestueux': 'Majestic',
    '« Nous respectons notre engagement. »': '"We honor our commitment."',
    'Minutieux': 'Meticulous',
    '« Nous prenons en compte tous les détails dans nos projets. »': '"We take into account every detail in our projects."',
    'Précis': 'Precise',
    '« La précision est un facteur déterminant de notre activité. »': '"Precision is a determining factor in our business."',
    'Vivace': 'Vivacious',
    '« Notre force, une équipe dynamique. »': '"Our strength, a dynamic team."',
    'Aperçu de nos Services': 'Overview of our Services',
    'Forage & Dynamitage': 'Drilling & Blasting',
    'Équipe expérimentée et équipements performants pour répondre à l\'ensemble de vos besoins en toute sécurité.': 'Experienced team and high-performance equipment to meet all your needs safely.',
    'En savoir plus': 'Learn more',
    'Vente de Substances Explosives': 'Sale of Explosive Substances',
    'Vente, fabrication et fourniture d\'explosifs dans le respect rigoureux des normes de sécurité internationales.': 'Sale, manufacturing and supply of explosives in strict compliance with international safety standards.',
    'Topographie de Précision': 'Precision Topography',
    'Équipements de dernière génération pour effectuer des travaux d\'implantation et de calculs de volumes.': 'Latest generation equipment for layout works and volume calculations.',
    'Voir tous nos services': 'See all our services',
    'Forage, Dynamitage, Explosifs': 'Drilling, Blasting, Explosives',
    
    # about.html specific
    'Notre Histoire': 'Our History',
    'GOLDEN EAGLE est une Société à Responsabilité Limitée (SARL) spécialisée dans le forage, la fabrication, la fourniture d\'explosifs et les services de dynamitage.': 'GOLDEN EAGLE is a Limited Liability Company (SARL) specialized in drilling, manufacturing, supplying explosives and blasting services.',
    'Nous sommes une entreprise assurant des formations pratiques dans le domaine des BTP, mines et carrières, et des sociétés industrielles en raison de notre solide expérience dans un secteur en pleine expansion.': 'We are a company providing practical training in the field of construction, mining and quarrying, and industrial companies due to our solid experience in a booming sector.',
    'Notre Capital Humain :': 'Our Human Capital:',
    'Le Directeur général s\'est entouré d\'une équipe dynamique et professionnelle. Le recrutement se fait avec des critères de sélection élevés. Notre force se trouve dans le partage de connaissances et d\'expériences à tous les niveaux, appuyé par des formations certifiées périodiques.': 'The General Manager has surrounded himself with a dynamic and professional team. Recruitment is done with high selection criteria. Our strength lies in sharing knowledge and experience at all levels, supported by periodic certified training.',
    'Nos Infrastructures :': 'Our Infrastructure:',
    'L\'entreprise dispose de trois sites principaux, dont le bureau et le garage au Burkina Faso, ainsi qu\'un bureau en Côte d\'Ivoire, offrant le confort et la sécurité nécessaires aux employés.': 'The company has three main sites, including the office and garage in Burkina Faso, and an office in Ivory Coast, offering the necessary comfort and safety to employees.',
    'Accroître la productivité des entreprises nationales afin d\'améliorer leur performance.': 'Increase the productivity of national companies to improve their performance.',
    'Donner de la valeur ajoutée aux entreprises et au capital humain dans le domaine des mines et carrières, du BTP et des activités similaires.': 'Add value to companies and human capital in the mining and quarrying, construction and similar activities sectors.',
    'NOS PILIERS FONDAMENTAUX': 'OUR FUNDAMENTAL PILLARS',
    'Nos Valeurs': 'Our Values',
    'Esprit de partage du capital d\'expériences accumulées, transmission de valeurs et d\'expertise, notion de courage, de détermination et de persévérance.': 'Spirit of sharing accumulated capital of experiences, transmission of values and expertise, notion of courage, determination and perseverance.',
    'Rejoindre l\'aventure': 'Join the adventure',
    
    # services.html specific
    'Notre Expertise': 'Our Expertise',
    'Des solutions industrielles de bout en bout.': 'End-to-end industrial solutions.',
    'GOLDEN EAGLE met à la disposition de sa clientèle une équipe expérimentée et des équipements performants, et utilise plusieurs techniques éprouvées de forage et de dynamitage pour répondre à l\'ensemble de ses besoins.': 'GOLDEN EAGLE provides its clients with an experienced team and high-performance equipment, and uses several proven drilling and blasting techniques to meet all their needs.',
    'Fourniture, Fabrication & Vente de substances explosives': 'Supply, Manufacturing & Sale of explosive substances',
    'Selon la demande du client, nous vendons, livrons et fabriquons des substances explosives tout en suivant les règles de l\'art, en respectant rigoureusement les normes de sécurité et les exigences techniques du terrain.': 'Depending on the client\'s request, we sell, deliver and manufacture explosive substances while following best practices, strictly respecting safety standards and technical requirements of the field.',
    'Produits fournis et fabriqués :': 'Supplied and manufactured products:',
    'Booster, Magnum Booster, Nitrate d’Ammonium, IED Détonateur Electrique Instantané, cordeaux détonateurs, Splitex, accessoires de surface Trun line, Anfex, Emulsion S100.': 'Booster, Magnum Booster, Ammonium Nitrate, IED Instant Electric Detonator, detonating cords, Splitex, Trun line surface accessories, Anfex, Emulsion S100.',
    'Consultation & Services techniques': 'Consultation & Technical Services',
    'Nous évaluons périodiquement les résultats de nos travaux de forage et de dynamitage sur les sites de nos partenaires. Ces évaluations permettent d\'améliorer la fragmentation après dynamitage et d\'optimiser le ratio coût/qualité.': 'We periodically evaluate the results of our drilling and blasting works on our partners\' sites. These evaluations help improve fragmentation after blasting and optimize the cost/quality ratio.',
    'Évaluation des risques professionnels': 'Professional risk assessment',
    'GOLDEN EAGLE dispose d\'une technologie de pointe dans l\'évaluation des risques liés au rendement, à la faisabilité opérationnelle et à la sécurisation globale des chantiers.': 'GOLDEN EAGLE has cutting-edge technology in risk assessment related to performance, operational feasibility and overall site security.',
    'Topographie': 'Topography',
    'Mise à disposition d\'équipements topographiques de dernière génération afin d\'effectuer des travaux de levé, d\'implantation et de calculs de volumes précis.': 'Provision of latest generation topographic equipment to carry out precise survey, layout and volume calculation works.',
    'Formation spécialisée': 'Specialized training',
    'Formations dispensées par des professionnels de terrain, alliant pédagogie pratique et transmission des dernières techniques du secteur (équipes de gradin, forage & dynamitage, HSE, gestion des risques).': 'Training provided by field professionals, combining practical pedagogy and transmission of the latest industry techniques (bench teams, drilling & blasting, HSE, risk management).',
    'Transport & Logistique sécurisée': 'Secure Transport & Logistics',
    'Acheminement sécurisé des produits et substances explosives depuis les usines ou ports jusqu\'aux sites miniers sous escorte armée (Police / Gendarmerie nationale), en stricte conformité avec la réglementation en vigueur.': 'Secure routing of explosive products and substances from factories or ports to mining sites under armed escort (Police / National Gendarmerie), in strict compliance with current regulations.',
    'Vente d\'équipements, outillage & maintenance': 'Sale of equipment, tools & maintenance',
    'Fourniture d\'équipements, pompes, accessoires et outillages industriels de haute qualité répondant aux exigences sévères des environnements miniers et de génie civil.': 'Supply of high-quality equipment, pumps, accessories and industrial tools meeting the severe requirements of mining and civil engineering environments.',
    'Catalogue d\'équipements :': 'Equipment catalog:',
    'Exploseurs, Outils de dynamitage performants, Couteaux, Équipements de Protection Individuelle (EPI), Drones, GPS, Outils et pièces de foreuses, Sirènes, etc.': 'Exploders, High-performance blasting tools, Knives, Personal Protective Equipment (PPE), Drones, GPS, Drill tools and parts, Sirens, etc.',
    'Solliciter nos services': 'Request our services',
    
    # contact.html specific
    'Parlons de votre Projet': 'Let\'s Talk About Your Project',
    'Nos ingénieurs sont prêts à vous accompagner.': 'Our engineers are ready to support you.',
    'NOUS JOINDRE': 'CONTACT US',
    'Que ce soit pour une demande d\'informations, une consultation technique, ou un projet de grande envergure, n\'hésitez pas à nous contacter.': 'Whether for a request for information, technical consultation, or a large-scale project, do not hesitate to contact us.',
    'Siège Social & Adresse Postale': 'Head Office & Postal Address',
    'Secteur 53 (ex-secteur 15), Ouaga 2000, Route de Pô': 'Sector 53 (ex-sector 15), Ouaga 2000, Route de Pô',
    '(à l\'arrière du bureau de la SONABEL)': '(behind the SONABEL office)',
    'Ouagadougou, Burkina Faso': 'Ouagadougou, Burkina Faso',
    '01 BP 6390 Ouagadougou 01 – Burkina Faso': '01 BP 6390 Ouagadougou 01 – Burkina Faso',
    'Téléphones': 'Phones',
    'Email': 'Email',
    'Horaires d\'ouverture': 'Opening hours',
    'Du Lundi au Vendredi': 'Monday to Friday',
    'de 08h00 à 16h00': 'from 08:00 to 16:00',
    'Envoyer un message': 'Send a message',
    'Votre nom complet': 'Your full name',
    'Objet de votre demande': 'Subject of your request',
    'Veuillez détailler votre projet ou votre demande ici...': 'Please detail your project or request here...',
    'Envoyer le message': 'Send the message'
}

for root, _, files in os.walk(path):
    for f in files:
        if f.endswith('.html'):
            filepath = os.path.join(root, f)
            with open(filepath, 'r', encoding='utf-8') as file:
                content = file.read()
            for fr, en in translations.items():
                content = content.replace(fr, en)
            with open(filepath, 'w', encoding='utf-8') as file:
                file.write(content)

print("Translation completed successfully")
