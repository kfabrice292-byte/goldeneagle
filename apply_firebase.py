import os
import re

DIR = r"c:\Users\HP ZBOOK\Downloads\Golden eagle\redesign"

# 1. Create firebase-config.js
firebase_config_js = """
// Configuration Firebase Partagée
export const firebaseConfig = {
  apiKey: "AIzaSyAL4boa5KiHah83CmwkHBQNiMGosUT3EKA",
  authDomain: "goldeneagle-ca0e5.firebaseapp.com",
  projectId: "goldeneagle-ca0e5",
  storageBucket: "goldeneagle-ca0e5.firebasestorage.app",
  messagingSenderId: "464530686942",
  appId: "1:464530686942:web:ddc1168f2104093d3ad34f",
  measurementId: "G-0L8SDX7K2J"
};
"""

with open(os.path.join(DIR, "firebase-config.js"), "w", encoding="utf-8") as f:
    f.write(firebase_config_js)


# 2. Update firebase-admin.js
admin_js = """import { initializeApp } from "https://www.gstatic.com/firebasejs/10.8.0/firebase-app.js";
import { getAuth, signInWithEmailAndPassword, onAuthStateChanged, signOut } from "https://www.gstatic.com/firebasejs/10.8.0/firebase-auth.js";
import { getFirestore, collection, getDocs, addDoc, doc, updateDoc, deleteDoc, getDoc, setDoc } from "https://www.gstatic.com/firebasejs/10.8.0/firebase-firestore.js";
import { firebaseConfig } from "./firebase-config.js";

const app = initializeApp(firebaseConfig);
const auth = getAuth(app);
const db = getFirestore(app);

// DOM Elements
const loginScreen = document.getElementById('login-screen');
const dashboardScreen = document.getElementById('dashboard-screen');
const loginForm = document.getElementById('login-form');
const loginError = document.getElementById('login-error');
const logoutBtn = document.getElementById('logout-btn');

// --- AUTHENTICATION ---
onAuthStateChanged(auth, (user) => {
    if (user) {
        // User is signed in
        loginScreen.style.display = 'none';
        dashboardScreen.style.display = 'block';
        loadNews();
        loadStats();
    } else {
        // User is signed out
        loginScreen.style.display = 'flex';
        dashboardScreen.style.display = 'none';
    }
});

loginForm.addEventListener('submit', (e) => {
    e.preventDefault();
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;
    
    signInWithEmailAndPassword(auth, email, password)
        .then(() => {
            loginError.style.display = 'none';
        })
        .catch((error) => {
            loginError.textContent = "Erreur de connexion : " + error.message;
            loginError.style.display = 'block';
        });
});

logoutBtn.addEventListener('click', () => {
    signOut(auth);
});

// --- FIRESTORE CRUD LOGIC (NEWS) ---
async function loadNews() {
    const tableBody = document.getElementById('news-table-body');
    tableBody.innerHTML = '<tr><td colspan="4" style="text-align: center;">Chargement...</td></tr>';
    
    try {
        const querySnapshot = await getDocs(collection(db, "news"));
        tableBody.innerHTML = ''; 
        
        if (querySnapshot.empty) {
            tableBody.innerHTML = '<tr><td colspan="4" style="text-align: center;">Aucune actualité trouvée.</td></tr>';
            return;
        }
        
        querySnapshot.forEach((doc) => {
            const data = doc.data();
            const tr = document.createElement('tr');
            tr.innerHTML = `
                <td><img src="${data.image || ''}" style="width: 50px; height: 50px; object-fit: cover; border-radius: 4px;" onerror="this.src='assets/formation.jpg'"></td>
                <td style="font-weight: bold;">${data.title}</td>
                <td><span style="background: #f1f5f9; padding: 5px 10px; border-radius: 20px; font-size: 0.8rem;">${data.category}</span></td>
                <td class="action-btns">
                    <button class="delete-btn" onclick="deleteNews('${doc.id}')"><i class="fas fa-trash"></i></button>
                </td>
            `;
            tableBody.appendChild(tr);
        });
    } catch (error) {
        console.error("Error loading news: ", error);
        tableBody.innerHTML = '<tr><td colspan="4" style="text-align: center; color: red;">Erreur lors du chargement des données. Assurez-vous que les règles Firestore autorisent la lecture.</td></tr>';
    }
}

document.getElementById('save-news-btn').addEventListener('click', async () => {
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
});

window.deleteNews = async function(id) {
    if(confirm("Êtes-vous sûr de vouloir supprimer cette actualité ?")) {
        try {
            await deleteDoc(doc(db, "news", id));
            loadNews();
        } catch (error) {
            console.error("Error deleting document: ", error);
            alert("Erreur lors de la suppression.");
        }
    }
};

// --- FIRESTORE CRUD LOGIC (STATS) ---
async function loadStats() {
    try {
        const docRef = doc(db, "settings", "globalStats");
        const docSnap = await getDoc(docRef);
        if (docSnap.exists()) {
            const data = docSnap.data();
            document.getElementById('stat-bases').value = data.bases || 3;
            document.getElementById('stat-pays').value = data.pays || 5;
            document.getElementById('stat-secu').value = data.secu || "100%";
        }
    } catch (e) {
        console.error("Error loading stats", e);
    }
}

document.getElementById('save-stats-btn').addEventListener('click', async () => {
    const bases = document.getElementById('stat-bases').value;
    const pays = document.getElementById('stat-pays').value;
    const secu = document.getElementById('stat-secu').value;
    
    try {
        await setDoc(doc(db, "settings", "globalStats"), {
            bases: bases,
            pays: pays,
            secu: secu
        });
        alert("Chiffres clés mis à jour avec succès sur le site !");
    } catch (e) {
        console.error("Error saving stats", e);
        alert("Erreur de sauvegarde: " + e.message);
    }
});
"""

with open(os.path.join(DIR, "firebase-admin.js"), "w", encoding="utf-8") as f:
    f.write(admin_js)


# 3. Create firebase-public.js for index.html
public_js = """import { initializeApp } from "https://www.gstatic.com/firebasejs/10.8.0/firebase-app.js";
import { getFirestore, collection, getDocs, doc, getDoc, query, orderBy, limit } from "https://www.gstatic.com/firebasejs/10.8.0/firebase-firestore.js";
import { firebaseConfig } from "./firebase-config.js";

const app = initializeApp(firebaseConfig);
const db = getFirestore(app);

// Fetch Global Stats
async function fetchGlobalStats() {
    try {
        const docRef = doc(db, "settings", "globalStats");
        const docSnap = await getDoc(docRef);
        
        if (docSnap.exists()) {
            const data = docSnap.data();
            // Store original values so script.js filter logic can use them
            window.originalBases = data.bases || "3";
            window.originalPays = data.pays || "5";
            
            document.getElementById('cifra-bases').textContent = data.bases || "3";
            document.getElementById('cifra-ops').textContent = "+" + (data.pays || "5");
            document.getElementById('cifra-secu').textContent = data.secu || "100%";
        }
    } catch(e) {
        console.error("Error fetching stats:", e);
    }
}

// Fetch News
async function fetchNews() {
    try {
        // Query the latest 3 news items
        const newsQuery = query(collection(db, "news"), orderBy("createdAt", "desc"), limit(3));
        const querySnapshot = await getDocs(newsQuery);
        const ul = document.getElementById('dynamic-news-list');
        
        if(!ul) return;
        
        if (querySnapshot.empty) {
            return; // Leave the hardcoded HTML as fallback if no data in DB yet
        }
        
        ul.innerHTML = ''; // Clear fallback HTML
        
        querySnapshot.forEach((doc) => {
            const data = doc.data();
            const li = document.createElement('li');
            li.innerHTML = `
                <a href="#">
                    <img src="${data.image || 'assets/formation.jpg'}" alt="${data.category}" onerror="this.src='assets/formation.jpg'">
                    <div class="text-cont">
                        <h3>${data.category}</h3>
                        <h4>${data.title}</h4>
                        <p>${data.excerpt}</p>
                    </div>
                </a>
            `;
            ul.appendChild(li);
        });
    } catch(e) {
        console.error("Error fetching news:", e);
        // We leave the fallback HTML visible if error
    }
}

// Load data when DOM is ready
document.addEventListener('DOMContentLoaded', () => {
    fetchGlobalStats();
    fetchNews();
});
"""

with open(os.path.join(DIR, "firebase-public.js"), "w", encoding="utf-8") as f:
    f.write(public_js)


# 4. Modify index.html and admin.html to add IDs and script modules
with open(os.path.join(DIR, "index.html"), "r", encoding="utf-8") as f:
    idx = f.read()

# Add ID to news list
idx = idx.replace('<ul class="lista-contenido">', '<ul class="lista-contenido" id="dynamic-news-list">')
# Add ID to secu stat
idx = idx.replace('<span class="cifra">100%</span>', '<span class="cifra" id="cifra-secu">100%</span>')
# Add public script tag before closing body
if 'firebase-public.js' not in idx:
    idx = idx.replace('</body>', '    <script type="module" src="firebase-public.js"></script>\n</body>')

with open(os.path.join(DIR, "index.html"), "w", encoding="utf-8") as f:
    f.write(idx)

# Modify admin.html to fix the save-stats-btn ID
with open(os.path.join(DIR, "admin.html"), "r", encoding="utf-8") as f:
    admin_html = f.read()
    
admin_html = admin_html.replace('<button class="btn btn-gold" style="width: 100%;">SAUVEGARDER LES CHIFFRES</button>', '<button id="save-stats-btn" class="btn btn-gold" style="width: 100%;">SAUVEGARDER LES CHIFFRES</button>')

with open(os.path.join(DIR, "admin.html"), "w", encoding="utf-8") as f:
    f.write(admin_html)

# 5. Modify script.js so the map filters don't hardcode "3" and "+5" anymore, but use window.originalBases
with open(os.path.join(DIR, "script.js"), "r", encoding="utf-8") as f:
    scriptjs = f.read()
    
new_filter_logic = """                // Update numbers based on filter
                const baseVal = window.originalBases || '3';
                const paysVal = window.originalPays || '5';
                
                if(filter === 'bases') {
                    cifraBases.textContent = baseVal;
                    cifraOps.textContent = '+' + Math.max(1, parseInt(paysVal)-2);
                }
                else if(filter === 'mmu') {
                    cifraBases.textContent = Math.max(1, parseInt(baseVal)-1);
                    cifraOps.textContent = '+' + Math.max(1, parseInt(paysVal)-3);
                }
                else {
                    cifraBases.textContent = baseVal;
                    cifraOps.textContent = '+' + paysVal;
                }"""
                
scriptjs = re.sub(r'// Update numbers based on filter.*?cifraOps\.textContent = \'\+5\';\s*\}', new_filter_logic, scriptjs, flags=re.DOTALL)

with open(os.path.join(DIR, "script.js"), "w", encoding="utf-8") as f:
    f.write(scriptjs)

print("Firebase integration applied to both Frontend and Admin.")
