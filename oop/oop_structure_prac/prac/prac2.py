
#?????????
def get_valid_input(input_string, valid_options):
    input_string += " ({}) ".format(", ".join(valid_options))
    response = input(input_string)
    while response.lower() not in valid_options:
        response = input(input_string)
    return response


class Property:

    valid_laundries = ("coin", "ensuite", "none")
    valid_balconies = ("yes", "no", "solarium")

    def __init__(self, square_feet='', num_bedrooms='', num_bathrooms='', **kwargs) -> None:
        super().__init__(**kwargs)
        self.square_feet = square_feet
        self.num_bedrooms = num_bedrooms
        self.num_bathrooms = num_bathrooms
        
    def display(self):
        print("PROPERTY DETAILS")
        print("================")
        print("square footage: {}".format(self.square_feet))
        print("bedrooms: {}".format(self.num_bedrooms))
        print("bathrooms: {}".format(self.num_baths))
        print()
        
    def prompt_init(self):
        return dict(square_feet=input("Enter the square feet: "),
                      numb_beds=input("Enter number of bedrooms: "),
                     numb_baths=input("Enter number of baths: "))
    
    prompt_init = staticmethod(prompt_init)
    
class House(Property):

    valid_garage = ("attached", "detached", "none")
    valid_fenced = ("yes", "no")

    def __init__(self, num_stories='', garage='', fenced_yard='', **kwargs) -> None:
        super().__init__(**kwargs)
        self.num_stories = num_stories
        self.garage = garage
        self.fenced_yard = fenced_yard
        
    def display(self):
        super().display()
    
    def prompt_init(self):
        pass
    
class Apartment(Property):

    valid_laundries = ("coin", "ensuite", "none")
    valid_balconies = ("yes", "no", "solarium")

    def __init__(self, balcony='', laundry='', **kwargs) -> None:
        super().__init__(**kwargs)
        self.balcony = balcony
        self.laundry = laundry
        
    def display(self):
        super().display()
    
    def prompt_init():
        parent_init = Property.prompt_init()
        laundry = get_valid_input(
                "What laundry facilities does "
                "the property have? ",
                Apartment.valid_laundries)
        balcony = get_valid_input(
                "Does the property have a balcony? ",
                Apartment.valid_balconies)
        parent_init.update({
                "laundry": laundry,
                "balcony": balcony
                                    }) 
        return parent_init
   
    prompt_init = staticmethod(prompt_init)
        
class Purchase:
    def __init__(self, price='', taxes='', **kwargs) -> None:
        super().__init__(**kwargs)
        self.price = price
        self.taxes = taxes
        
    def display(self):
        pass
    
    def prompt_init(self):
        pass
    
class Rental:
    def __init__(self, furnished='', ultilities='', rent='') -> None:
        self.furnished = furnished
        self.ultilities = ultilities
        self.rent = rent
        
    def display(self):
        pass
    
    def prompt_init(self):
        pass

        
class HouseRental( House, Rental ):
    pass

class HousePurchase( House, Purchase ):
    pass

class ApartmentRental( Apartment, Rental ):
    pass

class ApartmentPurchase( Apartment, Purchase ):
    pass



#dict2 = {'key': 11}
#dict2.update()