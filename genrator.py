# def even(n):
#     i=0
#     while i<=n:
#         if i%2==0:
#             print(i)
#         i=i+1
# x=even(10)
# print(x)
# print(type(x))   


# def new():
#     return "Anam"

# # x=new()
# # print(x)
# # print(type(x))

# generator is a specil type of funtion that can be use to genearte iterator---(use one by one) object.
# Instead of return keyword, [yeild] keyworf use and return object.

# def new():
#     yield 10

# x=new()
# # print(list(x))
# # print(x.__next__())
# print(next(x))

def even(n):
    i=0
    while i<=n:
        if i%2==0:
            yield i
        i=i+1
res=even(10)
# print(res)
# print(list(res))
# x=next(res)
# y=next(res)
# z=next(res)
# print(x,y,z)
x=next(res)
for i in range(x):
    print(i)
print(next(res))
print(next(res))

