def potencia(n, expo):
    if expo == 0:
        return 1
    else:
        return n * potencia(n, expo - 1)


if __name__ == "__main__":
    n = int(input("Digite um número para calcular a potência: "))

    expo = int(input("Digite o expoente: "))
    
    if n < 0:
        print("Potência não existe com números negativos!")
    else:
        resultado = potencia(n, expo)
        print("O número", n, "elevado à potência", expo, "é igual a:", resultado)