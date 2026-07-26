const API_URL = "/productos/";
const form = document.getElementById("producto-form");
const productoIdInput = document.getElementById("producto-id");
const nombreInput = document.getElementById("nombre");
const precioInput = document.getElementById("precio");
const cantidadInput = document.getElementById("cantidad");
const descripcionInput = document.getElementById("descripcion");
const listaProductos = document.getElementById("lista-productos");
const mensajeEstado = document.getElementById("mensaje-estado");

function mostrarMensaje(texto, tipo = "success") {
  mensajeEstado.innerHTML = `<div class="alert alert-${tipo} alert-dismissible fade show" role="alert">
    ${texto}
    <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
  </div>`;
}

function limpiarFormulario() {
  productoIdInput.value = "";
  nombreInput.value = "";
  precioInput.value = "";
  cantidadInput.value = "";
  descripcionInput.value = "";
  document.getElementById("form-title").textContent = "Añadir Producto";
}

function parsePrecio(value) {
  const normalized = value.toString().trim().replace(",", ".");
  return parseFloat(normalized);
}

async function cargarProductos() {
  try {
    const response = await fetch(API_URL);
    if (!response.ok) throw new Error("No se pudo cargar la lista de productos.");
    const productos = await response.json();
    listaProductos.innerHTML = productos
      .map(
        (producto) => `
          <tr>
            <td>${producto.nombre}</td>
            <td>${producto.precio.toFixed(2)}</td>
            <td>${producto.cantidad}</td>
            <td>${producto.descripcion}</td>
            <td>
              <button class="btn btn-sm btn-warning me-1" onclick="editarProducto(${producto.id})">Editar</button>
              <button class="btn btn-sm btn-danger" onclick="eliminarProducto(${producto.id})">Eliminar</button>
            </td>
          </tr>
        `
      )
      .join("");
  } catch (error) {
    mostrarMensaje(error.message, "danger");
  }
}

async function guardarProducto(event) {
  event.preventDefault();
  const nombre = nombreInput.value.trim();
  const precio = parsePrecio(precioInput.value);
  const cantidad = Number(cantidadInput.value);
  const descripcion = descripcionInput.value.trim();

  if (!nombre || Number.isNaN(precio) || Number.isNaN(cantidad) || !descripcion) {
    mostrarMensaje("Completa todos los campos correctamente.", "warning");
    return;
  }

  const producto = { nombre, precio, cantidad, descripcion };
  const id = productoIdInput.value;

  try {
    const method = id ? "PUT" : "POST";
    const url = id ? `${API_URL}${id}` : API_URL;
    const response = await fetch(url, {
      method,
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(producto),
    });

    if (!response.ok) {
      throw new Error("Error al guardar el producto.");
    }

    mostrarMensaje(id ? "Producto actualizado con éxito." : "Producto guardado con éxito.");
    limpiarFormulario();
    cargarProductos();
  } catch (error) {
    mostrarMensaje(error.message, "danger");
  }
}

async function editarProducto(id) {
  try {
    const response = await fetch(`${API_URL}${id}`);
    if (!response.ok) throw new Error("No se pudo cargar el producto.");
    const producto = await response.json();
    productoIdInput.value = producto.id;
    nombreInput.value = producto.nombre;
    precioInput.value = producto.precio.toString().replace(".", ",");
    cantidadInput.value = producto.cantidad;
    descripcionInput.value = producto.descripcion;
    document.getElementById("from-title").textContent = "Editar Producto";
  } catch (error) {
    mostrarMensaje(error.message, "danger");
  }
}

async function eliminarProducto(id) {
  if (!confirm("¿Estás seguro de eliminar este producto?")) return;

  try {
    const response = await fetch(`${API_URL}${id}`, { method: "DELETE" });
    if (!response.ok) throw new Error("No se pudo eliminar el producto.");
    mostrarMensaje("Producto eliminado correctamente.");
    cargarProductos();
  } catch (error) {
    mostrarMensaje(error.message, "danger");
  }
}

function cancelarEdicion() {
  limpiarFormulario();
}

form.addEventListener("submit", guardarProducto);
window.addEventListener("load", cargarProductos);
window.editarProducto = editarProducto;
window.eliminarProducto = eliminarProducto;
window.cancelarEdicion = cancelarEdicion;
