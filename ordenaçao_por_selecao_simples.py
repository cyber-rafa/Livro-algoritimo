def ordenacao_por_selecao(arr):
    
    lista = arr.copy()
    ordenada = []
    while lista:

        menor = min(lista)
        ordenada.append(menor)
        lista.remove(menor)
    
    return ordenada
print(ordenacao_por_selecao([5, 3, 6, 2, 10]))