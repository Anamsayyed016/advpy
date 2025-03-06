# Types of inheritence:-

# 1.Single Inheritance:-parent-----child

# 2.Multiple Inheritance:-parent1 parent2-----------------child

# 3.Multilevel Inheritance:-grand parent------parent------child1

# 4.Herarichical Inheritance:-parent-----child1----child2

# 5.Hybrid Inheritance:-
# -----------------------------------------------------------------------------------------
# Single Inheritance:-----

# class Parent:
#     x=10
#     def home(self):
#         print("Parent Home")

# class Child(Parent):
#     y=10
#     def car(self):
#         # print("Child car")
#         super().home
#         print("Child car")



# obj=Child()
# # print(obj.x)
# # obj.home()
# # obj.car()
# obj.home()

# ------------------------------------------------------------------------------------------------
# method overwriting---write same method in child---supoort overwriting---using supermethod
# does not support method over loading
# -------------------------------------------------------------------------------------------------

# Multiple Inheritance:-
# MRO:-method resoultion order--left firt technic

# class Parent1:
#     def home(self):
#         print("parent1 home")

# class Parent2:
#     def home(self):
#         print("parent2 home")

# class Child(Parent1,Parent2):
#     def car(self):
#         print("child car")


# obj=Child()
# obj.home()
# -------------------------------------------------------------------------------------

# Multilevel Inheritance:-


# class Grand_Parent:
#     def home(self):
#         print("parent1 home")

# class Parent(Grand_Parent):
#     def car(self):
#         print("parent2 home")

# class Child(Parent):
#     def new(self):
#         print("child new")


# obj=Child()
# obj.home()
# obj.new()
# obj.car()

# ------------------------------------------------------------------------------------------
# Herarichical Inheritance:-

# class Parent:
#     def home(self):
#         print("from parent class")

# class Child1(Parent):
#     def home(self):
#         # print("from child1 class")
#         super().home()
#         # Parent.home(self)----not needed

# class Child2(Parent):
#     def home(self):
#         print("from child2 class")
# obj1=Child1()
# obj1.home()
# obj2=Child2()
# obj2.home()

# -------------------------------------------------------------------------------------

# Hybrid Inheritance:-

# class Parent:
#     def home(self):
#         print("from parent class")

# class Child1(Parent):
#     def home(self):
#         print("from child1 class")
#         # super().home()
#         # Parent.home(self)----not needed

# class Child2(Parent):
#     def home(self):
#         print("from child2 class")

# class Child3(Child1,Child2):
#     def new(self):
#         print("from Child3")

# obj=Child3()
# obj.home()
# print(Child3.__mro__)

# overloading---py does not suppost---variabl lngth(*)---pass inlimuted value---tuple---args,key varable(**)---dict------eval----evloution---
# overriding


