from tkinter import *
import clipboard

win = Tk()
win.title("Cipherer/Decipherer")
win.configure(bg="Black")

def cipher_decipher():
    msg = msg_entry.get()
    new_msg = ""
    ans_box.delete("1.0", "end")
    
    for letter in msg:
        ciphered_letter = letter
        if ord(letter) >= ord("a") and ord(letter) <= ord("z"):
            ciphered_letter = chr(ord("z") - (ord(letter) - ord("a")))
        new_msg += ciphered_letter

    ans_box.insert(END, new_msg)

def copy_out():
    clipboard.copy(ans_box.get("1.0", "end"))

#Labels
Label(win, text="Enter message to cipher/decipher: ", bg="Black", fg="White").grid(row=0, column=0)
Label(win, text="Ciphered/Deciphered message is: ", bg="Black", fg="White").grid(row=1, column=0)
#Text box
ans_box = Text(win, width=20, height=1, font = ("Segoe UI", 9))
ans_box.grid(row=1, column=1)
#Entry box
msg_entry = Entry(win)
msg_entry.grid(row=0, column=1)
#Button
button = Button(win, text="Cipher/Decipher", command = cipher_decipher, bg="Black", fg="White")
button.grid(row=2, column=0)
copy_button = Button(win, text="Copy output", command = copy_out, bg="Black", fg="White")
copy_button.grid(row=2, column=1)

mainloop()