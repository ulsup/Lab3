import doctest
import lab3

def test():
    """
    >>> test()
    PROPERTY DETAILS
    ================
    square footage: 900
    bedrooms: 2
    bathrooms: one and a half
    <BLANKLINE>
    HOUSE DETAILS
    # of stories: 1
    garage: detached
    fenced yard: yes
    RENTAL DETAILS
    rent: $1200
    estimated utilities: included
    furnished: no
    PROPERTY DETAILS
    ================
    square footage: 800
    bedrooms: 3
    bathrooms: 2
    <BLANKLINE>
    APARTMENT DETAILS
    laundry: ensuite
    has balcony: yes
    PURCHASE DETAILS
    selling price: $200,000
    estimated taxes: $1500
    """
    rent = lab3.HouseRental()
    rent.square_feet = '900'
    rent.num_bedrooms = '2'
    rent.num_baths = 'one and a half'
    rent.num_stories = '1'
    rent.fenced = 'yes'
    rent.garage = 'detached'
    rent.rent = '$1200'
    rent.utilities = 'included'
    rent.furnished = 'no'
    rent.display()
    purchase = lab3.ApartmentPurchase()
    purchase.square_feet = '800'
    purchase.num_bedrooms = '3'
    purchase.num_baths = '2'
    purchase.laundry = 'ensuite'
    purchase.balcony = 'yes'
    purchase.price = '$200,000'
    purchase.taxes = '$1500'
    purchase.display()

if __name__ == '__main__':
    doctest.testmod()
