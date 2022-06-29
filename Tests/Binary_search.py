import random

arr = []
for i in range(0, 1000, 3):
    arr.append(i + random.randint(0, 2))

num = arr[random.randrange(0, len(arr))]

def bin_srh(array, counter):
    counter += 1
    p = round(len(array)/2)
    if array[p] == num:
        return(array[p], counter)
    elif array[p] > num:
        return(bin_srh(array[:p], counter))
    else:
        return(bin_srh(array[p + 1:], counter))

#print(arr)
print(bin_srh(arr, 0))