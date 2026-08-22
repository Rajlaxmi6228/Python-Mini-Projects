#NUMBER GUESSING GAME

list = []

for elements in range(1, 51):
    list.append(elements)
import random
computer = random.choice(list)

print("You have 10 chances-")

i=1
while i<=10:
    you = int(input("Guess the number (1-50): "))
    i = i + 1

    if you < computer:
        print("You lost a chance")
        print("Guess something greater!!")
        continue
    elif you > computer:
        print("You lost a chance")
        print("Guess something smaller!!")
        continue
    else:
        print("You did it!!")
        break