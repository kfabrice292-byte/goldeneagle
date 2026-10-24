document.addEventListener("DOMContentLoaded", () => {
    const navSwitch = document.getElementById("nav-switch");
    const navMenu = document.getElementById("nav-menu");

    if (navSwitch && navMenu) {
        navSwitch.addEventListener("click", () => {
            navSwitch.classList.toggle("active");
            navMenu.classList.toggle("active");
        });
        
        // Close menu when a link is clicked (especially important for mobile and anchor links)
        const navLinks = navMenu.querySelectorAll("a");
        navLinks.forEach(link => {
            link.addEventListener("click", () => {
                navSwitch.classList.remove("active");
                navMenu.classList.remove("active");
            });
        });
    }

    // Map Filtering Logic
    const filterBtns = document.querySelectorAll('.mapa-filtre button');
    const mapDots = document.querySelectorAll('.map-dot');
    const cifraBases = document.getElementById('cifra-bases');
    const cifraOps = document.getElementById('cifra-ops');
    
    if (filterBtns.length > 0) {
        filterBtns.forEach(btn => {
            btn.addEventListener('click', () => {
                // Remove active from all
                document.querySelectorAll('.mapa-filtre li').forEach(li => li.classList.remove('active'));
                if (btn.parentElement) {
                    btn.parentElement.classList.add('active');
                }
                
                const filter = btn.getAttribute('data-filter');
                let visibleCount = 0;
                
                mapDots.forEach(dot => {
                    if (filter === 'all' || dot.classList.contains('type-' + filter)) {
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
                
                // Update numbers based on filter if elements exist
                if (cifraBases && cifraOps) {
                    const baseVal = window.originalBases || '3';
                    const paysVal = window.originalPays || '5';
                    
                    if (filter === 'bases') {
                        cifraBases.textContent = baseVal;
                        cifraOps.textContent = '+' + Math.max(1, parseInt(paysVal) - 2);
                    } else if (filter === 'mmu') {
                        cifraBases.textContent = Math.max(1, parseInt(baseVal) - 1);
                        cifraOps.textContent = '+' + Math.max(1, parseInt(paysVal) - 3);
                    } else {
                        cifraBases.textContent = baseVal;
                        cifraOps.textContent = '+' + paysVal;
                    }
                }
            });
        });
    }
});
