document.addEventListener('DOMContentLoaded', () => {
    const btnCancelar = document.getElementById('cancelar-membresia');
    const modal = document.getElementById('modal-cancelar');
    const confirmar = document.getElementById('confirmar-cancelacion');
    const cerrar = document.getElementById('cerrar-modal');
    const estado = document.getElementById('estado');

    btnCancelar.addEventListener('click', () => {
        modal.style.display = 'flex';
    });

    cerrar.addEventListener('click', () => {
        modal.style.display = 'none';
    });

    confirmar.addEventListener('click', () => {
        const url = btnCancelar.dataset.url;

        fetch(url, {
            method: 'POST',
            headers: {
                'X-CSRFToken': getCSRFToken(),
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ accion: 'cancelar' })
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                estado.textContent = data.nuevo_estado;
                estado.classList.remove('estado-activo');
                estado.classList.add('estado-inactivo');
                // btnCancelar.disabled = true;
                btnCancelar.style.display = 'none';
                modal.style.display = 'none';
            } else {
                alert('Error: ' + data.error);
            }
        })
        .catch(error => {
            console.error('Error en la solicitud:', error);
            alert('Hubo un problema al cancelar la membresía.');
        });
    });
});

function getCSRFToken() {
    return document.getElementById('csrf-token').value;
}