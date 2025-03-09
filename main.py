class ItemList:
    __item_list = {1:{'item':'A4Tech Mouse','price':1000},2:{'item':'A4Tech Keyboard','price':1000}}
    
    def __init__(self, ids, item, price):
        self.__ids = ids
        self.__item = item
        self.__price = price
        
    @classmethod
    def get_item_list(cls):
        return cls.__item_list.copy()
    
    @classmethod   
    def display_items(cls): # This function will print out the available items.
        if not cls.__item_list:
            print("No items available.")
            return
        print("Menu:")
        for ids, details in cls.__item_list.items():
            print(f"[{ids}]: {details['item']}, P{details['price']}")
        
    @classmethod
    def _add_item(cls, ids, item, price):
        cls.__item_list[ids] = {'item': item, 'price': price}

class User:
    def __init__(self, name):
        self.__name = name
        
    def get_name(self):
        return self.__name
            
class Customer(User):
    def __init__(self, name, order_manager):
        super().__init__(name)
        self.order_manager = order_manager

    def start_order(self):
        print("----- PLACE ORDER [customer] -----")
        print('Enter the item id to order ([#] --> ID)')
        ItemList.display_items()
        print("Press 0 to cancel.")
        self.order_manager.select_item()

class Admin(User):
    def __init__(self, name, role_selection):
        super().__init__(name)
        self.role_selection = role_selection

    def add_item(self):
        while True:
            print("----- ADD ITEM [admin] -----")
            print("Enter blank character to cancel.")
            item_id  = len(ItemList.get_item_list())+1
            item = str(input("Enter item name: "))
            if not item:
                print("No item added.")
                break
            while True:
                try:
                    price = float(input("Enter item price: "))
                    break
                except Exception:
                    continue
            if not item_id or not item or not price:
                print("No item added.")
            else:
                ItemList._add_item(item_id, item, price)
                break
        self.role_selection.input_name()
        
class OrderManager:
    def __init__(self, order_processor, role_selection):
        self.order_processor = order_processor
        self.role_selection = role_selection
        self.item_order_ids = []

    def select_item(self):
        while True: # This block will ask the user the item id they want to order.
            try:
                orders = int(input("Enter item id: "))
                if orders > len(ItemList.get_item_list()) or orders < 0:
                    print('ID Not Available')
                elif orders == 0:
                    print('Order Cancelled')
                    self.role_selection.input_name()
                    break
                else: 
                    self.item_order_ids.append(orders)
                    print(f'Succesfully added to cart: {ItemList.get_item_list()[orders]['item']}, P{ItemList.get_item_list()[orders]['price']}')
                    self.continue_order()
            except Exception as e:
                print(f'ERROR: Invalid input. {e}')
        return
    
    def continue_order(self):
        while True: # Order more or finish order.
            cont = input("Do you want to add more? [Y/N]: ").upper()
            if cont == 'Y':
                self.select_item()
                return
            elif cont == 'N':
                print('Order Finished')
                self.order_processor.process_order(self)
                return
            else:
                print("Invalid Input.")
        
class OrderProcessor: # to be updated
    def __init__(self, payment_processor):
        self.payment_processor = payment_processor

    def process_order(self, customer):
        print("Ordered item(s):")
        total_amount = 0
        for orders in customer.item_order_ids:
            print(f"{ItemList.get_item_list()[orders]['item']}, P{ItemList.get_item_list()[orders]['price']}")
            total_amount += ItemList.get_item_list()[orders]['price']
        self.payment_processor.process_payment(total_amount)
        # print(f"{customer.get_name()}'s order: {customer.item_order_ids}")

class PaymentProcessor:
    def __init__(self, role_selection):
        self.role_selection = role_selection  # Store reference to RoleSelection

    def process_payment(self, total_amount):
        print(f"Total amount: P{total_amount}")   
        while True:
            try:
                payment = float(input("Enter payment: "))
                print(f"I have received: P{payment}")
                if payment < total_amount:
                    print("Insufficient payment.")
                    continue
                else:
                    print(f"Your change is: P{payment - total_amount}")
                    print("Thank you for ordering!")
                    self.role_selection.input_name()  # Go back to role selection
            except Exception:
                print("Invalid input. Please enter a valid number.")
                continue

class RoleSelection:
    def input_name(self):
        print("----- -----")
        name = input("Enter your name (Enter [0] to cancel): ")
        if name == '0':
            print("Exiting program.")
            return
        else:
            self.select_role(name)

    def select_role(self, name):
        print("----- SELECT ROLE -----")
        while True:
            try:
                role = int(input("Enter [1] for Customer, [2] for Admin: "))
                if role == 1:
                    payment_processor = PaymentProcessor(self)
                    order_processor = OrderProcessor(payment_processor)  
                    order_manager = OrderManager(order_processor, self)
                    customer = Customer(name, order_manager)  
                    customer.start_order()
                    break
                elif role == 2:
                    password = 'admin1234'
                    input_password = input("Enter password (Enter [0] to cancel): ")
                    if input_password != password:
                        print("Invalid password.")
                        continue
                    elif input_password == '0':
                        continue
                    else:
                        # payment_processor = PaymentProcessor(self)
                        admin = Admin(name, self)  
                        admin.add_item()
                        break
                else:
                    print("Invalid selection. Try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")

RoleSelection().input_name()
