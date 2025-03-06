def even(x):
    if x%2==0:
        return 'even'
    else:
        return 'odd'
    
    l1=[2,8,7,10]
    res=map(even,l1)
    print(res)
    print(tuple(res))