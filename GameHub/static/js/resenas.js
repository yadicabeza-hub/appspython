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
            const portada = juego.portada || 'https://via.placeholder.com/600x300';
            
            detalleContenedor.innerHTML = `
                <img src="${portada}" style="width:100%;max-height:400px;object-fit:cover;border-radius:8px;">
                <h1>${juego.titulo}</h1>
                <p><strong>Género:</strong> ${juego.genero} | <strong>Plataforma:</strong> ${juego.plataforma}</p>
                <p><strong>Estado:</strong> ${juego.estado} | <strong>Versión:</strong> ${juego.version}</p>
                <p><strong>Calificación:</strong> ⭐ ${calif.promedio} / 5</p>
                <p>${juego.descripcion}</p>
                ${juego.archivo_juego ? `<a href="${juego.archivo_juego}" class="btn btn-primary" download>⬇️ Descargar ZIP</a>` : ''}
                ${juego.enlace_descarga ? `<a href="${juego.enlace_descarga}" class="btn btn-primary" target="_blank">Enlace Externo</a>` : ''}
            `;
            
            cargarResenas();
        } catch (error) {
            console.error("Error", error);
        }
    }
    
    async function cargarResenas() {
        try {
            const resenas = await apiFetch(`/videojuegos/${idJuego}/resenas`);
            listaResenas.innerHTML = resenas.map(r => `
                <div class="card" style="margin-bottom:1rem;">
                    <div class="card-body">
                        <p><strong>Calificación:</strong> ⭐ ${r.calificacion}/5</p>
                        <p>${r.comentario}</p>
                        <small>Por Usuario #${r.id_usuario} el ${new Date(r.fecha_resena).toLocaleDateString()}</small>
                    </div>
                </div>
            `).join('');
        } catch (error) {
            console.error("Error", error);
        }
    }

    if (formResena) {
        formResena.addEventListener('submit', async (e) => {
            e.preventDefault();
            const calificacion = parseInt(document.getElementById('calificacion').value);
            const comentario = document.getElementById('comentario').value;

            try {
                await apiFetch(`/videojuegos/${idJuego}/resenas`, {
                    method: 'POST',
                    body: JSON.stringify({ calificacion, comentario })
                });
                mostrarMensaje('msgResena', 'Reseña enviada correctamente.');
                cargarDetalle();
                formResena.reset();
            } catch (error) {
                mostrarMensaje('msgResena', error.message, true);
            }
        });
    }

    cargarDetalle();
}
