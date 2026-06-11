document.addEventListener('DOMContentLoaded', () => {
    // Mobile Menu Toggle
    const hamburger = document.querySelector('.hamburger');
    const navLinks = document.querySelector('.nav-links');
    const links = document.querySelectorAll('.nav-links li a');

    if (hamburger) {
        hamburger.addEventListener('click', () => {
            hamburger.classList.toggle('active');
            navLinks.classList.toggle('active');
        });
    }

    // Close mobile menu when a link is clicked
    links.forEach(link => {
        link.addEventListener('click', () => {
            hamburger.classList.remove('active');
            navLinks.classList.remove('active');
        });
    });

    // Form Validation and Submission (Client Side)
    const form = document.getElementById('contact-form');
    const statusDiv = document.getElementById('form-status');

    if (form) {
        form.addEventListener('submit', (e) => {
            e.preventDefault();
            
            // Basic input sanitization (prevent XSS in local display)
            const escapeHTML = (str) => str.replace(/[&<>'"]/g, 
                tag => ({
                    '&': '&amp;',
                    '<': '&lt;',
                    '>': '&gt;',
                    "'": '&#39;',
                    '"': '&quot;'
                }[tag])
            );

            const name = escapeHTML(document.getElementById('name').value.trim());
            const email = escapeHTML(document.getElementById('email').value.trim());
            
            // Simple email regex validation
            const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

            if (name === '' || email === '') {
                statusDiv.textContent = 'Por favor, completa los campos requeridos.';
                statusDiv.className = 'form-status error';
                return;
            }

            if (!emailRegex.test(email)) {
                statusDiv.textContent = 'Por favor, ingresa un correo válido.';
                statusDiv.className = 'form-status error';
                return;
            }

            // Simulate successful submission
            statusDiv.textContent = `¡Gracias ${name}! Tu solicitud ha sido enviada correctamente.`;
            statusDiv.className = 'form-status success';
            form.reset();
            
            // Clear message after 5 seconds
            setTimeout(() => {
                statusDiv.textContent = '';
                statusDiv.className = 'form-status';
            }, 5000);
        });
    }
});
