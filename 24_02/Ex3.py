def somaArray(arr, n):
    if n == 0:
        return 0
    else:
        return arr[n - 1] + somaArray(arr, n - 1)
    
if __name__ == "__main__":
    n = int(input("Digite o tamanho do array: "))
    arr = []
    
    for i in range(n):
        num = int(input(f"Digite o elemento {i + 1}: "))
        arr.append(num)
    
    resultado = somaArray(arr, n)
    print("A soma dos elementos do array é:", resultado)