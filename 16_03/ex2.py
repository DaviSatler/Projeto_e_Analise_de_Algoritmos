#Escreva uma função recursiva que conte o número de itens de uma lista

def contar_itens(lista):
    if not lista:
        return 0
    else:
        return 1 + contar_itens(lista[1:])  
minha_lista = [1, 2, 3, 4, 5]
resultado = contar_itens(minha_lista)
print("Número de itens na lista:", resultado)

