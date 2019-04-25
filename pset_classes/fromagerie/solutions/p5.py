"""
Fromagerie
"""
# For the problems in this set, imagine you own a fromagerie (a cheese shop). 

# Add an instance method called "check_stock" to the Cheese class. If the amount of a cheese product is less than 15, it should return 'Low stock alert! Order more <that_cheese> now.' Call that on each of the promoted cheeses from p4.

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
    
    def check_stock(self):
      if self.stock < 15:
        return f'Low stock alert! Order more {self.name} now.'
      else:
          return None


provolone = Cheese('DRY2523', 'provolone', 12, 16, 4)
gorgonzola = Cheese('DRY2456', 'gorgonzola', 37, 12, 6)
mozzarella = Cheese('DRY6255', 'mozzarella', 78, 12, 7)
ricotta = Cheese('DRY9723', 'ricotta', 24, 13, 6)
mascarpone = Cheese('DRY6282', 'mascarpone', 52, 16, 4)
parmigiano_reggiano = Cheese('DRY9980', 'parmigiano reggiano', 24, 10, 8)
pecorino_romano = Cheese('DRY1601', 'pecorino romano', 36, 14, 9)

promoted_cheeses = [provolone, gorgonzola, mozzarella, ricotta, mascarpone, parmigiano_reggiano, pecorino_romano]

for i in promoted_cheeses:
	stock_check = i.check_stock()
	if stock_check != None:
		print(stock_check)

# Low stock alert! Order more provolone now.
