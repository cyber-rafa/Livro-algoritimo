# Algoritmos de Ordenação

Este repositório contém implementações do algoritmo de ordenação por seleção em Python.

## O que é Ordenação por Seleção?

A ordenação por seleção é um algoritmo que ordena uma lista encontrando o menor elemento e colocando-o na posição correta, um por um.

## Visualização com Animações

Para visualizar como o algoritmo funciona, você pode usar este código simples:

```python:d%3A%5CGithub%5CLivro-algoritimo%5Cvisualizar_ordenacao.py
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Dados para ordenar
numeros = [5, 3, 6, 2, 10]

# Função de ordenação que registra os passos
def ordenacao_com_passos(arr):
    arr = arr.copy()  # Não modificar o original
    passos = [arr.copy()]  # Registra estado inicial
    
    for i in range(len(arr)):
        # Encontrar o menor elemento
        indice_menor = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[indice_menor]:
                indice_menor = j
        
        # Trocar elementos
        arr[i], arr[indice_menor] = arr[indice_menor], arr[i]
        
        # Registrar este passo
        passos.append(arr.copy())
    
    return passos

# Gerar os passos da ordenação
passos = ordenacao_com_passos(numeros)

# Configurar a figura
fig, ax = plt.subplots(figsize=(8, 5))

# Função para atualizar a animação
def update(frame):
    ax.clear()
    ax.set_title(f'Ordenação por Seleção - Passo {frame}')
    ax.set_ylim(0, max(numeros) + 2)
    
    # Colorir as barras
    cores = ['skyblue'] * len(passos[frame])
    for i in range(frame):
        cores[i] = 'lightgreen'  # Elementos já ordenados
    
    if frame > 0 and frame < len(passos) - 1:
        cores[frame] = 'red'  # Elemento sendo posicionado
    
    ax.bar(range(len(passos[frame])), passos[frame], color=cores)
    
    # Adicionar valores acima das barras
    for i, valor in enumerate(passos[frame]):
        ax.text(i, valor + 0.3, str(valor), ha='center')
    
    return ax

# Criar a animação
ani = animation.FuncAnimation(fig, update, frames=len(passos), 
                             interval=1000, repeat=True)

# Salvar como GIF
ani.save('ordenacao_animada.gif', writer='pillow', fps=1)

# Mostrar a animação
plt.tight_layout()
plt.show()