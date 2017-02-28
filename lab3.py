class Property:
    def __init__(self, square_feet='', beds='', baths='', **kwargs):  # automatically called when an object of
        # that Class is created
        super().__init__(**kwargs)  # super is used for multiple inheritance in parentheses (e.g. House(Property))
        # **kwargs means we can use the arbitrary amount of arguments
        self.square_feet = square_feet  # refers to the created object's name
        self.num_bedrooms = beds
        self.num_baths = baths

    def display(self):  # just what it'll look like when calling the program
        print("PROPERTY DETAILS")
        print("================")
        print("square footage: {}".format(self.square_feet))  # positional formatting
        print("bedrooms: {}".format(self.num_bedrooms))
        print("bathrooms: {}".format(self.num_baths))
        print()

    def prompt_init():  # this method creates a dictionary of values (using input) that pass into __init__
        return dict(square_feet = input("Enter the square feet: "),
            beds = input("Enter number of bedrooms: "),
            baths = input("Enter number of baths: "))
    prompt_init = staticmethod(prompt_init)  # staticmethod used because we don't need to operate on a specific object

class Apartment(Property):  # extends Property class
    valid_laundries = ('coin', 'ensuite', 'none')  # possible variants of answers
    valid_balconies = ('yes', 'no', 'solarium') # possible variants of answers

    def __init__(self, balcony='', laundry='', **kwargs):
        # **kwargs means we can use the arbitrary amount of arguments
        # (e.g. Apartment class can have (or cannot have) balconies and laundries
        super().__init__(**kwargs)
        self.balcony = balcony  # refers to the created object's name (argument)
        self.laundry = laundry

    def display(self):  # just what it'll look like when calling the program
        super().display()  # calls a parent class Property (to ensure it is initialized)
        print("APARTMENT DETAILS")
        print("laundry: %s" % self.laundry)  # positional formatting
        print("has balcony: %s" % self.balcony)

    def prompt_init():
        parent_init = Property.prompt_init()  # staticmethod was used to use it with a particular object now
        # (prompt_init = staticmethod(prompt_init)) in any class (without creating duplicates)
        laundry = get_valid_input(
            "What laundry facilities does the property have? ",
            Apartment.valid_laundries)
        '''while laundry.lower() not in Apartment.valid_laundries:
            laundry = input("What laundry facilities does the property have? "
                            "({})".format('. '.join(Apartment.valid_laundries)))'''
        balcony = get_valid_input(
            "Does the property have a balcony? ",
            Apartment.valid_balconies)
        '''while balcony.lower() not in Apartment.valid_balconies:
            balcony = input("Does the property have a balcony? "
                            "({})".format('. '.join(Apartment.valid_balconies)))'''
        parent_init.update({
            'laundry': laundry,
            'balcony': balcony
        })  # updating parent class (property) with additional arguments (now using **kwargs)
        return parent_init  # getting dictionary from parent class
    prompt_init = staticmethod(prompt_init)  # staticmethod used because we don't need to operate on a specific object

def get_valid_input(input_string, valid_options):  # this function is used in other classes
    # to ask a question about realty and then use positional formatting to show variants of answers
    input_string += ' ({})'.format(', '.join(valid_options))
    response = input(input_string)
    while response.lower() not in valid_options:
        response = input(input_string)
    return response

class House(Property):
    valid_garage = ('attached', 'detached', 'none')  # possible variants of answers
    valid_fenced = ('yes', 'no')  # possible variants of answers

    def __init__(self, num_stories='', garage='', fenced='', **kwargs):
        super().__init__(**kwargs)
        self.garage = garage  # refers to the created object's name (argument)
        self.fenced = fenced
        self.num_stories = num_stories

    def display(self):  # just what it'll look like when calling the program
        super().display()  # calls a parent class Property (to ensure it is initialized)
        print("HOUSE DETAILS")
        print("# of stories: {}".format(self.num_stories))  # positional formatting
        print("garage: {}".format(self.garage))
        print("fenced yard: {}".format(self.fenced))

    def prompt_init():
        parent_init = Property.prompt_init()  # staticmethod was used to use it with a particular object now
        # (prompt_init = staticmethod(prompt_init)) in any class (without creating duplicates)
        fenced = get_valid_input("Is the yard fenced? ",
                                 House.valid_fenced)
        garage = get_valid_input("Is there a garage? ",
                                 House.valid_garage)
        num_stories = input("How many stories? ")
        parent_init.update({
            'fenced': fenced,
            'garage': garage,
            'num_stories': num_stories
        })  # updating parent class (property) with additional arguments (now using **kwargs)
        return parent_init  # getting dictionary from parent class
    prompt_init = staticmethod(prompt_init)  # staticmethod used because we don't need to operate on a specific object

class Purchase:  # does not have a superclass
    def __init__(self, price='', taxes='', **kwargs):
        super().__init__(**kwargs)  # but uses this method because it is going to be combined with other classes,
        # which super() calls in random order
        self.price = price  # refers to the created object's name (argument)
        self.taxes = taxes

    def display(self):  # just what it'll look like when calling the program
        super().display()
        print("PURCHASE DETAILS")
        print("selling price: {}".format(self.price))  # positional formatting
        print("estimated taxes: {}".format(self.taxes))

    def prompt_init():  # returned values will be used in display(self) function
        return dict(
            price = input("What is the selling price? "),
            taxes = input("What are the estimated taxes? ")
        )  # updating parent class (property) with additional arguments (now using **kwargs)
    prompt_init = staticmethod(prompt_init)

class Rental:  # does not have a superclass
    def __init__(self, furnished='', utilities='', rent='', **kwargs):
        super().__init__(**kwargs)  # but uses this method because it is going to be combined with other classes,
        # which super() calls in random order
        self.furnished = furnished  # refers to the created object's name (argument)
        self.rent = rent
        self.utilities = utilities

    def display(self):  # just what it'll look like when calling the program
        super().display()
        print("RENTAL DETAILS")
        print("rent: {}".format(self.rent))  # positional formatting
        print("estimated utilities: {}".format(self.utilities))
        print("furnished: {}".format(self.furnished))

    def prompt_init():  # returned values will be used in display(self) function
        return dict(
            rent = input("What is the monthly rent? "),
            utilities = input("What are the estimated utilities? "),
            furnished = get_valid_input("Is the property finished? ",
                                        ('yes', 'no'))
        )  # updating parent class (property) with additional arguments (now using **kwargs)
    prompt_init = staticmethod(prompt_init)

class HouseRental(Rental, House):  # does not have super() or display() methods because
    # we extend both parent classes (Rental, House) that already call super
    def prompt_init():  # prompting for initializers to all the superclasses
        init = House.prompt_init()
        init.update(Rental.prompt_init())
        return init
    prompt_init = staticmethod(prompt_init)

class HousePurchase(Purchase, House):  # does not have super() or display() methods because
    # we extend both parent classes (Rental, House) that already call super
    def prompt_init():  # prompting for initializers to all the superclasses
        init = House.prompt_init()
        init.update(Purchase.prompt_init())
        return init
    prompt_init = staticmethod(prompt_init)

class ApartmentRental(Rental, Apartment):  # does not have super() or display() methods because
    # we extend both parent classes (Rental, House) that already call super
    def prompt_init():  # prompting for initializers to all the superclasses
        init = Apartment.prompt_init()
        init.update(Rental.prompt_init())
        return init
    prompt_init = staticmethod(prompt_init)

class ApartmentPurchase(Purchase, Apartment):  # does not have super() or display() methods because
    # we extend both parent classes (Rental, House) that already call super
    def prompt_init():  # prompting for initializers to all the superclasses
        init = Apartment.prompt_init()
        init.update(Purchase.prompt_init())
        return init
    prompt_init = staticmethod(prompt_init)

class Agent:
    type_map = {
        ("house", "rental"): HouseRental,
        ("house", "purchase"): HousePurchase,
        ("apartment", "rental"): ApartmentRental,
        ("apartment", "purchase"): ApartmentPurchase
        }  # depending on characteristic of realty later we extract the correct subclass

    def __init__(self):
        self.property_list = []

    def display_properties(self):
        for property in self.property_list:
            property.display()

    def add_property(self):
        property_type = get_valid_input(
                "What type of property? ",
                ("house", "apartment")).lower()  # when using uppercase letters it returns it to the lowercase
        payment_type = get_valid_input(
                "What payment type? ",
                ("purchase", "rental")).lower()
        PropertyClass = self.type_map[(property_type, payment_type)]  # look for the class in dictionary
        # and store it in the variable PropertyClass
        init_args = PropertyClass.prompt_init()  # use the keyword argument syntax and convert the dict into arguments
        self.property_list.append(PropertyClass(**init_args))  # construct the new object to load the correct data
