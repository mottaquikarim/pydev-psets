"""
Fromagerie
"""
# For the problems in this set, imagine you own a fromagerie (a cheese shop). 


# Create a class called "ProductCat." This is where you store the full inventories of each category of product at your fromagerie (e.g. cheese, dips, sauces, yogurts, etc.). Instantiate the category "cheeses" using your "cheese_inventory" dict from p1.

# Your class should include the following:
### instance attributes - name & inventory
### class attributes - food_group, production_standards (e.g. organic, non-GMO, and carbon neutral), & source (some farm)
### instance methods - "view_inventory()", which prints out each item in your inventory for that category

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

cheese_inventory ={'brie': ['DRY8900', 27, 11, 5], 'feta': ['DRY7730', 74, 13, 9], 'cheddar': ['DRY3673', 2, 15, 1], 'mozzarella': ['DRY7506', 17, 13, 3], 'ricotta': ['DRY9723', 60, 14, 3], 'provolone': ['DRY5895', 55, 14, 7], 'gruyere': ['DRY3934', 49, 11, 4], 'pecorino romano': ['DRY9980', 24, 10, 8], 'parmigiano reggiano': ['DRY1601', 79, 10, 0], 'gorgonzola': ['DRY6408', 72, 18, 8], 'pepper jack': ['DRY2506', 85, 10, 9], 'gouda': ['DRY4270', 83, 15, 9], 'asiago': ['DRY1592', 42, 18, 2], 'mascarpone': ['DRY6230', 62, 17, 9], 'cotija': ['DRY4128', 95, 16, 5], 'manchego': ['DRY8027', 47, 11, 3]}

cheeses = ProductCat('cheese', cheese_inventory)

cheeses.view_inventory()