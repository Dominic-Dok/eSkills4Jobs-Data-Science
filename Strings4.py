import random


# pick_an_item = random.choice(["red", "green", "blue"])
# print(pick_an_item)

# generate a random number
# num = random.random(0, 9)
# 

user_input = int(input("Enter a number b/n 10 and20"))

while ((user_input < 10) or (user_input > 20)):
    if user_input < 10:
        print("Too low")
        user_input = int(input("Enter the guess again: "))

    if user_input > 20:
        print("Too High")
        user_input = int(input("Enter the guess again: "))

    user_input = int(input("Enter the guess again: "))
print("Thank you")

