$(document).ready(function () {
    // Função para carregar veículos baseado no emitente selecionado
    function carregarVeiculos() {
        var emitenteId = $('#id_emitente').val();
        if (emitenteId) {
            // Carregar veículos com situação=ESTOQUE
            $.ajax({
                url: ajaxLoadVeiculosUrl,
                data: {
                    'emitente': emitenteId,
                    'situacao': 'ESTOQUE',
                    'veiculo_atual': veiculoAtualId  // Usar a variável definida no template
                },
                success: function (data) {
                    console.log('Dados de veículos recebidos:', JSON.stringify(data, null, 2));
                    if (Array.isArray(data) && data.length > 0) {
                        var options = '<option value="">Selecione um veículo</option>';
                        data.forEach(function (veiculo) {
                            options += '<option value="' + veiculo.id + '">' + veiculo.descricao + '</option>';
                        });
                        $('#id_veiculo').html(options);
                        
                        // Restaurar o veículo selecionado se estiver editando
                        if (veiculoAtualId) {
                            $('#id_veiculo').val(veiculoAtualId);
                        }
                    } else {
                        console.log('Nenhum veículo em estoque encontrado');
                        $('#id_veiculo').html('<option value="">Nenhum veículo em estoque disponível</option>');
                    }
                },
                error: function (jqXHR, textStatus, errorThrown) {
                    console.error('Erro ao carregar veículos:', textStatus, errorThrown);
                    $('#id_veiculo').html('<option value="">Erro ao carregar veículos</option>');
                }
            });
        } else {
            // Resetar o campo de veículos se nenhum emitente for selecionado
            $('#id_veiculo').html('<option value="">Selecione um veículo</option>');
        }
    }

    // Carregar veículos quando o emitente mudar
    $('#id_emitente').change(carregarVeiculos);
    
    // Carregar veículos na inicialização se um emitente já estiver selecionado
    if ($('#id_emitente').val()) {
        carregarVeiculos();
    }
});