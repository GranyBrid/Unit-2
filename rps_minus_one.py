import random
"""
Name: Milo Lynch
File: rps_minus_one.py
Description: Implements the Rock Paper Scissor 
Minus One game from squid game
"""

"""
Pseudocode
Have computer pick two random hands of rps
SET comp_score, player_score to 0
STORE values in comp_hand somehow
ASK user for their hands
STORE values in player_hand
ASK user which hand to keep
Computer randomly chooses hand
EVALUATE who wins
UPDATE score
ASK if they want to continue or quit
IF quit, PRINT scores and End game
    ELSE, play again
"""
score = 0
comp_score = 0

def comp_hand():
    global hand1
    global hand2
    hand1 = random.choice(["rock", "paper", "scissors"])
    hand2 = random.choice(["rock", "paper", "scissors"])
    return(hand1, hand2)

def player_hand():
    global phand1
    global phand2
    phand1 = input("What is your first selection? ")
    debug = 1
    debug2 = 1
    while debug == 1:
        if phand1.lower() != "paper" and phand1.lower() != "rock" and phand1.lower() != "scissors":
            phand1 = input("INVALID INPUT: What is your first selection? ")
        else:
            debug = 2
    phand2 = input("What is your second selection? ")
    while debug2 == 1:
        if phand2.lower() != "paper" and phand2.lower() != "rock" and phand2.lower() != "scissors":
            phand2 = input("INVALID INPUT: What is your second selection? ")
        else:
            debug2 = 2
    return(phand1.lower(), phand2.lower())

def comp_hand_keep():
    global final_hand
    random_number = random.randint(1, 2)
    if random_number == 1:
        final_hand = hand1
    else:
        final_hand = hand2
    final_hand = final_hand.lower()
    return(final_hand)

def player_hand_keep():
    global pfinal_hand
    debug = 1
    player_number = int(input("Which hand would you like to keep? (1 or 2) "))
    while debug == 1:
        if player_number == 1:
            pfinal_hand = phand1
            debug = debug + 1
        elif player_number == 2:
            pfinal_hand = phand2
            debug = debug + 1
        else:
            player_number = int(input("INVALID INPUT: which hand would you like to keep? (1 or 2) "))
    pfinal_hand = pfinal_hand.lower()
    return(pfinal_hand)

def game():
    print(f"The computer chose {final_hand.lower()}")
    if pfinal_hand == "paper":
        if final_hand == "paper":
            print("The game was a draw")
        elif final_hand == "rock":
            print("You Win!")
            score = score + 1
        elif final_hand == "scissors":
            print("You Lose!")
            comp_score = comp_score + 1
    elif pfinal_hand == "rock":
        if final_hand == "paper":
            print("You Lose!")
            comp_score = comp_score + 1
        elif final_hand == "rock":
            print("The game was a draw")
        elif final_hand == "scissors":
            print("You Win!")
            score = score + 1
    elif pfinal_hand == "scissors":
        if final_hand == "paper":
            print("You Win!")
            score = score + 1
        elif final_hand == "rock":
            print("You Lose!")
            comp_score = comp_score + 1
        elif final_hand == "scissors":
            print("The game was a draw")

    print("Your score is", score)
    print("The computers score is", comp_score)


comp_hand()
player_hand()
comp_hand_keep()
player_hand_keep()
game()

check = int(input("Would you like to play again? (1 for yes, 2 for no) "))
while check == 1:
    comp_hand()
    player_hand()
    comp_hand_keep()
    player_hand_keep()
    game()
    check = int(input("Would you like to play again? (1 for yes, 2 for no) "))