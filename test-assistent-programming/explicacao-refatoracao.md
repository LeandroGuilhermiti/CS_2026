Explicação do Código em refatoracao.py

Visão Geral
O código define funções para calcular a média de uma lista de números, validar a idade como maior ou menor de idade, converter uma lista de strings para floats e exibir o resultado formatado. Em seguida, demonstra o uso dessas funções com valores de exemplo e imprime a saída.

Detalhes da Função calcular_media(valores)
A função calcular_media recebe um parâmetro valores, que é esperado ser uma lista de números de ponto flutuante.

Cálculo da Média
Retorna 0.0 se a lista estiver vazia.
Caso contrário, calcula `sum(valores) / len(valores)` e retorna o resultado.

Detalhes da Função validar_idade(idade)
A função validar_idade recebe um parâmetro idade, esperado ser um número inteiro.

Validação da Idade
Se a idade for negativa, levanta `ValueError` com a mensagem "Idade não pode ser negativa".
Caso contrário, retorna `idade >= 18`.

Detalhes da Função exibir_resultado(nome, valores, idade)
A função exibir_resultado recebe nome, valores e idade.

Processo de Exibição
Chama `calcular_media(valores)` para obter a média.
Chama `validar_idade(idade)` para determinar se é maioridade.
Define `status` como "maior de idade" ou "menor de idade".
Imprime o nome, a média formatada com duas casas decimais e o status.

Detalhes da Função converter_valores(valores)
A função converter_valores recebe uma lista de strings e retorna uma nova lista de floats.

Conversão de Valores
Utiliza list comprehension para converter cada string `valor` em `float(valor)`.

Detalhes da Função main()
A função main define os valores de exemplo e orquestra a execução.

Código de Demonstração
Define `nome = "Maria"`.
Define `valores` chamando `converter_valores(["7.5", "8.0", "9.2"])`.
Define `idade = 17`.
Chama `exibir_resultado(nome, valores, idade)`.

Observações
O código trata a lista vazia em `calcular_media` retornando 0.0.
O nome das funções e parâmetros é descritivo, o que melhora a legibilidade.
A conversão de strings para floats está isolada em `converter_valores`, deixando o fluxo principal mais claro.
A função `main()` coleta os dados de exemplo e mantém a execução organizada.
