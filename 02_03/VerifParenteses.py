#Verificação de Parênteses Balanceados: Validar expressões matemáticas verificando se cada abertura possui seu fechamento correspondente.
def verificar_parenteses(expressao):
    pilha = []
    pares = {')': '(', '}': '{', ']': '['}
    
    for char in expressao:
        if char in pares.values():
            pilha.append(char)
        elif char in pares.keys():
            if not pilha or pilha[-1] != pares[char]:
                return False
            pilha.pop()
    
    return len(pilha) == 0
if __name__ == "__main__":
    expressao = input("Digite a expressão a ser verificada: ")
    if verificar_parenteses(expressao):
        print("A expressão é balanceada com o fechamento correto.")
    else:
        print("A expressão não é balanceada.")
        