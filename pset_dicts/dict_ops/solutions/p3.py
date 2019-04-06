"""
Math with Girl Scout Cookies - SOLUTION
"""

Wendy = {'tagalongs': 5, 'thin mints': 12, 'samoas': 8}
Connie = {'tagalongs': 10, 'thin mints': 4, 'samoas': 12}
Francesca = {'tagalongs': 18, 'thin mints': 14, 'samoas': 10}

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

salesW = sum(list(Wendy.values()))
salesC = sum(list(Connie.values()))
salesF = sum(list(Francesca.values()))

print(f"""
Wendy: {salesW}
Connie: {salesC}
Francesca: {salesF}
""")

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

total_tagalongs = Wendy['tagalongs'] + Connie['tagalongs'] + Francesca['tagalongs']

total_thinmints = Wendy['thin mints'] + Connie['thin mints'] + Francesca['thin mints']

total_samoas = Wendy['samoas'] + Connie['samoas'] + Francesca['samoas']

print(f"""
Tagalongs: {total_tagalongs}
Thin Mints: {total_samoas}
Samoas: {total_thinmints}
""")

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

avg_tagalongs = total_tagalongs / 3
avg_thinmints = total_thinmints / 3
avg_samoas = total_samoas / 3

print(f"""
Tagalongs: {avg_tagalongs}
Thin Mints: {avg_thinmints}
Samoas: {avg_samoas}
""")

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

boxes_sold = salesW + salesC + salesF

print(f'This year we sold {boxes_sold} boxes!')
