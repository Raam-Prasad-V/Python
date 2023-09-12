
def print_positive_numbers(numbers):
    positive_numbers = [num for num in numbers if num > 0]
    
    if positive_numbers:
        print("Output:", positive_numbers)
    else:
        print("There are no positive numbers in the list.")

input_str = input("Input: list = ")
try:
    input_list = [int(x) for x in input_str.split(',')]
    print_positive_numbers(input_list)
except ValueError:
    print("Invalid input. Please enter a list of comma-separated numbers.")
