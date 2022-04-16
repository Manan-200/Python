n = int(input("Enter num: "))

def RecFib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return RecFib(n-1) + RecFib(n-2)
num = RecFib(n)
print(num)