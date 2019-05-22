"""
Shopping List Calculator II
"""

# Rewrite p1, but this time use the input() command to solicit user input for name, price, quantity. Here's how it works:

item_name_1 = input('Name your first item') 
	# ^ this will ask user to input value of item_name_1


# use input() function and ask user to name items
item_name_1 = input('Name your first item: ') 
item_name_2 = input('Name your second item: ') 
item_name_3 = input('Name your third item: ') 
item_name_4 = input('Name your fourth item: ') 
item_name_5 = input('Name your fifth item: ') 

# use input() function and ask user to name prices
item_price_1 = input(f'How much do {item_name_1} cost? ')
item_price_2 = input(f'How much do {item_name_2} cost? ')
item_price_3 = input(f'How much do {item_name_3} cost? ')
item_price_4 = input(f'How much do {item_name_4} cost? ')
item_price_5 = input(f'How much do {item_name_5} cost? ')

# use input() function and ask user to name quants
item_quant_1 = input(f'How many of {item_name_1} do you need? ')
item_quant_2 = input(f'How many of {item_name_2} do you need? ')
item_quant_3 = input(f'How many of {item_name_3} do you need? ')
item_quant_4 = input(f'How many of {item_name_4} do you need? ')
item_quant_5 = input(f'How many of {item_name_5} do you need? ')

# Print to the console the name and price of each item defined above as follows:
# 1 Coco Puffs = $8.95.
# where:
# 1 would be item_quant_1
# Coco Puffs would be item_name_1
# 8.95 would be item_name_2

# JUST REMEMBER: now this will be defined by the user!!

item_price_1 = format(item_price_1 * item_quant_1, '.2f')
item_price_2 = format(item_price_2 * item_quant_2, '.2f')
item_price_3 = format(item_price_3 * item_quant_3, '.2f')
item_price_4 = format(item_price_4 * item_quant_4, '.2f')
item_price_5 = format(item_price_5 * item_quant_5, '.2f')

print(f'''
{item_quant_1} {item_name_1} = ${item_price_1}
{item_quant_2} {item_name_2} = ${item_price_2}
{item_quant_3} {item_name_3} = ${item_price_3}
{item_quant_4} {item_name_4} = ${item_price_4}
{item_quant_5} {item_name_5} = ${item_price_5}
''')