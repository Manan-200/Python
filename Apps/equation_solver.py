from tkinter import *
from tkinter.messagebox import *

found_ans = False
zero_state, positive_state, negative_state = False, False, False
condition1, condition2, condition3, condition4, condition5, condition6, conditionNone = False, False, False, False, False, False, False

zero_counter = 0
positive_counter = 0
negative_counter = 0

win = Tk()
win.title('Graphing calculator')


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
    global condition1, condition2, condition3, condition4, condition5, condition6, conditionNone
    if positive_state == True and negative_state == True and zero_state == True:
        if x == 0 or y == 0 or z == 0:
            condition1 = True
        else:
            condition1 = False
    elif positive_state == True and zero_state == True and negative_state == False:
        if x <= 0 or y <= 0 or z <= 0:
            condition2 = True
        else:
            condition2 = False
    elif negative_state == True and zero_state == True and positive_state == False:
        if x >= 0 or y >= 0 or z >= 0:
            condition3 = True
        else:
            condition3 = False
    elif negative_state == True and positive_state == True and zero_state == False:
        conditionNone = True
        
    elif negative_state == True and positive_state == False and zero_state == False:
        if x > 0 or y > 0 or z > 0:
            condition4 = True
        else:
            condition4 = False
    elif positive_state == True and negative_state == False and zero_state == False:
        if x < 0 or y < 0 or z < 0:
            condition5 = True
        else:
            condition5 = False
    elif zero_state == True and negative_state == False and positive_state == False:
        if x == 0 or y == 0 or z == 0:
            condition6 = True
        else:
            condition6 = False


def print_xyz(variables, counter, x, y, z):
    if variables == 3:
        ans_val.insert(
            counter, f"counter:{counter}     value of x, y, z : {x}, {y}, {z}")
    elif variables == 2:
        ans_val.insert(
            counter, f"counter:{counter}     value of x, y, z : {x}, {y}, NA")
    elif variables == 1:
        ans_val.insert(
            counter, f"counter:{counter}     value of x, y, z : {x}, NA, NA")


def print_vals():
    global found_ans

    ans_val.delete(0, END)

    counter = 0

    variables = int(v.get())

    if variables == 3:
        a, b, c = 50, 50, 50

    elif variables == 2:
        a, b, c = 200, 200, 1

    elif variables == 1:
        a, b, c = 10000, 1, 1

    for x in range((a // 2 * -1), (a // 2 + 1)):
        for y in range((b // 2 * -1), (b // 2 + 1)):
            for z in range((c // 2 * -1), (c // 2 + 1)):

                LHS = eval(str(lhs.get()))
                RHS = eval(str(rhs.get()))

                if LHS == RHS:
                    found_ans = True
                    conditions(x, y, z)
                    if condition1 == True:
                        None
                    elif condition2 == True:
                        None
                    elif condition3 == True:
                        None
                    elif condition4 == True:
                        None
                    elif condition5 == True:
                        None
                    elif condition6 == True:
                        None
                    else:
                        counter += 1
                        print_xyz(variables, counter, x, y, z)
                        found_ans = True

    if found_ans == False:
        counter += 1
        ans_val.insert(counter,
                       f"counter:{counter}     value of x, y, z : NA, NA, NA")
    #print(counter)


Label(win, text="Enter Number of variables(Max : 3):").grid(row=0, column=0)
Label(win, text="Enter L.H.S:").grid(row=1, column=0)
Label(win, text="Enter R.H.S:").grid(row=2, column=0)
Label(win, text="Sort:").grid(row=3, column=0)

Val_button = Button(win, text="Print answer(s)", command=print_vals)
Val_button.grid(row=7, column=0)

zero_button = Button(win, text="Is not zero", command=isnt_zero)
zero_button.grid(row=5, column=1)

positive_button = Button(win, text="Is positive", command=is_positive)
positive_button.grid(row=6, column=1)

negative_button = Button(win, text="Is negative", command=is_negative)
negative_button.grid(row=7, column=1)

v = Entry(win)
v.grid(row=0, column=1)

lhs = Entry(win)
lhs.grid(row=1, column=1)

rhs = Entry(win)
rhs.grid(row=2, column=1)

ans_val = Listbox(win)
ans_val.grid(row=8, column=0, ipadx=100)

mainloop()
