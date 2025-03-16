# HYBRID INHERITENCE

class Parent:
    def home(self):
        print("from parent class")

class Child1(Parent):
    def home(self):
        print("from child1 class")
        super().home()

class Child2(Parent):
    def home(self):
        print("from child2 class")

class Child3(Child1,Child2):
    def new(self):
        print("from child3")


obj=Child3()
obj.home()
print(Child3.__mro__)