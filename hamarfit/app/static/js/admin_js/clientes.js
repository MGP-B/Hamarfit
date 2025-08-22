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
            const texto = textarea.value;
            textarea.removeAttribute('disabled');
            if (texto.include('Este cliente no tiene ninguna nota...')){
                textarea.value = ''
            }


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