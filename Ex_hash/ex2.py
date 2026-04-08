TAM = 10

# Tabela hash (lista de listas)
tabela = [[] for _ in range(TAM)]

# Função hash
def hash_func(chave):
    return chave % TAM

# Inserir
def inserir(valor):
    indice = hash_func(valor)
    
    if valor not in tabela[indice]:
        tabela[indice].append(valor)
        print("Inserido!")
    else:
        print("Valor já existe!")

# Buscar
def buscar(valor):
    indice = hash_func(valor)
    
    if valor in tabela[indice]:
        print("Encontrado!")
    else:
        print("Não encontrado!")

# Remover
def remover(valor):
    indice = hash_func(valor)
    
    if valor in tabela[indice]:
        tabela[indice].remove(valor)
        print("Removido!")
    else:
        print("Valor não encontrado!")

# Exibir
def exibir():
    print("\nTabela Hash:")
    for i in range(TAM):
        print(f"{i}: {tabela[i]}")


# Menu
while True:
    print("\n1-Inserir  2-Buscar  3-Remover  4-Exibir  0-Sair")
    op = input("Escolha: ")

    if op == "1":
        v = int(input("Valor: "))
        inserir(v)

    elif op == "2":
        v = int(input("Valor: "))
        buscar(v)

    elif op == "3":
        v = int(input("Valor: "))
        remover(v)

    elif op == "4":
        exibir()

    elif op == "0":
        break

    else:
        print("Opção inválida!")