import random

print("Welcome to my number chosing game.")
print("Choose the number from 1 to 10.")

x = random.randint(1, 10)
guess_attempts = 0

while True:
    try:
        number = int(input("Choose the number from 1 to 10: "))
        guess_attempts += 1
        if number == x:
            print(f"You have successfully guessed the correct number in {guess_attempts} attempt.")
            break
        elif number>x:
            print("Too big number.")
        else:
            print("Too small number.")
    except ValueError:
            if number != int:
                print("Choose the number.")
            else:
                print("Invalid option chosed.")
    finally:
        if number == x:
            print("You have succesfully completed game.")
        else:
            print("Try again!!")