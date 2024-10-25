# Ask the user if it is raining.
# If they answer "yes", ask if it is windy
# If they answer "yes", to this second question,
# display the answer "It is too windy for an umbrella",
# otherwise display the message "Take an umbrella".
# If they did not answer ye to the first question, display the 
# answer "Enjoy your day"

# # print("Enter" [yes] or [no] to the following questions")
# user_input = input("Is it raining?: ")

# if (user_input == "yes"):
#     user_input_2 = input("Is it also windy?: ")
#     if (user_input_2 == "yes"):
#         print("It is too windy for an umbrella")
#     else:
#         print("Take an umbrella")
# else:
#     print("Enjoy your day.")

# Ask the user's age. If they are 18 or over, display the message "You can vote", if they are aged 17, display
# the message "You can learn to drive", if they are 16, display the message "You can buy a lottery ticket", if they are under 16, display
# the message "You can go Trick-or-Treating".

# age = int(input("How old are you?: "))
# # Check age and display message
# if age >= 18:
#     print("You can vote")
# elif age == 17:
#     print("You can learn to drive")
# elif age == 16:
#     print("You can buy a lottery ticket")
# else:
#     print("You can go Trick-or-Treating")

# Ask the user to enter 1, 2, or 3. If they enter a 1, display the message "Thank you", if they enter a 2, display "Well done", 
# if they enter a 3, display "Correct". If they enter anything else display "Error message".


# user_name = input("Enter your name: ")
# for each_name in range (1, 35):
#     print("Your name is: ", user_name)

# user_name = input("Enter your name: ")
# for each_name in range (1, 6 + 1):
#     print("Your name is: ", user_name)

# Ask the user to enter their name and a number
# If the number is less than 10, then display their name that number of times;
# Otherwise display the message "Too high" three times.

user_name = input("Enter your name:" )
user_number = int(input("Enter the number of times: "))
if (user_number < 10 ):
    for each_name in range(1, user_number + 1):
        print(user_name)
else:
    for each_message in range (1, 4):
        print("Too High")
    
