'''
Due to errors in my import statement i have created one code challenge file
'''


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

    def __str__(self):
        # String representation of the Customer object
        return f"Customer: {self.full_name()}"


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

    def __str__(self):
        # String representation of the Restaurant object
        return f"Restaurant: {self.name}"


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

    @property
    def customer(self):
        # Getter method for the customer
        return self._customer

    @customer.setter
    def customer(self, customer):
        # Setter method for the customer with type checking
        if isinstance(customer, Customer):
            self._customer = customer
            print(self._customer)
        else:
            print("Error: Invalid customer object")

    # Similar getter and setter methods for restaurant and rating

    def __str__(self):
        # String representation of the Review object
        return f"{self.customer.full_name()} gave {self.rating} stars to {self.restaurant.name}"


# Test Suites
Kamenju = Customer("Kamenju", "Estifanos")
Steve = Customer("Steve", "Jobs")
restaurant_example_1 = Restaurant("Bwibo")
restaurant_example_2 = Restaurant("Nyama Mama")
review_example_1 = Review(Kamenju, restaurant_example_1, 4)
review_example_2 = Review(Steve, restaurant_example_1, 2)
review_example_3 = Review(Kamenju, restaurant_example_2, 3)

# Print the names of the restaurants Kamenju and Steve have reviewed
print("Restaurants reviewed by Kamenju:", Kamenju.restaurants())
print("Restaurants reviewed by Steve:", Steve.restaurants())

# Print all customers and restaurants
print("All Customers:", Customer.all_customers)
print("All Restaurants:", Restaurant.all_restaurants)

# Print all reviews for a specific restaurant
specific_restaurant = restaurant_example_1  # Change to the desired restaurant
print(f"\nAll Reviews for {specific_restaurant.name}:")
for review in specific_restaurant.reviews():
    print(f"{review.customer.full_name()} gave {review.rating} stars")
    
