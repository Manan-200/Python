#LCM = (a * b)/HCF

def get_HCF(a, b):
    HCF = 1
    for fac in range(1, a + 1):
        if a % fac == 0 and b % fac == 0:
            HCF = fac
    return(HCF)

n = int(input("Enter value of n: "))

LCM = 2
for num in range(3, n + 1, 2):
    LCM = int(LCM*(num)*(num + 1) / get_HCF(LCM, (num)*(num + 1)))

if n % 2 != 0:
    LCM = int(LCM * n / get_HCF(LCM, n))

print(LCM)