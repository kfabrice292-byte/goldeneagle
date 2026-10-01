import os
import re

base_dir = r"c:\Users\HP ZBOOK\Downloads\Golden eagle\redesign"

with open(os.path.join(base_dir, 'services.html'), 'r', encoding='utf-8') as f:
    fr_template = f.read()

with open(os.path.join(base_dir, 'en', 'services.html'), 'r', encoding='utf-8') as f:
    en_template = f.read()

# Update Active Links
fr_template = fr_template.replace('href="services.html" class="nav-link active"', 'href="services.html" class="nav-link"')
fr_template = fr_template.replace('href="products.html" class="nav-link"', 'href="products.html" class="nav-link active"')
# Language switcher fix
fr_template = fr_template.replace('<a href="services.html" class="active">FR</a> | <a href="en/services.html">EN</a>', '<a href="products.html" class="active">FR</a> | <a href="en/products.html">EN</a>')

en_template = en_template.replace('href="services.html" class="nav-link active"', 'href="services.html" class="nav-link"')
en_template = en_template.replace('href="products.html" class="nav-link"', 'href="products.html" class="nav-link active"')
# Language switcher fix
en_template = en_template.replace('<a href="../services.html">FR</a> | <a href="services.html" class="active">EN</a>', '<a href="../products.html">FR</a> | <a href="products.html" class="active">EN</a>')

# Replace Title and Headers
fr_template = fr_template.replace('<title>Nos Services | Golden Eagle</title>', '<title>Produits & Équipements | Golden Eagle</title>')
fr_template = fr_template.replace('<h1 class="page-title">Notre Expertise</h1>', '<h1 class="page-title">Nos Produits & Équipements</h1>')
fr_template = fr_template.replace('<p class="page-subtitle">Des solutions industrielles de bout en bout.</p>', '<p class="page-subtitle">Des explosifs de haute qualité et des équipements de pointe pour vos opérations.</p>')

en_template = en_template.replace('<title>Our Services | Golden Eagle</title>', '<title>Products & Equipment | Golden Eagle</title>')
en_template = en_template.replace('<h1 class="page-title">Our Expertise</h1>', '<h1 class="page-title">Our Products & Equipment</h1>')
en_template = en_template.replace('<p class="page-subtitle">End-to-end industrial solutions.</p>', '<p class="page-subtitle">High-quality explosives and cutting-edge equipment for your operations.</p>')

# Main content blocks
fr_content = """
            <!-- Product Section 1 -->
            <div class="service-row reveal">
                <div class="service-row-img">
                    <img src="assets/citerne.jpg" alt="Explosifs pour les mines">
                </div>
                <div class="service-row-content">
                    <h2 class="service-title-lg">Explosifs pour l'Industrie Minière</h2>
                    <div class="gold-line align-left"></div>
                    <p>Nous fournissons des produits explosifs à part entière de très haute qualité pour répondre aux exigences des sociétés minières et des grands projets de génie civil.</p>
                    <p>Notre gamme comprend : Booster, Magnum Booster, Nitrate d’Ammonium, Détonateurs électriques instantanés, Cordeaux détonateurs, Splitex, Accessoires de surface Trun line, Anfex, Emulsion S100.</p>
                </div>
            </div>

            <!-- Product Section 2 -->
            <div class="service-row reverse reveal">
                <div class="service-row-img">
                    <img src="assets/Camion-de-dynamitage-1024x768.jpeg" alt="Équipements et Accessoires">
                </div>
                <div class="service-row-content">
                    <h2 class="service-title-lg">Équipements & Accessoires</h2>
                    <div class="gold-line align-left"></div>
                    <p>Nous proposons une large gamme d'équipements de pointe pour optimiser vos opérations sur le terrain et garantir la plus haute sécurité de vos équipes.</p>
                    <ul>
                        <li><strong>Unité de transformation mobile (MMU)</strong> : pour le mélange et le chargement sur site.</li>
                        <li><strong>Télécommandes de tir</strong> et systèmes d'initiation électroniques (Exploseurs).</li>
                        <li><strong>Accessoires de forage et de minage</strong> (Outils et pièces de foreuses, couteaux).</li>
                        <li><strong>Équipements de pointe</strong> : Drones pour la surveillance, GPS de précision.</li>
                        <li><strong>Équipements de Protection Individuelle (EPI)</strong> et sirènes d'alerte.</li>
                    </ul>
                </div>
            </div>
            
            <div class="text-center mt-xl reveal">
                <a href="contact.html" class="btn btn-gold">Demander un devis <i class="fas fa-arrow-right"></i></a>
            </div>
"""

en_content = """
            <!-- Product Section 1 -->
            <div class="service-row reveal">
                <div class="service-row-img">
                    <img src="../assets/citerne.jpg" alt="Mining Explosives">
                </div>
                <div class="service-row-content">
                    <h2 class="service-title-lg">Explosives for the Mining Industry</h2>
                    <div class="gold-line align-left"></div>
                    <p>We provide full-fledged, high-quality explosive products to meet the requirements of mining companies and large-scale civil engineering projects.</p>
                    <p>Our range includes: Booster, Magnum Booster, Ammonium Nitrate, Instant Electric Detonators, Detonating cords, Splitex, Trun line surface accessories, Anfex, Emulsion S100.</p>
                </div>
            </div>

            <!-- Product Section 2 -->
            <div class="service-row reverse reveal">
                <div class="service-row-img">
                    <img src="../assets/Camion-de-dynamitage-1024x768.jpeg" alt="Equipment and Accessories">
                </div>
                <div class="service-row-content">
                    <h2 class="service-title-lg">Equipment & Accessories</h2>
                    <div class="gold-line align-left"></div>
                    <p>We offer a wide range of cutting-edge equipment to optimize your operations in the field and guarantee the highest safety for your teams.</p>
                    <ul>
                        <li><strong>Mobile Manufacturing Units (MMU)</strong>: for on-site mixing and loading.</li>
                        <li><strong>Firing remote controls</strong> and electronic initiation systems (Exploders).</li>
                        <li><strong>Drilling and blasting accessories</strong> (Drill tools and parts, knives).</li>
                        <li><strong>Advanced equipment</strong>: Drones for surveillance, precision GPS.</li>
                        <li><strong>Personal Protective Equipment (PPE)</strong> and warning sirens.</li>
                    </ul>
                </div>
            </div>
            
            <div class="text-center mt-xl reveal">
                <a href="contact.html" class="btn btn-gold">Request a quote <i class="fas fa-arrow-right"></i></a>
            </div>
"""

# Find the section and replace it
def replace_services_content(template, new_content):
    start_tag = '<section class="services-detailed section-padding">'
    end_tag = '</section>'
    
    start_idx = template.find(start_tag)
    if start_idx != -1:
        # Find the end of this section
        end_idx = template.find(end_tag, start_idx)
        if end_idx != -1:
            # We replace what's inside
            before = template[:start_idx + len(start_tag)]
            after = template[end_idx:]
            
            return before + '\n        <div class="container">\n' + new_content + '\n        </div>\n    ' + after
    return template

fr_final = replace_services_content(fr_template, fr_content)
en_final = replace_services_content(en_template, en_content)

with open(os.path.join(base_dir, 'products.html'), 'w', encoding='utf-8') as f:
    f.write(fr_final)
    
with open(os.path.join(base_dir, 'en', 'products.html'), 'w', encoding='utf-8') as f:
    f.write(en_final)
    
print("Created products.html and en/products.html")
