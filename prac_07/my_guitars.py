import csv

from prac_07.guitar import Guitar

guitar_list = []
def main():
    """Read file of programming language details, save as objects, display."""
    in_file = open('guitars.csv', 'r')
    in_file.readline()
    for line in in_file:
        # print(repr(line))  # debugging
        parts = line.strip().split(',')
        # print(parts)  # debugging
        language = Guitar(parts[0],parts[1], parts[2])
        guitar_list.append(language)

    in_file.close()
    guitar_list.sort()
    for guitar in guitar_list:
        print(guitar)
main()