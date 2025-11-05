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

pass
