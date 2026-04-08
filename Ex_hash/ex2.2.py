TAM = 10

class No:
    def __init__(self, nome):
        self.nome = nome
        self.prox = None


# Tabela hash
tabela = [None] * TAM


# Função hash
def funcao_hash(nome):
    return sum(ord(c) for c in nome) % TAM


# Verificar se já votou
def ja_votou(nome):
    indice = funcao_hash(nome)
    atual = tabela[indice]

    while atual:
        if atual.nome == nome:
            return True
        atual = atual.prox

    return False


# Registrar voto
def votar(nome):
    if ja_votou(nome):
        print("❌ Este nome já votou! Voto não permitido.")
        return

    indice = funcao_hash(nome)

    novo = No(nome)
    novo.prox = tabela[indice]
    tabela[indice] = novo

    print("✅ Voto registrado com sucesso!")


# Exibir votantes
def exibir():
    print("\n--- VOTANTES ---")
    for i in range(TAM):
        atual = tabela[i]
        if atual:
            print(f"[{i}] -> ", end="")
            while atual:
                print(atual.nome, end=" -> ")
                atual = atual.prox
            print("None")


# Programa principal
while True:
    print("\n--- SISTEMA DE VOTAÇÃO ---")
    print("1 - Votar")
    print("2 - Exibir votantes")
    print("0 - Sair")

    op = input("Escolha: ")

    if op == "1":
        nome = input("Digite seu nome: ")
        votar(nome)

    elif op == "2":
        exibir()

    elif op == "0":
        print("Encerrando votação...")
        break

    else:
        print("Opção inválida!")