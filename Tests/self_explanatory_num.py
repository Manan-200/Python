#14233221 Orjj 🙏🙏🙏

from attr import define


counter = 0

#Adding digits of number into an array
def break_num(num):
    arr = []
    while num != 0:
        r = num % 10
        arr.append(r)
        num = num // 10
    arr = arr[::-1]
    return(arr)

#Function to remove duplicates
def rem_dup(arr):
    arr_new = arr
    for index_1 in range(0, len(arr_new)):
        for index_2 in range(0, len(arr_new)):
            if index_1 != index_2 and arr_new[index_1] == arr_new[index_2]:
                arr_new.pop(index_1)
    return(arr_new)

#Checking if in abcd, b == d(redefining)
def check_redef(arr):
    for index_1 in range(1, len(arr), 2):
        for index_2 in range(1, len(arr), 2):
            if index_1 != index_2 and arr[index_1] == arr[index_2]:
                return(False)

#Checking if each definer is defined
def check_def(arr):
    defineds = []
    for index_1 in range(1, len(arr), 2):
        defineds.append(arr[index_1])
    for index_2 in range(0, len(arr), 2):
        if arr[index_2] not in defineds:
            return(False)

"""
The most important filter
"""
def main_filter(arr):
    for index_1 in range(0, len(arr), 2):
        def_list = []
        num = arr[index_1 + 1]
        for index_2 in range(len(arr)):
            if arr[index_2] == num:
                def_list.append(num)
        if arr[index_1] != len(def_list):
            return(False)


print("Self Explanatory Numbers are:")

for num in range(10, 14233223):

    #Defining conditions
    c1, c2, c3, c_main = True, True, True, True

    broken_list = break_num(num)
    length = len(broken_list)

    #Checking for condtions
    if length % 2 != 0:
        c1 = False
    if check_redef(broken_list) == False:
        c2 = False
    if check_def(broken_list) == False:
        c3 = False
    if c1 == True and main_filter(broken_list) == False:
        c_main = False
    
    #Printing number if all conditions are true
    if c1 == True and c2 == True and c3 == True and c_main == True:
        counter += 1
        print(num, "counter = ", counter)