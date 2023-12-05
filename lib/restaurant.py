from review import Review

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
            raise ValueError("The name must be a string")

    name = property(get_name, set_name)

    def reviews(self):
        return [review for review in Review.all_reviews if review.restaurant == self]

    def customers(self):
        return list(set(review.customer for review in self.reviews()))

    def __str__(self):
        return f"Restaurant: {self.name}"