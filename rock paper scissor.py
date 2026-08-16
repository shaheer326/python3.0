import random
playing = True

while playing:

    choice = random.choice(["paper", "scissors", "rock"])

    user_choice = input("Choose between Rock, Paper and Scissors: ").lower()
    if choice == user_choice:
        print("Draw")
        again = input("Do you want to play again? (Yes or No): ")
        if again == "yes":
            continue
        elif again == "no":
            break
        else:
            print("wrong Input")
    elif choice == "rock" and user_choice == "paper":
        print("You Won")
        again = input("Do you want to play again? (Yes or No): ")
        if again == "yes":
            continue
        elif again == "no":
            break
        else:
                    print("wrong Input")
    elif choice == "paper" and user_choice == "scissors":
        print("You Won")
        again = input("Do you want to play again? (Yes or No): ")
        if again == "yes":
            continue
        elif again == "no":
            break
        else:
            print("wrong Input")
    elif choice == "scissors" and user_choice == "rock":
        print("You Won")
        again = input("Do you want to play again? (Yes or No): ")
        if again == "yes":
            continue
        elif again == "no":
            break
        else:
            print("wrong Input")
    elif user_choice == "rock" and choice == "paper":
        print("You Lost")
        again = input("Do you want to play again? (Yes or No): ")
        if again == "yes":
            continue
        elif again == "no":
            break
        else:
            print("wrong Input")
    elif user_choice == "paper" and choice == "scissors":
        print("You Lost")
        again = input("Do you want to play again? (Yes or No): ")
        if again == "yes":
            continue
        elif again == "no":
            break
        else:
            print("wrong Input")
    elif user_choice == "scissors" and choice == "rock":
        print("You Lost")
        again = input("Do you want to play again? (Yes or No): ")
        if again == "yes":
            continue
        elif again == "no":
            break
        else:
            print("wrong Input")
    else:
        print("Wrong Input")
        break