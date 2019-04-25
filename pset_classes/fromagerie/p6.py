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


sales_today = {provolone: 8,
gorgonzola: 7, mozzarella: 25, ricotta: 5, mascarpone: 13, parmigiano_reggiano: 10, pecorino_romano: 8}