# This is a rock, paper, scissors game
import random as rand
import sys

no_of_wins = 0
no_of_losses = 0
no_of_ties = 0
choices = ['ROCK', 'PAPER', 'SCISSORS']
computers_choice = ''

print(f"ROCK PAPER SCISSORS \n {no_of_wins} Wins {no_of_losses} Losses {no_of_ties} Ties")
 
for i in range(1, 11):

    # Get user choice in form of r p s

    print("Choose one out of (r)ock (p)aper (s)cissors or (q)uit \nEnter r, p, s or q")
    users_choice = input("")
    
    # Display it in all caps with vs
    if(users_choice == 'q'):
        print(f"Are you sure you want to exit the game? \n {no_of_wins} Wins {no_of_losses} Losses {no_of_ties} Ties\n\nEnter (y/n) ")
        should_exit = input("=>: ")
        if(should_exit == 'n'):
            i -= 1
            continue
        elif(should_exit == 'y'):
            sys.exit()
    elif(users_choice == 'r'):
        print("ROCK vs ...")
    elif(users_choice == 'p'):
        print("PAPER vs ...")
    elif(users_choice == 's'):
        print("SCISSORS vs ...")

    # Get computers choice using randint
    random_number = rand.randint(0, 2)
    print(choices[random_number])

    if(random_number == 0):
        computers_choice = "r"
    elif(random_number == 1):
        computers_choice = "p"
    elif(random_number == 2):
        computers_choice = "s"
        

    # Evaluate Game Outcome
    if(users_choice == computers_choice):
        print("Its a tie 😑")
        no_of_ties += 1
    elif(users_choice == 'r' and computers_choice == 's'):
        print('You won 🙂')
        no_of_wins += 1
    elif(users_choice == 'p' and computers_choice == 'r'):
        print('You won 🙂')
        no_of_wins += 1
    elif(users_choice == 's' and computers_choice == 'p'):
        print('You won 🙂')
        no_of_wins += 1
    
    else:
        print("You lost this round 😢")
        no_of_losses += 1

    # Update scores
    print(f"\n {no_of_wins} Wins {no_of_losses} Losses {no_of_ties} Ties")

if i == 10: 
    print(f"GAME OVER \n Player: {no_of_wins} - Computer: {no_of_losses}")