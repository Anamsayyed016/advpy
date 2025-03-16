# def square(x):
#     return x**2
# li=eval(input("Enter your number:"))
# res=map(square,li)

# print(res)
# print(list(res))
# ---------------------------------------------------------

# def square(num):
#     return num**2

# li=eval(input("Enter your number:"))
# res=map(square,li)
# print(res)
# print(list(res))
# ----------------------------------------------------------

# def square(num):
#     return num**2

# li=eval(input("Enter your number:"))
# res=map(square,li)
# print(res)
# print(list(res))

# -----------------------------------------------------------------

# def add(x,y,z):
#     return x+y+z

# l1=eval(input("Enter your number:"))
# l2=eval(input("Enter your number:"))
# l3=eval(input("Enter your number:"))

# res=map(add,l1,l2,l3)
# print(list(res))
# ----------------------------------------------------------------------

# def add(x,y,z):
#     return x+y+z

# li=eval(input("Enter your number:"))
# li=eval(input("Enter your number:"))
# li=eval(input("Enter your number:"))

# res=map(add,li,li,li)
# print(res)
# print(list(res))
# ----------------------------------------------------------------------

# def power(x,y):
#     return x*y

# li=eval(input("Enter your number :"))
# li=eval(input("Enter your number :"))

# res=map(power,li,li)
# print(res)
# print(list(res))
# ------------------------------------------------------------------------
# ARMSTRONG:-


def armstrong(num):
    length = len(str(num))
    digits = map(int,str(num))
    armstrong_sum = sum(map(lambda x:x**length,digits))

    return armstrong_sum == num

num = int(input("Enter your number: "))

if armstrong(num):
    print(f"{num} is a armstrong")

else:
    print(f"{num} is not a armstrong ")