# Write a program that reads in integer numbers from a text file named indata.txt in the same directory as the executing program.
# Print the sum of the numbers with comma separators and two digits.
# For example if the file has the following data:
# 10
# 1000
# 20
# Your program should print 1030.00.


def read_numbers_from_file(filename):
    with open(filename, 'r') as file:
        numbers = [int(line.strip()) for line in file]
    return numbers

def print_sum_with_comma_separator(numbers):
    total = sum(numbers)
    formatted_total = '{:,.2f}'.format(total)
    print(formatted_total, end="")

def main():
    numbers = read_numbers_from_file('indata.txt')
    print_sum_with_comma_separator(numbers)

if __name__ == "__main__":
    main()
