remainder_list = []

num = int(input("Enter a number to break it into digits: "))

while num != 0:
    r = num % 10
    remainder_list.append(r)
    num = num // 10

print(remainder_list[::-1])