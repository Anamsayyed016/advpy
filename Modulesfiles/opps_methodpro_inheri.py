# Inheritence------access parent class properties in child,code reuseabiliti,time saving, reduce-redendensy

class A:
    x=10
    y=20

    def home(self):
        print("have a home")

    def car(self):
        print("have a car")

class B(A):

    def newhome(self):
        print("New home")

obj=B()
obj.home()
print(B.x)
obj.car()
obj.newhome()