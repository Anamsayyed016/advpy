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
# --------------------------------------------------------------------------------

# having error

# class Student:
#     school_name = "Leo"

#     def __init__(self,name,roll):
#         self.x = name
#         self.y = roll
    
#         Student.s_code="123"
    
#     def new_sec(self):
#         Student.classes="p37"
    
#     def show(self):
#         print(Student.school_name,Student.s_code,Student.classes,Student.subject)

# Student.subject="fsd"
# obj=Student("anam",101)
# obj.show()
# obj.new_sec()
# ____________________________________________________________________________________________

class Book:
    price = 100
    total_pages = 500

    def __init__(self, title, author):
        self.title = title
        self.author = author

    @classmethod
    def update(cls, new_price, new_page_count, author2):
        cls.price = new_price
        cls.total_pages = new_page_count
        cls.author2 = author2
    
    @classmethod
    def add_new(cls, author):
        cls.author2 = author
    
    def show_data(self):
        print(self.title, self.author, Book.price, Book.total_pages)
    
    def show_details(self):
        print(self.title, self.author, Book.price, Book.total_pages)

obj = Book('Python', 'Anam')
Book.update(110, 555, 'Author 2')  # Added third argument
obj.show_details()
price = Book.price
print(price)



        