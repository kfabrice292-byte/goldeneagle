import os
import re

DIR = r"c:\Users\HP ZBOOK\Downloads\Golden eagle\redesign"

def run():
    # 1. Update index.html
    with open(os.path.join(DIR, "index.html"), "r", encoding="utf-8") as f:
        idx = f.read()

    new_mapa = """<section class="mapa-home">
            <h1>Présence Globale</h1>
            <p class="mapa-titre-filtre">CHOISISSEZ UN TYPE D'IMPLANTATION</p>
            <ul class="mapa-filtre">
                <li class="active"><button data-filter="all">Golden Eagle</button></li>
                <li><button data-filter="bases">Bases Opérationnelles</button></li>
                <li><button data-filter="mmu">Unités Mobiles MMU</button></li>
            </ul>
            <div class="mapa-container">
                <!-- Map Dots representing West Africa locations roughly -->
                <div class="map-dot type-bases" style="top: 40%; left: 45%;">
                    <div class="tooltip">Ouagadougou, Burkina Faso (Base Principale)</div>
                </div>
                <div class="map-dot type-bases" style="top: 55%; left: 35%;">
                    <div class="tooltip">Bamako, Mali (Base)</div>
                </div>
                <div class="map-dot type-mmu" style="top: 60%; left: 55%;">
                    <div class="tooltip">Site Minier, Niger (Unité MMU)</div>
                </div>
                <div class="map-dot type-mmu" style="top: 30%; left: 30%;">
                    <div class="tooltip">Site Minier, Sénégal (Unité MMU)</div>
                </div>
                <div class="map-dot type-bases" style="top: 70%; left: 42%;">
                    <div class="tooltip">Abidjan, Côte d'Ivoire (Base)</div>
                </div>
                
                <div class="cifras-lista">
                    <div class="cifra-box">
                        <span class="cifra" id="cifra-bases">3</span>
                        <p>bases en<br>+2 pays</p>
                    </div>
                    <div class="cifra-box">
                        <span class="cifra" id="cifra-ops">+5</span>
                        <p>Opérations dans<br>pays</p>
                    </div>
                    <div class="cifra-box">
                        <span class="cifra">100%</span>
                        <p>Tirs<br>sécurisés</p>
                    </div>
                </div>
            </div>
            <p class="text-center" style="margin-top: 100px;">
                <a class="btn btn-gold" href="contact.html">IMPLANTATIONS RÉGIONALES</a>
            </p>
        </section>"""

    idx = re.sub(r'<section class="mapa-home">.*?</section>', new_mapa, idx, flags=re.DOTALL)
    
    with open(os.path.join(DIR, "index.html"), "w", encoding="utf-8") as f:
        f.write(idx)

    # 2. Update styles.css
    css_additions = """
/* === MAPA HOME INTERACTIVE === */
.mapa-home {
    padding: 80px 20px;
    background-color: #fff;
    text-align: center;
}
.mapa-home h1 {
    font-size: 2.8rem;
    color: var(--gray-dark);
    margin-bottom: 10px;
}
.mapa-titre-filtre {
    font-size: 0.9rem;
    color: var(--gray-text);
    letter-spacing: 2px;
    margin-bottom: 40px;
}
.mapa-filtre {
    list-style: none;
    padding: 0;
    display: flex;
    justify-content: center;
    gap: 40px;
    margin-bottom: 50px;
}
.mapa-filtre button {
    background: none;
    border: none;
    font-size: 1.1rem;
    color: var(--gray-text);
    cursor: pointer;
    padding-bottom: 8px;
    border-bottom: 2px solid transparent;
    transition: all 0.3s ease;
    font-weight: 600;
}
.mapa-filtre li.active button, .mapa-filtre button:hover {
    color: var(--gold);
    border-bottom: 2px solid var(--gold);
}
.mapa-container {
    position: relative;
    max-width: 1000px;
    margin: 0 auto 80px;
    height: 450px;
    background-image: radial-gradient(#d1d5db 2px, transparent 2px);
    background-size: 30px 30px;
    border-radius: 10px;
    border: 1px solid #f3f4f6;
}
.map-dot {
    position: absolute;
    width: 24px;
    height: 24px;
    background-color: var(--gold);
    border-radius: 50%;
    transform: translate(-50%, -50%);
    cursor: pointer;
    transition: all 0.3s;
    box-shadow: 0 0 0 0 rgba(204, 163, 0, 0.7);
    animation: pulse-gold 2s infinite;
    z-index: 5;
}
.map-dot:hover {
    transform: translate(-50%, -50%) scale(1.3);
    z-index: 10;
}
.map-dot .tooltip {
    position: absolute;
    bottom: 35px;
    left: 50%;
    transform: translateX(-50%) translateY(10px);
    background: var(--gray-dark);
    color: #fff;
    padding: 8px 15px;
    border-radius: 4px;
    font-size: 0.9rem;
    opacity: 0;
    pointer-events: none;
    transition: all 0.3s ease;
    white-space: nowrap;
    box-shadow: 0 5px 15px rgba(0,0,0,0.2);
}
.map-dot:hover .tooltip {
    opacity: 1;
    transform: translateX(-50%) translateY(0);
}
@keyframes pulse-gold {
    0% { box-shadow: 0 0 0 0 rgba(204, 163, 0, 0.7); }
    70% { box-shadow: 0 0 0 20px rgba(204, 163, 0, 0); }
    100% { box-shadow: 0 0 0 0 rgba(204, 163, 0, 0); }
}
.cifras-lista {
    position: absolute;
    bottom: -50px;
    width: 100%;
    display: flex;
    justify-content: center;
    gap: 30px;
    z-index: 20;
}
.cifra-box {
    background: #fff;
    box-shadow: 0 15px 40px rgba(0,0,0,0.1);
    padding: 25px 40px;
    border-radius: 8px;
    text-align: center;
    min-width: 220px;
    transition: transform 0.3s;
}
.cifra-box:hover {
    transform: translateY(-5px);
}
.cifra-box .cifra {
    display: block;
    font-size: 3.5rem;
    font-weight: 800;
    color: var(--gold);
    line-height: 1;
    margin-bottom: 10px;
}
.cifra-box p {
    color: var(--gray-dark);
    font-weight: 700;
    font-size: 1rem;
    text-transform: uppercase;
    margin: 0;
}
"""

    with open(os.path.join(DIR, "styles.css"), "a", encoding="utf-8") as f:
        f.write(css_additions)

    # 3. Update script.js
    js_additions = """
    // Map Filtering Logic
    const filterBtns = document.querySelectorAll('.mapa-filtre button');
    const mapDots = document.querySelectorAll('.map-dot');
    const cifraBases = document.getElementById('cifra-bases');
    const cifraOps = document.getElementById('cifra-ops');
    
    if(filterBtns.length > 0) {
        filterBtns.forEach(btn => {
            btn.addEventListener('click', () => {
                // Remove active from all
                document.querySelectorAll('.mapa-filtre li').forEach(li => li.classList.remove('active'));
                btn.parentElement.classList.add('active');
                
                const filter = btn.getAttribute('data-filter');
                let visibleCount = 0;
                
                mapDots.forEach(dot => {
                    if(filter === 'all' || dot.classList.contains('type-' + filter)) {
                        dot.style.display = 'block';
                        // Trigger reflow for animation restart
                        dot.style.animation = 'none';
                        void dot.offsetWidth; 
                        dot.style.animation = 'pulse-gold 2s infinite';
                        visibleCount++;
                    } else {
                        dot.style.display = 'none';
                    }
                });
                
                // Update numbers based on filter
                if(filter === 'bases') {
                    cifraBases.textContent = '3';
                    cifraOps.textContent = '+3';
                }
                else if(filter === 'mmu') {
                    cifraBases.textContent = '2';
                    cifraOps.textContent = '+2';
                }
                else {
                    cifraBases.textContent = '3';
                    cifraOps.textContent = '+5';
                }
            });
        });
    }
"""

    with open(os.path.join(DIR, "script.js"), "a", encoding="utf-8") as f:
        f.write(js_additions)

    print("Map section fully upgraded with animations and interactivity.")

run()
