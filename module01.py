
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
#
# def print_line(length):
#     print("-" * length)
#
# def Print_greeting():
#     Length= (len(name)+6)
#     print_line(Length)
#     print(f"Hello {name}")
#     print_line(Length)
#
#
#
# display_menu()
# choice = input("\n Which option would you like to choose: ").upper()
#
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
#



# def print_line (length, pen = '-'):
#     print(pen*length)
#
# print_line(5)


# FILENAME = "secret.txt"
#
#
# def main():
#     secret = load_number(FILENAME)
#     guess = get_valid_number()
#     while guess != secret:
#         print("Guess again")
#         guess = get_valid_number()
#     print("you got it")
#
# def get_valid_number():
#     is_valid_input = False
#     while not is_valid_input:
#         try:
#             guess = int(input("Guess a number: "))
#             is_valid_input = True
#         except ValueError:
#             print("Invalid integer")
#     return guess
#
# get_valid_number()
#
# def load_number(filename):
#     try:
#         infile = open(filename, "r")
#         number = int(infile.read())
#     except ValueError:
#         print(f"Invalid number in {filename}")
#         number = 6
#     except FileNotFoundError:
#         print(f"File {filename} not found")
#         number = 4
#     else:
#         infile.close()
#     return number
#
# main()


# line = "Indra Kiiver...."
# line.strip('.')
# print (line.strip())

# infile = open("SECRET.md")
# infile.readlines("#")
# infile.close()

# with open("data.txt", "r") as infile:
#     infile.readline()   #ignore header
#     for line in infile:
#         # print(line)
#         parts = line.strip().split(',')
#         # print(parts)
#
#         name = parts[0]
#         age = int(parts[1])
#         print(f"{name} will be {age+1} years old next year")

# infile = open("dataset.txt","r")
# for line in infile:
#     parts = line.strip("\n").split(',')
#     name = parts[0]
#     age = int(parts[1])
#     cost = float(parts[2]).strip("\n")
#     print(f"{name} was made in {age} and costs {cost}.")

# names = ("Craig", "Michael", "Terrance", "Philip")
# number = int(input(f"Enter number up to {len(names)}:"))
# try:
#     print(names[number-1])
# except IndexError:
#     print("Invalid input.")

# from operator import itemgetter
# data = [['Derek', 7], ['Carrie', 8],['Bob', 6], ['Aaron', 9] ]
# # data.sort()
# data.sort(key=itemgetter(1), reverse = True)
# for record in data:
#     print(data)

# score_pairs = [['Derek', 7], ['Carrie', 8], ['Bob', 6]]
# data = input ("Enter a name and score:")
# parts = data.split()
# score_pairs.append(parts)
# print(score_pairs)

# fruit = ['orange', 'apple', 'pear', 'banana']
# balls = "-{}- {}".format(*fruit)
# print(balls)
