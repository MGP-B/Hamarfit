document.addEventListener('DOMContentLoaded',() =>{
    const radio_pro = document.getElementById('radio-plan-pro');
    const radio_basico = document.getElementById('radio-plan-basico');
    const precio = document.getElementById('mensualidad-precio');
    
    const contenedor_pro = document.getElementById('contenedor-plan-pro')
    const contenedor_basico = document.getElementById('contenedor-plan-basico')

    radio_pro.addEventListener('focus',()=>{
        precio.innerHTML = '1500.0 $';

        contenedor_pro.style.boxShadow = '0 0 8px .5px #ffa500';
        contenedor_pro.style.transform = 'scale(1.03)';
        contenedor_basico.style.transform = 'scale(1)';
        contenedor_basico.style.boxShadow = '0 0 8px .5px rgba(0,0,0,.3)';
    })
    
    radio_basico.addEventListener('focus',()=>{
        precio.innerHTML = '1100.0 $';

        contenedor_pro.style.boxShadow = '0 0 8px .5px rgba(0,0,0,.3)';
        contenedor_pro.style.transform = 'scale(1)';
        contenedor_basico.style.boxShadow = '0 0 8px .5px #ffa500';
        contenedor_basico.style.transform = 'scale(1.03)';
    })
})