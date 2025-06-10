const boton_abrir = document.getElementById('nuevo_usuario');
const popup = document.getElementById('cuerpo_popup')
const cuerpo = document.getElementById('cuerpo')

boton_abrir.addEventListener('click', async ()=>{
    const respuesta = (await fetch('/html/admin/desplegables/configuracion/nuevo_usuario.html')).json;
    const contenido = respuesta.toString();
    
    const contenedor = document.createElement('div');
    contenedor.style.padding='100px';
    contenedor.style.backgroundColor='red';

    alert('respuesta: '+contenido)
})
