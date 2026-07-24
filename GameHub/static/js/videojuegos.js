// Catálogo de juegos
const gridJuegos = document.getElementById('gridJuegos');
if (gridJuegos) {
    async function cargarCatalogo() {
        const loading = document.getElementById('loadingCatalogo');
        const empty = document.getElementById('emptyCatalogo');
        
        if(loading) loading.classList.remove('hidden');
        if(empty) empty.classList.add('hidden');
        gridJuegos.innerHTML = '';

        try {
            const params = new URLSearchParams(window.location.search);
            const juegos = await apiFetch(`/videojuegos?${params.toString()}`);

            if (juegos.length === 0) {
                if(loading) loading.classList.add('hidden');
                if(empty) empty.classList.remove('hidden');
                return;
            }

            // Obtener calificaciones en paralelo
            const califPromises = juegos.map(j => 
                apiFetch(`/videojuegos/${j.id_videojuego}/calificacion`)
                    .catch(() => ({ promedio: 0.0, total_resenas: 0 }))
            );
            const calificaciones = await Promise.all(califPromises);

            const tarjetas = juegos.map((j, index) => {
                const calif = calificaciones[index];
                const portada = j.portada || 'https://via.placeholder.com/600x300';
                
                // Escapar valores para evitar XSS simple
                const titulo = escapeHTML(j.titulo);
                const genero = escapeHTML(j.genero || 'Desconocido');
                const plataforma = escapeHTML(j.plataforma || 'Varias');
                const estado = escapeHTML(j.estado || 'Lanzado');
                const prom = parseFloat(calif.promedio).toFixed(1);

                return `
                    <article class="game-card">
                        <a href="/detalle_juego?id=${j.id_videojuego}" class="game-card-cover">
                            <img src="${portada}" alt="Portada de ${titulo}" loading="lazy">
                        </a>

                        <div class="game-card-content">
                            <div class="game-card-header">
                                <h3>
                                    <a href="/detalle_juego?id=${j.id_videojuego}">${titulo}</a>
                                </h3>
                                <span class="status-badge">${estado}</span>
                            </div>

                            <p class="game-card-meta">
                                ${genero} · ${plataforma}
                            </p>

                            <div class="game-card-tags">
                                <span class="tag">${genero}</span>
                                <span class="tag">${plataforma}</span>
                            </div>

                            <div class="game-card-footer">
                                <span class="game-rating">
                                    ★ ${prom}
                                </span>
                                <span class="review-count">
                                    ${calif.total_resenas} reseñas
                                </span>
                            </div>
                        </div>
                    </article>
                `;
            });

            gridJuegos.innerHTML = tarjetas.join("");
            
            if(loading) loading.classList.add('hidden');

        } catch (error) {
            console.error("Error cargando catálogo", error);
            if(loading) loading.classList.add('hidden');
            gridJuegos.innerHTML = `<div class="error-state">Ocurrió un error al cargar los videojuegos.</div>`;
        }
    }
    
    // Función auxiliar para escape HTML
    function escapeHTML(str) {
        if(!str) return '';
        return String(str).replace(/[&<>'"]/g, 
            tag => ({
                '&': '&amp;',
                '<': '&lt;',
                '>': '&gt;',
                "'": '&#39;',
                '"': '&quot;'
            }[tag] || tag)
        );
    }

    cargarCatalogo();
}

// Publicar juego
const formPublicar = document.getElementById('formPublicar');
if (formPublicar) {
    // Lógica para previsualización de portada
    const portadaInput = document.getElementById('portada');
    const previewPortada = document.getElementById('previewPortada');
    
    if (portadaInput && previewPortada) {
        portadaInput.addEventListener('change', (e) => {
            const file = e.target.files[0];
            if (file && file.type.startsWith('image/')) {
                // Liberar URL anterior si existe
                if (previewPortada.src && previewPortada.src.startsWith('blob:')) {
                    URL.revokeObjectURL(previewPortada.src);
                }
                const url = URL.createObjectURL(file);
                previewPortada.src = url;
                previewPortada.classList.remove('hidden');
            } else {
                previewPortada.src = '';
                previewPortada.classList.add('hidden');
            }
        });
    }

    formPublicar.addEventListener('submit', async (e) => {
        e.preventDefault();
        
        const submitBtn = formPublicar.querySelector('button[type="submit"]');
        submitBtn.disabled = true;
        submitBtn.textContent = 'Publicando...';

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
            if (portadaInput && portadaInput.files.length > 0) {
                const fdPortada = new FormData();
                fdPortada.append('file', portadaInput.files[0]);
                await apiFetch(`/videojuegos/${juego.id_videojuego}/portada`, {
                    method: 'POST',
                    body: fdPortada
                });
            }

            // Subir ZIP si existe
            const archivoInput = document.getElementById('archivo_juego');
            if (archivoInput && archivoInput.files.length > 0) {
                const fdArchivo = new FormData();
                fdArchivo.append('file', archivoInput.files[0]);
                await apiFetch(`/videojuegos/${juego.id_videojuego}/archivo`, {
                    method: 'POST',
                    body: fdArchivo
                });
            }

            mostrarMensaje('msgPublicar', 'Videojuego publicado exitosamente');
            setTimeout(() => { window.location.href = '/mis_juegos'; }, 2000);
        } catch (error) {
            mostrarMensaje('msgPublicar', error.message, true);
            submitBtn.disabled = false;
            submitBtn.textContent = 'Publicar Videojuego';
        }
    });
}
