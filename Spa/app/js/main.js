document.addEventListener('DOMContentLoaded', () => {
    // ==========================================================================
    // 1. Menú Hamburguesa (Mobile)
    // ==========================================================================
    const hamburger = document.getElementById('hamburger');
    const nav = document.getElementById('nav');
    const navLinks = document.querySelectorAll('.nav-link, .btn-nav');

    const toggleMenu = () => {
        hamburger.classList.toggle('active');
        nav.classList.toggle('active');
        
        // Prevenir scroll del body cuando el menú está abierto
        if (nav.classList.contains('active')) {
            document.body.style.overflow = 'hidden';
        } else {
            document.body.style.overflow = '';
        }
    };

    hamburger.addEventListener('click', toggleMenu);

    // Cerrar menú al hacer clic en un enlace
    navLinks.forEach(link => {
        link.addEventListener('click', () => {
            if (nav.classList.contains('active')) {
                toggleMenu();
            }
        });
    });

    // ==========================================================================
    // 2. Header Dinámico al hacer Scroll
    // ==========================================================================
    const header = document.getElementById('header');
    
    const handleScroll = () => {
        if (window.scrollY > 50) {
            header.classList.add('scrolled');
        } else {
            header.classList.remove('scrolled');
        }
    };

    window.addEventListener('scroll', handleScroll);
    // Ejecutar una vez al cargar por si la página ya está scrolleada
    handleScroll();

    // ==========================================================================
    // 3. Botón "Volver Arriba"
    // ==========================================================================
    const backToTopBtn = document.getElementById('back-to-top');

    window.addEventListener('scroll', () => {
        if (window.scrollY > 500) {
            backToTopBtn.classList.add('show');
        } else {
            backToTopBtn.classList.remove('show');
        }
    });

    backToTopBtn.addEventListener('click', () => {
        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        });
    });

    // ==========================================================================
    // 4. Animaciones al hacer Scroll (Intersection Observer)
    // ==========================================================================
    const revealElements = document.querySelectorAll('.reveal');

    const revealCallback = (entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('active');
                observer.unobserve(entry.target); // Solo animar una vez
            }
        });
    };

    const revealOptions = {
        threshold: 0.15, // Ejecutar cuando el 15% del elemento es visible
        rootMargin: "0px 0px -50px 0px"
    };

    const revealObserver = new IntersectionObserver(revealCallback, revealOptions);

    revealElements.forEach(el => revealObserver.observe(el));

    // ==========================================================================
    // 5. Actualización Automática del Año (Footer)
    // ==========================================================================
    const currentYearSpan = document.getElementById('current-year');
    if (currentYearSpan) {
        currentYearSpan.textContent = new Date().getFullYear();
    }

    // ==========================================================================
    // 6. Validación del Formulario de Reservas
    // ==========================================================================
    const reservaForm = document.getElementById('reserva-form');
    const formSuccess = document.getElementById('form-success');

    if (reservaForm) {
        reservaForm.addEventListener('submit', (e) => {
            e.preventDefault();
            
            let isValid = true;

            // Validar campos requeridos
            const inputs = reservaForm.querySelectorAll('input[required], select[required]');
            
            inputs.forEach(input => {
                const formGroup = input.closest('.form-group');
                
                // Resetear estado
                formGroup.classList.remove('error');

                // Lógica de validación
                if (input.type === 'checkbox' && !input.checked) {
                    isValid = false;
                    formGroup.classList.add('error');
                } else if (input.value.trim() === '') {
                    isValid = false;
                    formGroup.classList.add('error');
                } else if (input.type === 'email') {
                    // Validación básica de email
                    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
                    if (!emailRegex.test(input.value.trim())) {
                        isValid = false;
                        formGroup.classList.add('error');
                    }
                } else if (input.type === 'tel') {
                    // Validación básica de teléfono (solo números y algunos caracteres)
                    const telRegex = /^[\d\s\+\-\(\)]{7,15}$/;
                    if (!telRegex.test(input.value.trim())) {
                        isValid = false;
                        formGroup.classList.add('error');
                    }
                }
            });

            if (isValid) {
                // Simular envío de datos
                const submitBtn = reservaForm.querySelector('.btn-submit');
                const originalText = submitBtn.textContent;
                
                submitBtn.disabled = true;
                submitBtn.textContent = 'Enviando...';

                setTimeout(() => {
                    // Mostrar mensaje de éxito
                    formSuccess.classList.remove('oculto');
                    
                    // Limpiar formulario
                    reservaForm.reset();
                    
                    // Restaurar botón
                    submitBtn.disabled = false;
                    submitBtn.textContent = originalText;

                    // Ocultar mensaje después de 5 segundos
                    setTimeout(() => {
                        formSuccess.classList.add('oculto');
                    }, 5000);
                }, 1500); // Simulación de retraso de red
            }
        });
        
        // Quitar error al empezar a escribir/cambiar
        reservaForm.addEventListener('input', (e) => {
            if (e.target.required) {
                const formGroup = e.target.closest('.form-group');
                if (formGroup.classList.contains('error')) {
                    formGroup.classList.remove('error');
                }
            }
        });
    }

    // ==========================================================================
    // 7. Smooth Scroll Fix para enlaces internos (Safari/Older browsers support)
    // ==========================================================================
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            const targetId = this.getAttribute('href');
            if (targetId === '#') return;

            const targetElement = document.querySelector(targetId);
            if (targetElement) {
                e.preventDefault();
                // Ajustar por el header fijo
                const headerOffset = 70;
                const elementPosition = targetElement.getBoundingClientRect().top;
                const offsetPosition = elementPosition + window.pageYOffset - headerOffset;

                window.scrollTo({
                    top: offsetPosition,
                    behavior: 'smooth'
                });
            }
        });
    });
});
