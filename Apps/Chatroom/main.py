from tkinter import *

user, msg = "xyz", "abc"
msg_list = []

bg_color = "#191919"

def insert_msg(msg, msg_list, box):
    msg_list.append(msg)
    box.insert(len(msg_list), f"{msg}")

def send_msg():
    pass

#Making the mainscreen
window = Tk()
window.title("Chatroom")
window.configure(bg=bg_color)

#Defining chatbox and textbox
chat_box = Listbox(window)
chat_box.grid(row=0, column=0, ipadx=250, ipady=100)
txt_box = Entry(window)
txt_box.grid(row=1, column=0, ipadx=215, sticky="w")
#Defining send button
send = Button(window, text="Send", command=send_msg)
send.grid(row=1, column=0, ipadx=25, sticky="e")

insert_msg(f"{user}: {msg}", msg_list, chat_box)

mainloop()