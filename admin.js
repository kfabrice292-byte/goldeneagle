/**
 * Golden Eagle - Admin Panel Logic & Operations
 */

document.addEventListener('DOMContentLoaded', () => {
    // Check ShopData
    if (typeof ShopData === 'undefined') {
        alert('Erreur: Le module ShopData n\'est pas chargé.');
        return;
    }

    // State
    const state = {
        currentTab: 'products',
        productSearch: '',
        productFilterCat: 'all',
        editingProductId: null,
        editingCategoryId: null,
        selectedImage: 'https://i.ibb.co/TDT0jSrq/e4902d683602.jpg'
    };

    // ImgBB API Key
    const IMGBB_API_KEY = '297115489f1f9b1f1d2536f5c157a5e9';

    // Direct Upload to ImgBB API
    async function uploadToImgBB(fileOrBase64) {
        const formData = new FormData();
        if (typeof fileOrBase64 === 'string') {
            const b64 = fileOrBase64.replace(/^data:image\/[a-z]+;base64,/, '');
            formData.append('image', b64);
        } else {
            formData.append('image', fileOrBase64);
        }

        const response = await fetch(`https://api.imgbb.com/1/upload?key=${IMGBB_API_KEY}`, {
            method: 'POST',
            body: formData
        });

        const data = await response.json();
        if (data && data.success && data.data && data.data.url) {
            return data.data.url;
        } else {
            const msg = data && data.error ? data.error.message : 'Erreur téléversement ImgBB';
            throw new Error(msg);
        }
    }

    // Official Golden Eagle hosted ImgBB Assets
    const PRESET_ASSETS = [
        'https://i.ibb.co/TDT0jSrq/e4902d683602.jpg',
        'https://i.ibb.co/LDtW6Frp/494758fb6e88.jpg',
        'https://i.ibb.co/ks6xWq4b/81fdf63d28e8.jpg',
        'https://i.ibb.co/vxNpZhKG/d2e7f8504b45.jpg',
        'https://i.ibb.co/s9SFPwV7/08ebd13e3d47.jpg',
        'https://i.ibb.co/TBddRpxr/5fa61a390d95.jpg',
        'https://i.ibb.co/LD5sWwyj/95440e962cb2.jpg',
        'https://i.ibb.co/3mWkgvPm/fd6e99980748.jpg'
    ];

    // DOM Elements
    const statTotalProducts = document.getElementById('stat-total-products');
    const statTotalCategories = document.getElementById('stat-total-categories');
    const statInStock = document.getElementById('stat-in-stock');
    const statOnDemand = document.getElementById('stat-on-demand');

    const productsTableBody = document.getElementById('admin-products-table-body');
    const categoriesGrid = document.getElementById('admin-categories-grid');
    const adminProductSearch = document.getElementById('admin-product-search');
    const adminCategoryFilter = document.getElementById('admin-category-filter');

    // Modals
    const productModal = document.getElementById('admin-product-modal');
    const categoryModal = document.getElementById('admin-category-modal');
    const productForm = document.getElementById('admin-product-form');
    const categoryForm = document.getElementById('admin-category-form');

    // --- Tab Switching ---
    const tabButtons = document.querySelectorAll('.admin-tab-btn');
    const tabPanels = document.querySelectorAll('.admin-panel');

    tabButtons.forEach(btn => {
        btn.addEventListener('click', () => {
            const targetTab = btn.dataset.tab;
            state.currentTab = targetTab;

            tabButtons.forEach(b => b.classList.remove('active'));
            tabPanels.forEach(p => p.classList.remove('active'));

            btn.classList.add('active');
            const activePanel = document.getElementById(`panel-${targetTab}`);
            if (activePanel) activePanel.classList.add('active');
        });
    });

    // --- Render Stats ---
    function renderStats() {
        const products = ShopData.getProducts();
        const categories = ShopData.getCategories();

        const inStockCount = products.filter(p => p.status === 'in-stock').length;
        const onDemandCount = products.filter(p => p.status === 'on-demand').length;

        if (statTotalProducts) statTotalProducts.textContent = products.length;
        if (statTotalCategories) statTotalCategories.textContent = categories.length;
        if (statInStock) statInStock.textContent = inStockCount;
        if (statOnDemand) statOnDemand.textContent = onDemandCount;
    }

    // --- Populate Category Dropdowns ---
    function populateCategoryDropdowns() {
        const categories = ShopData.getCategories();
        
        // Filter in Action Bar
        if (adminCategoryFilter) {
            let filterHtml = '<option value="all">Toutes les catégories</option>';
            categories.forEach(c => {
                filterHtml += `<option value="${c.id}" ${state.productFilterCat === c.id ? 'selected' : ''}>${c.name}</option>`;
            });
            adminCategoryFilter.innerHTML = filterHtml;
        }

        // Product Form Dropdown
        const formCatSelect = document.getElementById('prod-form-category');
        if (formCatSelect) {
            let formCatHtml = '<option value="">Sélectionnez une catégorie...</option>';
            categories.forEach(c => {
                formCatHtml += `<option value="${c.id}">${c.name}</option>`;
            });
            formCatSelect.innerHTML = formCatHtml;
        }
    }

    // --- Render Products Table ---
    function renderProductsTable() {
        if (!productsTableBody) return;
        const products = ShopData.getProducts(state.productFilterCat, state.productSearch);
        const categories = ShopData.getCategories();

        if (products.length === 0) {
            productsTableBody.innerHTML = `
                <tr>
                    <td colspan="6" style="text-align: center; padding: 3rem 1rem; color: #8e96a4;">
                        <i class="fas fa-box-open" style="font-size: 2rem; margin-bottom: 0.5rem; display:block; color: #3f4450;"></i>
                        Aucun produit trouvé avec les critères actuels.
                    </td>
                </tr>
            `;
            return;
        }

        let html = '';
        products.forEach(p => {
            const cat = categories.find(c => c.id === p.categoryId);
            const catName = cat ? cat.name : '<span style="color:#ef4444;">Non classé</span>';
            const statusLabel = p.status === 'in-stock' ? 'En Stock' : 'Sur Commande';
            const statusClass = p.status === 'in-stock' ? 'in-stock' : 'on-demand';

            html += `
                <tr data-id="${p.id}">
                    <td>
                        <div class="product-row-info">
                            <img src="${p.image || 'assets/citerne.jpg'}" alt="${p.name}" class="product-thumb" onerror="this.src='assets/golden-eagle-logo.png'">
                            <div class="product-title-group">
                                <h4>${p.name}</h4>
                                <span class="prod-ref">${p.ref || 'GE-REF'}</span>
                            </div>
                        </div>
                    </td>
                    <td>${catName}</td>
                    <td>
                        ${p.badge ? `<span class="badge-tag">${p.badge}</span>` : '<span style="color:#64748b;">—</span>'}
                    </td>
                    <td>
                        <span class="status-pill ${statusClass}">
                            <i class="fas fa-circle" style="font-size: 6px;"></i> ${statusLabel}
                        </span>
                    </td>
                    <td style="font-weight: 600; color: #ffffff;">${p.priceDisplay || 'Sur Devis'}</td>
                    <td>
                        <div class="admin-row-actions">
                            <button class="btn-action-icon" data-action="edit" data-id="${p.id}" title="Modifier">
                                <i class="fas fa-pen"></i>
                            </button>
                            <button class="btn-action-icon" data-action="duplicate" data-id="${p.id}" title="Dupliquer">
                                <i class="fas fa-copy"></i>
                            </button>
                            <button class="btn-action-icon delete" data-action="delete" data-id="${p.id}" title="Supprimer">
                                <i class="fas fa-trash-alt"></i>
                            </button>
                        </div>
                    </td>
                </tr>
            `;
        });

        productsTableBody.innerHTML = html;

        // Attach listeners
        productsTableBody.querySelectorAll('[data-action="edit"]').forEach(btn => {
            btn.addEventListener('click', () => openEditProductModal(btn.dataset.id));
        });

        productsTableBody.querySelectorAll('[data-action="duplicate"]').forEach(btn => {
            btn.addEventListener('click', () => {
                const prod = ShopData.duplicateProduct(btn.dataset.id);
                if (prod) {
                    showAdminToast(`Produit "${prod.name}" dupliqué avec succès.`);
                    refreshAll();
                }
            });
        });

        productsTableBody.querySelectorAll('[data-action="delete"]').forEach(btn => {
            btn.addEventListener('click', () => {
                const id = btn.dataset.id;
                const prod = ShopData.getProductById(id);
                if (confirm(`Êtes-vous sûr de vouloir supprimer définitivement le produit "${prod ? prod.name : id}" ?`)) {
                    ShopData.deleteProduct(id);
                    showAdminToast('Produit supprimé du catalogue.');
                    refreshAll();
                }
            });
        });
    }

    // --- Render Categories Grid ---
    function renderCategoriesGrid() {
        if (!categoriesGrid) return;
        const categories = ShopData.getCategories();
        const products = ShopData.getProducts();

        let html = '';
        categories.forEach(c => {
            const count = products.filter(p => p.categoryId === c.id).length;
            html += `
                <div class="admin-cat-card" data-id="${c.id}">
                    <div class="admin-cat-header">
                        <div class="admin-cat-icon">
                            <i class="fas ${c.icon || 'fa-tag'}"></i>
                        </div>
                        <div class="admin-row-actions">
                            <button class="btn-action-icon" data-action="edit-cat" data-id="${c.id}" title="Modifier">
                                <i class="fas fa-pen"></i>
                            </button>
                            <button class="btn-action-icon delete" data-action="delete-cat" data-id="${c.id}" title="Supprimer">
                                <i class="fas fa-trash-alt"></i>
                            </button>
                        </div>
                    </div>
                    <h3 class="admin-cat-title">${c.name}</h3>
                    <p class="admin-cat-desc">${c.description || 'Aucune description spécifiée.'}</p>
                    <div class="admin-cat-footer">
                        <span class="admin-cat-count"><i class="fas fa-boxes"></i> ${count} produit${count > 1 ? 's' : ''}</span>
                        <span style="font-family: monospace; font-size: 0.75rem; color: #64748b;">${c.slug || ''}</span>
                    </div>
                </div>
            `;
        });

        categoriesGrid.innerHTML = html;

        // Attach category listeners
        categoriesGrid.querySelectorAll('[data-action="edit-cat"]').forEach(btn => {
            btn.addEventListener('click', () => openEditCategoryModal(btn.dataset.id));
        });

        categoriesGrid.querySelectorAll('[data-action="delete-cat"]').forEach(btn => {
            btn.addEventListener('click', () => {
                const id = btn.dataset.id;
                const cat = ShopData.getCategoryById(id);
                if (confirm(`Supprimer la catégorie "${cat ? cat.name : id}" ? Les produits associés seront conservés sans catégorie.`)) {
                    ShopData.deleteCategory(id);
                    showAdminToast('Catégorie supprimée.');
                    refreshAll();
                }
            });
        });
    }

    // --- Image Selector Initialization ---
    function initImageSelector(currentImg) {
        state.selectedImage = currentImg || PRESET_ASSETS[0];
        const preview = document.getElementById('prod-img-preview');
        const imgInput = document.getElementById('prod-form-image');
        const presetsContainer = document.getElementById('preset-images-container');
        const fileUpload = document.getElementById('prod-file-upload');

        if (preview) preview.src = state.selectedImage;
        if (imgInput) imgInput.value = state.selectedImage;

        // Presets
        if (presetsContainer) {
            let phtml = '';
            PRESET_ASSETS.forEach(asset => {
                const isActive = asset === state.selectedImage ? 'active' : '';
                phtml += `<img src="${asset}" class="preset-thumb ${isActive}" data-src="${asset}" alt="preset">`;
            });
            presetsContainer.innerHTML = phtml;

            presetsContainer.querySelectorAll('.preset-thumb').forEach(thumb => {
                thumb.addEventListener('click', () => {
                    presetsContainer.querySelectorAll('.preset-thumb').forEach(t => t.classList.remove('active'));
                    thumb.classList.add('active');
                    state.selectedImage = thumb.dataset.src;
                    if (preview) preview.src = state.selectedImage;
                    if (imgInput) imgInput.value = state.selectedImage;
                });
            });
        }

        // Direct File Upload with automatic ImgBB API transmission
        if (fileUpload) {
            fileUpload.addEventListener('change', async (e) => {
                const file = e.target.files[0];
                if (!file) return;

                const statusEl = document.getElementById('imgbb-upload-status');
                if (statusEl) {
                    statusEl.textContent = 'Téléversement ImgBB en cours...';
                    statusEl.style.color = '#cc9933';
                }

                // Temporary local preview while uploading
                const localUrl = URL.createObjectURL(file);
                if (preview) preview.src = localUrl;

                try {
                    const imgbbUrl = await uploadToImgBB(file);
                    state.selectedImage = imgbbUrl;
                    if (preview) preview.src = imgbbUrl;
                    if (imgInput) imgInput.value = imgbbUrl;
                    if (statusEl) {
                        statusEl.textContent = '✓ Hébergé sur ImgBB';
                        statusEl.style.color = '#10b981';
                    }
                    showAdminToast('Image hébergée avec succès sur ImgBB !');
                } catch (err) {
                    console.error('ImgBB API upload error:', err);
                    if (statusEl) {
                        statusEl.textContent = 'Erreur upload : ' + err.message;
                        statusEl.style.color = '#ef4444';
                    }
                    alert('Erreur lors du téléversement sur ImgBB : ' + err.message);
                }
            });
        }

        // Custom URL input
        if (imgInput) {
            imgInput.addEventListener('input', (e) => {
                state.selectedImage = e.target.value;
                if (preview) preview.src = state.selectedImage;
            });
        }
    }

    // --- Product Modal Operations ---
    const btnOpenAddProduct = document.getElementById('btn-open-add-product');
    if (btnOpenAddProduct) {
        btnOpenAddProduct.addEventListener('click', () => {
            state.editingProductId = null;
            document.getElementById('product-modal-title').innerHTML = '<i class="fas fa-plus-circle"></i> Ajouter un Nouveau Produit';
            if (productForm) productForm.reset();
            document.getElementById('prod-form-ref').value = 'GE-PRD-' + Math.floor(100 + Math.random() * 900);
            initImageSelector(PRESET_ASSETS[0]);
            openModal(productModal);
        });
    }

    function openEditProductModal(id) {
        const product = ShopData.getProductById(id);
        if (!product) return;

        state.editingProductId = id;
        document.getElementById('product-modal-title').innerHTML = '<i class="fas fa-pen"></i> Modifier le Produit';
        
        document.getElementById('prod-form-name').value = product.name || '';
        document.getElementById('prod-form-ref').value = product.ref || '';
        document.getElementById('prod-form-category').value = product.categoryId || '';
        document.getElementById('prod-form-status').value = product.status || 'in-stock';
        document.getElementById('prod-form-badge').value = product.badge || '';
        document.getElementById('prod-form-price').value = product.priceDisplay || 'Sur Devis';
        document.getElementById('prod-form-short-desc').value = product.shortDesc || '';
        document.getElementById('prod-form-desc').value = product.description || '';
        document.getElementById('prod-form-features').value = (product.features || []).join('\n');

        initImageSelector(product.image);
        openModal(productModal);
    }

    if (productForm) {
        productForm.addEventListener('submit', (e) => {
            e.preventDefault();

            const name = document.getElementById('prod-form-name').value.trim();
            if (!name) {
                alert('Veuillez renseigner le nom du produit.');
                return;
            }

            const ref = document.getElementById('prod-form-ref').value.trim();
            const categoryId = document.getElementById('prod-form-category').value;
            const status = document.getElementById('prod-form-status').value;
            const badge = document.getElementById('prod-form-badge').value.trim();
            const priceDisplay = document.getElementById('prod-form-price').value.trim();
            const shortDesc = document.getElementById('prod-form-short-desc').value.trim();
            const description = document.getElementById('prod-form-desc').value.trim();
            const featuresRaw = document.getElementById('prod-form-features').value;
            const features = featuresRaw.split('\n').map(s => s.trim()).filter(Boolean);
            const image = document.getElementById('prod-form-image').value || state.selectedImage;

            const productData = {
                name,
                ref,
                categoryId,
                status,
                badge,
                priceDisplay,
                shortDesc,
                description,
                features,
                image
            };

            if (state.editingProductId) {
                ShopData.updateProduct(state.editingProductId, productData);
                showAdminToast(`Produit "${name}" mis à jour avec succès !`);
            } else {
                ShopData.addProduct(productData);
                showAdminToast(`Nouveau produit "${name}" ajouté au catalogue !`);
            }

            closeModal(productModal);
            refreshAll();
        });
    }

    // --- Category Modal Operations ---
    const btnOpenAddCategory = document.getElementById('btn-open-add-category');
    if (btnOpenAddCategory) {
        btnOpenAddCategory.addEventListener('click', () => {
            state.editingCategoryId = null;
            document.getElementById('category-modal-title').innerHTML = '<i class="fas fa-plus-circle"></i> Ajouter une Catégorie';
            if (categoryForm) categoryForm.reset();
            document.getElementById('cat-form-icon').value = 'fa-bomb';
            openModal(categoryModal);
        });
    }

    function openEditCategoryModal(id) {
        const cat = ShopData.getCategoryById(id);
        if (!cat) return;

        state.editingCategoryId = id;
        document.getElementById('category-modal-title').innerHTML = '<i class="fas fa-pen"></i> Modifier la Catégorie';
        document.getElementById('cat-form-name').value = cat.name || '';
        document.getElementById('cat-form-icon').value = cat.icon || 'fa-tag';
        document.getElementById('cat-form-desc').value = cat.description || '';
        openModal(categoryModal);
    }

    if (categoryForm) {
        categoryForm.addEventListener('submit', (e) => {
            e.preventDefault();

            const name = document.getElementById('cat-form-name').value.trim();
            if (!name) {
                alert('Veuillez renseigner le nom de la catégorie.');
                return;
            }

            const icon = document.getElementById('cat-form-icon').value.trim() || 'fa-tag';
            const description = document.getElementById('cat-form-desc').value.trim();

            const catData = { name, icon, description };

            if (state.editingCategoryId) {
                ShopData.updateCategory(state.editingCategoryId, catData);
                showAdminToast(`Catégorie "${name}" mise à jour !`);
            } else {
                ShopData.addCategory(catData);
                showAdminToast(`Catégorie "${name}" créée avec succès !`);
            }

            closeModal(categoryModal);
            refreshAll();
        });
    }

    // --- Modals Generic Helpers ---
    function openModal(modalEl) {
        if (!modalEl) return;
        modalEl.classList.add('active');
        document.body.style.overflow = 'hidden';
    }

    function closeModal(modalEl) {
        if (!modalEl) return;
        modalEl.classList.remove('active');
        document.body.style.overflow = '';
    }

    document.querySelectorAll('.btn-close-admin-modal').forEach(btn => {
        btn.addEventListener('click', () => {
            closeModal(productModal);
            closeModal(categoryModal);
        });
    });

    [productModal, categoryModal].forEach(modal => {
        if (modal) {
            modal.addEventListener('click', (e) => {
                if (e.target === modal) closeModal(modal);
            });
        }
    });

    // --- Search & Filter Listeners ---
    if (adminProductSearch) {
        adminProductSearch.addEventListener('input', (e) => {
            state.productSearch = e.target.value;
            renderProductsTable();
        });
    }

    if (adminCategoryFilter) {
        adminCategoryFilter.addEventListener('change', (e) => {
            state.productFilterCat = e.target.value;
            renderProductsTable();
        });
    }

    // --- Backup & Tools (Export / Import / Reset) ---
    const btnExportData = document.getElementById('btn-export-data');
    if (btnExportData) {
        btnExportData.addEventListener('click', () => {
            const data = ShopData.exportData();
            const jsonStr = "data:text/json;charset=utf-8," + encodeURIComponent(JSON.stringify(data, null, 2));
            const dlAnchor = document.createElement('a');
            const dateStr = new Date().toISOString().split('T')[0];
            dlAnchor.setAttribute("href", jsonStr);
            dlAnchor.setAttribute("download", `golden-eagle-catalogue-${dateStr}.json`);
            document.body.appendChild(dlAnchor);
            dlAnchor.click();
            dlAnchor.remove();
            showAdminToast('Sauvegarde exportée avec succès !');
        });
    }

    const fileImportInput = document.getElementById('file-import-data');
    if (fileImportInput) {
        fileImportInput.addEventListener('change', (e) => {
            const file = e.target.files[0];
            if (!file) return;

            const reader = new FileReader();
            reader.onload = (re) => {
                const res = ShopData.importData(re.target.result);
                if (res.success) {
                    showAdminToast(res.message);
                    refreshAll();
                } else {
                    alert(res.message);
                }
            };
            reader.readAsText(file);
        });
    }

    const btnResetDefaults = document.getElementById('btn-reset-defaults');
    if (btnResetDefaults) {
        btnResetDefaults.addEventListener('click', () => {
            if (confirm('ATTENTION: Voulez-vous vraiment réinitialiser tout le catalogue aux produits et catégories par défaut de Golden Eagle ? Vos modifications personnalisées seront écrasées.')) {
                ShopData.resetToDefaults();
                showAdminToast('Catalogue réinitialisé avec succès aux paramètres d\'usine.');
                refreshAll();
            }
        });
    }

    // --- Toast Notification ---
    function showAdminToast(msg) {
        let toast = document.getElementById('admin-toast');
        if (!toast) {
            toast = document.createElement('div');
            toast.id = 'admin-toast';
            toast.style.cssText = `
                position: fixed;
                bottom: 2rem;
                right: 2rem;
                background: #15171b;
                color: #ffffff;
                border-left: 4px solid #cc9933;
                border: 1px solid #262930;
                padding: 1rem 1.5rem;
                border-radius: 8px;
                box-shadow: 0 10px 30px rgba(0,0,0,0.5);
                z-index: 99999;
                display: flex;
                align-items: center;
                gap: 0.75rem;
                font-size: 0.9rem;
            `;
            document.body.appendChild(toast);
        }

        toast.innerHTML = `<i class="fas fa-check-circle" style="color:#cc9933;"></i> <span>${msg}</span>`;
        toast.style.display = 'flex';
        toast.style.opacity = '1';

        setTimeout(() => {
            toast.style.opacity = '0';
            toast.style.transition = 'opacity 0.4s';
            setTimeout(() => { toast.style.display = 'none'; }, 400);
        }, 3000);
    }

    // --- API Diagnostics & Status Checker ---
    async function checkApisStatus() {
        const fbIndicator = document.getElementById('firebase-status-indicator');
        const fbDetail = document.getElementById('firebase-status-detail');
        const fbGuide = document.getElementById('firebase-rules-guide');

        if (typeof FirebaseSync !== 'undefined') {
            const check = await FirebaseSync.checkConnection();
            if (check.status === 'connected') {
                if (fbIndicator) {
                    fbIndicator.innerHTML = '<i class="fas fa-check-circle"></i> Connecté & Synchro Active';
                    fbIndicator.style.color = '#10b981';
                }
                if (fbDetail) fbDetail.textContent = 'Synchronisation cloud Firestore 100% opérationnelle.';
                if (fbGuide) fbGuide.style.display = 'none';
            } else if (check.status === 'rules-required') {
                if (fbIndicator) {
                    fbIndicator.innerHTML = '<i class="fas fa-exclamation-triangle"></i> Règles à Activer';
                    fbIndicator.style.color = '#f59e0b';
                }
                if (fbDetail) fbDetail.textContent = 'Connecté au projet Firebase. Veuillez autoriser la lecture/écriture dans les règles Firestore pour activer la synchronisation multi-postes.';
                if (fbGuide) fbGuide.style.display = 'block';
            } else {
                if (fbIndicator) {
                    fbIndicator.innerHTML = '<i class="fas fa-times-circle"></i> Hors ligne';
                    fbIndicator.style.color = '#ef4444';
                }
                if (fbDetail) fbDetail.textContent = check.message;
            }
        }
    }

    const btnTestApis = document.getElementById('btn-test-apis');
    if (btnTestApis) {
        btnTestApis.addEventListener('click', async () => {
            btnTestApis.disabled = true;
            btnTestApis.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Test des connexions en cours...';
            await checkApisStatus();
            setTimeout(() => {
                btnTestApis.disabled = false;
                btnTestApis.innerHTML = '<i class="fas fa-sync-alt"></i> Tester l\'état de la connexion APIs';
                showAdminToast('Diagnostic des APIs effectué.');
            }, 600);
        });
    }

    // --- Refresh All UI ---
    function refreshAll() {
        renderStats();
        populateCategoryDropdowns();
        renderProductsTable();
        renderCategoriesGrid();
    }

    // Initial Execution
    refreshAll();
    checkApisStatus();
});
