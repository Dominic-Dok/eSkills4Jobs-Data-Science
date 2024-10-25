## asking for two inputs and converting to integer
first_number = int(input("Enter your first number:" ))

second_number = int(input("Enter your second number:" ))

## test for the condition and make a decision
if (first_number > second_number):
    print(second_number, first_number)
else:
    print(first_number, second_number)    


#Ask the user to enter a number that is under 20. If they enter a number that is 20 or more, display the message "Too high", otherwise display "Thank you"
## take an input from a user
user_input = int(inpt("Enter a number that is less than 20:"))

#Ask the user to enter a number between 10 and 20 (inclusive). If they enter a number within this range, display the message "Thank you", otherwise display the message "Incorrect Answer".
user_input = int(input("Enter a number between 10 and 20:" ))
if ((user_input >= 10) and (user_input <= 20)):
    print("Thank you")
else:
    print("Incorrect Answer")


colour = input("Enter your favorite colour: ")
if (colour == "red" or colour == "RED" or colour == "Red"):
    print("I like red too")
else:
    print("I dont like " + colour + "I prefer red")