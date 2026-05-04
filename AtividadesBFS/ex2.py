from collections import deque

# Grafo de rotas de ônibus de San Francisco (não-direcionado)
# Cada par de paradas compartilha uma aresta (uma linha de ônibus direta)
grafo = {
    "Twin Peaks":         ["Castro", "West Portal"],
    "Castro":             ["Twin Peaks", "Market & Church", "Noe Valley"],
    "West Portal":        ["Twin Peaks", "Forest Hill", "Sunset District"],
    "Market & Church":    ["Castro", "Civic Center", "Mission District"],
    "Noe Valley":         ["Castro", "Mission District"],
    "Forest Hill":        ["West Portal", "Civic Center"],
    "Sunset District":    ["West Portal", "Richmond District"],
    "Civic Center":       ["Market & Church", "Forest Hill", "Downtown"],
    "Mission District":   ["Market & Church", "Noe Valley", "Downtown"],
    "Richmond District":  ["Sunset District", "Golden Gate Park"],
    "Downtown":           ["Civic Center", "Mission District", "Fisherman's Wharf"],
    "Golden Gate Park":   ["Richmond District", "Presidio"],
    "Fisherman's Wharf":  ["Downtown", "Presidio"],
    "Presidio":           ["Golden Gate Park", "Fisherman's Wharf", "Golden Gate Bridge"],
    "Golden Gate Bridge":  ["Presidio"],
}

def bfs_menor_caminho(grafo, origem, destino):
    if origem == destino:
        return 0, [origem]

    fila = deque()
    fila.append((origem, [origem]))   # (parada_atual, caminho_percorrido)
    visitados = {origem}

    while fila:
        atual, caminho = fila.popleft()

        for vizinho in grafo.get(atual, []):
            if vizinho not in visitados:
                novo_caminho = caminho + [vizinho]

                if vizinho == destino:
                    etapas = len(novo_caminho) - 1
                    return etapas, novo_caminho

                visitados.add(vizinho)
                fila.append((vizinho, novo_caminho))

    return -1, []   # destino inalcançável

# ── Execução ──────────────────────────────────────────────────
origem  = "Twin Peaks"
destino = "Golden Gate Bridge"

etapas, caminho = bfs_menor_caminho(grafo, origem, destino)

print(f"De: {origem}")
print(f"Para: {destino}")
print(f"Etapas (arestas): {etapas}")
print(f"Caminho: {' → '.join(caminho)}")