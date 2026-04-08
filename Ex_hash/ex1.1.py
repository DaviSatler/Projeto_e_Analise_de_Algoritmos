TAM = 10

# Classe do contato
class Contato:
    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone
        self.prox = None


# Tabela hash
tabela = [None] * TAM


# Função hash
def funcao_hash(nome):
    soma = sum(ord(c) for c in nome)
    return soma % TAM


# Verificar duplicidade
def existe_contato(nome, telefone):
    for i in range(TAM):
        atual = tabela[i]
        while atual:
            if atual.nome == nome or atual.telefone == telefone:
                return True
            atual = atual.prox
    return False


# Inserir contato
def inserir(nome, telefone):
    if existe_contato(nome, telefone):
        print("Erro: nome ou telefone já existe!")
        return

    indice = funcao_hash(nome)

    novo = Contato(nome, telefone)
    novo.prox = tabela[indice]
    tabela[indice] = novo

    print("Contato inserido com sucesso!")


# Buscar contato
def buscar(nome):
    indice = funcao_hash(nome)
    atual = tabela[indice]

    while atual:
        if atual.nome == nome:
            print(f"Nome: {atual.nome} | Telefone: {atual.telefone}")
            return

        atual = atual.prox

    print("Contato não encontrado!")


# Remover contato
def remover(nome):
    indice = funcao_hash(nome)
    atual = tabela[indice]
    anterior = None

    while atual:
        if atual.nome == nome:
            if anterior is None:
                tabela[indice] = atual.prox
            else:
                anterior.prox = atual.prox

            print("Contato removido!")
            return

        anterior = atual
        atual = atual.prox

    print("Contato não encontrado!")


# Exibir agenda
def exibir():
    print("\n--- AGENDA ---")
    for i in range(TAM):
        atual = tabela[i]
        if atual:
            print(f"[{i}]")
            while atual:
                print(f"Nome: {atual.nome} | Telefone: {atual.telefone}")
                atual = atual.prox


# Menu
while True:
    print("\n--- AGENDA TELEFÔNICA ---")
    print("1 - Inserir contato")
    print("2 - Buscar contato")
    print("3 - Remover contato")
    print("4 - Exibir agenda")
    print("0 - Sair")

    opcao = input("Escolha: ")

    if opcao == "1":
        nome = input("Nome: ")
        telefone = input("Telefone: ")
        inserir(nome, telefone)

    elif opcao == "2":
        nome = input("Digite o nome: ")
        buscar(nome)

    elif opcao == "3":
        nome = input("Digite o nome: ")
        remover(nome)

    elif opcao == "4":
        exibir()

    elif opcao == "0":
        print("Saindo...")
        break

    else:
        print("Opção inválida!")