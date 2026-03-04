#Resolução de Labirintos (Backtracking): Usar a recursão para explorar caminhos e "voltar atrás" quando encontrar um beco sem saída.

def resolver_labirinto(labirinto, posicao_atual, destino, caminho):
    if posicao_atual == destino:
        return True
    x, y = posicao_atual
    if (x < 0 or x >= len(labirinto) or y < 0 or y >= len(labirinto[0]) or labirinto[x][y] == 1):
        return False
    caminho.append(posicao_atual)
    labirinto[x][y] = 1
    if (resolver_labirinto(labirinto, (x + 1, y), destino, caminho) or
        resolver_labirinto(labirinto, (x - 1, y), destino, caminho) or
        resolver_labirinto(labirinto, (x, y + 1), destino, caminho) or
        resolver_labirinto(labirinto, (x, y - 1), destino, caminho)):
        return True
    caminho.pop()
    labirinto[x][y] = 0
    return False
labirinto = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 1, 1, 0],
    [0, 0, 0, 1, 0]
]
caminho = []
if resolver_labirinto(labirinto, (0, 0), (4,
4), caminho):
    print("Caminho encontrado:", caminho)
else:
    print("Nenhum caminho encontrado.")
    