import time

def pesquisa_simples(lista, valor):
    i = 0
    
    while i < len(lista):
        if lista[i] == valor:
            return i
        i += 1
    
    return -1


lista = [i * 2 for i in range(1, 51)]

valor = int(input("Digite o valor que deseja buscar: "))

inicio = time.perf_counter()

resultado = pesquisa_simples(lista, valor)

fim = time.perf_counter()

tempo = fim - inicio

if resultado != -1:
    print(f"Valor encontrado na posição: {resultado}")
else:
    print("Valor não encontrado.")

print(f"Tempo de execução: {tempo:.10f} segundos")
