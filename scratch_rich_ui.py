import os

base_dir = r"c:\Users\HP ZBOOK\Downloads\Golden eagle\redesign"

css_to_add = """
/* --------------------------
   Product Grid (products.html)
--------------------------- */
.products-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 2.5rem;
    margin-top: 3rem;
}

.product-card {
    background: var(--white);
    border-radius: 12px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.05);
    overflow: hidden;
    position: relative;
    border: 1px solid rgba(0,0,0,0.05);
    transition: all 0.4s cubic-bezier(0.25, 1, 0.5, 1);
    display: flex;
    flex-direction: column;
}

.product-card:hover {
    transform: translateY(-10px);
    box-shadow: 0 20px 40px rgba(204, 153, 51, 0.15);
    border-color: var(--gold);
}

.product-img-wrapper {
    position: relative;
    height: 220px;
    overflow: hidden;
}

.product-img-wrapper img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    transition: transform 0.6s ease;
}

.product-card:hover .product-img-wrapper img {
    transform: scale(1.1);
}

.product-badge {
    position: absolute;
    top: 15px;
    right: 15px;
    background-color: var(--gold);
    color: var(--white);
    padding: 0.3rem 1rem;
    font-size: 0.8rem;
    font-family: var(--font-heading);
    text-transform: uppercase;
    border-radius: 30px;
    letter-spacing: 1px;
    z-index: 2;
    box-shadow: 0 2px 10px rgba(0,0,0,0.2);
}

.product-content {
    padding: 2rem;
    display: flex;
    flex-direction: column;
    flex: 1;
}

.product-content h3 {
    font-size: 1.4rem;
    margin-bottom: 1rem;
    color: var(--black);
}

.product-content p {
    font-size: 0.95rem;
    color: #666;
    margin-bottom: 1.5rem;
    flex: 1;
}

.product-features {
    list-style: none;
    margin-bottom: 1.5rem;
}

.product-features li {
    font-size: 0.85rem;
    color: #555;
    margin-bottom: 0.5rem;
    display: flex;
    align-items: center;
}

.product-features li i {
    color: var(--gold);
    margin-right: 10px;
    font-size: 0.8rem;
}

.product-btn {
    display: inline-block;
    padding: 0.8rem 1.5rem;
    background-color: transparent;
    border: 1px solid var(--gold);
    color: var(--gold);
    font-family: var(--font-heading);
    text-transform: uppercase;
    font-size: 0.85rem;
    border-radius: 4px;
    transition: all 0.3s ease;
    width: 100%;
    text-align: center;
}

.product-card:hover .product-btn {
    background-color: var(--gold);
    color: var(--white);
}

@media (max-width: 992px) {
    .products-grid {
        grid-template-columns: repeat(2, 1fr);
    }
}

@media (max-width: 768px) {
    .products-grid {
        grid-template-columns: 1fr;
    }
}
"""

css_path = os.path.join(base_dir, 'styles.css')
with open(css_path, 'r', encoding='utf-8') as f:
    css_content = f.read()

if ".products-grid" not in css_content:
    with open(css_path, 'a', encoding='utf-8') as f:
        f.write(css_to_add)

print("CSS updated!")

fr_content = """
            <div class="text-center mb-xl reveal">
                <h2 class="section-title-clean">Explosifs pour l'Industrie Minière</h2>
                <div class="gold-line"></div>
                <p class="welcome-text">Des produits explosifs à part entière, fabriqués selon les plus hauts standards de sécurité.</p>
            </div>

            <div class="products-grid mb-xl">
                <!-- Product 1 -->
                <div class="product-card reveal">
                    <div class="product-badge">Explosif</div>
                    <div class="product-img-wrapper">
                        <img src="assets/citerne.jpg" alt="Nitrate d'Ammonium">
                    </div>
                    <div class="product-content">
                        <h3>Nitrate d'Ammonium</h3>
                        <p>Substance de base pour la fabrication d'explosifs miniers, assurant une puissance de tir optimale.</p>
                        <ul class="product-features">
                            <li><i class="fas fa-check"></i> Haute pureté</li>
                            <li><i class="fas fa-check"></i> Rendement maximal</li>
                        </ul>
                        <a href="contact.html" class="product-btn">Commander</a>
                    </div>
                </div>

                <!-- Product 2 -->
                <div class="product-card reveal delay-100">
                    <div class="product-badge">Haute Puissance</div>
                    <div class="product-img-wrapper">
                        <img src="assets/formation.jpg" alt="Boosters & Magnum Boosters">
                    </div>
                    <div class="product-content">
                        <h3>Boosters & Magnum Boosters</h3>
                        <p>Conçus pour l'amorçage efficace d'explosifs insensibles, garantissant une détonation sûre.</p>
                        <ul class="product-features">
                            <li><i class="fas fa-check"></i> Amorçage fiable</li>
                            <li><i class="fas fa-check"></i> Divers grammages</li>
                        </ul>
                        <a href="contact.html" class="product-btn">Commander</a>
                    </div>
                </div>

                <!-- Product 3 -->
                <div class="product-card reveal delay-200">
                    <div class="product-badge">Accessoire de tir</div>
                    <div class="product-img-wrapper">
                        <img src="assets/WhatsApp-Image-2019-09-25-at-16.15.16-1.jpeg" alt="Détonateurs et Cordeaux">
                    </div>
                    <div class="product-content">
                        <h3>Détonateurs & Cordeaux</h3>
                        <p>Détonateurs électriques instantanés et cordeaux détonateurs pour une précision sans faille.</p>
                        <ul class="product-features">
                            <li><i class="fas fa-check"></i> Précision temporelle</li>
                            <li><i class="fas fa-check"></i> Sécurité optimale</li>
                        </ul>
                        <a href="contact.html" class="product-btn">Commander</a>
                    </div>
                </div>
            </div>

            <div class="text-center mb-xl reveal mt-xl">
                <h2 class="section-title-clean">Équipements & Accessoires</h2>
                <div class="gold-line"></div>
                <p class="welcome-text">Une sélection rigoureuse d'équipements de pointe pour optimiser vos opérations de terrain.</p>
            </div>

            <div class="products-grid mb-xl">
                <!-- Equip 1 -->
                <div class="product-card reveal">
                    <div class="product-badge" style="background-color: var(--black);">Ingénierie</div>
                    <div class="product-img-wrapper">
                        <img src="assets/Camion-de-dynamitage-1024x768.jpeg" alt="Unité de Transformation Mobile">
                    </div>
                    <div class="product-content">
                        <h3>Unité de Transformation Mobile (MMU)</h3>
                        <p>Camions spécialisés pour le mélange et le chargement d'explosifs directement sur site minier.</p>
                        <ul class="product-features">
                            <li><i class="fas fa-check"></i> Chargement sécurisé</li>
                            <li><i class="fas fa-check"></i> Technologie de pointe</li>
                        </ul>
                        <a href="contact.html" class="product-btn">Demander un devis</a>
                    </div>
                </div>

                <!-- Equip 2 -->
                <div class="product-card reveal delay-100">
                    <div class="product-badge" style="background-color: var(--black);">Contrôle</div>
                    <div class="product-img-wrapper">
                        <img src="assets/IMG-20260909-WA0019.jpg" alt="Télécommandes de tir">
                    </div>
                    <div class="product-content">
                        <h3>Exploseurs & Télécommandes</h3>
                        <p>Systèmes d'initiation électroniques (Exploseurs) pour un déclenchement des tirs à distance.</p>
                        <ul class="product-features">
                            <li><i class="fas fa-check"></i> Portée étendue</li>
                            <li><i class="fas fa-check"></i> Protection cryptée</li>
                        </ul>
                        <a href="contact.html" class="product-btn">Demander un devis</a>
                    </div>
                </div>

                <!-- Equip 3 -->
                <div class="product-card reveal delay-200">
                    <div class="product-badge" style="background-color: var(--black);">Topographie</div>
                    <div class="product-img-wrapper">
                        <img src="assets/topographie-gps.jpg" alt="Drones et GPS">
                    </div>
                    <div class="product-content">
                        <h3>Drones & GPS de Précision</h3>
                        <p>Solutions topographiques avancées pour le levé de terrain, calcul de volumes et surveillance.</p>
                        <ul class="product-features">
                            <li><i class="fas fa-check"></i> Topographie 3D</li>
                            <li><i class="fas fa-check"></i> Modélisation de terrain</li>
                        </ul>
                        <a href="contact.html" class="product-btn">Demander un devis</a>
                    </div>
                </div>
            </div>
            
            <div class="text-center mt-xl reveal">
                <a href="contact.html" class="btn btn-gold">Voir notre catalogue complet <i class="fas fa-arrow-right"></i></a>
            </div>
"""

en_content = """
            <div class="text-center mb-xl reveal">
                <h2 class="section-title-clean">Explosives for the Mining Industry</h2>
                <div class="gold-line"></div>
                <p class="welcome-text">Full-fledged explosive products, manufactured to the highest safety standards.</p>
            </div>

            <div class="products-grid mb-xl">
                <!-- Product 1 -->
                <div class="product-card reveal">
                    <div class="product-badge">Explosive</div>
                    <div class="product-img-wrapper">
                        <img src="../assets/citerne.jpg" alt="Ammonium Nitrate">
                    </div>
                    <div class="product-content">
                        <h3>Ammonium Nitrate</h3>
                        <p>Base substance for the manufacture of mining explosives, ensuring optimal blasting power.</p>
                        <ul class="product-features">
                            <li><i class="fas fa-check"></i> High purity</li>
                            <li><i class="fas fa-check"></i> Maximum yield</li>
                        </ul>
                        <a href="contact.html" class="product-btn">Order Now</a>
                    </div>
                </div>

                <!-- Product 2 -->
                <div class="product-card reveal delay-100">
                    <div class="product-badge">High Power</div>
                    <div class="product-img-wrapper">
                        <img src="../assets/formation.jpg" alt="Boosters & Magnum Boosters">
                    </div>
                    <div class="product-content">
                        <h3>Boosters & Magnum Boosters</h3>
                        <p>Designed for the effective initiation of insensitive explosives, ensuring safe detonation.</p>
                        <ul class="product-features">
                            <li><i class="fas fa-check"></i> Reliable initiation</li>
                            <li><i class="fas fa-check"></i> Various sizes</li>
                        </ul>
                        <a href="contact.html" class="product-btn">Order Now</a>
                    </div>
                </div>

                <!-- Product 3 -->
                <div class="product-card reveal delay-200">
                    <div class="product-badge">Blasting Accessory</div>
                    <div class="product-img-wrapper">
                        <img src="../assets/WhatsApp-Image-2019-09-25-at-16.15.16-1.jpeg" alt="Detonators and Cords">
                    </div>
                    <div class="product-content">
                        <h3>Detonators & Cords</h3>
                        <p>Instant electric detonators and detonating cords for flawless precision.</p>
                        <ul class="product-features">
                            <li><i class="fas fa-check"></i> Temporal precision</li>
                            <li><i class="fas fa-check"></i> Optimal security</li>
                        </ul>
                        <a href="contact.html" class="product-btn">Order Now</a>
                    </div>
                </div>
            </div>

            <div class="text-center mb-xl reveal mt-xl">
                <h2 class="section-title-clean">Equipment & Accessories</h2>
                <div class="gold-line"></div>
                <p class="welcome-text">A rigorous selection of cutting-edge equipment to optimize your field operations.</p>
            </div>

            <div class="products-grid mb-xl">
                <!-- Equip 1 -->
                <div class="product-card reveal">
                    <div class="product-badge" style="background-color: var(--black);">Engineering</div>
                    <div class="product-img-wrapper">
                        <img src="../assets/Camion-de-dynamitage-1024x768.jpeg" alt="Mobile Manufacturing Unit">
                    </div>
                    <div class="product-content">
                        <h3>Mobile Manufacturing Unit (MMU)</h3>
                        <p>Specialized trucks for mixing and loading explosives directly on the mining site.</p>
                        <ul class="product-features">
                            <li><i class="fas fa-check"></i> Secure loading</li>
                            <li><i class="fas fa-check"></i> Advanced technology</li>
                        </ul>
                        <a href="contact.html" class="product-btn">Request Quote</a>
                    </div>
                </div>

                <!-- Equip 2 -->
                <div class="product-card reveal delay-100">
                    <div class="product-badge" style="background-color: var(--black);">Control</div>
                    <div class="product-img-wrapper">
                        <img src="../assets/IMG-20260909-WA0019.jpg" alt="Firing Remote Controls">
                    </div>
                    <div class="product-content">
                        <h3>Exploders & Remote Controls</h3>
                        <p>Electronic initiation systems (Exploders) for remote triggering of blasts.</p>
                        <ul class="product-features">
                            <li><i class="fas fa-check"></i> Extended range</li>
                            <li><i class="fas fa-check"></i> Encrypted protection</li>
                        </ul>
                        <a href="contact.html" class="product-btn">Request Quote</a>
                    </div>
                </div>

                <!-- Equip 3 -->
                <div class="product-card reveal delay-200">
                    <div class="product-badge" style="background-color: var(--black);">Topography</div>
                    <div class="product-img-wrapper">
                        <img src="../assets/topographie-gps.jpg" alt="Drones and GPS">
                    </div>
                    <div class="product-content">
                        <h3>Drones & Precision GPS</h3>
                        <p>Advanced topographic solutions for terrain survey, volume calculation and surveillance.</p>
                        <ul class="product-features">
                            <li><i class="fas fa-check"></i> 3D Topography</li>
                            <li><i class="fas fa-check"></i> Terrain modeling</li>
                        </ul>
                        <a href="contact.html" class="product-btn">Request Quote</a>
                    </div>
                </div>
            </div>
            
            <div class="text-center mt-xl reveal">
                <a href="contact.html" class="btn btn-gold">View our full catalog <i class="fas fa-arrow-right"></i></a>
            </div>
"""

def replace_services_content(template, new_content):
    start_tag = '<section class="services-detailed section-padding">'
    end_tag = '</section>'
    
    start_idx = template.find(start_tag)
    if start_idx != -1:
        end_idx = template.find(end_tag, start_idx)
        if end_idx != -1:
            before = template[:start_idx + len(start_tag)]
            after = template[end_idx:]
            return before + '\n        <div class="container">\n' + new_content + '\n        </div>\n    ' + after
    return template

fr_html_path = os.path.join(base_dir, 'products.html')
en_html_path = os.path.join(base_dir, 'en', 'products.html')

with open(fr_html_path, 'r', encoding='utf-8') as f:
    fr_html = f.read()

with open(en_html_path, 'r', encoding='utf-8') as f:
    en_html = f.read()

fr_final = replace_services_content(fr_html, fr_content)
en_final = replace_services_content(en_html, en_content)

with open(fr_html_path, 'w', encoding='utf-8') as f:
    f.write(fr_final)

with open(en_html_path, 'w', encoding='utf-8') as f:
    f.write(en_final)

print("HTML updated with rich cards!")
