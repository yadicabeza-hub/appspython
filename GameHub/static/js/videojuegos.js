// Catálogo de juegos
const gridJuegos = document.getElementById('gridJuegos');
if (gridJuegos) {
    async function cargarCatalogo() {
        try {
            const params = new URLSearchParams(window.location.search);
            const juegos = await apiFetch(`/videojuegos?${params.toString()}`);
            gridJuegos.innerHTML = '';

            for (const j of juegos) {
                // Obtener calificación promedio
                const calif = await apiFetch(`/videojuegos/${j.id_videojuego}/calificacion`);
                const portada = j.portada || 'https://via.placeholder.com/250x150';

                gridJuegos.innerHTML += `
                    <div class="card">
                        <img src="${portada}" class="card-img" alt="Portada">
                        <div class="card-body">
                            <h3>${j.titulo}</h3>
                            <p>${j.genero} | ${j.plataforma}</p>
                            <p>⭐ ${calif.promedio} (${calif.total_resenas})</p>
                            <a href="/detalle_juego?id=${j.id_videojuego}" class="btn btn-primary">Ver Detalle</a>
                        </div>
                    </div>
                `;
            }
        } catch (error) {
            console.error("Error cargando catálogo", error);
        }
    }
    cargarCatalogo();
}

// Publicar juego
const formPublicar = document.getElementById('formPublicar');
if (formPublicar) {
    formPublicar.addEventListener('submit', async (e) => {
        e.preventDefault();

        const data = {
            titulo: document.getElementById('titulo').value,
            descripcion: document.getElementById('descripcion').value,
            genero: document.getElementById('genero').value,
            plataforma: document.getElementById('plataforma').value,
            version: document.getElementById('version').value,
            estado: document.getElementById('estado').value,
            enlace_descarga: document.getElementById('enlace_descarga').value || null
        };

        try {
            // Crear juego base
            const juego = await apiFetch('/videojuegos', {
                method: 'POST',
                body: JSON.stringify(data)
            });

            // Subir portada si existe
            const portadaInput = document.getElementById('portada');
            if (portadaInput.files.length > 0) {
                const fdPortada = new FormData();
                fdPortada.append('file', portadaInput.files[0]);
                await apiFetch(`/videojuegos/${juego.id_videojuego}/portada`, {
                    method: 'POST',
                    body: fdPortada
                });
            }

            // Subir ZIP si existe
            const archivoInput = document.getElementById('archivo_juego');
            if (archivoInput.files.length > 0) {
                const fdArchivo = new FormData();
                fdArchivo.append('file', archivoInput.files[0]);
                await apiFetch(`/videojuegos/${juego.id_videojuego}/archivo`, {
                    method: 'POST',
                    body: fdArchivo
                });
            }

            mostrarMensaje('msgPublicar', 'Juego publicado exitosamente');
            setTimeout(() => { window.location.href = '/mis_juegos'; }, 2000);
        } catch (error) {
            mostrarMensaje('msgPublicar', error.message, true);
        }
    });
}
