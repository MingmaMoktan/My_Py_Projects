import random

print("Welcome to Rock Paper and Scissor game.")
print("Choose R=Rock and P=Paper and S=Scissor.")


while True:
    x = random.randint(1,3)
    # Here 1 = Rock and 2 = Paper and 3 = Scissor for the computer.
    try:
        y = input("Choose your option: ").upper()
        if y not in ["R", "P", "S"]:
            raise ValueError
        computer_choice = "Rock" if x==1 else "Paper" if x==2 else "Scissor" 
        if (x==1 and y=="R") or (x==2 and y=="P") or (x==3 and y=="S"):
            print(f"It is draw because we both chose {computer_choice}.")
        elif x==1 and y=="P":
            print("You won. You chose paper I chose rock.")
        elif x==1 and y=="S":
            print("I win because you chose scissor and I chose rock.")
        elif x==2 and y=="R":
            print("I win because you chose rock and I choose paper.")
        elif x==2 and y=="S":
            print("You win because you chose scissor and I chose paper.")
        elif x==3 and y=="R":
            print("You win because you chose rock and I chose scissor.")
        elif x==3 and y=="P":
            print("I win because you chose paper and I chose scissor.")
        print("Do you want to play again?")
        play_again = input("Chose 'Y' for yes and 'N' to quit: ").upper()
        if play_again == "N":
            break
    except ValueError:
        print("Invalid option chose only r or p or s")