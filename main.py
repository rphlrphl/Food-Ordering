"""
TO DO LIST:
- place orders (customer class)
- separate class for processing orders
- interaction class (as much as possible, separate classes for customers and admin)
"""

class MenuList:
    def __init__(self, item, price):
        self.__item = item
        self.__price = price
        
    def get_item(self):
        return self.__item
        
    def get_price(self):
        return self.__price
        
    def __str__(self):
        return f"{self.__item}: ${self.__price}"

class User:
    def __init__(self, name):
        self.__name = name
        
class Customer(User):
    def display_menu(self):
        for i in range(len(menu)):
            print(f"[{i}]: {menu[i]}")
            
    def place_order(self):
        pass
            
class Admin(User):
    def add_item(self):
        item = str(input("Enter the name of the item: "))
        while True:
            try:
                price = float(input("Enter the price of the item: "))
                break
            except Exception: print()
        menu.append(MenuList(item, price))
    
menu = [
    MenuList('Fries', 9.99),
    MenuList('Burger',19.99),
    MenuList('Fried Chicken', 29.99)
    ]
