# def square (x):
#     return x**2

# li=eval(input("Enter the value:"))
# res=map(square,li)
# print(res)
# print(list(res))


# def square (a):
#     return a**2

# li=eval(input("ENter your value:"))
# res=map(square,li)
# print(res)
# print(list(res))


# def sqare (z):
#     return z**2

# li=eval(input("Enter the value:"))
# res=map(sqare,li)
# print(res)
# print(list(res))

# ----------------------------------------------------------------??--------------------------------------------
# Input from user
num = int(input("Enter a number: "))

# Step 1: Convert the number into a list of digits using map()
digits = list(map(int, str(num)))

# Step 2: Calculate the Armstrong sum using map()
armstrong_sum = sum(map(lambda x: x ** len(digits), digits))

# Step 3: Check if the sum is equal to the original number
if armstrong_sum == num:
    print(f"{num} is an Armstrong number")
else:
    print(f"{num} is NOT an Armstrong number")
