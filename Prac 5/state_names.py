"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""

# TODO: Reformat this file so the dictionary code follows PEP 8 convention
state_names = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
               "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania", "SA": "South Australia"}


def print_all_states():
    for name in state_names:
        length = len(state_names[name])
        print(f"{name:3} is {state_names[name]:{length}}")


print(state_names)
print_all_states()

state_code = input("Enter short state: ").upper()
while state_code != "":
    try:
        print(state_code, "is", state_names[state_code])
        state_code = input("Enter short state: ").upper()
    except KeyError:
        print("Invalid short state")
        state_code = input("Enter short state: ").upper()
# while state_code != "":
#     if state_code in state_names:
#         print(state_code, "is", state_names[state_code])
#     else:
#         print("Invalid short state")
#     state_code = input("Enter short state: ").upper()
