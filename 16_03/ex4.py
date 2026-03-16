#Voltando para pesquisa binária, você consegue determinar o caso base e o caso recursivo para a pesquisa binária?

def busca_binaria(vetor, inicio, fim, valor):

    # caso base: não encontrado
    if inicio > fim:
        return -1

    meio = (inicio + fim) // 2

    # caso base: encontrado
    if vetor[meio] == valor:
        return meio

    # caso recursivo
    elif valor < vetor[meio]:
        return busca_binaria(vetor, inicio, meio - 1, valor)
    else:
        return busca_binaria(vetor, meio + 1, fim, valor)


# O caso base ocorre quando o elemento do meio do vetor é igual ao valor procurado, indicando que o elemento foi encontrado...
# ou quando o índice de início ultrapassa o índice de fim, indicando que o elemento não está presente no vetor.
# Já caso recursivo ocorre quando o valor procurado é menor ou maior que o elemento...
# do meio, levando a uma nova chamada recursiva para a metade esquerda ou direita do vetor, respectivamente.

