dec = float(input("Enter a decimal number: "))
count = 0
def break_num(num):
    arr = []
    while num != 0:
        rem = num%10
        num = num // 10
        arr.append(rem)
    return(arr)

while dec % 1 != 0:
    dec *= 10
    count += 1
num_arr = break_num(dec)

for i in range(count - 1):
    if num_arr[i] >= 5:
        num_arr[i + 1] += 1

num = 0
for i in range(count - 2):
    num += num_arr[len(num_arr) - i] * 10**i

print(num)