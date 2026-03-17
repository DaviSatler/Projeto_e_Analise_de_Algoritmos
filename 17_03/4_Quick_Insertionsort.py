import random
import time


# insertion sort pra usar quando o pedaço do vetor for pequeno
def insertion_sort(vetor, inicio, fim):
    for i in range(inicio + 1, fim + 1):
        chave = vetor[i]
        j = i - 1

        # vai empurrando os maiores pra frente
        while j >= inicio and vetor[j] > chave:
            vetor[j + 1] = vetor[j]
            j -= 1

        vetor[j + 1] = chave


# partição padrão do quicksort (pivô no final)
def partition(vetor, inicio, fim):
    pivo = vetor[fim]
    i = inicio - 1

    for j in range(inicio, fim):
        if vetor[j] < pivo:
            i += 1
            vetor[i], vetor[j] = vetor[j], vetor[i]

    vetor[i + 1], vetor[fim] = vetor[fim], vetor[i + 1]
    return i + 1


# versão híbrida (quicksort + insertion sort)
def quicksort_hibrido(vetor, inicio, fim):
    while inicio < fim:
        # se o pedaço for pequeno, usa insertion (mais rápido nesses casos)
        if fim - inicio + 1 <= 10:
            insertion_sort(vetor, inicio, fim)
            break

        pivo = partition(vetor, inicio, fim)

        # sempre resolve primeiro o menor lado (evita muita recursão)
        if pivo - inicio < fim - pivo:
            quicksort_hibrido(vetor, inicio, pivo - 1)
            inicio = pivo + 1
        else:
            quicksort_hibrido(vetor, pivo + 1, fim)
            fim = pivo - 1


# quicksort normal (sem otimização)
def quicksort_puro(vetor, inicio, fim):
    if inicio < fim:
        pivo = partition(vetor, inicio, fim)
        quicksort_puro(vetor, inicio, pivo - 1)
        quicksort_puro(vetor, pivo + 1, fim)


# ============================
# TESTE
# ============================

tamanho = 50000

# criando vetor aleatório
vetor1 = [random.randint(1, 100000) for _ in range(tamanho)]
vetor2 = vetor1.copy()

print(f"Testando com {tamanho} números...\n")

# híbrido
inicio = time.time()
quicksort_hibrido(vetor1, 0, len(vetor1) - 1)
tempo_hibrido = time.time() - inicio
print(f"Quicksort híbrido: {tempo_hibrido:.4f}s")

# puro
inicio = time.time()
quicksort_puro(vetor2, 0, len(vetor2) - 1)
tempo_puro = time.time() - inicio
print(f"Quicksort puro: {tempo_puro:.4f}s")


# comparação final
melhoria = ((tempo_puro - tempo_hibrido) / tempo_puro) * 100

print("\nComparação:")
print(f"Melhoria: {melhoria:.2f}%")
print(f"Speedup: {tempo_puro / tempo_hibrido:.2f}x")


"""
Observação:

O quicksort híbrido costuma ser mais rápido porque evita recursões desnecessárias
quando o vetor fica pequeno, usando insertion sort nesses casos.

Além disso, ordenar primeiro a menor partição ajuda a reduzir o uso da pilha
de recursão, deixando o algoritmo mais eficiente na prática.
"""