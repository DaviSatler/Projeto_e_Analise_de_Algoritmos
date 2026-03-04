#Conversão de Decimal para Binário: Empilhar os restos das divisões sucessivas por 2 e exibi-los na ordem inversa para obter a representação binária.
def decimal_para_binario(n):
    if n == 0:
        return "0"
    elif n == 1:
        return "1"
    else:
        return decimal_para_binario(n // 2) + str(n % 2)
numero_decimal = 10
numero_binario = decimal_para_binario(numero_decimal)
print(f"Decimal: {numero_decimal} -> Binário: {numero_binario}")
