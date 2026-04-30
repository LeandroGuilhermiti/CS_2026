# Exemplo de Erro de Sintaxe em Python

## Código com erro

```python
def calcular_media(valores):
    if not valores:
        return 0
    soma = sum(valores)
    return soma / len(valores)


def validar_idade(idade):
    if idade < 0:
        raise ValueError("Idade não pode ser negativa")
    elif idade >= 18
        return True
    else:
        return False


def exibir_resultado(nome, valores, idade):
    media = calcular_media(valores)
    maioridade = validar_idade(idade)
    status = "maior de idade" if maioridade else "menor de idade"
    print(f"{nome}: média={media:.2f}, {status}")


if __name__ == "__main__":
    nome = "Maria"
    valores = [7.5, 8.0, 9.2]
    idade = 17
    exibir_resultado(nome, valores, idade)
```

## Erro identificado

- Tipo: `SyntaxError`
- Mensagem esperada: `SyntaxError: invalid syntax`
- Linha problemática: `elif idade >= 18`

## Causa do erro

O erro ocorre porque a linha do `elif` não termina com dois-pontos (`:`). Em Python, blocos condicionais (`if`, `elif`, `else`) e definições de função exigem `:` no final do cabeçalho para delimitar o início do bloco indentado.

## Melhoria proposta

Adicione os dois-pontos no final do cabeçalho do `elif`:

```python
def validar_idade(idade):
    if idade < 0:
        raise ValueError("Idade não pode ser negativa")
    elif idade >= 18:
        return True
    else:
        return False
```

## Por que essa melhoria resolve?

- Em Python, o `:` indica que a próxima linha indentada pertence ao bloco `elif`.
- Sem o `:`, o interpretador não pode reconhecer onde começa o bloco de código associado à condição.
- Essa correção mantém a estrutura condicional válida e permite que o programa seja executado corretamente.

## Observação

Erros de sintaxe podem aparecer em blocos maiores de código, mas sempre são causados por regras básicas de gramática da linguagem, como a falta de `:`, parênteses não fechados, ou indentação incorreta. Revisar o cabeçalho de cada bloco geralmente resolve o problema rapidamente.
