/**
 * Golden Eagle - Shop Data Management Module
 * Manages products, categories, persistence (localStorage), cart / quotation requests,
 * and import/export capabilities.
 */

const STORAGE_KEYS = {
    PRODUCTS: 'golden_eagle_products_v1',
    CATEGORIES: 'golden_eagle_categories_v1',
    CART: 'golden_eagle_cart_v1'
};

// Initial default categories
const DEFAULT_CATEGORIES = [
    {
        id: 'cat-explosifs',
        name: 'Explosifs Miniers',
        slug: 'explosifs',
        icon: 'fa-cubes',
        description: 'Produits explosifs à part entière et émulsions fabriqués selon les plus hauts standards de sécurité.'
    },
    {
        id: 'cat-amorcage',
        name: 'Amorçage & Détonation',
        slug: 'amorcage',
        icon: 'fa-bolt',
        description: 'Boosters haute puissance, détonateurs électroniques, électriques et cordeaux détonateurs.'
    },
    {
        id: 'cat-engins',
        name: 'Unités Mobiles (MMU) & Engins',
        slug: 'engins',
        icon: 'fa-truck',
        description: 'Camions de fabrication et de chargement d\'explosifs in situ (Mobile Manufacturing Units).'
    },
    {
        id: 'cat-topographie',
        name: 'Topographie, GPS & Drones',
        slug: 'topographie',
        icon: 'fa-map-marker-alt',
        description: 'Solutions topographiques haute précision, drones de surveillance et modélisation de front de taille.'
    },
    {
        id: 'cat-securite',
        name: 'Contrôle & Sécurité de Tir',
        slug: 'securite',
        icon: 'fa-shield-alt',
        description: 'Exploseurs électroniques cryptés, télécommandes de tir à distance et sismographes de contrôle.'
    }
];

// Initial default products
const DEFAULT_PRODUCTS = [
    {
        id: 'prod-nitrate',
        name: 'Nitrate d\'Ammonium Poreux',
        ref: 'GE-EXP-001',
        categoryId: 'cat-explosifs',
        badge: 'Explosif Majeur',
        status: 'in-stock', // in-stock, on-demand, express
        priceDisplay: 'Sur Devis (Tonnage)',
        image: 'https://i.ibb.co/TDT0jSrq/e4902d683602.jpg',
        shortDesc: 'Substance de base pour la fabrication d\'explosifs miniers (ANFO), assurant une puissance de tir et une fragmentation optimale.',
        description: 'Le nitrate d\'ammonium poreux de Golden Eagle est sélectionné auprès des meilleurs fabricants mondiaux pour garantir une capacité d\'absorption de carburant optimale et une vitesse de détonation maximale. Idéal pour les tirs de découverte et d\'abattage en mine à ciel ouvert ou carrières.',
        features: [
            'Haute pureté certifiée (> 99.2%)',
            'Porosité optimisée pour absorption fuel',
            'Rendement énergétique maximal',
            'Conformité stricte aux normes de sécurité internationales'
        ],
        specs: {
            'Pureté chimique': '≥ 99.2 %',
            'Taux d\'absorption de fioul': '≥ 6.0 %',
            'Densité apparente': '0.74 - 0.84 g/cm³',
            'Conditionnement': 'Big Bags 1 000 kg ou 1 250 kg',
            'Origine': 'Fournisseurs certifiés ISO 9001'
        }
    },
    {
        id: 'prod-boosters',
        name: 'Boosters & Magnum Boosters Pentolite',
        ref: 'GE-AMOR-002',
        categoryId: 'cat-amorcage',
        badge: 'Haute Puissance',
        status: 'in-stock',
        priceDisplay: 'Sur Devis au carton',
        image: 'https://i.ibb.co/LDtW6Frp/494758fb6e88.jpg',
        shortDesc: 'Charges d\'amorçage haute densité à base de Pentolite, assurant une détonation puissante et immédiate des colonnes d\'explosif.',
        description: 'Conçus spécifiquement pour l\'amorçage sûr et efficace des agents d\'abattage insensibles (ANFO et émulsions de vrac). Les boosters Golden Eagle résistent parfaitement aux pressions hydrostatiques et garantissent une amorce instantanée même dans les conditions de foration difficiles.',
        features: [
            'Vitesse de détonation > 7 500 m/s',
            'Pression de détonation ultra-élevée',
            'Excellente résistance à l\'eau et immersion',
            'Goulotte centrale adaptée pour cordeau et détonateur'
        ],
        specs: {
            'Composition': 'Pentolite (PETN / TNT)',
            'Vitesse de détonation': '7 500 m/s',
            'Grammages disponibles': '150g, 400g, 900g, 1200g',
            'Résistance à l\'eau': 'Excellente (plus de 7 jours sous 5 bars)',
            'Sécurité d\'initiation': 'Nécessite détonateur n°8 ou cordeau 10g'
        }
    },
    {
        id: 'prod-detonateurs',
        name: 'Détonateurs Électroniques & Cordeaux Détonants',
        ref: 'GE-AMOR-003',
        categoryId: 'cat-amorcage',
        badge: 'Précision Milliseconde',
        status: 'in-stock',
        priceDisplay: 'Sur Devis selon métrage',
        image: 'https://i.ibb.co/ks6xWq4b/81fdf63d28e8.jpg',
        shortDesc: 'Systèmes de mise à feu de pointe avec microprocesseur programmable pour synchroniser parfaitement les tirs et éliminer les vibrations.',
        description: 'Les détonateurs électroniques proposés par Golden Eagle offrent une programmation milliseconde ultra-précise (0 à 15 000 ms), permettant un contrôle absolu de la projection, de la fragmentation de la roche et la réduction drastique des nuisances sismiques autour des sites miniers.',
        features: [
            'Précision de temporisation ± 0.1 ms',
            'Test bidirectionnel avant tir sécurisé',
            'Cordeaux détonateurs 5g/m, 10g/m et 40g/m',
            'Protection totale contre les courants vagabonds'
        ],
        specs: {
            'Plage de délai': '0 à 15 000 ms (incrément 1 ms)',
            'Contrôle': 'Validation sur console de programmation',
            'Résistance à la traction du fil': '> 25 kg',
            'Température d\'utilisation': '-20°C à +65°C'
        }
    },
    {
        id: 'prod-mmu',
        name: 'Unité de Transformation Mobile (MMU Truck)',
        ref: 'GE-EQ-004',
        categoryId: 'cat-engins',
        badge: 'Ingénierie de Pointe',
        status: 'on-demand',
        priceDisplay: 'Location / Vente sur Devis',
        image: 'https://i.ibb.co/vxNpZhKG/d2e7f8504b45.jpg',
        shortDesc: 'Camions spécialisés tout-terrain pour le mélange, la sensibilisation et le pompage d\'émulsion et d\'ANFO directement sur le carreau de mine.',
        description: 'Nos camions MMU (Mobile Manufacturing Units) constituent le cœur technologique de l\'approvisionnement minier moderne. Équipés de compartiments multiples pour matrice d\'émulsion, nitrate, fioul et agents gélifiants, ils assurent un chargement mécanisé ultra-rapide des trous de mine avec un dosage contrôlé par ordinateur de bord.',
        features: [
            'Capacité de charge 10 à 20 tonnes de produit',
            'Pompage continu haute cadence (jusqu\'à 250 kg/min)',
            'Châssis renforcé 6x4 ou 6x6 pour pistes minières',
            'Système d\'arrêt d\'urgence et sécurité anti-incendie certifié'
        ],
        specs: {
            'Type d\'explosif produit': 'Émulsion lourde pompée & ANFO vrac',
            'Débit de refoulement': '50 à 250 kg/min',
            'Capacité cuve matrice': '12 000 litres',
            'Contrôle': 'Automate programmable avec écran tactile en cabine',
            'Certification': 'Norme ADR & Homologation minière'
        }
    },
    {
        id: 'prod-exploseurs',
        name: 'Exploseurs Électroniques & Télécommandes Sans Fil',
        ref: 'GE-SEC-005',
        categoryId: 'cat-securite',
        badge: 'Sécurité Cryptée',
        status: 'in-stock',
        priceDisplay: 'Sur Devis d\'Équipement',
        image: 'https://i.ibb.co/s9SFPwV7/08ebd13e3d47.jpg',
        shortDesc: 'Consoles de commande et déclencheurs de tir à distance longue portée cryptés avec clé de sécurité magnétique pour artificiers en chef.',
        description: 'Systèmes de déclenchement sécurisé de dernière génération assurant l\'amorçage des tirs à des distances sécuritaires supérieures à 2 km. Chaque séquence requiert une confirmation par clé de sécurité chiffrée, interdisant tout tir accidentel ou interférence électromagnétique.',
        features: [
            'Portée radio sécurisée jusqu\'à 3 000 mètres',
            'Chiffrement militaire des ordres de tir',
            'Autodiagnostic de ligne intégré avant autorisation',
            'Boîtier étanche et anti-chocs IP67'
        ],
        specs: {
            'Alimentation': 'Batterie Lithium longue durée rechargeable',
            'Tension de sortie': '450V à 1200V selon modèle',
            'Protocole sans fil': 'Fréquence industrielle sécurisée avec saut de fréquence',
            'Poids': '3.2 kg (valise renforcée)'
        }
    },
    {
        id: 'prod-drones-gps',
        name: 'Drones Topographiques & Stations GPS RTK',
        ref: 'GE-TOPO-006',
        categoryId: 'cat-topographie',
        badge: 'Topographie 3D',
        status: 'in-stock',
        priceDisplay: 'Sur Devis / Forfait',
        image: 'https://i.ibb.co/TBddRpxr/5fa61a390d95.jpg',
        shortDesc: 'Matériel de relevé géodésique haute définition pour la modélisation 3D des fronts de taille et le calcul précis des volumes d\'abattage.',
        description: 'La combinaison de nos drones de photogrammétrie aérienne et stations mobiles GPS différentiel (RTK) permet aux géomètres et ingénieurs de planifier les mailles de forage au centimètre près, d\'évaluer la charge d\'abattage et de générer des nuages de points 3D pour un bilan matière infaillible.',
        features: [
            'Précision géométrique centimétrique (< 1.5 cm)',
            'Modélisation automatique du nuage de points et MNT',
            'Calcul de volumétrie et surcharges avant / après tir',
            'Autonomie de vol de 45 minutes par batterie'
        ],
        specs: {
            'Capteur optique': 'Caméra 20 MP grand capteur 1"',
            'Positionnement': 'Double récepteur GNSS RTK multibande',
            'Formats d\'export': 'DXF, DWG, LAS, GeoTIFF, OBJ 3D',
            'Compatibilité logiciels': 'Surpac, Datamine, AutoCAD Mining'
        }
    },
    {
        id: 'prod-camion-citerne',
        name: 'Camion Citerne de Transport de Produits Chimiques',
        ref: 'GE-LOG-007',
        categoryId: 'cat-engins',
        badge: 'Logistique Sécurisée',
        status: 'on-demand',
        priceDisplay: 'Sur Devis d\'Exploitation',
        image: 'https://i.ibb.co/LD5sWwyj/95440e962cb2.jpg',
        shortDesc: 'Véhicules de convoi blindés et citernes calorifugées pour le transport certifié d\'émulsion chaude et de matières premières dangereuses.',
        description: 'Conçues selon les directives les plus strictes du transport des matières dangereuses de classe 1 et 5.1, ces citernes calorifugées en inox maintiennent la matrice d\'émulsion à sa température de formulation idéale durant les transits sur longues distances.',
        features: [
            'Citerne inox calorifugée double paroi',
            'Équipement complet de géo-repérage en temps réel',
            'Convoi sécurisé et extincteurs automatiques',
            'Autorisation et conformité ministérielle mines'
        ],
        specs: {
            'Capacité utile': '25 000 à 35 000 litres',
            'Matière de cuve': 'Acier inoxydable 316L',
            'Chauffage d\'appoint': 'Système autonome de maintien thermique',
            'Châssis': 'Scania / Mercedes 6x4 ou 8x4 renforcé piste'
        }
    },
    {
        id: 'prod-topographe',
        name: 'Mire & Scanner Laser 3D de Front de Taille',
        ref: 'GE-TOPO-008',
        categoryId: 'cat-topographie',
        badge: 'Contrôle Laser',
        status: 'in-stock',
        priceDisplay: 'Sur Devis Matériel',
        image: 'https://i.ibb.co/3mWkgvPm/fd6e99980748.jpg',
        shortDesc: 'Scanner laser terrestre pour mesurer la charge réelle en pied et éviter tout risque de projection ou de pied dur lors du tir.',
        description: 'Le scanner laser de profil de banquette permet de scanner la face libre du gradin en quelques secondes. Il identifie les zones de sous-charge (risque de projection de blocs) et de surcharge (risque de pied dur et de mauvaise fragmentation), garantissant une sécurité d\'implantation maximale.',
        features: [
            'Portée de mesure jusqu\'à 500 mètres sans réflecteur',
            'Acquisition de profil en moins de 3 minutes',
            'Détection automatique de la déviation des forages',
            'Logiciel de calcul de fardeau intégré'
        ],
        specs: {
            'Précision de portée': '± 5 mm',
            'Laser': 'Classe 1 sans danger oculaire',
            'Interface': 'Tablette durcie terrain Bluetooth / Wi-Fi',
            'Résistance': 'IP65 anti-poussière et projections d\'eau'
        }
    }
];

// Shop Database Controller
const ShopData = {
    // --- Initializer ---
    init() {
        if (!localStorage.getItem(STORAGE_KEYS.CATEGORIES)) {
            localStorage.setItem(STORAGE_KEYS.CATEGORIES, JSON.stringify(DEFAULT_CATEGORIES));
        }
        if (!localStorage.getItem(STORAGE_KEYS.PRODUCTS)) {
            localStorage.setItem(STORAGE_KEYS.PRODUCTS, JSON.stringify(DEFAULT_PRODUCTS));
        }
        if (!localStorage.getItem(STORAGE_KEYS.CART)) {
            localStorage.setItem(STORAGE_KEYS.CART, JSON.stringify([]));
        }

        // Asynchronous Cloud Sync with Firebase
        if (typeof FirebaseSync !== 'undefined' && FirebaseSync.isAvailable()) {
            this.syncWithFirebase();
        }
    },

    async syncWithFirebase() {
        if (!this._isSyncing) {
            this._isSyncing = true;
            try {
                // Seed if brand new
                await FirebaseSync.seedDefaultsIfEmpty(DEFAULT_CATEGORIES, DEFAULT_PRODUCTS);

                // Fetch cloud categories
                const cloudCats = await FirebaseSync.getCategories();
                if (cloudCats && cloudCats.length > 0) {
                    localStorage.setItem(STORAGE_KEYS.CATEGORIES, JSON.stringify(cloudCats));
                }

                // Fetch cloud products
                const cloudProds = await FirebaseSync.getProducts();
                if (cloudProds && cloudProds.length > 0) {
                    localStorage.setItem(STORAGE_KEYS.PRODUCTS, JSON.stringify(cloudProds));
                }

                this.notifyChange('cloud-sync');
            } catch (err) {
                console.warn('Firebase sync notice:', err);
            } finally {
                this._isSyncing = false;
            }
        }
    },

    // --- Categories CRUD ---
    getCategories() {
        this.init();
        try {
            return JSON.parse(localStorage.getItem(STORAGE_KEYS.CATEGORIES)) || DEFAULT_CATEGORIES;
        } catch (e) {
            console.error('Error reading categories from localStorage:', e);
            return DEFAULT_CATEGORIES;
        }
    },

    getCategoryById(id) {
        const categories = this.getCategories();
        return categories.find(c => c.id === id) || null;
    },

    saveCategories(categories) {
        localStorage.setItem(STORAGE_KEYS.CATEGORIES, JSON.stringify(categories));
        this.notifyChange('categories');
    },

    addCategory(cat) {
        const categories = this.getCategories();
        const newCat = {
            id: 'cat-' + Date.now(),
            name: cat.name.trim(),
            slug: (cat.slug || cat.name).toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/(^-|-$)/g, ''),
            icon: cat.icon || 'fa-folder',
            description: cat.description || ''
        };
        categories.push(newCat);
        this.saveCategories(categories);
        if (typeof FirebaseSync !== 'undefined') {
            FirebaseSync.saveCategory(newCat);
        }
        return newCat;
    },

    updateCategory(id, updatedData) {
        let categories = this.getCategories();
        const index = categories.findIndex(c => c.id === id);
        if (index !== -1) {
            categories[index] = {
                ...categories[index],
                ...updatedData,
                slug: (updatedData.slug || updatedData.name || categories[index].name).toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/(^-|-$)/g, '')
            };
            this.saveCategories(categories);
            if (typeof FirebaseSync !== 'undefined') {
                FirebaseSync.saveCategory(categories[index]);
            }
            return categories[index];
        }
        return null;
    },

    deleteCategory(id) {
        let categories = this.getCategories();
        // Remove category
        categories = categories.filter(c => c.id !== id);
        this.saveCategories(categories);
        if (typeof FirebaseSync !== 'undefined') {
            FirebaseSync.deleteCategory(id);
        }

        // Update products belonging to this category to 'sans-categorie'
        let products = this.getProducts();
        products = products.map(p => {
            if (p.categoryId === id) {
                return { ...p, categoryId: '' };
            }
            return p;
        });
        this.saveProducts(products);
        return true;
    },

    // --- Products CRUD ---
    getProducts(filterCategoryId = 'all', searchQuery = '', sortBy = 'default') {
        this.init();
        let products = [];
        try {
            products = JSON.parse(localStorage.getItem(STORAGE_KEYS.PRODUCTS)) || DEFAULT_PRODUCTS;
        } catch (e) {
            console.error('Error reading products from localStorage:', e);
            products = DEFAULT_PRODUCTS;
        }

        // Filter by category
        if (filterCategoryId && filterCategoryId !== 'all') {
            products = products.filter(p => p.categoryId === filterCategoryId);
        }

        // Filter by search query
        if (searchQuery && searchQuery.trim() !== '') {
            const query = searchQuery.trim().toLowerCase();
            products = products.filter(p => {
                const nameMatch = p.name && p.name.toLowerCase().includes(query);
                const descMatch = p.shortDesc && p.shortDesc.toLowerCase().includes(query);
                const refMatch = p.ref && p.ref.toLowerCase().includes(query);
                const badgeMatch = p.badge && p.badge.toLowerCase().includes(query);
                return nameMatch || descMatch || refMatch || badgeMatch;
            });
        }

        // Sorting
        if (sortBy === 'name-asc') {
            products.sort((a, b) => a.name.localeCompare(b.name));
        } else if (sortBy === 'name-desc') {
            products.sort((a, b) => b.name.localeCompare(a.name));
        } else if (sortBy === 'newest') {
            products.reverse();
        }

        return products;
    },

    getProductById(id) {
        const products = this.getProducts();
        return products.find(p => p.id === id) || null;
    },

    saveProducts(products) {
        localStorage.setItem(STORAGE_KEYS.PRODUCTS, JSON.stringify(products));
        this.notifyChange('products');
    },

    addProduct(prod) {
        const products = this.getProducts();
        const newProduct = {
            id: 'prod-' + Date.now(),
            name: prod.name.trim(),
            ref: prod.ref ? prod.ref.trim() : 'GE-' + Math.floor(1000 + Math.random() * 9000),
            categoryId: prod.categoryId || '',
            badge: prod.badge ? prod.badge.trim() : 'Équipement',
            status: prod.status || 'in-stock',
            priceDisplay: prod.priceDisplay ? prod.priceDisplay.trim() : 'Sur Devis',
            image: prod.image || 'https://i.ibb.co/TDT0jSrq/e4902d683602.jpg',
            shortDesc: prod.shortDesc ? prod.shortDesc.trim() : '',
            description: prod.description ? prod.description.trim() : '',
            features: Array.isArray(prod.features) ? prod.features : (prod.features ? prod.features.split('\n').filter(f => f.trim()) : []),
            specs: prod.specs || {}
        };
        products.unshift(newProduct); // Add to beginning
        this.saveProducts(products);
        if (typeof FirebaseSync !== 'undefined') {
            FirebaseSync.saveProduct(newProduct);
        }
        return newProduct;
    },

    updateProduct(id, updatedData) {
        let products = this.getProducts();
        const index = products.findIndex(p => p.id === id);
        if (index !== -1) {
            products[index] = {
                ...products[index],
                ...updatedData,
                features: Array.isArray(updatedData.features) ? updatedData.features : (updatedData.features ? updatedData.features.split('\n').filter(f => f.trim()) : products[index].features)
            };
            this.saveProducts(products);
            if (typeof FirebaseSync !== 'undefined') {
                FirebaseSync.saveProduct(products[index]);
            }
            return products[index];
        }
        return null;
    },

    deleteProduct(id) {
        let products = this.getProducts();
        products = products.filter(p => p.id !== id);
        this.saveProducts(products);
        if (typeof FirebaseSync !== 'undefined') {
            FirebaseSync.deleteProduct(id);
        }
        
        // Also remove from cart if present
        this.removeFromCart(id);
        return true;
    },

    duplicateProduct(id) {
        const original = this.getProductById(id);
        if (!original) return null;
        
        const copy = {
            ...JSON.parse(JSON.stringify(original)),
            id: 'prod-' + Date.now(),
            name: original.name + ' (Copie)',
            ref: original.ref + '-CPY'
        };
        
        const products = this.getProducts();
        products.unshift(copy);
        this.saveProducts(products);
        return copy;
    },

    // --- Quotation Cart ---
    getCart() {
        this.init();
        try {
            return JSON.parse(localStorage.getItem(STORAGE_KEYS.CART)) || [];
        } catch (e) {
            return [];
        }
    },

    saveCart(cart) {
        localStorage.setItem(STORAGE_KEYS.CART, JSON.stringify(cart));
        this.notifyChange('cart');
    },

    addToCart(productId, quantity = 1, notes = '') {
        const product = this.getProductById(productId);
        if (!product) return null;

        let cart = this.getCart();
        const existingIndex = cart.findIndex(item => item.productId === productId);

        if (existingIndex !== -1) {
            cart[existingIndex].quantity += quantity;
            if (notes) cart[existingIndex].notes = notes;
        } else {
            cart.push({
                productId,
                quantity: Math.max(1, quantity),
                notes: notes,
                addedAt: new Date().toISOString()
            });
        }

        this.saveCart(cart);
        return cart;
    },

    updateCartQuantity(productId, quantity) {
        let cart = this.getCart();
        if (quantity <= 0) {
            cart = cart.filter(item => item.productId !== productId);
        } else {
            const index = cart.findIndex(item => item.productId === productId);
            if (index !== -1) {
                cart[index].quantity = quantity;
            }
        }
        this.saveCart(cart);
        return cart;
    },

    removeFromCart(productId) {
        let cart = this.getCart();
        cart = cart.filter(item => item.productId !== productId);
        this.saveCart(cart);
        return cart;
    },

    clearCart() {
        this.saveCart([]);
    },

    getCartCount() {
        const cart = this.getCart();
        return cart.reduce((total, item) => total + item.quantity, 0);
    },

    getCartFullItems() {
        const cart = this.getCart();
        return cart.map(item => {
            const product = this.getProductById(item.productId);
            return {
                ...item,
                product: product || {
                    id: item.productId,
                    name: 'Produit archivé',
                    ref: 'N/A',
                    image: 'assets/golden-eagle-logo.png',
                    priceDisplay: 'Sur Devis'
                }
            };
        });
    },

    // --- Reset & Sync ---
    resetToDefaults() {
        localStorage.setItem(STORAGE_KEYS.CATEGORIES, JSON.stringify(DEFAULT_CATEGORIES));
        localStorage.setItem(STORAGE_KEYS.PRODUCTS, JSON.stringify(DEFAULT_PRODUCTS));
        localStorage.setItem(STORAGE_KEYS.CART, JSON.stringify([]));
        this.notifyChange('reset');
        return true;
    },

    exportData() {
        return {
            exportDate: new Date().toISOString(),
            version: '1.0',
            categories: this.getCategories(),
            products: this.getProducts()
        };
    },

    importData(jsonData) {
        try {
            const data = typeof jsonData === 'string' ? JSON.parse(jsonData) : jsonData;
            if (data.categories && Array.isArray(data.categories)) {
                this.saveCategories(data.categories);
            }
            if (data.products && Array.isArray(data.products)) {
                this.saveProducts(data.products);
            }
            this.notifyChange('import');
            return { success: true, message: 'Données importées avec succès !' };
        } catch (e) {
            return { success: false, message: 'Format JSON invalide : ' + e.message };
        }
    },

    // --- Event Notification ---
    notifyChange(type) {
        window.dispatchEvent(new CustomEvent('shopDataChanged', { detail: { type } }));
    }
};

// Export to window
window.ShopData = ShopData;
