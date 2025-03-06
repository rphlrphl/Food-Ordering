class Rooms:
    def __init__(self, room_type, price, description, number_of_rooms):
        self.room_type = room_type
        self.price = price
        self.description = description
        self.number_of_rooms = number_of_rooms
        
    def __str__(self):
        return f"{self.room_type} for P{self.price} per night - {self.description}."
        
class StandardRoom(Rooms):
    def __init__(self):
        super().__init__('Standard Room', 1934, 'These 20 square meter Queen bedded rooms are styled in a contemporary design with tasteful furnishings. Comfortable bathroom with toiletries, smart TV, air purifier, air conditioning, work desk, safety box and complimentary Wi-Fi', 10)
        
class DeluxeRoom(Rooms):
    def __init__(self):
        super().__init__('Deluxe Room', 2729, 'These 22 square meter spacious rooms with balcony are available with two Single beds and a sofa bed. Comfortable bathroom with toiletries, smart TV, air purifier, air conditioning, work desk, mini chiller, safety box and complimentary Wi-Fi', 10)
        
class ExecutiveRoom(Rooms):
    def __init__(self):
        super().__init__('Executive Room', 5557, 'This room features a loft type of bedroom which comes with 3 Queen size beds and a sofa bed caters to families or a group of friends. These 18 square meter room with a maximum capacity of 7 guests come equipped with bathroom amenities, eco-friendly rain shower, smart TV , kitchenette with a refrigerator, dining table, wooden sofa, ceiling fan,  air purifier, air conditioning, work desk, safety box and complimentary Wi-Fi', 10)
