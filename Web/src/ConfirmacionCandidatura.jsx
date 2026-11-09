
/* Importamos useState de React para guardar y actualizar datos */
import { useState } from "react";

/* Creamos el componente que mostrará la confirmación de candidatura */
function ConfirmacionCandidatura() {

    // Guardamos si se ha completado la candidatura
    // Al principio es false porque todavía no se ha enviado
    const [enviado, setEnviado] = useState(false);

    // Guardamos el nombre del candidato para mostrarlo después
    const [nombre, setNombre] = useState("");

    // Función que se ejecuta cuando pulsamos el botón de enviar
    function enviarCandidatura() {

        // Buscamos el formulario mediante su ID
        const formulario = document.getElementById("formulario-candidatura");

        // Comprobamos que todos los campos obligatorios estén completos
        // Si falta algún dato, el navegador nos avisa
        if (formulario.reportValidity()) {

            // Recogemos el nombre que ha escrito el candidato
            let nombreUsuario = document.getElementById("nombre").value;

            // Guardamos el nombre utilizando useState
            setNombre(nombreUsuario);

            // Cambiamos enviado a true para mostrar la confirmación
            setEnviado(true);
        }
    }

    // Devolvemos los elementos que se mostrarán en la página
    return (
        <div>
            {/* Creamos el botón para enviar la candidatura */}
            {/* onClick ejecuta nuestra función al pulsar el botón */}
            {/* className aplica los estilos CSS que ya teníamos */}
            <button type="button" className="boton-enviar" onClick={enviarCandidatura}>
                Enviar candidatura
            </button>

            {/* Mostramos el mensaje solamente cuando enviado es true */}
            {enviado && (
                <div className="confirmacion">

                    {/* Mostramos el nombre que hemos guardado */}
                    <h3>¡Gracias, {nombre}!</h3>

                    {/* Mensaje de confirmación */}
                    <p>Tu candidatura se ha enviado correctamente.</p>

                    {/* Aclaramos que todavía no existe un envío real */}
                    <p>Esta es una simulación, no se han enviado los datos realmente.</p>
                </div>
            )}
        </div>
    );
}

/* Exportamos el componente para poder utilizarlo en main.jsx */
export default ConfirmacionCandidatura;

