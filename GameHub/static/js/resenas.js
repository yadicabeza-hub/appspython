// Detalle y Reseñas
const detalleContenedor = document.getElementById('detalleJuego');
const listaResenas = document.getElementById('listaResenas');
const formResena = document.getElementById('formResena');

if (detalleContenedor) {
    const urlParams = new URLSearchParams(window.location.search);
    const idJuego = urlParams.get('id');
    
    async function cargarDetalle() {
        if (!idJuego) return;
        
        try {
            const juego = await apiFetch(`/videojuegos/${idJuego}`);
            const calif = await apiFetch(`/videojuegos/${idJuego}/calificacion`);
            const portada = juego.portada || 'https://via.placeholder.com/800x400';
            const prom = parseFloat(calif.promedio).toFixed(1);
            
            detalleContenedor.innerHTML = `
                <div class="game-detail">
                    <img src="${portada}" class="game-detail-cover" alt="Portada de ${escapeHTML(juego.titulo)}">
                    <div class="game-detail-content">
                        <div class="game-detail-main">
                            <h1>${escapeHTML(juego.titulo)}</h1>
                            <p class="game-detail-author">Por <strong>Desarrollador #${juego.id_usuario}</strong></p>
                            
                            <div class="game-card-tags" style="margin-bottom: 20px;">
                                <span class="tag">${escapeHTML(juego.genero)}</span>
                                <span class="tag">${escapeHTML(juego.plataforma)}</span>
                                <span class="status-badge">${escapeHTML(juego.estado)}</span>
                            </div>

                            <div style="margin-top:30px;">
                                <h3>Acerca de este videojuego</h3>
                                <p style="white-space: pre-line; margin-top:10px; color:var(--color-text-secondary); line-height:1.6;">${escapeHTML(juego.descripcion)}</p>
                            </div>
                        </div>

                        <aside class="game-detail-sidebar">
                            <div class="download-panel">
                                <h3 style="margin-bottom:15px; font-size:18px;">Descargar videojuego</h3>
                                ${juego.archivo_juego ? 
                                    `<a href="${juego.archivo_juego}" class="btn btn-primary" download>Descargar archivo</a>` : 
                                    `<button class="btn btn-primary" disabled>Descarga no disponible</button>`
                                }
                                ${juego.enlace_descarga ? 
                                    `<a href="${juego.enlace_descarga}" class="btn btn-outline" style="margin-top:10px;" target="_blank">Enlace externo</a>` : ''
                                }
                            </div>

                            <div class="tech-info">
                                <h3>Información técnica</h3>
                                <p><span>Calificación</span> <span>⭐ ${prom} (${calif.total_resenas})</span></p>
                                <p><span>Estado</span> <span>${escapeHTML(juego.estado)}</span></p>
                                <p><span>Plataforma</span> <span>${escapeHTML(juego.plataforma)}</span></p>
                                <p><span>Género</span> <span>${escapeHTML(juego.genero)}</span></p>
                                <p><span>Versión</span> <span>${escapeHTML(juego.version)}</span></p>
                            </div>
                        </aside>
                    </div>
                </div>
            `;
            
            // Actualizar título de la página
            document.title = `${juego.titulo} - GameHub`;

            cargarResenas();
        } catch (error) {
            console.error("Error", error);
            detalleContenedor.innerHTML = `<div class="error-state">Error al cargar los detalles del juego.</div>`;
        }
    }
    
    async function cargarResenas() {
        try {
            const resenas = await apiFetch(`/videojuegos/${idJuego}/resenas`);
            if (resenas.length === 0) {
                listaResenas.innerHTML = `<div class="empty-state" style="padding:20px;">Aún no hay reseñas. ¡Sé el primero!</div>`;
                return;
            }

            listaResenas.innerHTML = resenas.map(r => {
                let estrellas = '⭐'.repeat(r.calificacion);
                return `
                <div class="review-card">
                    <div style="display:flex; justify-content:space-between; margin-bottom:10px;">
                        <strong>Usuario #${r.id_usuario}</strong>
                        <span class="game-rating">${estrellas}</span>
                    </div>
                    <p style="color:var(--color-text-secondary); margin-bottom:10px;">${escapeHTML(r.comentario)}</p>
                    <small style="color:#aaa;">${new Date(r.fecha_resena).toLocaleDateString()}</small>
                </div>
                `;
            }).join('');
        } catch (error) {
            console.error("Error", error);
        }
    }

    if (formResena) {
        formResena.addEventListener('submit', async (e) => {
            e.preventDefault();
            const calificacion = parseInt(document.getElementById('calificacion').value);
            const comentario = document.getElementById('comentario').value;
            const submitBtn = formResena.querySelector('button');
            
            submitBtn.disabled = true;
            submitBtn.textContent = "Enviando...";

            try {
                await apiFetch(`/videojuegos/${idJuego}/resenas`, {
                    method: 'POST',
                    body: JSON.stringify({ calificacion, comentario })
                });
                mostrarMensaje('msgResena', 'Reseña publicada correctamente.');
                cargarDetalle();
                formResena.reset();
            } catch (error) {
                mostrarMensaje('msgResena', error.message, true);
            } finally {
                submitBtn.disabled = false;
                submitBtn.textContent = "Publicar reseña";
            }
        });
    }

    // Auxiliar escape html
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

    cargarDetalle();
}
