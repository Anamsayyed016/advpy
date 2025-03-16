def palindrome(num):
    yield num == num [::-1]

string=input("Enter the string:")

if next(palindrome(string)):
    print(f"{string} is a palindrome")

else:
    print(f"{string}is not palindrome")