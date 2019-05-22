"""
Shopping List Calculator I
"""

# Create five variables,
# set them to strings that represent 5 common shopping list items

item_name_1 = 'pasta'
item_name_2 = 'olive oil'
item_name_3 = 'fresh basil'
item_name_4 = 'parmesan'
item_name_5 = 'walnuts'

# Create five more variables,
# set them to floats that represent the prices of each of the items above

item_price_1 = format(1.50, '.2f')
item_price_2 = format(6.99, '.2f')
item_price_3 = format(3.99, '.2f')
item_price_4 = format(5.00, '.2f')
item_price_5 = format(8.50, '.2f')

# Create five more variables,
# set them to ints that represent the quantity of each of the items above

item_quant_1 = 2
item_quant_2 = 1
item_quant_3 = 3
item_quant_4 = 2
item_quant_5 = 1

# Print to the console the name and price of each item defined above as follows:
# 1 Coco Puffs = $8.95.
# where:
# 1 would be item_quant_1
# Coco Puffs would be item_name_1
# 8.95 would be item_name_2

print(f'''
{item_quant_1} {item_name_1} = ${item_price_1}
{item_quant_2} {item_name_2} = ${item_price_2}
{item_quant_3} {item_name_3} = ${item_price_3}
{item_quant_4} {item_name_4} = ${item_price_4}
{item_quant_5} {item_name_5} = ${item_price_5}
''')
