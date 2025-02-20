# LAMDA:-
# A function that doesn't have  any name(ananymous function).
# Here, function define with lamba keyword instead of def.
# It takes n number of argument and excute only one expression.
# excute only single line expression.
# Syn:- Lamba arguemt: expression

# add = lambda x,y :print(x+y)
# p=int(input("Enter your value :"))
# q=int(input("Enter your value :"))
    
# add(p,q)

# add = lambda x,y :(x+y)
# p=int(input("Enter your value :"))
# q=int(input("Enter your value :"))
    
# print(add(p,q))
# ------------------------------------
# Evan and odd:-

# syn:-lamda with if-else
# lamda argument : res_of_if if (cond.) else (res_of_else)

# n=int(input("Enter your value :"))
# check_number = lambda x:'even_no' if x%2==0 else 'odd_no'
# print (check_number(n))

# POSETIVE , NEGATIVE , OR ZERO:-

# n=int(input("Enter your value :"))
# check_num=lambda x:("+ve" if n>0 else "-ve" if x<0 else "zero")
# print(check_num(n))

# Collection genrate lamda for :-
# syn:-lamda:[iteam for item in range]

# n=lambda p:[i for i in range(p)]
# p=int(input("enter your value: "))
# print(n(p))

# x=lambda p,q:[[r for r in range(p) ] for i in range (q)]
# p=int(input("Enter how many collection required :"))
# q=int(input("Enter how many repetation required :"))
# print(x(p,q))

# x=lambda str1,q:[str1 for i in range (q)]
# str1=input("Enter how many collection required :")
# q=(input("Enter how many repetation required :"))
# print(x(str1,q))

