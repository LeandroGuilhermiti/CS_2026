# Função de Verificação de Números Primos em Python

## 📌 Introdução

Um **número primo** é um número natural maior que 1 que tem exatamente dois divisores distintos: 1 e ele mesmo. 

Exemplos de números primos: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31...

## 🎯 Objetivo da Função

A função `eh_primo(numero)` verifica se um número inteiro fornecido é primo ou não, retornando `True` se for primo e `False` caso contrário.

## 💡 Conceitos Fundamentais

### Características dos Números Primos:
- **2 é o único número primo par** - todos os outros números pares são divisíveis por 2
- **Números menores que 2 não são primos** - 0, 1 e números negativos não são considerados primos
- **Para verificar divisibilidade** - só precisamos testar até a raiz quadrada do número

### Por que até a raiz quadrada?

Se um número `n` tem um divisor maior que sua raiz quadrada, ele também terá um divisor menor que sua raiz quadrada. Por exemplo:
- Para verificar se 25 é primo: √25 = 5, então só testamos divisores até 5
- Se testássemos 10, já teríamos encontrado 2 e 5 antes

## 🔧 Implementação da Função

```python
def eh_primo(numero):
    """
    Verifica se um número é primo.
    
    Args:
        numero: Um número inteiro a ser verificado
        
    Returns:
        bool: True se o número é primo, False caso contrário
    """
    # Números menores que 2 não são primos
    if numero < 2:
        return False
    
    # 2 e 3 são primos
    if numero in (2, 3):
        return True
    
    # Eliminando múltiplos de 2 e 3 rapidamente
    if numero % 2 == 0 or numero % 3 == 0:
        return False
    
    # Usa a forma 6k ± 1 para reduzir os testes de divisibilidade
    i = 5
    while i * i <= numero:
        if numero % i == 0 or numero % (i + 2) == 0:
            return False
        i += 6
    
    return True
```

## 📊 Explicação Passo a Passo

### 1. Verificação de números menores que 2
```python
if numero < 2:
    return False
```
- Números menores que 2 (negativos, 0 e 1) não são primos por definição

### 2. Verificação especial para 2 e 3
```python
if numero in (2, 3):
    return True
```
- 2 e 3 são os primeiros números primos

### 3. Eliminação de múltiplos de 2 e 3
```python
if numero % 2 == 0 or numero % 3 == 0:
    return False
```
- Qualquer número par maior que 2 é divisível por 2
- Qualquer número divisível por 3 (exceto 3 mesmo) não é primo

### 4. Otimização com a forma 6k ± 1
```python
i = 5
while i * i <= numero:
    if numero % i == 0 or numero % (i + 2) == 0:
        return False
    i += 6
```
- **Princípio importante**: Todo número primo maior que 3 pode ser escrito na forma `6k + 1` ou `6k - 1` (equivalente a `6k + 5`)
- Começamos em `i = 5` (que é 6×1 - 1)
- Testamos `i` (6k - 1) e `i + 2` (6k + 1)
- Incrementamos `i` de 6 em 6
- Continuamos enquanto `i * i <= numero`

**Sequência de verificações**: 5, 7, 11, 13, 17, 19, 23, 25, 29, 31...

## ⚡ Otimizações Aplicadas

| Aspecto | Benefício |
|---------|-----------|
| **Raiz quadrada** | Reduz testes de O(n) para O(√n) |
| **Poda de pares** | Elimina 50% dos candidatos imediatamente |
| **Poda de múltiplos de 3** | Elimina mais 33% dos candidatos |
| **Forma 6k ± 1** | Reduz testes em ~66% comparado ao método de testar todos ímpares |

## 📈 Complexidade

- **Tempo**: O(√n) - verifica até a raiz quadrada do número
- **Espaço**: O(1) - usa apenas variáveis constantes

## 🧪 Casos de Teste

| Número | Resultado | Razão |
|--------|-----------|-------|
| -5 | False | Números negativos não são primos |
| 0 | False | Zero não é primo |
| 1 | False | Um não é primo |
| 2 | **True** | 2 é primo (único par primo) |
| 3 | **True** | 3 é primo |
| 4 | False | 4 = 2 × 2 |
| 5 | **True** | 5 é primo |
| 97 | **True** | 97 é primo |
| 100 | False | 100 = 2 × 50 |
| 101 | **True** | 101 é primo |

## 🚀 Exemplos de Uso

```python
# Verificando números individuais
print(eh_primo(7))      # True
print(eh_primo(10))     # False
print(eh_primo(23))     # True

# Em um loop
for n in range(1, 20):
    if eh_primo(n):
        print(f"{n} é primo")
```

## 📝 Notas Importantes

1. A função funciona com números inteiros positivos e negativos
2. A otimização com 6k ± 1 é especialmente eficiente para números grandes
3. Para números muito grandes (> 10^12), existem algoritmos ainda mais eficientes como Miller-Rabin
4. A função é determinística e sempre retorna o mesmo resultado para o mesmo número

## 🔍 Referências Teóricas

- **Crivo de Eratóstenes**: Método para encontrar todos os primos até um número n
- **Teste de Primalidade**: Determinação se um número é primo
- **Teorema Fundamental da Aritmética**: Todo inteiro maior que 1 é único na fatoração em primos
- **Densidade de Primos**: A quantidade de números primos diminui conforme os números crescem
