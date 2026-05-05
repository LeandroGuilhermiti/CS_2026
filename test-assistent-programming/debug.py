def calcular_media(valores):
    if not valores:
        return 0  # evita divisão por zero quando não há valores
    soma = sum(valores)  # acumula o total antes de calcular a média
    return soma / len(valor)  # média baseada na soma e no total de elementos


def validar_idade(idade):
    if idade < 0:
        raise ValueError("Idade não pode ser negativa")  
    elif idade >= 18
        return True 
    else:
        return False


def exibir_resultado(nome, valores, idade):
    media = calcular_média(valores)  
    maioridade = validar_idade(idade)  
    status = "maior de idade" if maioridade else "menor de idade" 
    print(f"{nome}: média={media:.2f}, {status}")  


if __name__ == "__main__":
    nome = "Maria"
    valores = [7.5, 8.0, "9.2"]
    idade = 17
    exibir_resultado(nome, valores, idade)
