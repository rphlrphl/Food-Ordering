class Menu:
    __food_list = {}
    
    def __init__(self, ids, item, price):
        self.__ids = ids
        self.__item = item
        self.__price = price
        
    @classmethod
    def get_food_list(cls):
        return cls.__food_list.copy()
        
    @classmethod
    def _add_food(cls, ids, item, price):
        cls.__food_list[ids] = {'item': item, 'price': price}


class User:
    def __init__(self, name):
        self.__name = name
        
    def get_name(self):
        return self.__name
        
class Customer(User):
    def place_order(self):
        pass
    
class Admin(User):
    def add_food(self):
        food_id  = len(Menu.get_food_list())+1
        item = str(input("Enter food name: "))
        while True:
            try:
                price = float(input("Enter food price: "))
                break
            except Exception:
                continue
        Menu._add_food(food_id, item, price)
    
        

    
        


        
