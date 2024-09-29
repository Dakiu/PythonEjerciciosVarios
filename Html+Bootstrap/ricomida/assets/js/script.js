$(document).ready(function (){

    $('#enviarCorreo').click(function () {
        alert("El correo fue enviado con éxito")
    })
    $('#receta').on("dblclick", "h3", (function(){
        $(this).css({
            "color":"red"
        });
    })
    )
    $('.card-title').click(function(){
        $('#recetasRelacionadas img, #recetasRelacionadas p').toggle('hide')
    })


 var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
 var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
 return new bootstrap.Tooltip(tooltipTriggerEl)
 })

})