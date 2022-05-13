num = int(input("Enter number for its factorial: "))

def rec_fac(n):
    if n == 1 or n == 0:
        return(1)
    else:
        return(n * rec_fac(n - 1))

print(f"factorial of {num} is: {rec_fac(num)}")