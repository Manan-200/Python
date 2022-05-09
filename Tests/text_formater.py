msg = input("Enter a message: ")
msg_list = []
caps = 0
new_msg = ""

for text in msg:
    msg_list.append(text)

for i in range(len(msg_list)):
    if msg_list[i] == " ":
        caps += 1
    elif caps % 2 == 0:
        msg_list[i] = (msg_list[i]).upper()
        caps += 1
    elif caps % 2 != 0:
        msg_list[i] = (msg_list[i]).lower()
    new_msg += msg_list[i]

print(new_msg)