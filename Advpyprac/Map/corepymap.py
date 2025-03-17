# Write a program to check if a given number is an Armstrong number using map.

# num = int(input("Enter a number: "))
# digits = list(map(int, str(num)))
# armstrong_sum = sum(map(lambda x: x**len(digits), digits))

# if armstrong_sum == num:
#     print(f"{num} is an Armstrong number.")
# else:
#     print(f"{num} is not an Armstrong number.")
# ----------------------------------------------------------------------------
# Write a program to check if the given string is a palindrome using map.

# s = input("Enter a string: ")
# if list(s) == list(map(str, reversed(s))):
#     print("Palindrome")
# else:
#     print("Not a palindrome")
# -----------------------------------------------------------------------------
# Write a program to get the Fibonacci series. map-

# n = int(input("Enter number of terms: "))
# fib = [0, 1]
# list(map(lambda _: fib.append(fib[-1] + fib[-2]), range(n - 2)))
# print(fib[:n])
# ---------------------------------------------------------------------------

# Write a program to find the factorial of a given number map?
# ------------------------------------------------------------------

# Write a program to create calculator through functions using map?

                  # Define functions for basic operations
# def add(x, y): return x + y
# def subtract(x, y): return x - y
# def multiply(x, y): return x * y
# def divide(x, y): return x / y if y != 0 else 'Cannot divide by zero'

#                 # Create a dictionary of operations
# operations = {
#     '+': add,
#     '-': subtract,
#     '*': multiply,
#     '/': divide
# }

#                     # Take user input
# x = float(input("Enter first number: "))
# y = float(input("Enter second number: "))
# op = input("Enter operator (+, -, *, /): ")

#                     # Use map() to apply the operation
# result = list(map(lambda func: func(x, y) if op in operations else 'Invalid operator', [operations.get(op)]))[0]

# print(f"Result: {result}")
# -----------------------------------------------------------------------------------------

# Write a program to check given year is leep year or not. using map

# year = int(input("Enter a year: "))

#             # Use map to check leap year condition
# result = list(map(lambda y: (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0), [year]))[0]

# if result:
#     print(f"{year} is a leap year.")
# else:
#     print(f"{year} is not a leap year.")

# --------------------------------------------------------------------------------
# Write a program to check if the given strings are anagram or not using map

            # Function to check if two strings are anagrams
# def is_anagram(s1, s2):
#     return sorted(map(str, s1)) == sorted(map(str, s2))

#             # Input strings
# s1 = input("Enter first string: ").lower()
# s2 = input("Enter second string: ").lower()

#                 # Check anagram
# if is_anagram(s1, s2):
#     print(f"{s1} and {s2} are anagrams.")
# else:
#     print(f"{s1} and {s2} are not anagrams.")
# -----------------------------------------------------------------------

# Python program to check if a given number is a Harshad number (Niven number) using map():


                        # Function to check Harshad number
# def is_harshad(num):
#     digit_sum = sum(map(int, str(num)))
#     return num % digit_sum == 0

#                             # Input from user
# num = int(input("Enter a number: "))

#                             # Check if Harshad number
# if is_harshad(num):
#     print(f"{num} is a Harshad number.")
# else:
#     print(f"{num} is not a Harshad number.")
# --------------------------------------------------------------------------------

# Write a program to check given number is neon number or not using map?

            # Function to check Neon number
# def is_neon(num):
#     square = num ** 2
#     digit_sum = sum(map(int, str(square)))
#     return digit_sum == num

#                 # Input from user
# num = int(input("Enter a number: "))

#                 # Check if Neon number
# if is_neon(num):
#     print(f"{num} is a Neon number.")
# else:
#     print(f"{num} is not a Neon number.")
# --------------------------------------------------------------------------------------------

# Write a program to check given number is Peterson number or not using map?





