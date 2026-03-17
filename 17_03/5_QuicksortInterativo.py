def quicksort_iterativo(arr):
    """Quicksort iterativo com stack."""
    if len(arr) <= 1:
        return arr
    
    def particionar(arr, low, high):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1
    
    stack = [(0, len(arr) - 1)]
    
    while stack:
        low, high = stack.pop()
        if low < high:
            pi = particionar(arr, low, high)
            stack.append((low, pi - 1))
            stack.append((pi + 1, high))
    
    return arr


if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90, 88]
    print("Array original:", arr)
    print("Array ordenado:", quicksort_iterativo(arr))
