r_list = []
p_list = []
s_list = []
r_probab = 0
p_probab = 0
s_probab = 0
counter = 0
reset_counter = 3
comp_choice = None
correct_predictions = 0
other = 0

while True:

    counter += 1

    #input
    choice = input("choose : rock(r) / paper(p) / scissors(s)")

    #Reseting lists if its length increases reset counter
    if len(r_list) > reset_counter:
        while len(r_list) != 0:
            r_list.remove(r_list[0])
    if len(p_list) > reset_counter:
        while len(p_list) != 0:
            p_list.remove(p_list[0])
    if len(s_list) > reset_counter:
        while len(s_list) != 0:
            s_list.remove(s_list[0])

    #Calculating probabilities
    for i in r_list:
        r_probab += i
    for i in p_list:
        p_probab += i
    for i in s_list:
        s_probab += i

    #Checking if user is repeating options
    if len(r_list) > 2 and r_list[-1] == r_list[-2]:
        r_probab -= 1
    if len(p_list) > 2  and p_list[-1] == p_list[-2]:
        p_probab -= 1
    if len(s_list)  > 2 and s_list[-1] == s_list[-2]:
        s_probab -= 1

    #Making probablities unequal
    if r_probab == p_probab or r_probab == s_probab:
        r_probab += 1
    if p_probab == r_probab or p_probab == s_probab:
        p_probab += 1
    
    #Choosing option based on max probability
    if max([r_probab, p_probab, s_probab]) == r_probab:
        comp_choice = "paper"
    elif max([r_probab, p_probab, s_probab]) == p_probab:
        comp_choice = "scissors"
    elif max([r_probab, p_probab, s_probab]) == s_probab:
        comp_choice = "rock"

    #Counter for correct_predictions
    if choice == "r" and comp_choice == "paper":
        correct_predictions += 1
    if choice == "p" and comp_choice == "scissors":
        correct_predictions += 1
    if choice == "s" and comp_choice == "rock":
        correct_predictions += 1

    #Counter for won / tie
    other = counter - correct_predictions

    print(f"Counter : {counter} ; Comp_choice : {comp_choice} ; Correct_predictions : {correct_predictions} ; Other : {other}")
    print("")

    #reseting probablities
    r_probab = 0
    p_probab = 0
    s_probab = 0

    #Increasing lists based on input
    if choice == "r":
        r_list.append(1)
        p_list.append(0)
        s_list.append(0)
    elif choice == "p":
        r_list.append(0)
        p_list.append(1)
        s_list.append(0)
    elif choice == "s":
        r_list.append(0)
        p_list.append(0)
        s_list.append(1)

    if counter % 6 == 0:
        print(f"""
                -----------------------------------------------------------------------------------
                CORRECT     PREDICTIONS     TO     OTHER     RATIO : {(correct_predictions/other)}
                -----------------------------------------------------------------------------------
            """)