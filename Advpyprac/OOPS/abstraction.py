# ABSTRACTION:- Hiding internal process----
# from abc import ABC,abstractmethod
# class BankApp(ABC):
#     def login(self):
#         print("User Login")
    
#     def logout(self):
#         print("LogOut")

#     def UserData(self):
#         print("User Data")
    
#     @abstractmethod
#     def database(self):
#         pass

# class WebPage(BankApp):
#     def database(self):
#         print("DataBase Connected")

# obj=WebPage()
# obj.database()
# obj.login()
# obj.UserData()
# obj.logout()
# -------------------------------------------------------------------------------------------
# from abc import ABC, abstractmethod
# class BankApp(ABC):
#     def UserLogin(self):
#         print("User Login")
    
#     def UderLogout(self):
#         print("User Logout")

#     def UserDetails(self):
#         print("User Details")
#         pass
#     @abstractmethod
#     def Database(self):
#         pass

# class Webpage(BankApp):
#     def Database(self):
#         print("DataBase Connected")

# obj=Webpage()
# obj.Database()
# obj.UserDetails()
# obj.UserLogin()
# obj.UderLogout


