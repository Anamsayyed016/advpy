class Book:
    price=100
    total_pages=500

    def __init__(self,title,author):
        self.title=title
        self.author=author
    
    @classmethod
    def update(cls,new_price,new_pages_count):
        cls.price=new_price
        cls.total_pages=new_pages_count

    @classmethod
    def add_new(cls,author):
        cls.author=author

    def show_details(self):
        print(self.title,self.author,Book.price,Book.total_pages)

obj=Book('Python','Anam')
Book.update(110,550)
obj.show_details()


        