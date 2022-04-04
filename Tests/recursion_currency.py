#a = bq + r
note_type = [1, 2, 5, 10, 20, 50, 100]

val = int(input("Enter the value of the currency: "))

def divide(rem):
    if rem == 0:
        return(f"0 * 0")
    else:
        num = note_type[-1]
        for i in range(len(note_type)):
            if i != len(note_type) - 1:
                if note_type[i] < rem and note_type[i + 1] > rem:
                    num = note_type[i]
                if note_type[i] == rem:
                    num = note_type[i]
        new_rem = rem%num
        quot = int((rem-new_rem)/num)
        print(f"{num} * {quot} +")
        print(divide(new_rem))

if divide(val) != None:
    print(divide(val))