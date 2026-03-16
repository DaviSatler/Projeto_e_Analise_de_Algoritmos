#Encontre o valor mais alto de uma lista

def valor_MaisAlto(lista):
    if len(lista) == 1:
        return lista[0]
    else:
        max_restante = valor_MaisAlto(lista[1:])
        return max(lista[0], max_restante)
minha_lista = [3, 1, 4, 1, 5, 9]
resultado = valor_MaisAlto(minha_lista)


print("O valor mais alto da lista é:", resultado)