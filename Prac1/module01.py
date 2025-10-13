
# name = input("Hello: ")
# print("Hello", name)

# monthly_cost = float(input("Monthly cost: "))
# total_cost = monthly_cost * 12
# print(f"The total is ${total_cost:.2f}")


# age = int(input("Enter your age: "))
# while age < 0 or age > 150:
#     print("Invalid age")
#     age = int(input("Enter your age: "))
#
# if age >= 66:
#     category = ("old")
# elif age >= 18:
#     category = ("Adult")
# elif age >= 5:
#     category = ("Child")
# else:
#     category = ("Baby")
# print(f"Your age {age} is considered {category}")


# secret_number = 5
# input_number = int(input("Enter a number from 1 - 10: "))
# while input_number != secret_number:
#     print("Guess again ")
#     input_number = int(input("Enter a number from 1 - 10: "))
# print("You Win")

# for i in range(1, 5):
#     print (i)

# name = "Indra"
# for character in name:
#     print (character)
#

# def print_line(length):
#     print('-' * length)
#
# print_line(30)

# def print_grid(number_of_rows, number_of_columns):
#     for i in range(number_of_rows):
#         print("*"*number_of_columns)
#
# print_grid(3, 7)


# def get_limits():
#     low = int(input("enter lower limit: "))
#     high = int(input("enter upper limit: "))
#     return low, high, -1
# thing = get_limits()
# print(thing)
# print(type(thing))
#

# import random
# def print_secret_name(name):
#     letters = list(name)
#     random.shuffle(letters)
#     print("".join(letters))
#
# def display_menu():
#     print("\nMenu:")
#     print("G - get Valid Non Empty Name")
#     print("P - Hello")
#     print("S - Print Secret name")
#     print("Q - Quit")
#
# def get_name():
#     name = input("Enter your name: ")
#     while name == "":
#         print("Name cannot be blank")
#         name = input("Enter your name: ")
#     return name
# def print_line(length):
#     print("-" * length)
#
#
# display_menu()
# choice = input("\n Which option would you like to choose: ").upper()
#
#
# def Print_greeting():
#     Length= (len(name)+6)
#     print_line(Length)
#     print(f"Hello {name}")
#     print_line(Length)
#
#
# while choice != "Q":
#     if choice == "G":
#         name = get_name()
#         display_menu()
#         choice = input("Which option would you like to choose: ").upper()
#     elif choice == "P":
#         Print_greeting()
#         display_menu()
#         choice = input("Which option would you like to choose: ").upper()
#     elif choice == "S":
#         print_secret_name(name)
#         display_menu()
#         choice = input("Which option would you like to choose: ").upper()
#     else:
#         print("Invalid choice")
#         display_menu()
#         choice = input("Which option would you like to choose: ").upper()
# print("Thank you for playing")


# def print_line (length, pen = '-'):
#     print(pen*length)
#
# print_line(5)
#

