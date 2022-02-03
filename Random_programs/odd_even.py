import random

#The concept of the game is that the player has to enter a number, then the bot also prints another number based on previous numbers entered. 
#The sum of both the numbers should be even. 
#If the sum is even, the bot's prediction is wrong and if it is odd, the bot's prediction is correct
#The objective of the bot is to print such a number so that the sum should be odd.

#Variables
odd_list, even_list = [], []
odd_probab, even_probab = 0, 0 
correct_predictions, wrong_preictions = 0, 0
num_state = None
counter = 0

#Loop
while True:

    counter += 1

    #Input player's choice
    player_choice = int(input("Enter a number so that the sum is even"))

    #Length of lists shouldn't be more than 5
    if len(odd_list) == 5:
        odd_list.remove(odd_list[0])
    if len(even_list) == 5:
        even_list.remove(even_list[0])

    #Calculating probablities
    for num in odd_list:
        odd_probab += num
    for num in even_list:
        even_probab += num

    #Checking for repitition
    if len(odd_list) > 2 and len(even_list) > 2:
        if odd_list[-1] == odd_list[-2]:
            odd_probab -= 1
        if even_list[-1] == even_list[-2]:
            even_probab -= 1

    #Deciding choice based on probablities
    if even_probab > odd_probab:
        comp_choice = (random.choice([1, 3, 5, 7, 9]))
    elif odd_probab > even_probab:
        comp_choice = (random.choice([0, 2, 4, 6, 8]))
    elif odd_probab == even_probab:
        comp_choice = (random.randint(0, 10))

    #Increasing lists based on player's choice
    if player_choice % 2 == 1:
        odd_list.append(1)
        even_list.append(0)
    elif player_choice % 2 == 0:
        even_list.append(1)
        odd_list.append(0)

    #Sum of Bot's choice and Player's choice(final num)
    final_num = comp_choice + player_choice

    #Checking if final number is odd/even
    if final_num % 2 == 1:
        correct_predictions += 1
        num_state = "odd"
    elif final_num % 2 == 0:
        wrong_preictions += 1
        num_state = "even"

    #Printing Stuff
    print(f"Bot's choice : {comp_choice} ; Correct predictions : {correct_predictions} ; Wrong_predictioons : {wrong_preictions} ; Final State = {num_state}")
    print("")

    #Reseting probabilities
    odd_probab, even_probab = 0, 0