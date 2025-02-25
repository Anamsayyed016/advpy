# # chnage the internal workinf without change the code.
# # Special type of higher order function that can take function an argument it alse return function (where we change the behaviour).

# # Syn:-
#         # def outer(fun.)
#                 #def inner_fun(parameters)
#                   #modification
#         #return inner_fun
#         # def fun1(argument)
#         # 
#         # res=outer-fun(fun1)

# # def outer_fun(fun1):
# #     def inner_fun():
# #         print("Before modifi :")
# #         fun1()
# #         print("After modifi")
# #     return inner_fun

# # @outer_fun
# # def fun():
# #     print("this is from main")
# #     # res=outer_fun
# #     # fun()
# # fun()

# def outer_fun(fun1):
#     def inner_fun(r,s,t):
#         r=r+5
#         s=s+5
#         t=t+5
#         a=fun1(r,s,t)
#         print(a)
#     return inner_fun


# def fun(x,y,z):
#     return x+y+z
# res=outer_fun(fun)
# x=10
# y=10
# z=10
#     # res=outer_fun
#     # fun()
# res(x,y,z)
