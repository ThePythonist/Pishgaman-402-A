from random import randint

number = randint(1, 10)
chances = 5
print("Welcome to number guessing game")


while chances > 0:
    print()
    print(f"You have {chances} chances left")
    guess = input("Guess the number between (1-10) : ")

    try:
        guess = int(guess)
        if 0 < guess < 11 :
            if guess == number:
                print("You won!")
                break
            elif guess > number:
                print("Try smaller than", guess)
            else:
                print("Try bigger than", guess)
            chances -= 1
        else :
            print("Entry must be between 1-10")
    except ValueError:
        print("Entry must be a integer. Try again")

if chances == 0:
    print("Game over! The number was", number)
