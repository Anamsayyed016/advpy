# class Student:
#     '''Student Details'''
#     name="Anam"
#     quali="MBA"

# # print(dir(Student))

# # print(Student.__doc__)

# # x=Student
# # print(obj)

# x=Student()
# print(x)

# -----------------------------------------------------

# class Student:
#     '''student details'''
#     def __init__(self):
#       print("contructor called")
 
# obj=Student()
# ------------------------------------------------------------

class Student:
    '''student details'''
    def __init__(self):
        print("contructor called")
        print("Self:",id(self))

obj=Student()
print(id(obj))