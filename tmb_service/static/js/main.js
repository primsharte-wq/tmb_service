// ============================================
// TMB SERVICE - JAVASCRIPT PREMIUM
// Expérience utilisateur fluide et moderne
// Version: 3.0
// ============================================

document.addEventListener('DOMContentLoaded', function() {
    
    // ============================================
    // 1. MOBILE NAVIGATION
    // ============================================
    const navToggle = document.getElementById('nav-toggle');
    const navMenu = document.getElementById('nav-menu');
    
    if (navToggle && navMenu) {
        navToggle.addEventListener('click', function() {
            navMenu.classList.toggle('active');
            document.body.style.overflow = navMenu.classList.contains('active') ? 'hidden' : '';
        });
        
        document.addEventListener('click', function(event) {
            if (!navMenu.contains(event.target) && !navToggle.contains(event.target)) {
                navMenu.classList.remove('active');
                document.body.style.overflow = '';
            }
        });
    }
    
    // ============================================
    // 2. NAVBAR SCROLL EFFECT (FLUIDE)
    // ============================================
    const navbar = document.querySelector('.navbar');
    if (navbar) {
        window.addEventListener('scroll', function() {
            if (window.scrollY > 50) {
                navbar.classList.add('scrolled');
            } else {
                navbar.classList.remove('scrolled');
            }
        });
    }
    
    // ============================================
    // 3. COOKIE CONSENT PREMIUM
    // ============================================
    const cookieConsent = document.getElementById('cookie-consent');
    const acceptBtn = document.getElementById('accept-cookies');
    const declineBtn = document.getElementById('decline-cookies');
    
    if (cookieConsent && !localStorage.getItem('cookieConsent')) {
        setTimeout(() => {
            cookieConsent.classList.add('show');
        }, 1500);
    }
    
    if (acceptBtn) {
        acceptBtn.addEventListener('click', () => {
            localStorage.setItem('cookieConsent', 'accepted');
            cookieConsent.classList.remove('show');
        });
    }
    
    if (declineBtn) {
        declineBtn.addEventListener('click', () => {
            localStorage.setItem('cookieConsent', 'declined');
            cookieConsent.classList.remove('show');
        });
    }
    
    // ============================================
    // 4. LIKE SYSTEM (CŒUR AVEC ANIMATION)
    // ============================================
    const likeButton = document.querySelector('.like-button');
    if (likeButton) {
        likeButton.addEventListener('click', function(e) {
            e.preventDefault();
            const modeleId = this.dataset.modeleId;
            const csrfToken = getCookie('csrftoken');
            
            // Animation de chargement
            this.style.opacity = '0.7';
            
            fetch(`/like/${modeleId}/`, {
                method: 'POST',
                headers: {
                    'X-CSRFToken': csrfToken,
                    'X-Requested-With': 'XMLHttpRequest',
                    'Content-Type': 'application/json'
                }
            })
            .then(response => response.json())
            .then(data => {
                this.style.opacity = '1';
                
                if (data.liked) {
                    this.classList.add('liked');
                    // Animation du cœur
                    const heartIcon = this.querySelector('i');
                    heartIcon.style.animation = 'none';
                    setTimeout(() => {
                        heartIcon.style.animation = 'heartBeat 0.4s cubic-bezier(0.34, 1.56, 0.64, 1)';
                    }, 10);
                } else {
                    this.classList.remove('liked');
                }
                
                const likesCountSpan = this.querySelector('.likes-count');
                if (likesCountSpan) {
                    likesCountSpan.textContent = data.likes_count;
                }
            })
            .catch(error => {
                console.error('Erreur:', error);
                this.style.opacity = '1';
            });
        });
    }
    
    // ============================================
    // 5. COMMENT SYSTEM (CLAVIER AUTOMATIQUE)
    // ============================================
    const commentToggle = document.querySelector('.comment-toggle');
    const commentFormContainer = document.getElementById('comment-form');
    
    if (commentToggle && commentFormContainer) {
        commentToggle.addEventListener('click', function() {
            commentFormContainer.classList.toggle('show');
            if (commentFormContainer.classList.contains('show')) {
                const textarea = commentFormContainer.querySelector('textarea');
                if (textarea) {
                    setTimeout(() => textarea.focus(), 100);
                }
            }
        });
    }
    
    // ============================================
    // 6. AUTO-HIDE MESSAGES (DOUCEUR)
    // ============================================
    const messages = document.querySelectorAll('.alert');
    messages.forEach(message => {
        setTimeout(() => {
            message.style.transition = 'opacity 0.5s ease';
            message.style.opacity = '0';
            setTimeout(() => {
                if (message.parentNode) message.remove();
            }, 500);
        }, 5000);
    });
    
    // ============================================
    // 7. SMOOTH SCROLL (ULTRA FLUIDE)
    // ============================================
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            const targetId = this.getAttribute('href');
            if (targetId !== '#' && targetId !== '') {
                e.preventDefault();
                const target = document.querySelector(targetId);
                if (target) {
                    const offsetTop = target.offsetTop - 80;
                    window.scrollTo({
                        top: offsetTop,
                        behavior: 'smooth'
                    });
                }
            }
        });
    });
    
    // ============================================
    // 8. REVEAL ON SCROLL (ANIMATION AU SCROLL)
    // ============================================
    const revealElements = document.querySelectorAll('.category-card, .service-card, .model-card');
    
    const revealOnScroll = () => {
        revealElements.forEach(element => {
            const elementTop = element.getBoundingClientRect().top;
            const windowHeight = window.innerHeight;
            
            if (elementTop < windowHeight - 100) {
                element.style.opacity = '1';
                element.style.transform = 'translateY(0)';
            }
        });
    };
    
    // Initialisation des éléments pour animation
    revealElements.forEach(element => {
        element.style.opacity = '0';
        element.style.transform = 'translateY(30px)';
        element.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
    });
    
    window.addEventListener('scroll', revealOnScroll);
    revealOnScroll();
    
    // ============================================
    // 9. FORM VALIDATION (EN TEMPS RÉEL)
    // ============================================
    const forms = document.querySelectorAll('form');
    forms.forEach(form => {
        const inputs = form.querySelectorAll('input, textarea');
        inputs.forEach(input => {
            input.addEventListener('focus', function() {
                this.style.borderColor = '#0066CC';
                this.style.boxShadow = '0 0 0 3px rgba(0,102,204,0.1)';
            });
            
            input.addEventListener('blur', function() {
                this.style.borderColor = '#E8E8ED';
                this.style.boxShadow = 'none';
            });
        });
    });
    
    // ============================================
    // 10. ANIMATION HEART BEAT (KEYFRAMES)
    // ============================================
    const style = document.createElement('style');
    style.textContent = `
        @keyframes heartBeat {
            0%, 100% { transform: scale(1); }
            30% { transform: scale(1.3); }
            60% { transform: scale(1.1); }
        }
    `;
    document.head.appendChild(style);
});

// ============================================
// CSRF TOKEN HELPER
// ============================================
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

// ============================================
// PRELOADER OPTIONNEL (DÉSACTIVÉ PAR DÉFAUT)
// ============================================
window.addEventListener('load', function() {
    document.body.style.opacity = '1';
});