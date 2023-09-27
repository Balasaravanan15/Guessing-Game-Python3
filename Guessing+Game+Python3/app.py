import random

random_number = random.randint(1, 10)
guess = None

while True:
    guess = int(input("Pick a number from 1 to 10: "))
    if guess < random_number:
        print("TOO LOW!") 
    elif guess > random_number:
        print("TOO HIGH!")
    else:
        print("YOU WON!")
        play_again = input("DO YOU WANT TO PLAY AGAIN? (y/n) ")
        if play_again == 'y':
            random_number = random.randint(1, 10)
            guess = None
        else:
            print("THANK YOU FOR PLAYING")
            break
