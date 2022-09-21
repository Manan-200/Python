def sum_comb(n):
    if n == 2:
        arr = []
        arr.append([1, 1])

    else:
        arr = sum_comb(n - 1)

        for p1 in range(len(arr)):
            sub_arr = list(tuple(arr[p1]))
            arr[p1].append(1)

            repeated_ele = []
            for p2 in range(len(sub_arr)):
                if sub_arr[p2] not in repeated_ele:
                    sub_arr[p2] += 1

                    new_arr = list(tuple(sub_arr))
                    arr.append(list(tuple(new_arr)))

                    sub_arr[p2] -= 1
                    repeated_ele.append(sub_arr[p2])
        
    return(arr)


if __name__ == "__main__":
    num = int(input("Enter a number: "))
    sum_arr = sum_comb(num)
    sum_arr = set(tuple(element) for element in sum_arr)
    print(f"Sum combinations of {num} are: {len(sum_arr)}")
    print(sum_arr)
else:
    x = []
    y = []
    for num in range(2, 16):
        sum_arr = sum_comb(num)
        sum_arr = set(tuple(element) for element in sum_arr)
        x.append(num)
        y.append(len(sum_arr))