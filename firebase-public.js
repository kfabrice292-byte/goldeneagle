import { initializeApp } from "https://www.gstatic.com/firebasejs/10.8.0/firebase-app.js";
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
