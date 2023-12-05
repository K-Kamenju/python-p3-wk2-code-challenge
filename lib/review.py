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
    
    def get_rating(self):
        return self._rating
    
    def set_rating(self, rating):
        if (type(rating) == int) and (1 <= rating <= 5):
            self._rating = rating
            print(self._rating)
        else:
            print("Rating must be an interger and between 1 and 5")
    
    def get_customer(self):
        return self._customer 
    
    def set_customer(self, customer):
        self._customer = customer
        print(self._customer)
    
    customer = property(get_customer, set_customer)
    
    def get_restaurant(self):
        return self._restaurant
    
    def set_restaurant(self, restaurant):
        self._restaurant = restaurant
        print(self._restaurant)
    
    restaurant = property(get_restaurant, set_restaurant)
    
    def __str__(self):
        return f"{self.customer} gave {self.rating} stars to {self.restaurant}"
            
    rating = property(get_rating, set_rating)
    
    
review1 = Review(Customer("Selam", "Estifanos"), Restaurant("Bwibo"), 5)
print(review1)