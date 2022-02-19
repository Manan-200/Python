t1_list, t2_list, t3_list, t4_list = [], [], [], []
t1, t2, t3, t4 = None, None, None, None

def mult(l):
    var = 0
    for i in range(len(l)):
        if i + 1 < len(l):
            var += l[i] * l[i+1]
    return var

def check_valid(l):
    for i in range(len(l)):
        if i + 2 < len(l):
            if l[i] == l[i+2]:
                return False

for i in range(1000, 1000000):
    broken_list = []

    while i != 0:
        r = i % 10
        broken_list.append(r)
        i = i // 10

    broken_list = broken_list[::-1]

    if sum(broken_list) == mult(broken_list) and check_valid(broken_list):

        t1 = broken_list[0]

        if broken_list[0] != broken_list[1]:
            t2 = broken_list[1]
        if broken_list[0] != broken_list[2] and broken_list[1] != broken_list[2]:
            t3 = broken_list[2] 
        if broken_list[0] != broken_list[3] and broken_list[1] != broken_list[3] and broken_list[2] != broken_list[3]:
            t4 = broken_list[3]

        for num in broken_list:
            if num == t1:
                t1_list.append(t1)
            if num == t2:
                t2_list.append(t2)
            if num == t3:
                t3_list.append(t3)
            if num == t4:
                t4_list.append(t4)

        if t1 == len(t2_list):
            print("")
            print(f"{t1} {t2} {t3} {t4}")
            print(f"{t1_list} {t2_list} {t3_list} {t4_list}")
            print(f"Number : {broken_list}")
            print("")
        
        t1, t2, t3, t4 = None, None, None, None
        t1_list, t2_list, t3_list, t4_list = [], [], [], []