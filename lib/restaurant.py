'''
RESTAURANT
'''



class Restaurant:
    # Class variable to keep track of all restaurants
    all_restaurants = []

    def __init__(self, name):
        # Instance variable for the restaurant name
        self._name = name.title()
        # Add formatted name to the list of all restaurants
        self.add_to_restaurant_list(name.title())

    @classmethod
    def add_to_restaurant_list(cls, restaurant):
        # Class method to add a restaurant to the list of all restaurants
        cls.all_restaurants.append(restaurant)

    def get_name(self):
        # Getter method for the restaurant name
        return self._name

    def set_name(self, name):
        # Setter method for the restaurant name with type checking
        if isinstance(name, str):
            self._name = name.title()
            print(self._name)
        else:
            print("The name must be a string")

    name = property(get_name, set_name)

    def reviews(self):
        # Method to get a list of reviews for the restaurant
        return [review for review in Review.all_reviews if review.restaurant == self]

    def customers(self):
        # Method to get a list of customers who reviewed the restaurant
        return list(set(review.customer for review in self.reviews()))
    
    def average_star_rating(self):
        # Method to calculate the average star rating for the restaurant
        ratings = [review.rating for review in self.reviews()]
        if ratings:
            return sum(ratings) / len(ratings)
        else:
            return 0


    def __str__(self):
        # String representation of the Restaurant object
        return f"Restaurant: {self.name}"
    
from review import Review  # Import Review here to resolve circular dependency