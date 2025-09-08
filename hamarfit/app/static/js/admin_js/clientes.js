
// Crear un observador de cambios
const observador = new MutationObserver(() =>{
    // Llamar elementos del html
    const cuerpo_popup = document.getElementById('cuerpo_popup');

    const input = document.getElementById('notas-del-cliente');

    const boton_agregar = document.getElementById('agregar-nota');
    const boton_guardar = document.getElementById('boton-guardar');
    const boton_cancelar = document.getElementById('boton-cancelar');
    const botones = document.getElementById('botones')
    const selectEntrenador = document.getElementById('entrenador');
    const btnCambiar = document.getElementById('activar-cambio-entrenador');
    const btnGuardar = document.getElementById('guardar-cambio-entrenador');

    if (btnCambiar && selectEntrenador) {
        btnCambiar.addEventListener('click', () => {
            selectEntrenador.removeAttribute('disabled');
            btnCambiar.style.display = 'none';
            btnGuardar.style.display = 'inline-block';
        });
    }

    // Verificar que el popup se agregó
    if(cuerpo_popup){
        console.log('Pop up agregado')
    }

    // Evento al botón de agregar_notas
    boton_agregar.addEventListener('click', ()=>{
        if(input.hasAttribute('disabled')){
            input.removeAttribute('disabled');
            input.style.display = 'block';
            
            botones.style.display = 'flex';
            boton_agregar.style.display = 'none';
            boton_guardar.style.display = 'block';
            boton_cancelar.style.display = 'block';
        }else{
            alert('Ya se está agregando una nota');
        }
    })

    // Evento al botón de cancelar
    boton_cancelar.addEventListener('click',()=>{
        input.setAttribute('disabled', '');
        input.style.display = 'none';

        boton_agregar.style.display = 'flex';

        botones.style.display = 'none';
        boton_guardar.style.display = 'none';
        boton_cancelar.style.display = 'none';
    })
})
// Poner el observador a mirar dentro del contenedor-popup
observador.observe(contenedor_popup, {childList: true, subtree: true});
console.log('Archivo abierto');

function eliminarCliente(id) {
    if (!confirm("¿Estás seguro de que deseas eliminar este cliente? Esta acción no se puede deshacer.")) {
        return;
    }

    fetch(`/admin/clientes/eliminar_cliente/${id}/`, {
        method: 'POST',
        headers: {
            'X-CSRFToken': getCookie('csrftoken'),
            'Content-Type': 'application/json'
        }
    })
    .then(response => {
        if (response.ok) {
            return response.json();
        } else if (response.status === 403) {
            throw new Error("No tienes permiso para eliminar este cliente.");
        } else {
            throw new Error("Error al eliminar el cliente.");
        }
    })
    .then(data => {
        alert(data.message);
        // Eliminar la fila del cliente en la tabla
        const fila = document.getElementById(`div_acciones_${id}`).closest('tr');
        if (fila) fila.remove();
    })
    .catch(error => {
        alert(error.message);
    });
}

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let cookie of cookies) {
            cookie = cookie.trim();
            if (cookie.startsWith(name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

document.addEventListener('DOMContentLoaded', function () {
    const botonFiltro = document.querySelector('.boton-filtro');
    const panelFiltros = document.getElementById('panel-filtros');

    if (botonFiltro && panelFiltros) {
        botonFiltro.addEventListener('click', function (e) {
            e.preventDefault();
            panelFiltros.classList.toggle('oculto');
        });
    }
});