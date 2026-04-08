TAM = 20

class No:
    def __init__(self, valor):
        self.valor = valor
        self.freq = 1
        self.prox = None


# Tabela hash
tabela = [None] * TAM


# Função hash
def funcao_hash(valor):
    return valor % TAM


# Inserir / atualizar número
def inserir(valor):
    indice = funcao_hash(valor)
    atual = tabela[indice]

    while atual:
        if atual.valor == valor:
            atual.freq += 1
            return
        atual = atual.prox

    novo = No(valor)
    novo.prox = tabela[indice]
    tabela[indice] = novo


# Encontrar números únicos
def numeros_unicos():
    unicos = []

    for i in range(TAM):
        atual = tabela[i]
        while atual:
            if atual.freq == 1:
                unicos.append(atual.valor)
            atual = atual.prox

    return unicos


# Programa principal
entrada = input("Digite números separados por espaço:\n")
numeros = list(map(int, entrada.split()))

# Inserir na tabela
for n in numeros:
    inserir(n)

# Mostrar resultado
print("Números únicos:", numeros_unicos())