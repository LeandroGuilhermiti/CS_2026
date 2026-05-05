def calcular_media(valores: list[float]) -> float:
    """Calcula a média de uma lista de números.

    Args:
        valores (list[float]): Lista de valores numéricos.

    Returns:
        float: Média dos valores ou 0.0 se a lista estiver vazia.
    """
    if not valores:
        return 0.0
    return sum(valores) / len(valores)


def validar_idade(idade: int) -> bool:
    """Verifica se a idade representa maioridade.

    Args:
        idade (int): Idade a ser validada.

    Returns:
        bool: True se a idade for maior ou igual a 18, False caso contrário.

    Raises:
        ValueError: Se a idade for negativa.
    """
    if idade < 0:
        raise ValueError("Idade não pode ser negativa")
    return idade >= 18


def exibir_resultado(nome: str, valores: list[float], idade: int) -> None:
    """Exibe o resultado formatado com a média e o status de maioridade.

    Args:
        nome (str): Nome da pessoa.
        valores (list[float]): Lista de valores numéricos.
        idade (int): Idade da pessoa.
    """
    media = calcular_media(valores)
    maioridade = validar_idade(idade)
    status = "maior de idade" if maioridade else "menor de idade"
    print(f"{nome}: média={media:.2f}, {status}")


def converter_valores(valores: list[str]) -> list[float]:
    """Converte uma lista de strings para uma lista de floats.

    Args:
        valores (list[str]): Lista de valores numéricos em formato de string.

    Returns:
        list[float]: Lista convertida para floats.
    """
    return [float(valor) for valor in valores]


def main() -> None:
    """Executa o fluxo principal do programa com valores de exemplo."""
    nome = "Maria"
    valores = converter_valores(["7.5", "8.0", "9.2"])
    idade = 17
    exibir_resultado(nome, valores, idade)


if __name__ == "__main__":
    main()
