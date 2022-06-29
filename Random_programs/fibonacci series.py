a = 0
b = 1
numbers = []
n = int(input("Enter number till which series is to be calculated"))
for i in range (1,n+1):
        c = a + b
        a = b
        b = c
        numbers.append(c)
print (numbers)