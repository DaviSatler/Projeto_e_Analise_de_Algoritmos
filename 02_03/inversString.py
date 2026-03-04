#Inversão de uma String: Usar chamadas recursivas para empilhar cada caractere e reconstruir a string na ordem inversa ao retornar.
resp = input("Escreva uma palavra.")

def inverter_string(s):
 if len(s) <= 1:
     return s
 
 return inverter_string(s[1:]) + s[0]

resultado = inverter_string(resp)
    
print(f"A sua palavra {resp} ao inverso será: {resultado}")

