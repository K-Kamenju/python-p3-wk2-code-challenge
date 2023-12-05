from lib.review import Review
from lib.customer import Customer

class Restaurant:
    
    all_restaurants = []
    
    def __init__(self, name):
        self.name = name.title()
        self.add_to_restaurant_list(name.title())
    
    @classmethod
    def add_to_restaurant_list(cls, restaurant):
        cls.all_restaurants.append(restaurant)
    
    def get_name(self):
        return self._name
    
    def set_name(self, name):
        if (type(name) == str):
            self._name = name.title()
            print(self._name)
        else:
            print("The name must be a string")
            
    name = property(get_name, set_name)
    
Bwibo = Restaurant("Bwibo")
print(Restaurant.all_restaurants)
