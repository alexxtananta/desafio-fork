from collections import Counter

# Função para calcular a média

def calcular_media(lista):
    if not lista:
        return 0
    soma = sum(lista)
    tamanho = len(lista)
    media = soma / tamanho
    return media

# Função para calcular a mediana

def calcular_mediana(lista):
    lista_ordenada = sorted(lista)
    tamanho = len(lista_ordenada)

    if tamanho == 0:
        return 0
    
    meio = tamanho // 2

    if tamanho % 2 != 0:
        mediana = lista_ordenada[meio]
    else:
        elemento1 = lista_ordenada[meio - 1]
        elemento2 = lista_ordenada[meio]
        mediana = (elemento1 + elemento2) / 2
        
    return mediana

# Função para calcular a moda

def calcular_moda(lista):
    if not lista:
        return []

    contagem = Counter(lista)
    
    frequencia_maxima = max(contagem.values())
    
    moda = [num for num, frequencia in contagem.items() if frequencia == frequencia_maxima]
    
    return moda

def main():
    try:
        numeros_a = [10, 20, 20, 30, 40, 40, 40, 50]
        print("--- Exemplo 1 (Moda: [40]) ---")
        print(f"Lista de números: {numeros_a}")
        print(f"Média: {calcular_media(numeros_a):.2f}")
        print(f"Mediana: {calcular_mediana(numeros_a):.2f}")
        print(f"Moda: {calcular_moda(numeros_a)}")
        print("-" * 30)

        numeros_b = [10, 20, 20, 30, 40, 40, 50, 60]
        print("--- Exemplo 2 (Modas: [20, 40]) ---")
        print(f"Lista de números: {numeros_b}")
        print(f"Média: {calcular_media(numeros_b):.2f}")
        print(f"Mediana: {calcular_mediana(numeros_b):.2f}")
        print(f"Moda: {calcular_moda(numeros_b)}")
        print("-" * 30)

    except Exception as e:
        print(f"⚠️ Ocorreu um erro: {e}")

if __name__ == "__main__":
    main()