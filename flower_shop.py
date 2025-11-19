# flower_shop.py starts

#import variables and functions
from version import *
from bouquet import *
from vendor import *
from flower import *

# The flower_shop file focuses on managing the cash flow, employees, stock, vendor and simulating the flower shop by month.

class FlowerShop:
    Max_Florists = 4 #Attribute to the maximum number of florists in the flower shop
    Min_Florists = 1 #Attribute to the minimum number of florists in the flower shop
    Rent = 800 #Attribute to the house rent of the flower shop per month
    Hourly_Rate = 15.5 #Attribute to the salary of florists per hour
    Hours_Per_Month = 80 #Attribute to the maximum working hours of each florist

    # greenhouse capacity
    Max_Roses = 200
    Max_Daisies = 250
    Max_Greenery = 400

    def __init__(
        self,
        initial_cash: float,
        bouquets: list[Bouquet],
        vendors: list[Vendor],
    ) -> None:
        # Cash
        self.cash: float = initial_cash

        # bouquet types
        self.bouquets: list[Bouquet] = bouquets

        # vendor
        self.vendors: list[Vendor] = vendors

        # florist
        self.florists: list[Florist] = []

        # flower
        self.roses: int = 0
        self.daisies: int = 0
        self.greenery: int = 0

        # current month
        self.current_month: int = 0

# ---------------------------------------------------------------------------------------
# Each of month

def process_month(self) -> None:
        self.hire_or_fire_florists()
        sales_plan = self.decide_bouquet_sales()
        for b in self.bouquets:
            qty = get_int(
                f"How many '{b.name}' bouquets do you want to sell? (max demand = {b.demand}): ",
                min_value=0,
                max_value=b.demand
                )
        
        income = self.produce_and_sell_bouquets(sales_plan)
        self.cash += income
        print(f"Total income from sales this month: £{income:.2f}")
        self.pay_expenses()

        if self.cash < 0:
            return
        self.apply_depreciation()
        self.print_status()
        self.restock()
        if self.cash < 0:
            print("The shop has gone bankrupt after restocking.")






