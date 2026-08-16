import random
playing = True
number = random.randint(0, 9)

print("I wil pick a number between 0 and 9 and you have to guess it")
print("===== Good Luck!! =====")

while playing:
    guess = int(input("Enter your Guess: "))
    if number == guess:
        print("===== You Won =====")
        playing = False
        break
    else:
        print("Your Guess is wrong Try again!")