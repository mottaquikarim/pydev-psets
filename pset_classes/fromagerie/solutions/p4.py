"""
Fromagerie IV - Italian Cheese Sale
"""

# You're having a sale on Italian cheeses. Create a function called "gen_promo_copy" that dynamically creates a string of copy to be stored in a new attribute called promo_copy. 

# Call the function for the cheeses in the "promoted_cheeses" list below. Once finished, you should be able to access the copy as an instance attribute of each of the cheese instances below. For example, the outcome for mascarpone would read something like:
"""
Taste Rome, Tuscany, and Naples.
Parmigiano reggiano for
$10 during our Formaggio Italiano sale!
Sustainably produced at Cheesequake Farms -
organic, non-GMO, & carbon neutral.
"""


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

def gen_promo_copy(promo_items):
  for i in promo_items:
    i.promo_copy = f'''Taste Rome, Tuscany, and Naples.
{i.name.capitalize()} for 
${i.retail_price} during our Formaggio Italiano sale!
Sustainably produced at {i.source} - 
{i.production_standards[0]}, {i.production_standards[1]}, and {i.production_standards[2]}.
    '''
  return None


provolone = Cheese('DRY2523', 'provolone', 12, 16, 4)
gorgonzola = Cheese('DRY2456', 'gorgonzola', 37, 12, 6)
mozzarella = Cheese('DRY6255', 'mozzarella', 78, 12, 7)
ricotta = Cheese('DRY9723', 'ricotta', 24, 13, 6)
mascarpone = Cheese('DRY6282', 'mascarpone', 52, 16, 4)
parmigiano_reggiano = Cheese('DRY9980', 'parmigiano reggiano', 24, 10, 8)
pecorino_romano = Cheese('DRY1601', 'pecorino romano', 36, 14, 9)

promoted_cheeses = [provolone, gorgonzola, mozzarella, ricotta, mascarpone, parmigiano_reggiano, pecorino_romano]

gen_promo_copy(cheese_promotions)

