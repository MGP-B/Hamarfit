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
    .then(contenido=>{
        // Agregar el contenido de la respuesta al contenedor del pop up
        contenedor_popup.innerHTML = contenido;
    })
    // En caso de error atrapa...
    .catch(error=>{
        // Agregar el mensaje de error al contenedor del pop up
        contenedor_popup.innerHTML = 'Error => '+ error + 'Qué hiciste? ya se dañó';
    })
};