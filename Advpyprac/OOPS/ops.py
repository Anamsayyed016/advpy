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

# class Student:
#     '''student details'''
#     def __init__(self):
#         print("contructor called")
#         print("Self:",id(self))

# obj=Student()
# print(id(obj))
# _____-----------------------------------------------------------------------

# class Student:
#     '''student details'''
#     def __init__(self):
#         print("contructor called")
#         print("self id",id(self))
# obj=Student()
# print(id(obj))
# ----------------------------------------------------------------------------------

# class Student:
#     '''student details'''
#     def __init__(self,name,roll,marks):
#         self.x = name
#         self.y = roll
#         self.z = marks

# obj=Student("Anam",100,63)

# print(obj.x)
# print(obj.y)
# print(obj.z)
# ----------------------------------------------------------------------------
# class Employee:
#     '''Employee details'''
#     def __init__(self,name,id_number,employee_number):
#         self.x = name
#         self.y = id_number
#         self.z = employee_number
# obj=Employee("Anam",10002,455213687)
# print(obj.x)
# print(obj.y)
# print(obj.z)
# ---------------------------------------------------------------------------------
# class People:
#     '''People Details'''
#     def __init__(self,name,occupation,salry):
#         self.p = name
#         self.q = occupation
#         self.r = salry
# obj=People("Anam","FSP",40000)
# print(obj.p)
# print(obj.q)
# print(obj.r)
# ==================================================================================

# class Student:
#     '''student details'''
#     def __init__(self,name,roll_number,marks):
#         self.x = name
#         self.y = roll_number
#         self.z = marks
        
#     def __init__(self):   
#         print("Contructor Called")

# obj=Student()     
# --------------------------------------------------------------------------
# class Employee:
#     '''employee details'''
#     def __init__(self,name,occupation,salry):
#         self.x = name
#         self.y = occupation
#         self.z = salry
#     def __init__(self):
#         print("constructor called")

# obj=Employee()
# ----------------------------------------------------------------------------

# class Student:
#     def __init__(self,name,roll,marks):
#         self.x = name
#         self.y = roll
#         self.z = marks
# obj=Student()    
# obj=Student("Anam",101,75)
# obj=Student("Anam",101,75)
# obj=Student("Anam",101,75)
# -----------------------------------------------------------------------

# class Student:
#     def __init__(self,name,rol,marks):

#         self.x = name
#         self.y = rol
#         self.z = marks
#     def show(self,city):
#         self.p=city

# obj = Student("Anam",102,85)
# obj.show('Bhopal')
# print(obj.p)
# print(obj.x)
# print(obj.y)
# print(obj.z)
# -------------------------------------------------------------------------------

# INSTANCE VARIABLE:-

# class Student:
#     def __init__(self,name,roll,marks):
#         self.x = name
#         self.y = roll
#         self.z = marks

#     def add_new(self,city):
#         self.p = city
    
#     def show(self):
#         print(self.x, self.y, self.z, self.p,self.school_name)

# obj=Student('Anam',101,85)
# obj.school_name="SHAA"
# obj.add_new('bhopal')
# obj.show()
# print(obj.x,obj.y,obj.z,obj.p)
# -----------------------------------------------------------------------------

# STATIC VARIABLE/CLASS:
# class Student:
#     School = 'SHSS' 
#                                 # ---declartation of static variable----
#     def __init__(self,name,roll_number):
#         self.x = name
#         self.y = roll_number
#                                  # ---declartation of static variable----

#         Student.s_code=123

#     def new(self):
#         Student.city="Bhopal"
#                                     # ---declartation of static variable----
    
#     def show(self):
#         print(Student.School,Student.s_code,Student.city,Student.subject)
        
# Student.subject="pcm"
# obj=Student('Anam',101)
# obj.new()
# obj.show()
# print(obj.x,obj.y)
# --------------------------------------------------------------------------------------

# @CLASSMETHOD:-

# class Book:
#     price = 100
#     total_pages = 500

#     def __init__(self,title,author):
#         self.title = title
#         self.author = author

#     @classmethod
#     def update (cls,new_price,new_page_count,author2):
#         cls.price= new_price
#         cls.total_pages=new_page_count
        
    
#     @classmethod
#     def add_new(cls,author):
#         cls.author2=author
    
    
    
#     def  show_details(self):
#         print(self.title,self.author,Book.price,Book.total_pages)
    
# obj=Book('python','Anam',)
# Book.update(110,555,"ALi")
# obj.show_details()
# price=Book.price



        




