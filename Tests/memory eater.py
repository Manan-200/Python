a = 0
b = 1
c = 0
list1 = []
while a != b:
    b += 1
    a += 1
    c += a ** 1000000000
    for n in range (1,1000000000000000000000000000000000):
        list1.append(c)