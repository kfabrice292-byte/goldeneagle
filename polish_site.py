import os
import re

DIR = r"c:\Users\HP ZBOOK\Downloads\Golden eagle\redesign"

HTML_FILES = ["index.html", "about.html", "services.html", "products.html", "contact.html"]

AOS_CSS = '    <link href="https://unpkg.com/aos@2.3.1/dist/aos.css" rel="stylesheet">\n</head>'
AOS_JS = """
    <!-- AOS Animation Library -->
    <script src="https://unpkg.com/aos@2.3.1/dist/aos.js"></script>
    <script>
        document.addEventListener('DOMContentLoaded', function() {
            if(typeof AOS !== 'undefined') {
                AOS.init({
                    duration: 800,
                    easing: 'ease-out-cubic',
                    once: true,
                    offset: 50
                });
            }
        });
    </script>
</body>"""

for filename in HTML_FILES:
    filepath = os.path.join(DIR, filename)
    if not os.path.exists(filepath):
        continue
        
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
        
    # Inject AOS CSS
    if "aos.css" not in content:
        content = content.replace("</head>", AOS_CSS)
        
    # Inject AOS JS
    if "aos.js" not in content:
        content = content.replace("</body>", AOS_JS)
        
    # Add data-aos tags to common elements if not already there
    # Hero text
    content = re.sub(r'<div class="hero-text">', '<div class="hero-text" data-aos="fade-up">', content)
    # Page intro
    content = re.sub(r'<section class="page-intro">', '<section class="page-intro" data-aos="fade-up">', content)
    # Cards
    content = re.sub(r'<div class="card">', '<div class="card" data-aos="fade-up" data-aos-delay="100">', content)
    # Destacados content
    content = re.sub(r'<div class="destacados-content([^"]*)">', r'<div class="destacados-content\1" data-aos="fade-left">', content)
    content = re.sub(r'<div class="destacados-img([^"]*)">', r'<div class="destacados-img\1" data-aos="fade-right">', content)
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)


# Rebuild contact.html to have a real contact form
contact_path = os.path.join(DIR, "contact.html")
if os.path.exists(contact_path):
    with open(contact_path, "r", encoding="utf-8") as f:
        contact_html = f.read()
        
    # Let's replace the contact grid section with a real form
    # We will use regex to find the premium-grid or the content area and inject a form
    contact_form_html = """
    <section style="max-width: 1200px; margin: 0 auto 80px; padding: 0 20px;">
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 50px;">
            <div data-aos="fade-right">
                <h3 style="font-family: 'Roboto Slab', serif; font-size: 2rem; color: var(--gray-dark); margin-bottom: 20px;">Parlons de votre projet</h3>
                <p style="color: var(--gray-text); line-height: 1.6; margin-bottom: 30px;">Nos équipes d'experts sont à votre disposition pour étudier vos besoins en dynamitage, forage et fourniture d'explosifs civils en Afrique de l'Ouest.</p>
                
                <div style="margin-bottom: 20px;">
                    <i class="fas fa-map-marker-alt" style="color: var(--gold); font-size: 1.5rem; width: 30px;"></i>
                    <span style="font-weight: 600; color: var(--gray-dark);">Siège Social :</span>
                    <p style="margin-left: 35px; color: var(--gray-text);">Ouagadougou, Burkina Faso</p>
                </div>
                
                <div style="margin-bottom: 20px;">
                    <i class="fas fa-envelope" style="color: var(--gold); font-size: 1.5rem; width: 30px;"></i>
                    <span style="font-weight: 600; color: var(--gray-dark);">Email :</span>
                    <p style="margin-left: 35px; color: var(--gray-text);">contact@goldeneagle.com</p>
                </div>
                
                <div style="margin-bottom: 20px;">
                    <i class="fas fa-phone" style="color: var(--gold); font-size: 1.5rem; width: 30px;"></i>
                    <span style="font-weight: 600; color: var(--gray-dark);">Téléphone :</span>
                    <p style="margin-left: 35px; color: var(--gray-text);">+226 00 00 00 00</p>
                </div>
            </div>
            
            <div data-aos="fade-left" style="background: #fff; padding: 40px; border-radius: 8px; box-shadow: 0 10px 30px rgba(0,0,0,0.08);">
                <form action="https://formspree.io/f/VOTRE_ID_FORMSPREE" method="POST">
                    <div style="margin-bottom: 20px;">
                        <label style="display: block; font-weight: 600; margin-bottom: 8px; color: var(--gray-dark);">Nom complet *</label>
                        <input type="text" name="name" required style="width: 100%; padding: 12px; border: 1px solid #e5e7eb; border-radius: 4px; font-family: 'Inter', sans-serif;">
                    </div>
                    
                    <div style="margin-bottom: 20px;">
                        <label style="display: block; font-weight: 600; margin-bottom: 8px; color: var(--gray-dark);">Email professionnel *</label>
                        <input type="email" name="email" required style="width: 100%; padding: 12px; border: 1px solid #e5e7eb; border-radius: 4px; font-family: 'Inter', sans-serif;">
                    </div>
                    
                    <div style="margin-bottom: 20px;">
                        <label style="display: block; font-weight: 600; margin-bottom: 8px; color: var(--gray-dark);">Sujet</label>
                        <select name="subject" style="width: 100%; padding: 12px; border: 1px solid #e5e7eb; border-radius: 4px; font-family: 'Inter', sans-serif; background: #fff;">
                            <option value="Demande de devis">Demande de devis</option>
                            <option value="Partenariat">Partenariat / Fourniture</option>
                            <option value="Recrutement">Recrutement</option>
                            <option value="Autre">Autre demande</option>
                        </select>
                    </div>
                    
                    <div style="margin-bottom: 30px;">
                        <label style="display: block; font-weight: 600; margin-bottom: 8px; color: var(--gray-dark);">Message *</label>
                        <textarea name="message" required rows="5" style="width: 100%; padding: 12px; border: 1px solid #e5e7eb; border-radius: 4px; font-family: 'Inter', sans-serif; resize: vertical;"></textarea>
                    </div>
                    
                    <button type="submit" class="btn btn-gold" style="width: 100%;">ENVOYER LE MESSAGE</button>
                    <p style="font-size: 0.8rem; color: #999; margin-top: 15px; text-align: center;">Nous vous répondrons sous 24h ouvrées.</p>
                </form>
            </div>
        </div>
    </section>
    """
    
    # Replace the existing grid in contact with the new form
    if '<div class="premium-grid">' in contact_html:
        contact_html = re.sub(r'<div class="premium-grid">.*?</div>\s*</section>', contact_form_html, contact_html, flags=re.DOTALL)
    elif '<section class="mapa-home"' in contact_html:
        # If I injected the mapa here by mistake earlier
        pass
    else:
        # Just append it before footer if we can't find a good replace target
        contact_html = contact_html.replace('</main>', contact_form_html + '\n</main>')
        
    with open(contact_path, "w", encoding="utf-8") as f:
        f.write(contact_html)

print("AOS Animations added to all pages and Contact form upgraded.")
