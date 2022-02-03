flag = False
a = int(input("Enter number to check prime"))
for i in range (2,a):
    if a % i == 0:
        flag = False
    else:
        flag = True
    break
if flag:
    print (a,"is a prime number")
else:
    print (a,"is not a prime number")
