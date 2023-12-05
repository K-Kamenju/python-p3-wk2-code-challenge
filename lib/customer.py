class Customer:
    
    all_customers = []
    
    def __init__(self, given_name, family_name):
        self.given_name = given_name
        self.family_name = family_name
        self.add_to_customer_list(f"{given_name.title()} {family_name.title()}")
        
    @classmethod
    def add_to_customer_list(cls, customer):
        cls.all_customers.append(customer)
        
    def get_given_name(self):
        return self._given_name
    
    def set_given_name(self, given_name):
        if (type(given_name) == str):
            self._given_name = given_name
            print(given_name)
        else:
            print("Given_name must be a string")
            
    given_name = property(get_given_name, set_given_name)
    
    def get_family_name(self):
        return self._family_name
    
    def set_family_name(self, family_name):
        if (type(family_name) == str):
            self._family_name = family_name
            print(family_name)
        else:
            print("Given_name must be a string")
    
    family_name = property(get_family_name, set_family_name)
    
    def full_name(self):
        return f"{self.given_name} {self.family_name}"
    

Kamenju = Customer("Selam", "Estifanos")
print(Kamenju.full_name())
print(Customer.all_customers)