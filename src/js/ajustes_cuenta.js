// Evento que se va a ejecutar cuando el documento esté completamente cargado
document.addEventListener('DOMContentLoaded',()=>{
    const cambio_contrasena = document.getElementById('cambio_contrasena');
    const cambio_correo = document.getElementById('cambio_correo');
    const cambio_telefono = document.getElementById('cambio_telefono');


    const boton_contrasena = document.getElementById('boton_contrasena');
    const boton_correo = document.getElementById('boton_correo');
    const boton_telefono = document.getElementById('boton_telefono');


    const input_contrasena = document.getElementById('input_contrasena');
    const input_telefono = document.getElementById('input_telefono');
    const input_correo = document.getElementById('input_correo');
    const input_confirmar_contrasena = document.getElementById('confirmar-contrasena');

    boton_contrasena.addEventListener('click',()=>{
        cambio_contrasena.style.display = 'inline-flex';

        if (cambio_correo.style.display === 'inline-flex' || cambio_telefono.style.display === 'inline-flex'){
            cambio_correo.style.display = 'none';
            cambio_telefono.style.display = 'none'; 

            input_correo.value = '';
            input_telefono.value = '';
        }else{
            console.log('Los otros contenedores ya tienen display none')
        }
    })

    boton_correo.addEventListener('click',()=>{
        cambio_correo.style.display = 'inline-flex';

        if (cambio_contrasena.style.display === 'inline-flex' || cambio_telefono.style.display === 'inline-flex'){
            cambio_contrasena.style.display = 'none';
            cambio_telefono.style.display = 'none'; 

            input_telefono.value = '';
            input_confirmar_contrasena.value = '';
            input_contrasena.value = '';
        }else{
            console.log('Los otros contenedores ya tienen display none')
        }
    })

    boton_telefono.addEventListener('click',()=>{
        cambio_telefono.style.display = 'inline-flex';

        if (cambio_correo.style.display === 'inline-flex' || cambio_contrasena.style.display === 'inline-flex'){
            cambio_correo.style.display = 'none';
            cambio_contrasena.style.display = 'none'; 

            input_correo.value = '';
            input_confirmar_contrasena.value = '';
            input_contrasena.value = '';
        }else{
            console.log('Los otros contenedores ya tienen display none')
        }
    })
})