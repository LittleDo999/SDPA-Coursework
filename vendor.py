class Vendor:
    def __init__(self, name, costs_r, costs_d, costs_g):
        self.name = name #Attribute for the vendor's name
        self.costs_r = costs_r #Attribute for the costs of roses per bunch
        self.costs_d = costs_d #Attribute for the costs of daisies per bunch
        self.costs_g = costs_g #Attribute for the costs of greenery per bunch


# Create objects from the class

Vendor1 = Vendor("Evergreen Essentials", 2.80, 1.50, 0.95)
Vendor2 = Vendor("FloraGrow Distributors", 1.60, 1.20, 1.80)
