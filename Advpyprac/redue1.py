import functools

li=[2,14,10,20]
def my_max(x,y):
    if x<y:
        return x
    else:
        return y
    
res=functools.reduce(my_max,li)
print(res)