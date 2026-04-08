TAM = 20

class No:
    def __init__(self, palavra):
        self.palavra = palavra
        self.freq = 1
        self.prox = None


# Tabela hash
tabela = [None] * TAM


# Função hash
def funcao_hash(palavra):
    return sum(ord(c) for c in palavra) % TAM


# Inserir / atualizar palavra
def inserir(palavra):
    indice = funcao_hash(palavra)
    atual = tabela[indice]

    # Verifica se já existe
    while atual:
        if atual.palavra == palavra:
            atual.freq += 1
            return
        atual = atual.prox

    # Se não existe, cria novo nó
    novo = No(palavra)
    novo.prox = tabela[indice]
    tabela[indice] = novo


# Processar texto
def processar_texto(texto):
    palavras = texto.lower().split()

    for palavra in palavras:
        # Remove pontuação simples
        palavra = palavra.strip(".,!?;:")
        inserir(palavra)


# Exibir tabela
def exibir():
    print("\n--- FREQUÊNCIA DE PALAVRAS ---")
    for i in range(TAM):
        atual = tabela[i]
        if atual:
            print(f"[{i}]")
            while atual:
                print(f"{atual.palavra}: {atual.freq}")
                atual = atual.prox


# Programa principal
texto = input("Digite um texto:\n")
processar_texto(texto)
exibir()