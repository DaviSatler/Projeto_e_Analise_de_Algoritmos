import time

def busca_binaria_par(lista, alvo):
    # só permite busca de números divisíveis por 2
    if alvo % 2 != 0:
        return -1

    inicio = 0
    fim = len(lista) - 1

    while inicio <= fim:
        meio = (inicio + fim) // 2

        if lista[meio] == alvo:
            return meio

        elif lista[meio] < alvo:
            inicio = meio + 1

        else:
            fim = meio - 1

    return -1


# lista ordenada (necessária para busca binária)
vetor = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

numero = int(input("Digite um número para buscar: "))

inicio_tempo = time.time()

resultado = busca_binaria_par(vetor, numero)

fim_tempo = time.time()

if resultado != -1:
    print("Número encontrado na posição:", resultado)
else:
    print("-1 (não encontrado ou não divisível por 2)")

print("Tempo de execução:", fim_tempo - inicio_tempo, "segundos")
