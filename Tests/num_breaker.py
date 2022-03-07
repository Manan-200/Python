reversed_list = []

num = int(input("Enter a number to break it into digits: "))

while num != 0:
    r = num % 10
    reversed_list.append(r)
    num = num // 10

reversed_list = reversed_list[::-1]

print(reversed_list)