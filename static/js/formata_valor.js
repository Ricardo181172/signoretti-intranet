$(document).ready(function(){
    $('.money-input').on('input', function(e) {
        let value = e.target.value.replace(/\D/g, '');
        value = (parseInt(value) / 100).toFixed(2);
        value = value.replace('.', ',');
        value = value.replace(/\B(?=(\d{3})+(?!\d))/g, ".");
        e.target.value = value;
    });

    // Formatação inicial para campos preenchidos
    $('.money-input').each(function() {
        let value = $(this).val();
        if (value) {
            value = parseFloat(value.replace(',', '.')).toFixed(2);
            value = value.replace('.', ',');
            value = value.replace(/\B(?=(\d{3})+(?!\d))/g, ".");
            $(this).val(value);
        }
    });

    // Antes de enviar o formulário, converta vírgulas para pontos
    $('form').on('submit', function() {
        $('.money-input').each(function() {
            let value = $(this).val();
            if (value) {
                value = value.replace(/\./g, '').replace(',', '.');
                $(this).val(value);
            }
        });
    });
});