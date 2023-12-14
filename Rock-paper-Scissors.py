while True:
    import random
    letters = ["Rock","Paper","Scissors"]
    x = input("Enter your choice (x,y,z):")
    choice=x.lower()
    computer_choice = random.randint(0,2)
    computer = letters[computer_choice]
    if choice == "rock" and computer == "Rock":
        print("It is draw")
        print(computer)
    elif choice == "rock" and computer == "Paper":
        print("You loose")
        print(computer)
    elif choice == "rock" and computer == "Scissors":
        print("You win")
        print(computer)
    elif choice == "paper" and computer == "Rock":
        print("You win")
        print(computer)
    elif choice == "paper" and computer == "Scissors":
        print("You loose")
        print(computer)
    elif choice == "paper" and computer == "Paper":
        print("It is draw")
        print(computer)
    elif choice == "scissors" and computer == "Rock":
        print("You loose")
        print(computer)
    elif choice == "scissors" and computer == "Paper":
        print("You win")
        print(computer)
    elif choice == "scissors" and computer == "Scissors":
        print("It is draw")
        print(computer)
    else:
        print("Try again")

