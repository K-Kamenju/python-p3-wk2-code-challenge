from restaurant import Restaurant
from review import Review

class Customer:
    all_customers = []

    def __init__(self, given_name, family_name):
        self._given_name = given_name
        self._family_name = family_name
        self.add_to_customer_list(f"{given_name.title()} {family_name.title()}")

    @classmethod
    def add_to_customer_list(cls, customer):
        cls.all_customers.append(customer)

    def get_given_name(self):
        return self._given_name

    def set_given_name(self, given_name):
        if isinstance(given_name, str):
            self._given_name = given_name
            print(given_name)
        else:
            raise ValueError("Given_name must be a string")

    given_name = property(get_given_name, set_given_name)

    def get_family_name(self):
        return self._family_name

    def set_family_name(self, family_name):
        if isinstance(family_name, str):
            self._family_name = family_name
            print(family_name)
        else:
            raise ValueError("Family_name must be a string")

    family_name = property(get_family_name, set_family_name)

    def full_name(self):
        return f"{self._given_name} {self._family_name}"

    def restaurants(self):
        return list(set(review.restaurant.name for review in Review.all_reviews if review.customer == self))

    def add_review(self, restaurant, rating):
        if restaurant in Restaurant.all_restaurants:
            new_review = Review(self, restaurant, rating)
            return new_review
        else:
            print("Error: Restaurant not found.")
            return None

    def __str__(self):
        return f"Customer: {self.full_name()}"

# Example
Kamenju = Customer("Selam", "Estifanos")
restaurant_example = Restaurant("Example Restaurant")
review_example = Review(Kamenju, restaurant_example, 4)

# Print the restaurants Kamenju has reviewed
print("Restaurants reviewed by Kamenju:", Kamenju.restaurants())

# Print all customers and restaurants
print("All Customers:", Customer.all_customers)
print("All Restaurants:", Restaurant.all_restaurants)