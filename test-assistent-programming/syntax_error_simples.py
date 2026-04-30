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
