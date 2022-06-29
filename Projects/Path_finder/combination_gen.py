num = 6
NUM = num
comb_arr = []
def init_num(n):
    if n == 0:
        return(0)
    else:
        return(n*10**(NUM-n)) + init_num(n - 1)

def final_num(n):
    if n == 0:
        return(0)
    else:
        return((n * 10**(n-1)) + final_num(n-1))

def break_num(n):
    rem_arr = []
    while n != 0:
        rem = n % 10
        n = n // 10
        rem_arr.append(rem)
    return(rem_arr[::-1])

def mult_num(arr):
    mult = 1
    for i in arr:
        mult *= i
    return(mult)
    
def sum_num(arr):
    Sum = 0
    for i in arr:
        Sum += i
    return(Sum)

f_num = final_num(num)
i_num = init_num(num)

for n in range(i_num, f_num + 1):
    num_arr = break_num(n)

    if mult_num(break_num(f_num)) == mult_num(num_arr) and sum_num(break_num(f_num)) == sum_num(num_arr) and len(num_arr) == num:
        num_arr.insert(0, 0)
        num_arr.append(NUM + 1)
        comb_arr.append(num_arr)