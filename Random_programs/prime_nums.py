def check_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return(False)

for a in range(11):
    for b in range(11):
        if check_prime(a) != False and check_prime(b) != False:
            num = 10*a + b
            SUM = a + b
            if check_prime(num) != False and check_prime(SUM) != False and num <= 100:
                print(num)