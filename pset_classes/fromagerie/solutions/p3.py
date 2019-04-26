"""
Fromagerie III - Cheeses
"""

# Create a "Cheese" class that inherits from ProductCat. Create 10 instances based on info from cheese_inventory. 

# Your class should include the following instance attributes:
### sku
### name
### stock
### retail_price
### wholesale_price
### profit_margin (Hint: You don't need to pass this one during instantiation.)

class ProductCat():
    def __init__(self, name, inventory, *args):
        self.name = name
        self.inventory = inventory

    food_group = 'dairy'

    production_standards = ['organic', 'non-GMO', 'carbon neutral']

    source = 'Cheesequake Farms' # <-- real place by the way

    def view_inventory(self):
        for k, v in self.inventory.items():
            print(f'{k}: {v}')

class Cheese(ProductCat):
    def __init__(self, sku, name, stock = 0, retail_price = 0, wholesale_price = 0, *args):
        self.sku = sku
        self.name = name
        self.stock = stock
        self.retail_price = retail_price
        self.wholesale_price = wholesale_price
        self.profit_margin = retail_price - wholesale_price

# Based on the info from cheese_inventory, create instances for the cheese below. (Hint: Make sure one has a stock value of < 15. You'll need this later.)
### provolone
### gorgonzola
### mozzarella
### ricotta
### mascarpone
### parmigiano_reggiano
### pecorino_romano

provolone = Cheese('DRY2523', 'provolone', 12, 16, 4)
gorgonzola = Cheese('DRY2456', 'gorgonzola', 37, 12, 6)
mozzarella = Cheese('DRY6255', 'mozzarella', 78, 12, 7)
ricotta = Cheese('DRY9723', 'ricotta', 24, 13, 6)
mascarpone = Cheese('DRY6282', 'mascarpone', 52, 16, 4)
parmigiano_reggiano = Cheese('DRY9980', 'parmigiano reggiano', 24, 10, 8)
pecorino_romano = Cheese('DRY1601', 'pecorino romano', 36, 14, 9)
