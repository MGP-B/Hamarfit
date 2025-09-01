
// Crear un observador de cambios
const observador = new MutationObserver(() =>{
    // Llamar elementos del html
    const cuerpo_popup = document.getElementById('cuerpo_popup');

    const input = document.getElementById('notas-del-cliente');

    const boton_agregar = document.getElementById('agregar-nota');
    const boton_guardar = document.getElementById('boton-guardar');
    const boton_cancelar = document.getElementById('boton-cancelar');
    const botones = document.getElementById('botones')
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

        boton_agregar.style.display = 'block';

        botones.style.display = 'none';
        boton_guardar.style.display = 'none';
        boton_cancelar.style.display = 'none';
    })
})
// Poner el observador a mirar dentro del contenedor-popup
observador.observe(contenedor_popup, {childList: true, subtree: true});
console.log('Archivo abierto');