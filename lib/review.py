'''
REVIEW
'''


class Review:
    # Class variable to keep track of all reviews
    all_reviews = []

    def __init__(self, customer, restaurant, rating):
        # Instance variables for customer, restaurant, and rating
        self.customer = customer
        self.restaurant = restaurant
        self.rating = rating
        # Add the review to the list of all reviews
        self.add_to_review_list(self)

    @classmethod
    def add_to_review_list(cls, review):
        # Class method to add a review to the list of all reviews
        cls.all_reviews.append(review)

   # Getter and setter for customer
    def get_customer(self):
        return self._customer

    def set_customer(self, customer):
        if isinstance(customer, Customer):
            self._customer = customer
        else:
            print("Error: Invalid customer object")

    customer = property(get_customer, set_customer)

    # Getter and setter for restaurant
    def get_restaurant(self):
        return self._restaurant

    def set_restaurant(self, restaurant):
        if isinstance(restaurant, Restaurant):
            self._restaurant = restaurant
        else:
            print("Error: Invalid restaurant object")

    restaurant = property(get_restaurant, set_restaurant)

    # Getter and setter for rating
    def get_rating(self):
        return self._rating

    def set_rating(self, rating):
        if (isinstance(rating, int)) and (1 <= rating <= 5):
            self._rating = rating
        else:
            print("Rating must be an integer and between 1 and 5")

    rating = property(get_rating, set_rating)
    
    def __str__(self):
        # String representation of the Review object
        return f"{self.customer.full_name()} gave {self.rating} stars to {self.restaurant.name}"


from customer import Customer  # Import Customer here to resolve circular dependency
from restaurant import Restaurant  # Import Restaurant here to resolve circular dependency