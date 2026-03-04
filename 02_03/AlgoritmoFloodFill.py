#Algoritmo de Flood Fill: O algoritmo de "balde de tinta" para preencher áreas conectadas em uma matriz/imagem.
def flood_fill(matriz, x, y, nova_cor, cor_antiga=None):
    if cor_antiga is None:
        cor_antiga = matriz[x][y]
    if x < 0 or x >= len(matriz) or y < 0 or y >= len(matriz[0]):
        return
    if matriz[x][y] != cor_antiga:
        return
    matriz[x][y] = nova_cor
    flood_fill(matriz, x + 1, y, nova_cor, cor_antiga)
    flood_fill(matriz, x - 1, y, nova_cor, cor_antiga)
    flood_fill(matriz, x, y + 1, nova_cor, cor_antiga)
    flood_fill(matriz, x, y - 1, nova_cor, cor_antiga)
matriz = [
    [1, 1, 1, 2, 2],
    [1, 1, 0, 2, 2],
    [1, 0, 0, 2, 2],
    [1, 1, 1, 2, 2]
]
print("Matriz Original:")
for linha in matriz:
    print(linha)

        