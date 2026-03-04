#Resolução da Torre de Hanói: O exemplo clássico que demonstra como a recursão gerencia a movimentação de discos entre pilhas.
def hanoi(n, origem, destino, auxiliar):
    if n == 1:
        print(f"Mova o disco 1 de {origem} para {destino}")
        return
    hanoi(n - 1, origem, auxiliar, destino)
    print(f"Mova o disco {n} de {origem} para {destino}")
    hanoi(n - 1, auxiliar, destino, origem)
num_discos = 3
hanoi(num_discos, 'A', 'C', 'B')
