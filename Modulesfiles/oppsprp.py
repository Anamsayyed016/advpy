# Abstraction=>----hiding internal process
# Encapsulation
# Inheritence------access parent properties in child,code reuseabiliti,time saving, reduce-redendensy
# Polymorphism
# -------------------------------------------------------------------------------------


# Abstraction=>----hiding internal process---abstact class and method logic--for privacy/security
# decalre method not implimention
# write code in child
# restriction in parent class throgh abstraction
# imporct module

from abc import ABC , abstractmethod

class BankApp(ABC):
    def login (self):
        print("User Login")
        
    def logout(self):
        print("User Logout")

    def User_detail(self):
        print("User Detail")

    @abstractmethod
    def database(self):
        pass

class webpage(BankApp):
    def database(self):
        print("database connected")

obj=webpage()
obj.database()
obj.login()
obj.User_detail()
obj.logout()
    