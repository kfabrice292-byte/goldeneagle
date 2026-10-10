import { initializeApp } from "https://www.gstatic.com/firebasejs/10.8.0/firebase-app.js";
import { getAuth, signInWithEmailAndPassword, onAuthStateChanged, signOut } from "https://www.gstatic.com/firebasejs/10.8.0/firebase-auth.js";
import { getFirestore, collection, getDocs, addDoc, doc, updateDoc, deleteDoc, getDoc, setDoc } from "https://www.gstatic.com/firebasejs/10.8.0/firebase-firestore.js";
import { firebaseConfig, imgbbApiKey } from "./firebase-config.js";

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
