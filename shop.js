/**
 * Golden Eagle - Boutique Logic & Interaction Engine
 */

document.addEventListener('DOMContentLoaded', () => {
    // Current Filter State
    const state = {
        category: 'all',
        searchQuery: '',
        sortBy: 'default'
    };

    // DOM Elements
    const categoriesNav = document.getElementById('shop-categories-nav');
    const productsGrid = document.getElementById('shop-products-grid');
    const searchInput = document.getElementById('shop-search-input');
    const sortSelect = document.getElementById('shop-sort-select');
    const cartCountBadges = document.querySelectorAll('.cart-counter');
    const quoteDrawer = document.getElementById('quote-drawer');
    const quoteOverlay = document.getElementById('quote-drawer-overlay');
    const btnOpenQuote = document.getElementById('btn-open-quote');
    const btnCloseQuote = document.getElementById('btn-close-quote');
    const quoteItemsList = document.getElementById('quote-items-list');
    const productDetailModal = document.getElementById('product-detail-modal');
    const modalOverlay = document.getElementById('modal-overlay');
    const btnCloseModal = document.getElementById('btn-close-modal');
    const btnSendWhatsApp = document.getElementById('btn-send-whatsapp');
    const btnSendEmail = document.getElementById('btn-send-email');

    // Helper to resolve asset path whether in / or /en/
    function resolveAssetPath(path) {
        if (!path) return 'assets/golden-eagle-logo.png';
        if (path.startsWith('http://') || path.startsWith('https://') || path.startsWith('data:')) return path;
        const isEn = window.location.pathname.includes('/en/') || window.location.href.includes('/en/');
        if (isEn) {
            if (!path.startsWith('../')) return '../' + path;
        } else {
            if (path.startsWith('../')) return path.replace('../', '');
        }
        return path;
    }

    if (typeof ShopData !== 'undefined') {
        ShopData.init();
    } else {
        console.error('ShopData engine not loaded.');
        return;
    }

    // --- Render Categories Bar ---
    function renderCategories() {
        if (!categoriesNav) return;
        const categories = ShopData.getCategories();
        const allProducts = ShopData.getProducts();

        let html = `
            <button class="category-pill ${state.category === 'all' ? 'active' : ''}" data-cat="all">
                Tous les Équipements
                <span class="pill-count">${allProducts.length}</span>
            </button>
        `;

        categories.forEach(cat => {
            const count = allProducts.filter(p => p.categoryId === cat.id).length;
            const isActive = state.category === cat.id ? 'active' : '';
            html += `
                <button class="category-pill ${isActive}" data-cat="${cat.id}">
                    ${cat.name}
                    <span class="pill-count">${count}</span>
                </button>
            `;
        });

        categoriesNav.innerHTML = html;

        // Attach Click Listeners to category pills
        categoriesNav.querySelectorAll('.category-pill').forEach(btn => {
            btn.addEventListener('click', () => {
                const catId = btn.dataset.cat;
                state.category = catId;
                renderCategories();
                renderProducts();
            });
        });
    }

    // --- Render Products Grid ---
    function renderProducts() {
        if (!productsGrid) return;
        const products = ShopData.getProducts(state.category, state.searchQuery, state.sortBy);
        const categories = ShopData.getCategories();

        if (products.length === 0) {
            productsGrid.innerHTML = `
                <div class="shop-empty-state">
                    <h3>Aucun équipement trouvé</h3>
                    <p>Aucun produit ne correspond à votre recherche ou catégorie sélectionnée. Réinitialisez vos filtres ou contactez nos ingénieurs.</p>
                    <button class="btn btn-gold" id="btn-reset-filters">Réinitialiser les filtres</button>
                </div>
            `;
            const resetBtn = document.getElementById('btn-reset-filters');
            if (resetBtn) {
                resetBtn.addEventListener('click', () => {
                    state.category = 'all';
                    state.searchQuery = '';
                    if (searchInput) searchInput.value = '';
                    renderCategories();
                    renderProducts();
                });
            }
            return;
        }

        let html = '';
        products.forEach(p => {
            const cat = categories.find(c => c.id === p.categoryId);
            const catName = cat ? cat.name : 'Catalogue Minier';
            const statusClass = p.status === 'in-stock' ? 'status-in-stock' : 'status-on-demand';
            const statusLabel = p.status === 'in-stock' ? 'En Stock' : 'Sur Commande';

            let featuresHtml = '';
            if (p.features && p.features.length > 0) {
                featuresHtml = '<ul class="product-features">';
                p.features.slice(0, 3).forEach(f => {
                    featuresHtml += `<li><i class="fas fa-check"></i> <span>${f}</span></li>`;
                });
                featuresHtml += '</ul>';
            }

            html += `
                <div class="shop-card" data-id="${p.id}">
                    <div class="shop-card-media">
                        <img src="${resolveAssetPath(p.image)}" alt="${p.name}" loading="lazy" onerror="this.src='${resolveAssetPath('assets/golden-eagle-logo.png')}'">
                        ${p.badge ? `<div class="shop-card-badge">${p.badge}</div>` : ''}
                        <div class="shop-card-status ${statusClass}">${statusLabel}</div>
                    </div>
                    <div class="shop-card-body">
                        <div class="shop-card-meta">
                            <span class="shop-card-category">${catName}</span>
                            <span class="shop-card-ref">${p.ref || 'REF: GE'}</span>
                        </div>
                        <h3 class="shop-card-title">${p.name}</h3>
                        <p class="shop-card-desc">${p.shortDesc || ''}</p>
                        ${featuresHtml}
                        <div class="shop-card-footer">
                            <div class="shop-card-actions">
                                <button class="btn-card-details" data-action="details" data-id="${p.id}">
                                    Fiche technique
                                </button>
                                <button class="btn-card-quote" data-action="add-quote" data-id="${p.id}">
                                    Demander un devis
                                </button>
                            </div>
                        </div>
                    </div>
                </div>
            `;
        });

        productsGrid.innerHTML = html;

        // Attach action listeners
        productsGrid.querySelectorAll('[data-action="details"]').forEach(btn => {
            btn.addEventListener('click', (e) => {
                const id = btn.dataset.id;
                openProductModal(id);
            });
        });

        productsGrid.querySelectorAll('[data-action="add-quote"]').forEach(btn => {
            btn.addEventListener('click', (e) => {
                const id = btn.dataset.id;
                ShopData.addToCart(id, 1);
                updateCartUI();
                showToast('Article ajouté à votre demande de devis !');
            });
        });
    }

    // --- Product Detail Modal ---
    function openProductModal(productId) {
        const product = ShopData.getProductById(productId);
        if (!product || !productDetailModal) return;

        const categories = ShopData.getCategories();
        const cat = categories.find(c => c.id === product.categoryId);

        let specsHtml = '';
        if (product.specs && Object.keys(product.specs).length > 0) {
            specsHtml = '<table class="modal-specs-table">';
            for (const [key, value] of Object.entries(product.specs)) {
                specsHtml += `<tr><td>${key}</td><td>${value}</td></tr>`;
            }
            specsHtml += '</table>';
        }

        const modalBody = productDetailModal.querySelector('.modal-dialog');
        if (modalBody) {
            modalBody.innerHTML = `
                <button class="btn-modal-close" id="btn-modal-close-inner"><i class="fas fa-times"></i></button>
                <div class="modal-content-grid">
                    <div class="modal-product-img">
                        <img src="${resolveAssetPath(product.image)}" alt="${product.name}" onerror="this.src='${resolveAssetPath('assets/golden-eagle-logo.png')}'">
                    </div>
                    <div class="modal-product-details">
                        <div class="modal-meta">
                            ${product.badge ? `<span class="modal-badge">${product.badge}</span>` : ''}
                            <span class="modal-ref">${product.ref || 'GE-REF'}</span>
                            <span style="font-size:0.8rem; color:#166534; font-weight:600;">
                                ${product.status === 'in-stock' ? 'En Stock' : 'Sur Commande'}
                            </span>
                        </div>
                        <h2 class="modal-title">${product.name}</h2>
                        <p class="modal-desc">${product.description || product.shortDesc || ''}</p>
                        
                        ${specsHtml ? `
                            <h4 style="font-size: 0.95rem; margin-bottom: 0.5rem; text-transform:uppercase; color:var(--black); letter-spacing:0.5px;">
                                Caractéristiques Techniques
                            </h4>
                            ${specsHtml}
                        ` : ''}

                        <div class="modal-footer-actions">
                            <button class="btn btn-gold" id="btn-modal-add-quote" style="flex:1;">
                                Ajouter au Devis
                            </button>
                            <a href="https://wa.me/22678839090?text=${encodeURIComponent('Bonjour Golden Eagle, je souhaite des informations sur le produit : ' + product.name + ' (' + (product.ref || '') + ')')}" 
                               target="_blank" class="btn btn-black" style="background:#25D366; border-color:#25D366; color:#fff;">
                                <i class="fab fa-whatsapp"></i> Échanger sur WhatsApp
                            </a>
                        </div>
                    </div>
                </div>
            `;

            // Attach inner close button
            const closeInner = document.getElementById('btn-modal-close-inner');
            if (closeInner) {
                closeInner.addEventListener('click', closeModal);
            }

            const modalAddQuote = document.getElementById('btn-modal-add-quote');
            if (modalAddQuote) {
                modalAddQuote.addEventListener('click', () => {
                    ShopData.addToCart(product.id, 1);
                    updateCartUI();
                    showToast('Article ajouté à la cotation !');
                    closeModal();
                });
            }
        }

        if (productDetailModal) {
            productDetailModal.classList.add('active');
            document.body.style.overflow = 'hidden';
        }
    }

    function closeModal() {
        if (productDetailModal) {
            productDetailModal.classList.remove('active');
            document.body.style.overflow = '';
        }
    }

    if (btnCloseModal) {
        btnCloseModal.addEventListener('click', closeModal);
    }
    if (modalOverlay) {
        modalOverlay.addEventListener('click', (e) => {
            if (e.target === modalOverlay) closeModal();
        });
    }

    // --- Quotation Drawer & Cart ---
    function updateCartUI() {
        const count = ShopData.getCartCount();
        cartCountBadges.forEach(b => {
            b.textContent = count;
        });

        if (!quoteItemsList) return;
        const items = ShopData.getCartFullItems();

        if (items.length === 0) {
            quoteItemsList.innerHTML = `
                <div style="text-align: center; padding: 2.5rem 1rem; color: #94a3b8;">
                    <i class="fas fa-clipboard-list" style="font-size: 2.5rem; margin-bottom: 0.75rem; color: #cbd5e1;"></i>
                    <p style="font-weight: 500;">Votre sélection de cotation est vide</p>
                    <p style="font-size: 0.8rem;">Ajoutez des explosifs ou équipements depuis la boutique pour demander un devis groupé.</p>
                </div>
            `;
            if (btnSendWhatsApp) btnSendWhatsApp.disabled = true;
            if (btnSendEmail) btnSendEmail.disabled = true;
            return;
        }

        if (btnSendWhatsApp) btnSendWhatsApp.disabled = false;
        if (btnSendEmail) btnSendEmail.disabled = false;

        let html = '';
        items.forEach(item => {
            const prod = item.product;
            html += `
                <div class="quote-item-card" data-id="${item.productId}">
                    <img src="${resolveAssetPath(prod.image)}" class="quote-item-thumb" alt="${prod.name}" onerror="this.src='${resolveAssetPath('assets/golden-eagle-logo.png')}'">
                    <div class="quote-item-info">
                        <h4 class="quote-item-title">${prod.name}</h4>
                        <div class="quote-item-ref">${prod.ref || 'GE-REF'}</div>
                        <div class="quote-qty-control">
                            <button class="quote-qty-btn" data-action="dec" data-id="${item.productId}">-</button>
                            <span class="quote-qty-value">${item.quantity}</span>
                            <button class="quote-qty-btn" data-action="inc" data-id="${item.productId}">+</button>
                        </div>
                    </div>
                    <button class="btn-item-remove" data-action="remove" data-id="${item.productId}" title="Supprimer">
                        <i class="fas fa-trash-alt"></i>
                    </button>
                </div>
            `;
        });

        quoteItemsList.innerHTML = html;

        // Attach listeners to cart items
        quoteItemsList.querySelectorAll('[data-action="inc"]').forEach(btn => {
            btn.addEventListener('click', () => {
                const id = btn.dataset.id;
                const item = items.find(i => i.productId === id);
                if (item) {
                    ShopData.updateCartQuantity(id, item.quantity + 1);
                    updateCartUI();
                }
            });
        });

        quoteItemsList.querySelectorAll('[data-action="dec"]').forEach(btn => {
            btn.addEventListener('click', () => {
                const id = btn.dataset.id;
                const item = items.find(i => i.productId === id);
                if (item) {
                    ShopData.updateCartQuantity(id, item.quantity - 1);
                    updateCartUI();
                }
            });
        });

        quoteItemsList.querySelectorAll('[data-action="remove"]').forEach(btn => {
            btn.addEventListener('click', () => {
                const id = btn.dataset.id;
                ShopData.removeFromCart(id);
                updateCartUI();
                showToast('Article retiré de la cotation');
            });
        });
    }

    function openQuoteDrawer() {
        if (quoteDrawer && quoteOverlay) {
            updateCartUI();
            quoteDrawer.classList.add('active');
            quoteOverlay.classList.add('active');
            document.body.style.overflow = 'hidden';
        }
    }

    function closeQuoteDrawer() {
        if (quoteDrawer && quoteOverlay) {
            quoteDrawer.classList.remove('active');
            quoteOverlay.classList.remove('active');
            document.body.style.overflow = '';
        }
    }

    if (btnOpenQuote) btnOpenQuote.addEventListener('click', openQuoteDrawer);
    if (btnCloseQuote) btnCloseQuote.addEventListener('click', closeQuoteDrawer);
    if (quoteOverlay) quoteOverlay.addEventListener('click', closeQuoteDrawer);

    // --- Quotation Submission (WhatsApp & Email) ---
    function getQuotationPayload() {
        const name = (document.getElementById('quote-name') || {}).value || 'Client Professionnel';
        const company = (document.getElementById('quote-company') || {}).value || 'Non précisé';
        const phone = (document.getElementById('quote-phone') || {}).value || 'Non précisé';
        const location = (document.getElementById('quote-location') || {}).value || 'Non précisé';
        const notes = (document.getElementById('quote-notes') || {}).value || '';

        const items = ShopData.getCartFullItems();
        return { name, company, phone, location, notes, items };
    }

    if (btnSendWhatsApp) {
        btnSendWhatsApp.addEventListener('click', () => {
            const data = getQuotationPayload();
            if (data.items.length === 0) {
                alert('Veuillez ajouter au moins un produit à votre devis.');
                return;
            }

            let msg = `*DEMANDE DE DEVIS / COTATION - GOLDEN EAGLE*\n`;
            msg += `--------------------------------------\n`;
            msg += `👤 *Client :* ${data.name}\n`;
            msg += `🏢 *Entreprise / Mine :* ${data.company}\n`;
            msg += `📞 *Téléphone :* ${data.phone}\n`;
            msg += `📍 *Site / Localité :* ${data.location}\n`;
            if (data.notes) msg += `📝 *Notes :* ${data.notes}\n`;
            msg += `--------------------------------------\n`;
            msg += `*ARTICLES SÉLECTIONNÉS :*\n`;

            data.items.forEach((item, index) => {
                msg += `${index + 1}. *${item.product.name}* (${item.product.ref || 'Réf N/A'})\n`;
                msg += `   Quantité : ${item.quantity}\n`;
            });

            msg += `--------------------------------------\n`;
            msg += `Merci de nous transmettre votre meilleure offre de prix et délais de livraison.`;

            const waNumber = '22678839090';
            const url = `https://wa.me/${waNumber}?text=${encodeURIComponent(msg)}`;
            window.open(url, '_blank');
        });
    }

    if (btnSendEmail) {
        btnSendEmail.addEventListener('click', () => {
            const data = getQuotationPayload();
            if (data.items.length === 0) {
                alert('Veuillez ajouter au moins un produit à votre devis.');
                return;
            }

            const subject = `Demande de Devis Golden Eagle - ${data.company} (${data.name})`;
            let body = `Bonjour Direction Commerciale Golden Eagle,\n\n`;
            body += `Veuillez trouver ci-dessous notre demande de cotation détaillée :\n\n`;
            body += `Coordonnées du demandeur :\n`;
            body += `- Nom : ${data.name}\n`;
            body += `- Société / Mine : ${data.company}\n`;
            body += `- Contact Téléphonique : ${data.phone}\n`;
            body += `- Localisation / Chantier : ${data.location}\n\n`;
            body += `Équipements & Produits souhaités :\n`;

            data.items.forEach((item, idx) => {
                body += `${idx + 1}. ${item.product.name} [Ref: ${item.product.ref || 'N/A'}] - Quantité: ${item.quantity}\n`;
            });

            if (data.notes) {
                body += `\nPrécisions / Spécifications particulières :\n${data.notes}\n`;
            }

            body += `\nDans l'attente de votre proposition technique et financière,\nCordialement,\n${data.name}`;

            window.location.href = `mailto:info@goldeneaglebf.com?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(body)}`;
        });
    }

    // --- Search & Filter Events ---
    let searchDebounce = null;
    if (searchInput) {
        searchInput.addEventListener('input', (e) => {
            clearTimeout(searchDebounce);
            searchDebounce = setTimeout(() => {
                state.searchQuery = e.target.value;
                renderProducts();
            }, 250);
        });
    }

    if (sortSelect) {
        sortSelect.addEventListener('change', (e) => {
            state.sortBy = e.target.value;
            renderProducts();
        });
    }

    // Toast Helper
    function showToast(message) {
        let container = document.querySelector('.shop-toast-container');
        if (!container) {
            container = document.createElement('div');
            container.className = 'shop-toast-container';
            document.body.appendChild(container);
        }

        const toast = document.createElement('div');
        toast.className = 'shop-toast';
        toast.innerHTML = `<i class="fas fa-check-circle"></i> <span>${message}</span>`;
        container.appendChild(toast);

        setTimeout(() => {
            toast.style.opacity = '0';
            toast.style.transition = 'opacity 0.4s ease';
            setTimeout(() => toast.remove(), 400);
        }, 2800);
    }

    // React to storage events (e.g. edits from admin panel)
    window.addEventListener('shopDataChanged', () => {
        renderCategories();
        renderProducts();
        updateCartUI();
    });

    // Initial Execution
    renderCategories();
    renderProducts();
    updateCartUI();
});
