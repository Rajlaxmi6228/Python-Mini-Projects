#ROCK-PAPER-SCISSOR GAME
i=1
while i<=5:
    play = input("yes/no : ")
    if play == "yes":
        you = input("Enter rock/paper/scissor: ")
        elements = ["rock", "paper", "scissor"]

        import random
        computer = random.choice(elements)
        print(you)
        print(computer)

        if you == "rock" and computer == "paper":
            print("computer won!!") 
        elif you == "paper" and computer == "scissor": 
            print("computer won!!") 
        elif you == "scissor" and computer == "rock":
            print("computer won!!")
        elif you == "rock" and computer == "scissor": 
            print("you won!!")
        elif you == "paper" and computer == "rock": 
            print("you won!!") 
        elif you == "scissor" and computer == "paper": 
            print("you won!!") 
        else:
            print("uff! its a draw..")
    else:
        break
    i = i + 1
    