def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n - 1)


if __name__ == "__main__":
    n = int(input("Digite um número para calcular o fatorial: "))
    
    if n < 0:
        print("Fatorial não existe com números negativos!")
    else:
        resultado = fatorial(n)
        print("Fatorial de", n, "é:", resultado)