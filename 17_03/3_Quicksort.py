# Classe Funcionario
class Funcionario:
    def __init__(self, nome, salario, idade):
        self.nome = nome
        self.salario = salario
        self.idade = idade

    def __repr__(self):
        return f"{self.nome} (Salário: {self.salario}, Idade: {self.idade})"


# Lista de funcionários
funcionarios = [
    Funcionario("Alice", 5000, 30),
    Funcionario("Bob", 4500, 25),
    Funcionario("Charlie", 5500, 35),
    Funcionario("David", 4000, 28),
    Funcionario("Eve", 6000, 32),
    Funcionario("Frank", 4800, 27),
    Funcionario("Grace", 5200, 29),
    Funcionario("Heidi", 4700, 31),
    Funcionario("Ivan", 5300, 26),
    Funcionario("Judy", 4900, 33),
    Funcionario("Karl", 5100, 24),
    Funcionario("Leo", 4600, 34),
    Funcionario("Mallory", 5400, 30),
    Funcionario("Nina", 4700, 28),
    Funcionario("Oscar", 5000, 29)
]


# Função de comparação (isso que o professor quer!)
def comparar(f1, f2):
    # prioridade 1: salário (decrescente)
    if f1.salario > f2.salario:
        return True
    if f1.salario < f2.salario:
        return False

    # prioridade 2: nome (crescente)
    return f1.nome < f2.nome


# Partição usando comparator
def partition(arr, low, high, comp):
    pivo = arr[high]
    i = low - 1

    for j in range(low, high):
        if comp(arr[j], pivo):
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


# Quicksort adaptado
def quicksort(arr, low, high, comp):
    if low < high:
        pi = partition(arr, low, high, comp)
        quicksort(arr, low, pi - 1, comp)
        quicksort(arr, pi + 1, high, comp)


# Executando
quicksort(funcionarios, 0, len(funcionarios) - 1, comparar)


# Resultado
print("Funcionários ordenados:\n")
for f in funcionarios:
    print(f)