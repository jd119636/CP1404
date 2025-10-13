"""
CP1404/CP5632 - Practical
Program for temperature conversion
"""
def temperature_to_celsius():
    temp = (float(input("Enter the temperature in Farrenheit: ")))
    final_temp = ((temp - 32) * 5/9)
    print(final_temp)

def temperature_to_fahrenheit():
    temp = (float(input("Enter the temperature in Celsius: ")))
    final_temp = ((temp * 9) / 5) + 32
    print(final_temp)

MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""
print(MENU)
choice = input(">>> ").upper()
while choice != "Q":
    if choice == "C":
        temperature_to_fahrenheit()
    elif choice == "F":
        temperature_to_celsius()
    else:
        print("Invalid option")
    print(MENU)
    choice = input(">>> ").upper()
print("Thank you.")
