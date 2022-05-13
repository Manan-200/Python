arr = [1, "+", 2, "-", 3, "*", 4, "/", 5]
print(f"original array: {arr}")
i, j = 0, len(arr) - 1

while i < j:
    arr[i], arr[j] = arr[j], arr[i]
    i += 1
    j -= 1
print(f"reversed array: {arr}")