#Faça uma função soma como vista no slide anteriormente
def soma(lista):
    if len(lista) == 0:
        return 0
    else:
        return lista[0] + soma(lista[1:])

resultado = soma([3, 5, 2, 8])
print("A soma é:", resultado)