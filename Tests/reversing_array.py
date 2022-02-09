array = [1, "+", 2, "-", 3, "*", 4, "/", 5]
reveresed_array = []

for i in range(len(array)):
    num = (i + 1) * -1
    reveresed_array.append(array[num])
print(array)
print(reveresed_array)