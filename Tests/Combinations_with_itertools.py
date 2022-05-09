from itertools import permutations
counter = 0
E = permutations([1,2,3,4,5,6], 6)
for i in E:
    counter += 1
    print(i,"Counter:",counter)