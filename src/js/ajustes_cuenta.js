// Evento que se va a ejecutar cuando el documento esté completamente cargado
document.addEventListener('DOMContentLoaded',()=>{
    // Obtener los contenedores
    const cambio_contrasena = document.getElementById('cambio_contrasena');
    const cambio_correo = document.getElementById('cambio_correo');
    const cambio_telefono = document.getElementById('cambio_telefono');

    // Obtener los botones
    const boton_contrasena = document.getElementById('boton_contrasena');
    const boton_correo = document.getElementById('boton_correo');
    const boton_telefono = document.getElementById('boton_telefono');

    // Obtener los input
    const input_contrasena = document.getElementById('input_contrasena');
    const input_telefono = document.getElementById('input_telefono');
    const input_correo = document.getElementById('input_correo');
    const input_confirmar_contrasena = document.getElementById('confirmar-contrasena');

    // Evento al botón de contraseña
    boton_contrasena.addEventListener('click',()=>{
        if(cambio_contrasena.style.display === 'none'){
            cambio_contrasena.style.display = 'inline-flex';
            input_contrasena.focus()
        }else{
            cambio_contrasena.style.display = 'none';
        }

        if (cambio_correo.style.display === 'inline-flex' || cambio_telefono.style.display === 'inline-flex'){
            cambio_correo.style.display = 'none';
            cambio_telefono.style.display = 'none'; 

            input_correo.value = '';
            input_telefono.value = '';
        }
    })

    // Evento al botón del correo
    boton_correo.addEventListener('click',()=>{
        
        if(cambio_correo.style.display === 'none'){
            cambio_correo.style.display = 'inline-flex';
            input_correo.focus()
        }else{
            cambio_correo.style.display = 'none';
        }

        if (cambio_contrasena.style.display === 'inline-flex' || cambio_telefono.style.display === 'inline-flex'){
            cambio_contrasena.style.display = 'none';
            cambio_telefono.style.display = 'none'; 

            input_telefono.value = '';
            input_confirmar_contrasena.value = '';
            input_contrasena.value = '';
        }
    })

    // Evento al botón de telefono
    boton_telefono.addEventListener('click',()=>{

        if(cambio_telefono.style.display === 'none'){
            cambio_telefono.style.display = 'inline-flex';
            input_telefono.focus()
        }else{
            cambio_telefono.style.display = 'none'; 
        }

        if (cambio_correo.style.display === 'inline-flex' || cambio_contrasena.style.display === 'inline-flex'){
            cambio_correo.style.display = 'none';
            cambio_contrasena.style.display = 'none'; 

            input_correo.value = '';
            input_confirmar_contrasena.value = '';
            input_contrasena.value = '';
        }
    })
})