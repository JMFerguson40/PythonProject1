###Test for GitHub

# Reptitive Task Function
def sum_of_squares(numbers):
    total = 0
    for num in numbers:
        total += num ** 2
    return total

my_numbers = [1, 2, 3, 4, 5]
result = sum_of_squares(my_numbers)
print(result) # Output: 55 (1 + 4 + 9 + 16 + 25)

#######################################################
#Example of breaking down a function into more manageable pieces

def read_data():
    data = []
    with open('data.txt', 'r') as file:
        for line in file:
            data.append(line.strip())
    return data

def process_data(data):
    processed_data = []
    for item in data:
        processed_data.append(item.upper())
    return processed_data

def save_data(processed_data):
    with open('processed_data.txt', 'w') as file:
        for item in processed_data:
            file.write(item + '\n')

def main():
    data = read_data()
    processed_data = process_data(data)
    save_data(processed_data)

main()
# In this example, the main() function is the entry point of the program. It calls three other functions: read_data(), process_data(), and save_data(). Each function is responsible for a specific task:
#
# read_data(): reads data from a file and returns it as a list of strings.
# process_data(): takes a list of strings as input, processes it and returns it as a list of processed data.
# save_data(): takes a list of processed data as input and saves it to a file.


#######################################################
##Implementing an algorithim

def bubble_sort(numbers):
    for i in range(len(numbers) - 1):
        for j in range(len(numbers) - i - 1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
    return numbers

my_numbers = [3, 7, 4, 1, 5, 2]
sorted_numbers = bubble_sort(my_numbers)
print(sorted_numbers) # Output: [1, 2, 3, 4, 5, 7]


#######################################################
##Validating input

def validate_age(age):
    if not isinstance(age, int):
        raise ValueError("Age must be an integer")
    if age < 0 or age > 120:
        raise ValueError("Age must be between 0 and 120")
    return True

try:
    age = int(input("Enter your age: "))
    validate_age(age)
    print("Age is valid")
except ValueError as e:
    print("Invalid age:", e)

#######################################################
##error handling

def divide(numerator, denominator):
    try:
        result = numerator / denominator
    except ZeroDivisionError:
        print("Error: Cannot divide by zero")
        return None
    else:
        return result

result = divide(10, 2)
print(result) # Output: 5.0

result = divide(10, 0)
print(result) # Output: Error: Cannot divide by zero

#######################################################
##Unit Testing
import unittest

def add(a, b):
    return a + b

class TestAdd(unittest.TestCase):
    def test_add_two_positive_numbers(self):
        result = add(3, 4)
        self.assertEqual(result, 7)

    def test_add_two_negative_numbers(self):
        result = add(-3, -4)
        self.assertEqual(result, -7)

    def test_add_positive_and_negative_numbers(self):
        result = add(3, -4)
        self.assertEqual(result, -1)

if __name__ == '__main__':
    unittest.main()