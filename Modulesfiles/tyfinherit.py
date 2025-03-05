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

