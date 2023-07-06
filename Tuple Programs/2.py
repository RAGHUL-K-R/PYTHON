def filter_positive_numbers(numbers):
    positive_numbers = tuple(num for num in numbers if num > 0)
    return positive_numbers
input_str = input("Enter a list of numbers (space-separated): ")
numbers = [int(num) for num in input_str.split()]
positive_tuple = filter_positive_numbers(numbers)
print(positive_tuple)
