#Cálculo de Fatorial e Fibonacci: Atividades para analisar visualmente como os frames são empilhados na memória durante a execução.


entrada = input("Digite um número: ")
num = int(entrada)    

def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n - 1)
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

print(f"Fatorial de {num} é: {fatorial(num)}")
print(f"{num}º número de Fibonacci é: {fibonacci(num)}")

