
// Crear un observador de cambios
const observador = new MutationObserver(() =>{
    // Llamar elementos del html
    const cuerpo_popup = document.getElementById('cuerpo_popup');

    const textarea = document.getElementById('notas-del-cliente');
    const contenido_textarea = textarea.textContent;

    const boton_agregar = document.getElementById('agregar-nota');
    const boton_guardar = document.getElementById('boton-guardar');
    const boton_cancelar = document.getElementById('boton-cancelar');
    
    // Verificar que el popup se agregó
    if(cuerpo_popup){
        console.log('Pop up agregado')
    }

    // Evento al botón de agregar_notas
    boton_agregar.addEventListener('click', ()=>{
        if(textarea.hasAttribute('disabled')){
            textarea.removeAttribute('disabled');
            

            boton_guardar.style.display = 'block';
            boton_cancelar.style.display = 'block';
        }else{
            alert('Ya se está agregando una nota');
        }
    })

    // Evento al botón de cancelar
    boton_cancelar.addEventListener('click',()=>{
        textarea.setAttribute('disabled', '');

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
