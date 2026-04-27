#Melhor: Para o exercício 3, o melhor uso é a Letra D (primos), 
# pois o Ex 3 (primeiro caractere) gerava colisão entre Maus e Watchmen — ambas resultavam no índice 7.
#  A função de primos resolveu isso ao considerar todos os caracteres da string, distribuindo os títulos nos índices 3, 5 e 7 
# sem nenhuma colisão.

PRIMES = {
    'a':2,  'b':3,  'c':5,  'd':7,  'e':11, 'f':13, 'g':17,
    'h':19, 'i':23, 'j':29, 'k':31, 'l':37, 'm':41, 'n':43,
    'o':47, 'p':53, 'q':59, 'r':61, 's':67, 't':71, 'u':73,
    'v':79, 'w':83, 'x':89, 'y':97, 'z':101
}

class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [None] * size

    def _hash(self, key):
        return sum(PRIMES[c] for c in key.lower() if c in PRIMES) % self.size

    def insert(self, key, value):
        index = self._hash(key)
        self.table[index] = (key, value)
        soma = sum(PRIMES[c] for c in key.lower() if c in PRIMES)
        print(f"{key:10} → soma={soma:4}  índice {index}")

    def get(self, key):
        return self.table[self._hash(key)]

    def display(self):
        print("\n--- Tabela Hash ---")
        for i, slot in enumerate(self.table):
            content = f"{slot[0]}: {slot[1]}" if slot else "vazio"
            print(f"[{i}] {content}")


ht = HashTable()
ht.insert("Maus",     "Art Spiegelman")
ht.insert("Fun Home", "Alison Bechdel")
ht.insert("Watchmen", "Alan Moore")
ht.display()
