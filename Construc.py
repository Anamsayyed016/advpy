# Constructor:-
# class Student:
#     '''Student Details'''
#     name="Anam"
#     quali='MBA'

# print(dir(Student))

# print(Student.__doc__)
# print(Student)
# obj=Student()
# print(obj)

# x=Student()
# print(x)

# __init__----special type

# class Student:
#     ''' studen det'''

#     def __init__(self):
#         print("Constructor called")
#         print("self :",id(self))

# # obj = Student---no ouput
# obj= Student()
# print(id(obj))

# class Student:
#     ''' studen det'''
#     def __init__(self,name,rol,marks):
#         self .x = name
#         self .y = rol
#         self .z = marks
# obj=Student("Anam",106,80)
# print(obj.x)
# print(obj.y)
# print(obj.z)

# Constructor:- is a special type of method that called automatically when object created
# Self:- is a reference variable that holds address of current obj of current class.

class Student:
    ''' studen det'''
    def __init__(self,name,rol,marks):
        self .x = name
        self .y = rol
        self .z = marks
    def __init__(self):
        print("Constructor called")
obj=Student()
obj.__init__()