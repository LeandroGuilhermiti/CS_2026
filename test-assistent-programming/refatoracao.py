def calcular_media(valores: list[float]) -> float:
    if not valores:
        return 0.0
    return sum(valores) / len(valores)


def validar_idade(idade: int) -> bool:
    if idade < 0:
        raise ValueError("Idade não pode ser negativa")
    return idade >= 18


def exibir_resultado(nome: str, valores: list[float], idade: int) -> None:
    media = calcular_media(valores)
    maioridade = validar_idade(idade)
    status = "maior de idade" if maioridade else "menor de idade"
    print(f"{nome}: média={media:.2f}, {status}")


def converter_valores(valores: list[str]) -> list[float]:
    return [float(valor) for valor in valores]


def main() -> None:
    nome = "Maria"
    valores = converter_valores(["7.5", "8.0", "9.2"])
    idade = 17
    exibir_resultado(nome, valores, idade)


if __name__ == "__main__":
    main()
