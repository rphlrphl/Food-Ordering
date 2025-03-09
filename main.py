class Menu:
    __food_list = {1:{'item':'Adobo','price':65},2:{'item':'Caldereta','price':65}}
    
    def __init__(self, ids, item, price):
        self.__ids = ids
        self.__item = item
        self.__price = price
        
    @classmethod
    def get_food_list(cls):
        return cls.__food_list.copy()
    
    @classmethod   
    def display_menu(cls): # This function will print out the available foods.
        if not cls.__food_list:
            print("No items available.")
            return
        print("Menu:")
        for ids, details in cls.__food_list.items():
            print(f"[{ids}]: {details['item']}, P{details['price']}")
        
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
        print("----- PLACE ORDER [customer] -----")
        print('Enter the item id to order ([#] --> ID)')
        Menu.display_menu()
        food_order_ids = []
        print("Press 0 to cancel.")
        while True:
            try:
                orders = int(input("Enter food id: "))
                if orders > len(Menu.get_food_list()) or orders < 0:
                    print('ID Not Available')
                elif orders == 0:
                    print('Order Cancelled')
                    break
                else: 
                    food_order_ids.append(orders)
                    print('') # ADD KO MAYA
                    
            except Exception:
                print('')
        return
    
class Admin(User):
    def add_food(self):
        while True:
            print("----- ADD FOOD [admin] -----")
            print("Enter blank character to cancel.")
            food_id  = len(Menu.get_food_list())+1
            item = str(input("Enter food name: "))
            if not item:
                print("No item added.")
                break
            while True:
                try:
                    price = float(input("Enter food price: "))
                    break
                except Exception:
                    continue
            if not food_id or not item or not price:
                print("No item added.")
            else:
                Menu._add_food(food_id, item, price)
                break
        return
        
# class OrderProcessor: # to be updated
#     def process_order
        
# Admin('test').add_food()
# Menu.display_menu()

Customer('test').place_order()    
