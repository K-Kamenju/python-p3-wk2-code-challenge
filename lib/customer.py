from review import Review
from restaurant import Restaurant

class Customer:
    
    all_customers = []
    reviews_list = []
    
    
    def __init__(self, given_name, family_name):
        self.given_name = given_name
        self.family_name = family_name
        self.add_to_customer_list(f"{given_name.title()} {family_name.title()}")
        
    @classmethod
    def add_to_customer_list(cls, customer):
        cls.all_customers.append(customer)
        
    def get_given_name(self):
        return self._given_name
    
    def set_given_name(self, given_name):
        if (type(given_name) == str):
            self._given_name = given_name
        else:
            print("Given_name must be a string")
            
    given_name = property(get_given_name, set_given_name)
    
    def get_family_name(self):
        return self._family_name
    
    def set_family_name(self, family_name):
        if (type(family_name) == str):
            self._family_name = family_name
        else:
            print("Given_name must be a string")
    
    family_name = property(get_family_name, set_family_name)
    
    def full_name(self):
        return f"{self.given_name} {self.family_name}"
    
    def restaurants(self):
        return list(set(review.get_restaurant() for review in Review.all_reviews if review.get_customer() == self))

    def add_review(self, restaurant, rating):
        if restaurant in Restaurant.all_restaurants:
            new_review = Review(self, restaurant, rating)
            return new_review
        else:
            print("Error: Restaurant not found.")
            return None
    

Kamenju = Customer("Selam", "Estifanos")

# Example for adding a review
restaurant_example = Restaurant("Bwibo")
review_example = Kamenju.add_review(restaurant_example, 4)

# Print the restaurants Kamenju has reviewed
print("Restaurants reviewed by Kamenju:", Kamenju.restaurants())
