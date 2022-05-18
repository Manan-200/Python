from tkinter import *

cip_win = Tk()
cip_win.title("Cipherer")
cip_win.configure(bg="Black")

decip_win = Tk()
decip_win.title("Decipherer")
decip_win.configure(bg="Black")

def cipher(msg, ans_box):
    msg_arr = []
    new_msg = ""
    #print(msg)

    for letter in msg:
        if ord(letter) <= ord("z") and ord(letter) >= ord("a"):
            new_letter = ord("z") - (ord(letter) - ord("a"))
            msg_arr.append(new_letter)

    for letter in msg_arr:
        new_msg += letter

    ans_box.insert(END, "new_msg")
    

#CIPHERER
#Labels
Label(cip_win, text="Enter message to cipher: ", bg="Black", fg="White").grid(row=0, column=0)
Label(cip_win, text="Ciphered message is: ", bg="Black", fg="White").grid(row=1, column=0)
#Text box
cip_ans_box = Text(cip_win, width=15, height=1)
cip_ans_box.grid(row=1, column=1)
#Entry box
cip_msg_entry = Entry(cip_win)
cip_msg_entry.grid(row=0, column=1)
#Cipher button
cip_button = Button(cip_win, text="Cipher", command = cipher(cip_msg_entry.get(), cip_ans_box), bg="Black", fg="White")
cip_button.grid(row=2, column=0)

#DECIPHERER
#Labels
Label(decip_win, text="Enter text to decipher: ", bg="Black", fg="White").grid(row=0, column=0)
Label(decip_win, text="Deciphered message is: ", bg="Black", fg="White").grid(row=1, column=0)
#Text box
decip_ans_box = Text(decip_win, width=15, height=1)
decip_ans_box.grid(row=1, column=1)
#Entry box
decip_msg_entry = Entry(decip_win)
decip_msg_entry.grid(row=0, column=1)
#Decipher button
decip_button = Button(decip_win, text="Decipher", command = None, bg="Black", fg="White")
decip_button.grid(row=2, column=0)

mainloop()