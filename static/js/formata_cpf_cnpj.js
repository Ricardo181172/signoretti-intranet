$(document).ready(function() {
    function aplicarMascara() {
        var tipoCliente = $('#id_tipo_cliente').val();
        var cpfCnpjField = $('#id_cpf_cnpj');

        // Inicializa novamente com entrada limpa
        cpfCnpjField.unmask();

        if (tipoCliente === 'JURIDICA') {
            // Aplica máscara de CNPJ
            cpfCnpjField.mask('00.000.000/0000-00', {reverse: true});
        } else if (tipoCliente === 'FISICA') {
            // Aplica máscara de CPF
            cpfCnpjField.mask('000.000.000-00', {reverse: true});
        }
    }

    // Aplica máscara na inicialização do documento
    aplicarMascara();

    // Atualiza máscara ao mudar o tipo de cliente
    $('#id_tipo_cliente').change(function() {
        aplicarMascara();
    });
});