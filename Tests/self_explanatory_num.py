reversed_list = []
odd_pos_list = []
c1, c2, c3, c4, c5 = True, True, True, True, True
t1_list, t2_list, t3_list, t4_list = [], [], [], []
t1, t2, t3, t4 = None, None, None, None
var = 0

"""
condition 1 = checking for redefining at odd postions
condition 2 = checking if defining is correct 
condition 3 = checking there is 0 in the broken list
condition 4 = checking if sum of digits at even places in list is equal to the length of broken list
condition 5 = checking if sum of digits of broken list is equal to sum of multiplication of adjacent digits
"""

print("started")

for num in range(1000, 9999):
    a = num
    while num != 0:
        r = num % 10
        reversed_list.append(r)
        num = num // 10

    broken_list = reversed_list[::-1]

    if len(broken_list) % 2 == 0:

        #Checking for condition 1
        for i in range(len(broken_list)):
            if i % 2 == 0:  #Needs to be i % 2 == 0 and not i % 2 != 0 due to unkown error
                odd_pos_list.append(broken_list[i])
                for j in range(len(odd_pos_list)):
                    for k in range(len(odd_pos_list)):
                        if j != k:
                            if odd_pos_list[j] == odd_pos_list[k]: 
                                c1 = False

        #Checking for condition 2
        t1 = broken_list[0]

        if broken_list[0] != broken_list[1]:
            t2 = broken_list[1]
        if broken_list[0] != broken_list[2] and broken_list[1] != broken_list[2]:
            t3 = broken_list[2] 
        if broken_list[0] != broken_list[3] and broken_list[1] != broken_list[3] and broken_list[2] != broken_list[3]:
            t4 = broken_list[3]

        for i in broken_list:
            if i == t1:
                t1_list.append(t1)
            if i == t2:
                t2_list.append(t2)
            if i == t3:
                t3_list.append(t3)
            if i == t4:
                t4_list.append(t4)

        if t1 != len(t2_list):
            c2 = False

        #Checking for condition 3
        for i in broken_list:
            if i == 0:
                c3 = False

        #Checking for condition 4
        for i in range(len(broken_list)):
            if i % 2 == 0:
                var += broken_list[i]
        if var != len(broken_list):
            c4 = False

        #Checking for condition 5
        var = 0
        for i in range(0, len(broken_list), 2):
            var += broken_list[i] * broken_list[i+1]
        if var != sum(broken_list):
            c5 = False

        #Printing if all conditions are true
        if c1 == True and c2 == True and c3 == True and c4 == True and c5 == True:
            print(reversed_list)

        if a == 7391:
            b = 100

    broken_list.clear()
    reversed_list.clear()
    odd_pos_list.clear()
    t1_list.clear()
    t2_list.clear()
    t3_list.clear()
    t4_list.clear()
    c1, c2, c3, c4, c5 = True, True, True, True, True
    var = 0