# change the internal working without change the code
# special type of higher order function that can take function as argument and it is also return function.
# in this we change the behaviour

# def outer_fun(fun1):
#     def inner_fun():
#         print("before modifi.")
#         fun1()
#         print("after modifi.")

#     return inner_fun
    
# @outer_fun
# def fun():
#     print("this is from main")
#     res=outer_fun
# fun()
# ----------------------------------------------------------
# def outer_fun(fun1):
#     def inner_fun():
#         print('befor modifi')
#         fun1()
#         print('after modifi')

#     return inner_fun
# @outer_fun
# def fun():
#     print('this is from main')
#     res=outer_fun
# fun()
# ------------------------------------------------------

# def outer_function(fun1):
#     def inner_function():
#         print('before modifi')
#         fun1()
#         print('after modifi')
    
#     return inner_function

# @outer_function
# def function1():
#     print("this is user data")
#     res=outer_function
# function1()
# ---------------------------------------------------------