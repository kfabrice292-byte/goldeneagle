import os
import re

DIR = r"c:\Users\HP ZBOOK\Downloads\Golden eagle\redesign"

# 1. Update firebase-config.js to include IMGBB key
config_path = os.path.join(DIR, "firebase-config.js")
with open(config_path, "r", encoding="utf-8") as f:
    config_content = f.read()

if "imgbbApiKey" not in config_content:
    config_content = config_content.replace(
        "measurementId: \"G-0L8SDX7K2J\"\n};", 
        "measurementId: \"G-0L8SDX7K2J\"\n};\n\n// TODO: Ajoutez votre clé API ImgBB ici (obtenez-la sur https://api.imgbb.com/)\nexport const imgbbApiKey = \"VOTRE_CLE_IMGBB\";"
    )
    with open(config_path, "w", encoding="utf-8") as f:
        f.write(config_content)


# 2. Update admin.html to add file input instead of text input for image
admin_path = os.path.join(DIR, "admin.html")
with open(admin_path, "r", encoding="utf-8") as f:
    admin_content = f.read()

old_input = """            <div class="form-group">
                <label>URL de l'image (Firebase Storage ou lien externe)</label>
                <input type="text" id="news-image" placeholder="https://...">
            </div>"""
            
new_input = """            <div class="form-group">
                <label>Image de l'actualité (Upload vers ImgBB)</label>
                <input type="file" id="news-image-file" accept="image/*">
                <small style="color: #666; display: block; margin-top: 5px;">Sélectionnez une image de votre ordinateur. Elle sera hébergée automatiquement.</small>
                <input type="hidden" id="news-image" value="">
            </div>"""

admin_content = admin_content.replace(old_input, new_input)
with open(admin_path, "w", encoding="utf-8") as f:
    f.write(admin_content)


# 3. Update firebase-admin.js to handle ImgBB upload
admin_js_path = os.path.join(DIR, "firebase-admin.js")
with open(admin_js_path, "r", encoding="utf-8") as f:
    admin_js = f.read()

# Add import for imgbbApiKey
if "imgbbApiKey" not in admin_js:
    admin_js = admin_js.replace(
        'import { firebaseConfig } from "./firebase-config.js";',
        'import { firebaseConfig, imgbbApiKey } from "./firebase-config.js";'
    )

# Replace the save-news-btn logic
old_save_logic = """document.getElementById('save-news-btn').addEventListener('click', async () => {
    const title = document.getElementById('news-title').value;
    const category = document.getElementById('news-category').value;
    const excerpt = document.getElementById('news-excerpt').value;
    let image = document.getElementById('news-image').value;
    if(!image) image = "assets/formation.jpg"; // default fallback
    
    if (!title) { alert("Le titre est obligatoire"); return; }
    
    try {
        await addDoc(collection(db, "news"), {
            title: title,
            category: category,
            excerpt: excerpt,
            image: image,
            createdAt: new Date().toISOString()
        });
        
        document.getElementById('news-modal').style.display = 'none';
        document.getElementById('news-title').value = '';
        document.getElementById('news-category').value = '';
        document.getElementById('news-excerpt').value = '';
        document.getElementById('news-image').value = '';
        
        loadNews(); 
    } catch (error) {
        console.error("Error adding document: ", error);
        alert("Erreur lors de l'enregistrement: " + error.message);
    }
});"""

new_save_logic = """document.getElementById('save-news-btn').addEventListener('click', async () => {
    const title = document.getElementById('news-title').value;
    const category = document.getElementById('news-category').value;
    const excerpt = document.getElementById('news-excerpt').value;
    const imageFileInput = document.getElementById('news-image-file');
    const saveBtn = document.getElementById('save-news-btn');
    
    if (!title) { alert("Le titre est obligatoire"); return; }
    
    let finalImageUrl = "assets/formation.jpg"; // default fallback
    saveBtn.textContent = "ENREGISTREMENT...";
    saveBtn.disabled = true;
    
    try {
        // Upload to ImgBB if a file is selected
        if (imageFileInput.files.length > 0) {
            if (imgbbApiKey === "VOTRE_CLE_IMGBB") {
                alert("Erreur : La clé API ImgBB n'est pas configurée dans firebase-config.js");
                saveBtn.textContent = "ENREGISTRER";
                saveBtn.disabled = false;
                return;
            }
            
            const file = imageFileInput.files[0];
            const formData = new FormData();
            formData.append('image', file);
            
            saveBtn.textContent = "UPLOAD IMGBB...";
            const imgbbResponse = await fetch('https://api.imgbb.com/1/upload?key=' + imgbbApiKey, {
                method: 'POST',
                body: formData
            });
            
            const imgbbData = await imgbbResponse.json();
            if (imgbbData.success) {
                finalImageUrl = imgbbData.data.url;
            } else {
                throw new Error("Échec de l'upload ImgBB : " + imgbbData.error.message);
            }
        }
        
        saveBtn.textContent = "SAUVEGARDE DB...";
        await addDoc(collection(db, "news"), {
            title: title,
            category: category,
            excerpt: excerpt,
            image: finalImageUrl,
            createdAt: new Date().toISOString()
        });
        
        document.getElementById('news-modal').style.display = 'none';
        document.getElementById('news-title').value = '';
        document.getElementById('news-category').value = '';
        document.getElementById('news-excerpt').value = '';
        imageFileInput.value = '';
        
        loadNews(); 
    } catch (error) {
        console.error("Error adding document: ", error);
        alert("Erreur: " + error.message);
    } finally {
        saveBtn.textContent = "ENREGISTRER";
        saveBtn.disabled = false;
    }
});"""

admin_js = admin_js.replace(old_save_logic, new_save_logic)

with open(admin_js_path, "w", encoding="utf-8") as f:
    f.write(admin_js)

print("ImgBB integration completed.")
