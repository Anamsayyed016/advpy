# LAMDA:-
# A function that doest have any name(ananymous function)
# In this funtion define with lamda keyword instead of def
# In this it takes number of argument and excute only one statement
# In this excute only one line expression
# ---------------------------------------------------
# add = lambda x,y : print(x+y)
# p=int(input("Enter any number:"))
# q=int(input("Enter any number:"))
# --------------------------------------------
# square = lambda x,y :print(x*y)
# p=int(input("Enter any number:"))
# q=int(input("Enter any number:"))
# square(p,q)
# ---------------------------------------------------

# n=int(input("Enter any number:"))
# check_num = lambda x:'even_no' if x%2==0 else 'odd_no'
# print(check_num(n))

# --------------------------------------------------------

# n= lambda p:[i for i in range(p)]
# p=int (input("Enter Your value:"))
# print(n(p))
# ----------------------------------------------------------

# x=lambda p,q:[[r for r in range(p) ]for i in range(q)]

# p=int(input("Enter how many collection required:"))
# q=int(input("Enter how many reptation required:"))

# print(x(p,q))
# ==========================================================

# c=lambda a,b:[[r for r in range (a)]for i in range (b)]
# p=int(input("Enter the collection:"))
# q=int(input("How many repetation:"))
# print(c(p,q))
# -----------------------------------------------------------------

# x=lambda str1,q:[str1 for i in range(q)]
# str1=(input("how many collection:"))
# q=int(input("how many repetation:"))
# print(x(str1,q))