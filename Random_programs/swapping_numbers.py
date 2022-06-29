a=int(input("Enter first value"))
b=int(input("Enter second value"))
a = a - b
b = a + b # b = a + b = a - b + b = a
a = b - a # a = b - a = (a - a + b) = b
print(a)
print(b)