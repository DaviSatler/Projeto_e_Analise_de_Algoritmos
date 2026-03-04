#Percorrimento de Árvores Binárias: Implementar os métodos Pré-ordem, Em-ordem e Pós-ordem, que dependem intrinsecamente da pilha de chamadas.
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
def pre_ordem(node):
    if node:
        print(node.value, end=' ')
        pre_ordem(node.left)
        pre_ordem(node.right)
def em_ordem(node):
    if node:
        em_ordem(node.left)
        print(node.value, end=' ')
        em_ordem(node.right)
def pos_ordem(node):
    if node:
        pos_ordem(node.left)
        pos_ordem(node.right)
        print(node.value, end=' ')
# Exemplo de uso
if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    
    print("Pré-ordem:")
    pre_ordem(root)
    print("\nEm-ordem:")
    em_ordem(root)
    print("\nPós-ordem:")
    pos_ordem(root)

        