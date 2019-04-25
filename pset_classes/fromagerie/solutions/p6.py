"""
Fromagerie
"""
# For the problems in this set, imagine you own a fromagerie (a cheese shop). 


# Add an instance method called "record_sale" to the Cheese class. Hint: You will need to add instance attributes for profits_to_date and sales (i.e. number of items sold) to the __init__() method in your Cheese class definition BEFORE writing the instance method. 

# The record_sale method should do the following:
### Add the sale's profits to profits_to_date attribute.
### Add the number sold to the running total in the sales attribute.
### Subtract the number sold from the stock attribute.
### Check the stock (Hint: Call the check_stock method within the record_sale method.)

# Once finished, call record_sale on each sale from the sales_today dict below and print out the name of the cheese, whether it has a low stock alert, the remaining stock value, the running total of units of that cheese sold, and the running total of your profits to date. It should look something like this:

"""
Parmigiano reggiano - Low stock alert! Order more parmigiano reggiano now.
Remaining Stock: 14
Total Sales: 10
Profits to Date: 20
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
        self.profits_to_date = 0
        self.num_sold = 0

    def check_stock(self):
      if self.stock < 15:
        return f'Low stock alert! Order more {self.name} now.'
      else:
          return None

    def record_sale(self,num):
        paid = self.retail_price * num
        profit = paid - (self.wholesale_price * num)
        self.profits_to_date += profit
        self.num_sold += num
        self.stock -= num
        stock_check = self.check_stock()
        return stock_check

provolone = Cheese('DRY2523', 'provolone', 12, 16, 4)
gorgonzola = Cheese('DRY2456', 'gorgonzola', 37, 12, 6)
mozzarella = Cheese('DRY6255', 'mozzarella', 78, 12, 7)
ricotta = Cheese('DRY9723', 'ricotta', 24, 13, 6)
mascarpone = Cheese('DRY6282', 'mascarpone', 52, 16, 4)
parmigiano_reggiano = Cheese('DRY9980', 'parmigiano reggiano', 24, 10, 8)
pecorino_romano = Cheese('DRY1601', 'pecorino romano', 36, 14, 9)




sales_today = {provolone: 8,
gorgonzola: 7, mozzarella: 25, ricotta: 5, mascarpone: 13, parmigiano_reggiano: 10, pecorino_romano: 8}

for k, v in sales_today.items():
  stock_check = k.record_sale(v)
  if stock_check != None:
    low = stock_check
    print(k.name.capitalize(),'-',low)
    print(f'Remaining Stock: {k.stock}')
    print(f'Total Sales: {k.num_sold}')
    print(f'Profits to Date: ${k.profits_to_date}\n')
  else:
    print(k.name.capitalize())
    print(f'Remaining Stock: {k.stock}')
    print(f'Total Sales: {k.num_sold}')
    print(f'Profits to Date: ${k.profits_to_date}\n')