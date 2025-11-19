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
