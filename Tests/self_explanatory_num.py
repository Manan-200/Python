a_list, b_list, c_list, d_list, e_list = [], [], [], [], []
for i in range(1000):
    broken_list = []

    while i != 0:
        r = i % 10
        broken_list.append(r)
        i = i // 10

    broken_list = broken_list[::-1]

    for num in broken_list:
        if num == 0:
            a_list.append(num)
        elif num == 1:
            b_list.append(num)
        elif num == 2:
            c_list.append(num)
        elif num == 3:
            d_list.append(num)
        elif num == 4:
            e_list.append(num)

    if len(broken_list) >= 3:
        if broken_list[0] == len(b_list) and broken_list[2] == len(d_list):
            print(i)