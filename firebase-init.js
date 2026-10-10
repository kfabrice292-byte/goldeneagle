/**
 * Golden Eagle - Firebase Configuration & Cloud Sync Module
 * Project: goldeneagle-ca0e5
 */

const firebaseConfig = {
  apiKey: "AIzaSyAL4boa5KiHah83CmwkHBQNiMGosUT3EKA",
  authDomain: "goldeneagle-ca0e5.firebaseapp.com",
  projectId: "goldeneagle-ca0e5",
  storageBucket: "goldeneagle-ca0e5.firebasestorage.app",
  messagingSenderId: "464530686942",
  appId: "1:464530686942:web:ddc1168f2104093d3ad34f",
  measurementId: "G-0L8SDX7K2J"
};

// Initialize Firebase
let firebaseApp = null;
let firestoreDb = null;

try {
    if (typeof firebase !== 'undefined') {
        if (!firebase.apps.length) {
            firebaseApp = firebase.initializeApp(firebaseConfig);
        } else {
            firebaseApp = firebase.app();
        }
        firestoreDb = firebase.firestore();
        console.log('Golden Eagle - Firebase Initialized successfully.');
    }
} catch (e) {
    console.warn('Firebase init notice:', e.message);
}

const FirebaseSync = {
    isAvailable() {
        return !!firestoreDb;
    },

    // --- Products ---
    async getProducts() {
        if (!this.isAvailable()) return null;
        try {
            const snapshot = await firestoreDb.collection('products').get();
            if (snapshot.empty) return null;
            const products = [];
            snapshot.forEach(doc => {
                products.push({ id: doc.id, ...doc.data() });
            });
            return products;
        } catch (e) {
            console.warn('Firebase getProducts fallback to local:', e.message);
            return null;
        }
    },

    async saveProduct(product) {
        if (!this.isAvailable()) return false;
        try {
            const prodRef = firestoreDb.collection('products').doc(product.id);
            await prodRef.set(product, { merge: true });
            return true;
        } catch (e) {
            console.warn('Firebase saveProduct error:', e.message);
            return false;
        }
    },

    async deleteProduct(productId) {
        if (!this.isAvailable()) return false;
        try {
            await firestoreDb.collection('products').doc(productId).delete();
            return true;
        } catch (e) {
            console.warn('Firebase deleteProduct error:', e.message);
            return false;
        }
    },

    // --- Categories ---
    async getCategories() {
        if (!this.isAvailable()) return null;
        try {
            const snapshot = await firestoreDb.collection('categories').get();
            if (snapshot.empty) return null;
            const categories = [];
            snapshot.forEach(doc => {
                categories.push({ id: doc.id, ...doc.data() });
            });
            return categories;
        } catch (e) {
            console.warn('Firebase getCategories fallback to local:', e.message);
            return null;
        }
    },

    async saveCategory(category) {
        if (!this.isAvailable()) return false;
        try {
            const catRef = firestoreDb.collection('categories').doc(category.id);
            await catRef.set(category, { merge: true });
            return true;
        } catch (e) {
            console.warn('Firebase saveCategory error:', e.message);
            return false;
        }
    },

    async deleteCategory(categoryId) {
        if (!this.isAvailable()) return false;
        try {
            await firestoreDb.collection('categories').doc(categoryId).delete();
            return true;
        } catch (e) {
            console.warn('Firebase deleteCategory error:', e.message);
            return false;
        }
    },

    // Seed defaults into Firebase if empty
    async seedDefaultsIfEmpty(defaultCategories, defaultProducts) {
        if (!this.isAvailable()) return;
        try {
            const catSnap = await firestoreDb.collection('categories').limit(1).get();
            if (catSnap.empty) {
                const batch = firestoreDb.batch();
                defaultCategories.forEach(cat => {
                    const ref = firestoreDb.collection('categories').doc(cat.id);
                    batch.set(ref, cat);
                });
                await batch.commit();
                console.log('Firebase: Default categories seeded.');
            }

            const prodSnap = await firestoreDb.collection('products').limit(1).get();
            if (prodSnap.empty) {
                const batch = firestoreDb.batch();
                defaultProducts.forEach(prod => {
                    const ref = firestoreDb.collection('products').doc(prod.id);
                    batch.set(ref, prod);
                });
                await batch.commit();
                console.log('Firebase: Default products seeded with ImgBB images.');
            }
        } catch (e) {
            console.warn('Firebase seed notice:', e.message);
        }
    },

    // --- Realtime Listeners ---
    listenToProducts(callback) {
        if (!this.isAvailable()) return null;
        try {
            return firestoreDb.collection('products').onSnapshot(snapshot => {
                const products = [];
                snapshot.forEach(doc => {
                    products.push({ id: doc.id, ...doc.data() });
                });
                if (products.length > 0 && typeof callback === 'function') {
                    callback(products);
                }
            }, err => {
                console.warn('Firestore products listener:', err.message);
            });
        } catch (e) {
            return null;
        }
    },

    listenToCategories(callback) {
        if (!this.isAvailable()) return null;
        try {
            return firestoreDb.collection('categories').onSnapshot(snapshot => {
                const categories = [];
                snapshot.forEach(doc => {
                    categories.push({ id: doc.id, ...doc.data() });
                });
                if (categories.length > 0 && typeof callback === 'function') {
                    callback(categories);
                }
            }, err => {
                console.warn('Firestore categories listener:', err.message);
            });
        } catch (e) {
            return null;
        }
    },

    // --- Connection Status Diagnostic ---
    async checkConnection() {
        if (!this.isAvailable()) return { status: 'offline', message: 'SDK Firebase non chargé' };
        try {
            await firestoreDb.collection('categories').limit(1).get();
            return { status: 'connected', message: 'Connecté au Cloud Firestore (goldeneagle-ca0e5)' };
        } catch (e) {
            const isPerm = e.code === 'permission-denied' || (e.message && e.message.toLowerCase().includes('permission'));
            if (isPerm) {
                return { 
                    status: 'rules-required', 
                    message: 'Permissions Firestore à débloquer dans la console Firebase (règles de lecture/écriture).' 
                };
            }
            return { status: 'error', message: e.message };
        }
    }
};

window.FirebaseSync = FirebaseSync;

