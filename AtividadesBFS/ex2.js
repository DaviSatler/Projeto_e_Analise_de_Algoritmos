// AVISO: Não sei fazer isso em JavaScript.
// Peguei o mesmo código Python e traduzi para JS mantendo a mesma lógica.

const grafo = {
  "Twin Peaks":        ["Castro", "West Portal"],
  "Castro":            ["Twin Peaks", "Market & Church", "Noe Valley"],
  "West Portal":       ["Twin Peaks", "Forest Hill", "Sunset District"],
  "Market & Church":   ["Castro", "Civic Center", "Mission District"],
  "Noe Valley":        ["Castro", "Mission District"],
  "Forest Hill":       ["West Portal", "Civic Center"],
  "Sunset District":   ["West Portal", "Richmond District"],
  "Civic Center":      ["Market & Church", "Forest Hill", "Downtown"],
  "Mission District":  ["Market & Church", "Noe Valley", "Downtown"],
  "Richmond District": ["Sunset District", "Golden Gate Park"],
  "Downtown":          ["Civic Center", "Mission District", "Fisherman's Wharf"],
  "Golden Gate Park":  ["Richmond District", "Presidio"],
  "Fisherman's Wharf": ["Downtown", "Presidio"],
  "Presidio":          ["Golden Gate Park", "Fisherman's Wharf", "Golden Gate Bridge"],
  "Golden Gate Bridge": ["Presidio"],
};

function bfsMenorCaminho(grafo, origem, destino) {
  if (origem === destino) return { etapas: 0, caminho: [origem] };

  const fila = [[origem, [origem]]]; // equivale ao deque do Python
  const visitados = new Set([origem]);

  while (fila.length > 0) {
    const [atual, caminho] = fila.shift(); // shift() = popleft()

    for (const vizinho of (grafo[atual] || [])) {
      if (!visitados.has(vizinho)) {
        const novoCaminho = [...caminho, vizinho];

        if (vizinho === destino) {
          return { etapas: novoCaminho.length - 1, caminho: novoCaminho };
        }

        visitados.add(vizinho);
        fila.push([vizinho, novoCaminho]);
      }
    }
  }

  return { etapas: -1, caminho: [] }; // destino inalcançável
}

const origem  = "Twin Peaks";
const destino = "Golden Gate Bridge";

const { etapas, caminho } = bfsMenorCaminho(grafo, origem, destino);

console.log(`De: ${origem}`);
console.log(`Para: ${destino}`);
console.log(`Etapas (arestas): ${etapas}`);
console.log(`Caminho: ${caminho.join(" → ")}`);