document.addEventListener('DOMContentLoaded', function() {
    const estadoSelect = document.querySelector('select[name="uf"]');
    const cidadeSelect = document.querySelector('select[name="cidade"]');

    // Verificar se os selects foram encontrados
    if (!estadoSelect || !cidadeSelect) {
        console.error('Campos UF ou Cidade não encontrados');
        return;
    }

    // Log para verificar se o script está funcionando e os eventos estão registrados.
    console.log("Estado select encontrado:", estadoSelect);
    console.log("Cidade select encontrado:", cidadeSelect);

    estadoSelect.addEventListener('change', function() {
        const uf = this.value;
        console.log(`Busca iniciada para UF: ${uf}`);

        // Certifique-se de que a UF não está vazia antes de prosseguir
        if (!uf) {
            cidadeSelect.innerHTML = '<option value="">Selecione uma cidade</option>';
            return;
        }
        fetch(`/api/v1/emitentes/get-cidades/${uf}/`)
            .then(response => {
                console.log("Status da resposta:", response.status, response.statusText);
                if (!response.ok) {
                    throw new Error('Erro na resposta do servidor');
                }
                return response.json();
            })
            .then(data => {
                console.log('Dados recebidos:', data);
                cidadeSelect.innerHTML = '<option value="">Selecione uma cidade</option>';
                data.cidades.forEach(cidade => {
                    const option = document.createElement('option');
                    option.value = cidade.id;
                    option.textContent = cidade.municipio;
                    cidadeSelect.appendChild(option);
                });
            })
            .catch(error => console.error('Erro ao obter cidades:', error));
    });
});