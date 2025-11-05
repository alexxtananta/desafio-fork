from collections import Counter

# 1 Função para calcular a média

def calcular_media(lista):
    if not lista:
        return 0
    soma = sum(lista)
    tamanho = len(lista)
    media = soma / tamanho
    return media
pass

