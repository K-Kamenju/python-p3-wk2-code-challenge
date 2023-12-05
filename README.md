# Python Week 2 - Code Challenge

This project involves three main models in a Yelp-style domain: Restaurant, Customer, and Review. The relationships between these models are defined as follows:

1. A Restaurant has many Reviews.
2. A Customer has many Reviews.
3. A Review belongs to both a Customer and a Restaurant.
4. The relationship between Restaurant and Customer forms a many-to-many relationship.

## Project Setup

1. Create a new project folder.
2. Create a new GitHub repository
3. Please make sure you regularly commit to the repository.
4. Ensure to add a READEME.md file
5. Add a License file, preferrably the MIT license
6. Ensure to organize your python solution in a lib folder

## `DELIVERABLE 1 - Initialization`

The deliverables for this project involve writing specific methods within three classes: Customer, Restaurant, and Review. Each class has an initializer (__init__() method) responsible for setting up the initial state of an instance. 

### Customer

For the Customer class, instances should be initialized with a given name and family name, both represented as strings. Additionally, the class should have methods to retrieve the customer's given name, family name, and the full name by concatenating the given name and family name in Western style. 

```python

def __init__(self, given_name, family_name):
        # Instance variables for customer's names
        self._given_name = given_name
        self._family_name = family_name

# more code ...

# getter and setter methods for the given name as an example:
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


# full name
def full_name(self):
        # Method to get the full name of the customer
        return f"{self._given_name} {self._family_name}"


```

Moreover, there should be a method to retrieve all instances of customers. 

```python

class Customer:
    # Class variable to keep track of all customers
    all_customers = []

    def __init__(self, given_name, family_name):
            # ...
            self.add_to_customer_list(f"{given_name.title()} {family_name.title()}")


    # more code ...

    # class method that handles the addition
    @classmethod
        def add_to_customer_list(cls, customer):
            # Class method to add a customer to the list of all customers
            cls.all_customers.append(customer)

```

### Restaurant

In the Restaurant class, instances should be initialized with a name, and a method should allow retrieving the restaurant's name. It's important to note that the restaurant name should not be changeable after the restaurant is created. 


```python

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

```



### Reviews

Lastly, the Review class should be initialized with a customer, restaurant, and a rating. Methods should be implemented to retrieve the rating for a restaurant and to retrieve all reviews.

```python

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

```

## `DELIVERABLE 2 - Object Relationship Methods`

1. The additional object relationship methods build upon the existing classes (Review, Restaurant, and Customer) to enhance the functionality and relationships between them. For the Review class, two methods are introduced. The customer() method returns the customer object associated with a particular review, providing a way to retrieve information about the customer who wrote the review. Similarly, the restaurant() method returns the restaurant object associated with the review, allowing access to details about the restaurant being reviewed. 

```python

   def __init__(self, customer, restaurant, rating):
        # Instance variables for customer, restaurant, and rating
        self.customer = customer
        self.restaurant = restaurant
        self.rating = rating
        # Add the review to the list of all reviews
        self.add_to_review_list(self)

```

2. In the Restaurant class, two methods are introduced to facilitate the understanding of reviews associated with a particular restaurant. The reviews() method returns a list of all reviews for that restaurant, providing a comprehensive view of customer feedback. The customers() method, on the other hand, returns a unique list of customers who have reviewed a specific restaurant. This functionality allows for a deeper analysis of customer engagement with a restaurant, as it identifies the distinct individuals contributing reviews.

```python

   def reviews(self):
        # Method to get a list of reviews for the restaurant
        return [review for review in Review.all_reviews if review.restaurant == self]

    def customers(self):
        # Method to get a list of customers who reviewed the restaurant
        return list(set(review.customer for review in self.reviews()))

```

3. The Customer class gains two methods that provide insights into a customer's reviewing behavior. The restaurants() method returns a unique list of all restaurants a customer has reviewed, offering a quick summary of a customer's preferences. Additionally, the add_review(restaurant, rating) method allows a customer to create a new review by associating it with a specific restaurant and providing a star rating. This method not only enables customers to express their opinions but also ensures that reviews are connected to the relevant customer and restaurant instances, maintaining the integrity of the data model.

```python

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

```

### Test Cases

Test cases have been created to test out the methods:

```python

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

```
