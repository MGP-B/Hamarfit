document.addEventListener('DOMContentLoaded',() =>{

    const radio_pro = document.getElementById('radio-plan-pro');
    const radio_basico = document.getElementById('radio-plan-basico');
    const precio = document.getElementById('mensualidad-precio');
    
    const contenedor_pro = document.getElementById('contenedor-plan-pro');
    const contenedor_basico = document.getElementById('contenedor-plan-basico');

    const nombre_plan = document.getElementById('nombre-plan');

    radio_pro.addEventListener('focus',()=>{
        // Cambiar el precio
        precio.innerHTML = '1500.0 $';

        // Cambios para el contenedor del plan pro
        contenedor_pro.style.boxShadow = '0 0 8px .5px #ffa500';
        contenedor_pro.style.transform = 'scale(1.03)';

        // Cambios para el contenedor del plan básico
        contenedor_basico.style.transform = 'scale(1)';
        contenedor_basico.style.boxShadow = '0 0 8px .5px rgba(0,0,0,.3)';

        // Cambios al nombre del plan
        nombre_plan.innerHTML = 'Pro';
        nombre_plan.style.color = '#ffa500';
    })
    
    radio_basico.addEventListener('focus',()=>{
        // Cambiar el precio
        precio.innerHTML = '1100.0 $';

        // Cambios para el contenedor del plan pro
        contenedor_pro.style.boxShadow = '0 0 8px .5px rgba(0,0,0,.3)';
        contenedor_pro.style.transform = 'scale(1)';

        
        // Cambios para el contenedor del plan básico
        contenedor_basico.style.boxShadow = '0 0 8px .5px #ffa500';
        contenedor_basico.style.transform = 'scale(1.03)';

        // Cambios al nombre del plan
        nombre_plan.innerHTML = 'Básico';
        nombre_plan.style.color = '#626262';
    })
})