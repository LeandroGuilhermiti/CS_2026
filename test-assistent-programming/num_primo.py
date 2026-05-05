"""Fornece utilitários para verificação de números primos e testes."""


def eh_primo(numero):
    """Verifica se um número inteiro é primo.

    Args:
        numero (int): Número inteiro a ser verificado.

    Returns:
        bool: True se o número for primo, False caso contrário.
    """
    if numero < 2:
        return False

    if numero in (2, 3):
        return True

    if numero % 2 == 0 or numero % 3 == 0:
        return False

    i = 5
    while i * i <= numero:
        if numero % i == 0 or numero % (i + 2) == 0:
            return False
        i += 6

    return True


def testar_funcao():
    """Executa casos de teste para validar a função eh_primo.

    Returns:
        bool: True se todos os testes passarem, False caso contrário.
    """
    print("=" * 50)
    print("TESTANDO A FUNÇÃO eh_primo()")
    print("=" * 50)
    
    testes = [
        (0, False, "Zero não é primo"),
        (1, False, "Um não é primo"),
        (2, True, "Dois é primo"),
        (3, True, "Três é primo"),
        (4, False, "Quatro não é primo (par)"),
        (5, True, "Cinco é primo"),
        (10, False, "Dez não é primo (par)"),
        (11, True, "Onze é primo"),
        (17, True, "Dezessete é primo"),
        (20, False, "Vinte não é primo (par)"),
        (23, True, "Vinte e três é primo"),
        (97, True, "Noventa e sete é primo"),
        (100, False, "Cem não é primo"),
        (101, True, "Cento e um é primo"),
        (-5, False, "Números negativos não são primos"),
    ]
    
    testes_passados = 0
    testes_falhados = 0
    
    for numero, esperado, descricao in testes:
        resultado = eh_primo(numero)
        status = "✓ PASSOU" if resultado == esperado else "✗ FALHOU"
        
        if resultado == esperado:
            testes_passados += 1
        else:
            testes_falhados += 1
        
        print(f"{status} | eh_primo({numero}) = {resultado} | {descricao}")
    
    print("=" * 50)
    print(f"Resultado: {testes_passados} testes passaram, {testes_falhados} falharam")
    print("=" * 50)
    
    return testes_falhados == 0


if __name__ == "__main__":
    sucesso = testar_funcao()
    
    if sucesso:
        print("\n✓ Todos os testes passaram com sucesso!")
    else:
        print("\n✗ Alguns testes falharam!")
