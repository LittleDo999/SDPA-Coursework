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



    
