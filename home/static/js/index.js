function goToHome() 
{
  window.addEventListener('load', function() {
    // Establece la cabecera "Cache-Control" para evitar el almacenamiento en caché
        window.addEventListener('pageshow', function(event) {
            if (event.persisted) {
                window.location.reload();
            } else {
                window.location.replace('/');
            }
        });
        // Realiza alguna lógica aquí...
        // Redirecciona a la página deseada
        window.location.replace('/');
    });
}

document.getElementById('home').addEventListener('click', goToHome);