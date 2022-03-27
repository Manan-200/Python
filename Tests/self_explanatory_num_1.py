#14233221 Orjj 🙏🙏🙏

#Adding digits of number into an array
def break_num(num):
    arr = []
    while num != 0:
        r = num % 10
        arr.append(r)
        num = num // 10
    arr = arr[::-1]
    return arr

#Checking if in abcd, a + b + c + d == a*b + c*d
def mult_and_sum(arr):
    SUM  = sum(arr)
    MULT = 0
    for index_1 in range(0, len(arr) - 1, 2):
        MULT += arr[index_1] * arr[index_1 + 1]
    if SUM == MULT:
        return(True)

#Checking if in abcd, a + c == len(abcd)
def check_valid(arr):
    SUM = 0
    for index in range(0, len(arr) - 1, 2):
        SUM += arr[index]
    if SUM == len(arr):
        return(True)

#Checking if in abcd, a == 0 or c == 0
def check_zero(arr):
    for index in range(0, len(arr) - 1, 2):
        if arr[index] == 0:
            return(False)

#Checking if in abcd, b == d(redefining)
def check_redefine(arr):
    for index_1 in range(1, len(arr) - 1, 2):
        for index_2 in range(1, len(arr) - 1, 2):
            if index_1 != index_2 and arr[index_1] == arr[index_2]:
                return(False)

def sort_check(arr):
    for index_1 in range(0, len(arr) - 1, 2):
        def_list = []
        num = arr[index_1 + 1]
        for index_2 in range(len(arr) - 1):
            if arr[index_2] == num:
                def_list.append(num)
        if arr[index_1] != len(def_list):
            return(False)
            break


for num in range(10, 1000000):

    #Defining conditions
    c1, c2, c3, c4, c5, c6 = True, True, True, True, True, True

    broken_list = break_num(num)
    length = len(broken_list)

    #Checking for condtions
    if length % 2 != 0:
        c1 = False
    if mult_and_sum(broken_list) != True:
        c2 = False
    if check_valid(broken_list) != True:
        c3 = False
    if check_zero(broken_list) == False:
        c4 = False
    if check_redefine(broken_list) == False:
        c5 = False
    if sort_check(broken_list) == False:
        c6 = False
    
    #Printing number if all conditions are true
    if c1 == True and c2 == True and c3 == True and c4 == True and c5 == True and c6 == True:
        print(num)