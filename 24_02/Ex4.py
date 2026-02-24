def maior_elemento(arr, n):
    if n == 1:
        return arr[0]
    else:
        max_anterior = maior_elemento(arr, n - 1)
        return max(max_anterior, arr[n - 1])
    
if __name__ == "__main__":
    n = int(input("Digite o tamanho do array: "))
    arr = []
    
    for i in range(n):
        num = int(input(f"Digite o elemento {i + 1}: "))
        arr.append(num)
    
    resultado = maior_elemento(arr, n)
    print("O maior elemento do array é:", resultado)