import random

# função que faz a partição do quicksort
def particionar(vetor, inicio, fim):
    pivo = vetor[fim]  # escolhi o último elemento como pivô
    i = inicio - 1

    # percorrendo o vetor
    for j in range(inicio, fim):
        if vetor[j] < pivo:
            i += 1
            # troca os elementos
            vetor[i], vetor[j] = vetor[j], vetor[i]

    # coloca o pivô na posição correta
    vetor[i + 1], vetor[fim] = vetor[fim], vetor[i + 1]

    return i + 1


# quicksort com "print" pra ver o que está acontecendo
def quicksort_rastreando(vetor, inicio, fim, passo=[1]):
    if inicio < fim:
        pos_pivo = particionar(vetor, inicio, fim)
        pivo = vetor[pos_pivo]

        # mostrando o estado atual
        print(f"\nPasso {passo[0]}")
        print("Vetor:", vetor)
        print(f"Pivô escolhido: {pivo} (índice {pos_pivo})")

        passo[0] += 1

        # chamadas recursivas
        quicksort_rastreando(vetor, inicio, pos_pivo - 1, passo)
        quicksort_rastreando(vetor, pos_pivo + 1, fim, passo)


def quicksort(vetor):
    print("=" * 40)
    print("Rodando Quicksort com rastreamento")
    print("=" * 40)

    print("\nAntes:", vetor)

    quicksort_rastreando(vetor, 0, len(vetor) - 1)

    print("\nDepois:", vetor)
    print("=" * 40)


# gerando um vetor aleatório só pra teste
teste = [random.randint(1, 100) for i in range(10)]

quicksort(teste)