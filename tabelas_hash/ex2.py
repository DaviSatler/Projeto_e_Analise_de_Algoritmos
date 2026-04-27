#Melhor: Letra B (comprimento) - pois como todas as chaves são compostas apenas pela letra "A"
# o comprimento é o único atributo que as diferencia, resultando em índices únicos para cada uma.

class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [None] * size

    def _hash(self, key):
        return len(key) % self.size

    def insert(self, key, value):
        index = self._hash(key)
        self.table[index] = (key, value)
        print(f"{key:6} → índice {index}  (len={len(key)})")

    def get(self, key):
        return self.table[self._hash(key)]

    def display(self):
        print("\n--- Tabela Hash ---")
        for i, slot in enumerate(self.table):
            content = f"{slot[0]}: {slot[1]}" if slot else "vazio"
            print(f"[{i}] {content}")


ht = HashTable()
ht.insert("A",    "1.5V — 1200 mAh")
ht.insert("AA",   "1.5V — 2500 mAh")
ht.insert("AAA",  "1.5V — 1000 mAh")
ht.insert("AAAA", "1.5V — 500 mAh")
ht.display()