#Melhor: Letra D — Caso 1 utilizou a Função 4 (primos), 
# pois as demais funções geravam colisões: a Função 2 (comprimento) colocaria Ben, Bob e Dan no mesmo índice 3, 
# já que os três têm o mesmo tamanho, e a Função 3 (primeiro caractere) colocaria Ben e Bob juntos por compartilharem a inicial "B". 
# A função de primos, ao considerar todos os caracteres da string, distribuiu os nomes nos índices 2, 3, 4 e 7 sem nenhuma colisão.


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
        print(f"{key:10} → índice {index}")

    def get(self, key):
        return self.table[self._hash(key)]

    def display(self):
        print("\n--- Tabela Hash ---")
        for i, slot in enumerate(self.table):
            content = f"{slot[0]}: {slot[1]}" if slot else "vazio"
            print(f"[{i}] {content}")


ht = HashTable()
ht.insert("Esther", "(55) 9999-0004")
ht.insert("Ben",    "(55) 9999-0007")
ht.insert("Bob",    "(55) 9999-0003")
ht.insert("Dan",    "(55) 9999-0002")
ht.display()