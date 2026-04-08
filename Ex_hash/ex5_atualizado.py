def encontrar_pares(nums, alvo):
    hash_map = {}  # valor -> índice
    pares = []

    for i, num in enumerate(nums):
        complemento = alvo - num

        if complemento in hash_map:
            pares.append((complemento, num))

        hash_map[num] = i

    return pares


# Programa principal
nums = list(map(int, input("Digite os números: ").split()))
alvo = int(input("Digite o valor alvo: "))

pares = encontrar_pares(nums, alvo)

if pares:
    print("Pares encontrados:")
    for p in pares:
        print(p)
else:
    print("Nenhum par encontrado.")