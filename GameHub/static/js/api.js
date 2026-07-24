const API_URL = '/api';

// Función genérica para mostrar mensajes
function mostrarMensaje(idElemento, mensaje, esError = false) {
    const el = document.getElementById(idElemento);
    if (!el) return;
    el.textContent = mensaje;
    el.className = `alert ${esError ? 'alert-danger' : 'alert-success'}`;
    el.style.display = 'block';
    setTimeout(() => { el.style.display = 'none'; }, 5000);
}

// Función base para Fetch
async function apiFetch(endpoint, opciones = {}) {
    const headers = opciones.headers || {};
    const token = localStorage.getItem('token');
    
    if (token) {
        headers['Authorization'] = `Bearer ${token}`;
    }
    
    // Si no es FormData, añadimos Content-Type JSON por defecto
    if (!(opciones.body instanceof FormData) && !headers['Content-Type']) {
        headers['Content-Type'] = 'application/json';
    }

    const res = await fetch(`${API_URL}${endpoint}`, {
        ...opciones,
        headers
    });

    if (res.status === 204) return null; // No content

    const data = await res.json();
    if (!res.ok) {
        throw new Error(data.detail || 'Error en la petición');
    }
    return data;
}

// Ajustar interfaz según si hay sesión
document.addEventListener('DOMContentLoaded', () => {
    const token = localStorage.getItem('token');
    const authLinks = document.querySelectorAll('.req-auth');
    const unauthLinks = document.querySelectorAll('.req-unauth');
    
    if (token) {
        authLinks.forEach(el => el.classList.remove('hidden'));
        unauthLinks.forEach(el => el.classList.add('hidden'));
    } else {
        authLinks.forEach(el => el.classList.add('hidden'));
        unauthLinks.forEach(el => el.classList.remove('hidden'));
    }
});

function cerrarSesion() {
    localStorage.removeItem('token');
    localStorage.removeItem('userId');
    window.location.href = '/login';
}
