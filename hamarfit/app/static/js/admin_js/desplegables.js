// Crear una constante que llame al contenedor del pop up
const contenedor_popup = document.getElementById('contenedor_popup')

// Crear la función para agregar los pop ups
function agregar_popup(ruta){
    // Buscar en la ruta especificada
    fetch(ruta)    
    // Luego
    .then(respuesta =>{
        // Retornar la respuesta en texto
        return respuesta.text();
    })
    // Luego
    .then(contenido =>{
        // Agregar el contenido de la respuesta al contenedor del pop up
        contenedor_popup.innerHTML = contenido;
        contenedor_popup.style.display = 'flex';
    })
    // En caso de error atrapa...
    .catch(error =>{
        // Agregar el mensaje de error al contenedor del pop up
        contenedor_popup.innerHTML = 'Error => '+ error + ', Qué hiciste? ya se dañó';
    })

    // Condicional para cerrar el desplegable en caso de haber uno
    if (desplegable.style.display == 'block'){
        desplegable.style.display = 'none';
    }

    // Condicional para hacer visible el contenedor en caso de que no lo sea
    if(contenedor_popup.style.display == 'none'){
        contenedor_popup.style.display = 'flex'
    }
};

// Obtener el elemento desplegable
// const desplegable = document.getElementById('desplegable');
// Hacerlo visible
function visible(id) {
    // Cierra todos los desplegables
    document.querySelectorAll('.desplegable').forEach(el => {
        el.style.display = 'none';
    });

    // Abre el desplegable correspondiente
    const desplegable = document.getElementById(`desplegable_${id}`);
    if (desplegable) {
        desplegable.style.display = 'block';
    } else {
        console.warn(`No se encontró el desplegable con ID: desplegable_${id}`);
    }
}


// Cerrar el pop up
function cerrar_popup(){
    contenedor_popup.style.display = 'none'
    contenedor_popup.innerHTML = ''
}

// Cerrar el desplegable
function cerrar_desplegable(id){
    const desplegable = document.getElementById(`desplegable_${id}`);
    if (desplegable) {
        desplegable.style.display = 'none';
    }
}

document.addEventListener('click', function(event, id) {
    // Verifica si el clic fue dentro de algún .div_acciones
    const isAcciones = event.target.closest('[id^="div_acciones_"]');
    
    // Si no fue dentro, cierra todos los desplegables
    if (!isAcciones) {
        document.querySelectorAll('.desplegable').forEach(el => {
            el.style.display = 'none';
        });
    }
});

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

// ✅ Función para confirmar la reasignación
function confirmarReasignacion(origenId) {
    const destinoSelect = document.getElementById('empleado_destino');
    if (!destinoSelect) {
        alert("No se encontró el selector de empleado destino.");
        return;
    }

    const destinoId = destinoSelect.value;

    console.log("Reasignando inscripciones de:", origenId, "a:", destinoId);

    fetch('/admin/configuracion/ejecutar_reasignacion/', {
        method: 'POST',
        headers: {
            'X-CSRFToken': getCookie('csrftoken'),
            'Content-Type': 'application/x-www-form-urlencoded'
        },
        body: `origen_id=${origenId}&destino_id=${destinoId}`
    })
    .then(res => {
        if (!res.ok) throw new Error("Error en la solicitud");
        return res.json();
    })
    .then(data => {
        console.log("Respuesta del servidor:", data);
        alert(data.message);
        if (data.success) {
            cerrar_popup();  // Esta función debe estar definida en otro archivo o aquí si lo prefieres
            location.reload();  // Refresca la vista para mostrar los cambios
        }
    })
    .catch(error => {
        console.error("Error al reasignar:", error);
        alert("Hubo un problema al intentar reasignar las inscripciones.");
    });
}