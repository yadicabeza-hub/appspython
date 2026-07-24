// Manejo del formulario de registro
const formRegistro = document.getElementById('formRegistro');
if (formRegistro) {
    formRegistro.addEventListener('submit', async (e) => {
        e.preventDefault();
        
        const nombre_usuario = document.getElementById('nombre_usuario').value;
        const correo = document.getElementById('correo').value;
        const contrasena = document.getElementById('contrasena').value;
        const confirmar = document.getElementById('confirmar').value;

        if (contrasena !== confirmar) {
            mostrarMensaje('msgRegistro', 'Las contraseñas no coinciden', true);
            return;
        }

        try {
            await apiFetch('/auth/registro', {
                method: 'POST',
                body: JSON.stringify({ nombre_usuario, correo, contrasena })
            });
            mostrarMensaje('msgRegistro', 'Registro exitoso. Redirigiendo a Login...');
            setTimeout(() => { window.location.href = '/login'; }, 2000);
        } catch (error) {
            mostrarMensaje('msgRegistro', error.message, true);
        }
    });
}

// Manejo del formulario de Login
const formLogin = document.getElementById('formLogin');
if (formLogin) {
    formLogin.addEventListener('submit', async (e) => {
        e.preventDefault();
        
        const username = document.getElementById('username').value;
        const contrasena = document.getElementById('contrasena').value;

        const body = new URLSearchParams();
        body.append('username', username);
        body.append('password', contrasena);

        try {
            const data = await apiFetch('/auth/login', {
                method: 'POST',
                headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
                body: body
            });
            
            // Guardar token temporalmente en LocalStorage (ver README para prod)
            localStorage.setItem('token', data.access_token);
            
            // Obtener ID de usuario
            const user = await apiFetch('/auth/me');
            localStorage.setItem('userId', user.id_usuario);
            
            window.location.href = '/perfil';
        } catch (error) {
            mostrarMensaje('msgLogin', error.message, true);
        }
    });
}

// Cargar perfil
const infoPerfil = document.getElementById('infoPerfil');
if (infoPerfil) {
    async function cargarPerfil() {
        const userId = localStorage.getItem('userId');
        if (!userId) return window.location.href = '/login';
        
        try {
            const user = await apiFetch('/auth/me');
            const perfil = await apiFetch(`/perfiles/${user.id_usuario}`);
            
            document.getElementById('usernameDisplay').textContent = `@${user.nombre_usuario}`;
            document.getElementById('nombreCompleto').textContent = perfil.nombre_completo || 'Sin nombre';
            document.getElementById('biografia').textContent = perfil.biografia || 'Sin biografía';
            document.getElementById('pais').textContent = perfil.pais || 'No especificado';
            document.getElementById('tipo').textContent = perfil.tipo_usuario;
            
            if (perfil.fotografia) {
                document.getElementById('fotoPerfil').src = perfil.fotografia;
            }
            
            // Llenar formulario de edición
            const formUpdatePerfil = document.getElementById('formUpdatePerfil');
            if(formUpdatePerfil) {
                document.getElementById('edit_nombre').value = perfil.nombre_completo || '';
                document.getElementById('edit_pais').value = perfil.pais || '';
                document.getElementById('edit_bio').value = perfil.biografia || '';

                formUpdatePerfil.onsubmit = async (e) => {
                    e.preventDefault();
                    try {
                        await apiFetch('/perfiles/me', {
                            method: 'PUT',
                            body: JSON.stringify({
                                nombre_completo: document.getElementById('edit_nombre').value,
                                biografia: document.getElementById('edit_bio').value,
                                pais: document.getElementById('edit_pais').value
                            })
                        });
                        mostrarMensaje('msgPerfil', 'Perfil actualizado correctamente');
                        setTimeout(() => window.location.reload(), 1500);
                    } catch(error) {
                        mostrarMensaje('msgPerfil', error.message, true);
                    }
                };
            }
            
            // Cargar juegos publicados
            const juegos = await apiFetch(`/perfiles/${user.id_usuario}/videojuegos`);
            const listaJuegos = document.getElementById('listaMisJuegos');
            listaJuegos.innerHTML = juegos.map(j => `<li>${j.titulo} - ${j.estado}</li>`).join('');
            
        } catch (error) {
            console.error("Error cargando perfil", error);
        }
    }
    cargarPerfil();
}
