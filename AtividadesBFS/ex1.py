from collections import deque

# Grafo de amizades modelado como tabela hash (dicionário)
grafo = {
    "você":    ["alice", "bob", "claire"],
    "alice":   ["peggy"],
    "bob":     ["anuj", "peggy"],
    "claire":  ["thom", "jonny"],
    "peggy":   [],
    "anuj":    [],
    "thom":    [],
    "jonny":   [],
}

def eh_vendedor(nome):
    """Vendedor de mangas: nome termina com a letra 'm'."""
    return nome.endswith("m")

def buscar_vendedor(grafo, inicio):
    fila = deque(grafo[inicio])   # começa com os amigos diretos
    verificados = set()           # evita loops infinitos

    while fila:
        pessoa = fila.popleft()

        if pessoa not in verificados:
            if eh_vendedor(pessoa):
                print(f'✔ Vendedor encontrado: "{pessoa}"')
                return pessoa
            else:
                print(f'  Verificando "{pessoa}"... não é vendedor.')
                fila.extend(grafo.get(pessoa, []))
                verificados.add(pessoa)

    print("Nenhum vendedor encontrado na rede.")
    return None

buscar_vendedor(grafo, "você")