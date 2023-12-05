from customer import Customer
from restaurant import Restaurant
from review import Review

# Test Suites 
Kamenju = Customer("Kamenju", "Estifanos")
Steve = Customer("Steve", "Jobs")
restaurant_example_1 = Restaurant("Bwibo")
restaurant_example_2 = Restaurant("Nyama Mama")
review_example_1 = Review(Kamenju, restaurant_example_1, 4)
review_example_2 = Review(Steve, restaurant_example_1, 2)
review_example_3 = Review(Kamenju, restaurant_example_2, 3)

# Print the names of the restaurants Kamenju and Steve have reviewed
print("\nRestaurants reviewed by Kamenju:", Kamenju.restaurants())
print("Restaurants reviewed by Steve:", Steve.restaurants())

# Print all customers and restaurants
print("\nAll Customers:", Customer.all_customers)
print("All Restaurants:", Restaurant.all_restaurants)

# Print the number of reviews by Kamenju
print(f"\nNumber of reviews by {Kamenju.full_name()}: {Kamenju.num_reviews()}")


# Print all reviews for a specific restaurant
specific_restaurant = restaurant_example_1  # Change to the desired restaurant
print(f"\nAll Reviews for {specific_restaurant.name}:")
for review in specific_restaurant.reviews():
    print(f"{review.customer.full_name()} gave {review.rating} stars")
    
# Print Average star rating for specific restaurant
print(f"\nAverage star rating for {restaurant_example_1.name}: {restaurant_example_1.average_star_rating()}")

