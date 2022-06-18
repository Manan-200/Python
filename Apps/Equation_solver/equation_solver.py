from tkinter import *
from tkinter.messagebox import *

zero_counter = 0
positive_counter = 0
negative_counter = 0
zero_state, positive_state, negative_state = False, False, False

win = Tk()
win.title('Equation Solver')

def isnt_zero():
    global zero_counter, zero_state
    zero_counter += 1
    if zero_counter % 2 == 0:
        Button.configure(zero_button, relief=RAISED)
        zero_state = False
    elif zero_counter % 2 != 0:
        Button.configure(zero_button, relief=SUNKEN)
        zero_state = True

def is_positive():
    global positive_counter, positive_state
    positive_counter += 1
    if positive_counter % 2 == 0:
        Button.configure(positive_button, relief=RAISED)
        positive_state = False
    elif positive_counter % 2 != 0:
        Button.configure(positive_button, relief=SUNKEN)
        positive_state = True

def is_negative():
    global negative_counter, negative_state
    negative_counter += 1
    if negative_counter % 2 == 0:
        Button.configure(negative_button, relief=RAISED)
        negative_state = False
    elif negative_counter % 2 != 0:
        Button.configure(negative_button, relief=SUNKEN)
        negative_state = True

def conditions(x, y, z):
    if positive_state == True:
        if x < 0 or y < 0 or z < 0:
            return(False)
    if negative_state == True:
        if x > 0 or y > 0 or z > 0:
            return(False)
    if zero_state == True:
        if x*y*z == 0:
            return(False)
    return(True)

def print_xyz(vars, counter, x, y, z):
    if vars == 3:
        ans_val.insert(
            counter, f"counter:{counter}     value of x, y, z : {x}, {y}, {z}")
    elif vars == 2:
        ans_val.insert(
            counter, f"counter:{counter}     value of x, y, z : {x}, {y}, NA")
    elif vars == 1:
        ans_val.insert(
            counter, f"counter:{counter}     value of x, y, z : {x}, NA, NA")

def print_vals():

    ans_val.delete(0, END)

    counter = 0

    vars = int(var_entry.get())
    if vars == 3:
        a, b, c = 50, 50, 50
    elif vars == 2:
        a, b, c = 200, 200, 1
    elif vars == 1:
        a, b, c = 10000, 1, 1

    for x in range((a // 2 * -1), (a // 2 + 1)):
        for y in range((b // 2 * -1), (b // 2 + 1)):
            for z in range((c // 2 * -1), (c // 2 + 1)):

                LHS = eval(str(lhs.get()))
                RHS = eval(str(rhs.get()))

                if LHS == RHS:
                    if conditions(x, y, z):
                        counter += 1
                        print_xyz(vars, counter, x, y, z)

    if counter == 0:
        counter += 1
        ans_val.insert(0, f"counter:{counter}     value of x, y, z : NA, NA, NA")



#Labels
Label(win, text="Enter Number of vars(Max=3):").grid(row=0, column=0)
Label(win, text="Enter L.H.S:").grid(row=1, column=0)
Label(win, text="Enter R.H.S:").grid(row=2, column=0)
Label(win, text="Sort:").grid(row=3, column=0)

#Entry boxes
var_entry = Entry(win)
var_entry.grid(row=0, column=1)

lhs = Entry(win)
lhs.grid(row=1, column=1)

rhs = Entry(win)
rhs.grid(row=2, column=1)

#Buttons
Val_button = Button(win, text="Print answer(s)", command=print_vals)
Val_button.grid(row=7, column=0)

zero_button = Button(win, text="non-zero", command=isnt_zero)
zero_button.grid(row=5, column=1)

positive_button = Button(win, text="positive", command=is_positive)
positive_button.grid(row=6, column=1)

negative_button = Button(win, text="negative", command=is_negative)
negative_button.grid(row=7, column=1)

#Answer box
ans_val = Listbox(win)
ans_val.grid(row=8, column=0, ipadx=100)

mainloop()