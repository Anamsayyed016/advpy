# # GENERATOR:-
# # generator is a special type of funtion that create itrable using obj
# # In this we use special type of keyword which is Yeild

# # def even(n):
# #     i=10
# #     while i<=n:
# #         if i%2 == 0:
# #             print(i)

# #             i=i+1
# # x=even(10)
# # print(x)
# # print(type(x))
# # ------------------------------------------------------------------------

# # def new():
# #     return "Anam"

# # x=new()
# # print(x)
# # print(type(x))
# # -------------------------------------------------------------------------------

# # def new():
# #     yield 10

# # x=new()
# # print(list(x))
# # x=new()
# # print(x.__next__())
# # print(next(x))
# # -------------------------------------------------------------------------

# def even (n):
#     i=0
#     while i<=n:
#         if i%2==0:
#             yield i
#             i=i+1
    
# res = even(10)
# print(res)
# print(list(res))

# # x=next(res)
# # y=next(res)
# # z=next(res)

# # print(x,y,z)
# # x=next(res)

# # for i in range(x):
# #     print(i)

# # print(next(res))

