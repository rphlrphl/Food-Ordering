"""
TO DO LIST:
- place orders (customer class)
- separate class for processing orders
- interaction class (as much as possible, separate classes for customers and admin)
"""

class MenuList:
    food_menu = {}
    def __init__(self, id, item, price):
        self.__id = id
        self.__item = item
        self.__price = price
        
    def get_id(self):
        return self.__id
        
    def get_item(self):
        return self.__item
        
    def get_price(self):
        return self.__price
        
    def update_menu(self):
        self.food_menu.update({self.__id:{'item':self.__item,'price':self.__price}})
        
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
        menu = MenuList((len(MenuList.food_menu) + 1), item, price)
        menu.update_menu()

print(MenuList(00,00,00).food_menu)
Admin('test').add_item()    
print(MenuList(00,00,00).food_menu)


# menu = [
#     MenuList('Fries', 9.99),
#     MenuList('Burger',19.99),
#     MenuList('Fried Chicken', 29.99)
#     ]
