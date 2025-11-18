# bouquet.py defines the class of bouquet

class Bouquet:
    def __init__(self, name, qty_g, qty_r, qty_d, time, demand, price):
        self.name = name # Attribute for the bouquet's name
        self.qty_g = qty_g # Attribute for the quantity of Greenery
        self.qty_r = qty_r # Attribute for the quantity of Roses
        self.qty_d = qty_d # Attribute for the quantity of Daisies
        self.time = time # Attribute for the time to prepare
        self.demand = demand # Attribute for the demand of this bouquet
        self.price = price # Attribute for the price of this bouquet

# Create objects from the class

bouquet1 = Bouquet("Fern-tastic", 4, 0, 2, 20, 175, 18.50)
bouquet2 = Bouquet("Be-Leaf in Yourself", 2, 1, 3, 30, 100, 17.75)
bouquet3 = Bouquet("You Rose to the Occasion", 2, 4, 2, 45, 250, 32.50)


class Flower:
    def __init__(self, name, capacity, depreciation, cost):
        self.name = name # Attribute for the flower name
        self.capacity = capacity # Attribute for the Greenhouse Capacity
        self.depreciation = depreciation # Attribute for the flower depreciation
        self.cost = cost # Attribute for the Greenhouse Costs

# Create objects from the class

Roses = Flower("Roses", 200, 0.40, 1.50)
Daisies = Flower("Daisies", 250, 0.15, 0.80)
Greenery = Flower("Greenery", 400, 0.05, 0.20)


class Vendor:
    def __init__(self, name, costs_r, costs_d, costs_g):
        self.name = name #Attribute for the vendor's name
        self.costs_r = costs_r #Attribute for the costs of roses per bunch
        self.costs_d = costs_d #Attribute for the costs of daisies per bunch
        self.costs_g = costs_g #Attribute for the costs of greenery per bunch


# Create objects from the class

Vendor1 = Vendor("Evergreen Essentials", 2.80, 1.50, 0.95)
Vendor2 = Vendor("FloraGrow Distributors", 1.60, 1.20, 1.80)
    
