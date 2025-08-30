document.addEventListener('DOMContentLoaded', function() {
    let mensajeError = document.getElementById('mensaje_error');
    if (mensajeError) {
        alert(mensajeError.textContent);
    }
});