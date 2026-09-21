document.addEventListener('DOMContentLoaded', () => {
    // Mobile Menu Toggle
    const mobileMenuBtn = document.getElementById('mobile-menu');
    const navList = document.querySelector('.nav-list');

    if (mobileMenuBtn) {
        mobileMenuBtn.addEventListener('click', () => {
            navList.classList.toggle('active');
        });
    }

    // Intersection Observer for Scroll Animations
    const observerOptions = {
        root: null,
        rootMargin: '0px',
        threshold: 0.15 // Triggers when 15% of the element is visible
    };

    const observer = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('active');
                // Optional: stop observing once animated to keep it visible
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);

    // Select all elements with the .reveal class
    const revealElements = document.querySelectorAll('.reveal');
    revealElements.forEach(el => {
        observer.observe(el);
    });
    // Contact Form Mailto Handler
    const contactForm = document.getElementById('contact-form');
    if (contactForm) {
        contactForm.addEventListener('submit', (e) => {
            e.preventDefault();
            const name = document.getElementById('contact-name').value;
            const email = document.getElementById('contact-email').value;
            const subject = document.getElementById('contact-subject').value;
            const body = document.getElementById('contact-body').value;
            
            const mailtoSubject = encodeURIComponent(subject);
            const mailtoBody = encodeURIComponent("Nom: " + name + "\nEmail: " + email + "\n\nMessage:\n" + body);
            
            window.location.href = "mailto:info@goldeneaglebf.com?subject=" + mailtoSubject + "&body=" + mailtoBody;
        });
    }

    // Initialize Swiper Event Gallery
    if (document.querySelector('.event-slider') && typeof Swiper !== 'undefined') {
        const swiper = new Swiper('.event-slider', {
            effect: 'coverflow',
            grabCursor: true,
            centeredSlides: true,
            slidesPerView: 'auto',
            coverflowEffect: {
                rotate: 20,
                stretch: 0,
                depth: 200,
                modifier: 1,
                slideShadows: true,
            },
            loop: true,
            autoplay: {
                delay: 3500,
                disableOnInteraction: false,
            },
            pagination: {
                el: '.swiper-pagination',
                clickable: true,
            },
            navigation: {
                nextEl: '.swiper-button-next',
                prevEl: '.swiper-button-prev',
            },
        });
    }
});
