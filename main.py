"""
TO DO LIST:
- place orders (customer class)
- separate class for processing orders
- interaction class (as much as possible, separate classes for customers and admin)
- fix encapsulation
"""

class Menu:
    __food_list = {}
    
    def __init__(self, ids, item, price):
        self.ids = ids
        self.item = item
        self.price = price
        
    def get_food_list(self):
        return Menu.__food_list.copy()
        
    def add_food(self):
        Menu.__food_list[self.ids] = {'item': self.item, 'price': self.price}


class User:
    def __init__(self, name):
        self.__name = name
        
    def get_name(self):
        return self.__name
        
class Customer(User):
    def place_order(self):
        pass
    
class Admin(User):
    def add_food(self, ids, item, price):
        new_food = Menu(ids, item, price)
        new_food.add_food()
        
