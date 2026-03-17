def quicksort(arr, low, high, partition_func):
    if low < high:
        pi = partition_func(arr, low, high)
        quicksort(arr, low, pi - 1, partition_func)
        quicksort(arr, pi + 1, high, partition_func)
        
def part_um(arr, low, high):
    pivot = arr[low]
    i = low + 1

    for j in range(low + 1, high + 1):
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1

    arr[low], arr[i - 1] = arr[i - 1], arr[low]
    return i - 1        

import random

def part_dois(arr, low, high):
    # escolhe um pivô aleatório no intervalo
    pivot_index = random.randint(low, high)
    
    # move o pivô escolhido pro início
    arr[low], arr[pivot_index] = arr[pivot_index], arr[low]
    
    # usa a partição normal a partir daqui
    return part_um(arr, low, high)

def part_3(arr, low, high):
    mid = (low + high) // 2

    a = arr[low]
    b = arr[mid]
    c = arr[high]

    # descobrir a mediana
    if (a <= b <= c) or (c <= b <= a):
        median_index = mid
    elif (b <= a <= c) or (c <= a <= b):
        median_index = low
    else:
        median_index = high

    # coloca a mediana no início
    arr[low], arr[median_index] = arr[median_index], arr[low]

    return part_um(arr, low, high)

#Array decrescente
n = 10000
array_original = list(range(n, 0, -1))

import time
import sys

# Increase recursion limit to handle worst-case depth
sys.setrecursionlimit(n + 100)

# Primeiro pivô
arr1 = array_original.copy()
start = time.time()
quicksort(arr1, 0, len(arr1) - 1, part_um)
end = time.time()
print("Primeiro pivô:", end - start)

# Aleatório
arr2 = array_original.copy()
start = time.time()
quicksort(arr2, 0, len(arr2) - 1, part_dois)
end = time.time()
print("Pivô aleatório:", end - start)

# Mediana de três
arr3 = array_original.copy()
start = time.time()
quicksort(arr3, 0, len(arr3) - 1, part_3)
end = time.time()
print("Mediana de três:", end - start)


"""
Analisando os resultados, dá pra perceber que usar o primeiro elemento como pivô
em um vetor já ordenado de forma decrescente faz o quicksort cair no pior caso,
porque ele sempre escolhe um pivô ruim e acaba dividindo o vetor de forma muito
desbalanceada (um lado enorme e o outro vazio).
Já com o pivô aleatório, isso melhora pois diminui a chance de sempre
pegar um pivô ruim, deixando o desempenho mais próximo de O(n log n). A mediana de
três melhora ainda mais, pois tenta escolher um pivô mais central, evitando essas
divisões ruins, principalmente em vetores já ordenados, o que explica o melhor tempo.
"""