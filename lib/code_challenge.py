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
            print("Given_name must be a string")

    given_name = property(get_given_name, set_given_name)

    def get_family_name(self):
        return self._family_name

    def set_family_name(self, family_name):
        if isinstance(family_name, str):
            self._family_name = family_name
            print(family_name)
        else:
            print("Family_name must be a string")

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

class Restaurant:
    all_restaurants = []

    def __init__(self, name):
        self._name = name.title()
        self.add_to_restaurant_list(name.title())

    @classmethod
    def add_to_restaurant_list(cls, restaurant):
        cls.all_restaurants.append(restaurant)

    def get_name(self):
        return self._name

    def set_name(self, name):
        if isinstance(name, str):
            self._name = name.title()
            print(self._name)
        else:
            print("The name must be a string")

    name = property(get_name, set_name)

    def reviews(self):
        return [review for review in Review.all_reviews if review.restaurant == self]

    def customers(self):
        return list(set(review.customer for review in self.reviews()))

    def __str__(self):
        return f"Restaurant: {self.name}"

class Review:
    all_reviews = []

    def __init__(self, customer, restaurant, rating):
        self.customer = customer
        self.restaurant = restaurant
        self.rating = rating
        self.add_to_review_list(self)

    @classmethod
    def add_to_review_list(cls, review):
        cls.all_reviews.append(review)

    @property
    def customer(self):
        return self._customer

    @customer.setter
    def customer(self, customer):
        if isinstance(customer, Customer):
            self._customer = customer
            print(self._customer)
        else:
            print("Error: Invalid customer object")

    @property
    def restaurant(self):
        return self._restaurant

    @restaurant.setter
    def restaurant(self, restaurant):
        if isinstance(restaurant, Restaurant):
            self._restaurant = restaurant
            print(self._restaurant)
        else:
            print("Error: Invalid restaurant object")

    def get_rating(self):
        return self._rating

    def set_rating(self, rating):
        if (isinstance(rating, int)) and (1 <= rating <= 5):
            self._rating = rating
            print(self._rating)
        else:
            print("Rating must be an integer and between 1 and 5")

    rating = property(get_rating, set_rating)

    def __str__(self):
        return f"{self.customer.full_name()} gave {self.rating} stars to {self.restaurant.name}"




# Test Suites
Kamenju = Customer("Selam", "Estifanos")
restaurant_example_1 = Restaurant("Bwibo")
review_example_1 = Review(Kamenju, restaurant_example_1, 4)

# Print the restaurants Kamenju has reviewed
print("Restaurants reviewed by Kamenju:", Kamenju.restaurants())

# Print all customers and restaurants
print("All Customers:", Customer.all_customers)
print("All Restaurants:", Restaurant.all_restaurants)
