'''
CUSTOMER 
'''

class Customer:
    # Class variable to keep track of all customers
    all_customers = []

    def __init__(self, given_name, family_name):
        # Instance variables for customer's names
        self._given_name = given_name
        self._family_name = family_name
        # Add formatted full name to the list of all customers
        self.add_to_customer_list(f"{given_name.title()} {family_name.title()}")

    @classmethod
    def add_to_customer_list(cls, customer):
        # Class method to add a customer to the list of all customers
        cls.all_customers.append(customer)

    def get_given_name(self):
        # Getter method for the given name
        return self._given_name

    def set_given_name(self, given_name):
        # Setter method for the given name with type checking
        if isinstance(given_name, str):
            self._given_name = given_name
            print(given_name)
        else:
            print("Given_name must be a string")

    given_name = property(get_given_name, set_given_name)

    # Similar getter and setter methods for family name

    def full_name(self):
        # Method to get the full name of the customer
        return f"{self._given_name} {self._family_name}"

    def restaurants(self):
        # Method to get a list of restaurant names reviewed by the customer
        return list(set(review.restaurant.name for review in Review.all_reviews if review.customer == self))

    def add_review(self, restaurant, rating):
        # Method to add a review for a restaurant
        if restaurant in Restaurant.all_restaurants:
            new_review = Review(self, restaurant, rating)
            return new_review
        else:
            print("Error: Restaurant not found.")
            return None
        
    def num_reviews(self):
        # Method to get the total number of reviews authored by the customer
        return len([review for review in Review.all_reviews if review.customer == self])

    @classmethod
    def find_by_full_name(cls, name):
        # Class method to find the first customer whose full name matches
        for customer in cls.all_customers:
            if customer.full_name() == name.title():
                return customer
        return None

    @classmethod
    def find_all_by_given_name(cls, name):
        # Class method to find all customers with a given name
        return [customer for customer in cls.all_customers if customer.get_given_name().title() == name.title()]

    def __str__(self):
        # String representation of the Customer object
        return f"Customer: {self.full_name()}"

from review import Review  # Import Review here to resolve circular dependency
from restaurant import Restaurant  # Import Restaurant here to resolve circular dependency