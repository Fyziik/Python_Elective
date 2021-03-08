#From 2 lists, using a list comprehension, create a list containing:
# [(‘Black’, ‘s’), (‘Black’, ‘m’), (‘Black’, ‘l’), (‘Black’, ‘xl’), (‘White’, ‘s’), (‘White’, ‘m’), (‘White’, ‘l’), (‘White’, ‘xl’)]

#If the tuple pair is in the following list, it should not be added to the comprehension generated list.
#ed_out = [('Black', 'm'), ('White', 's')]
colors = ['Black', 'White']
sizes = ['s', 'm', 'l', 'xl']
sold_out = [('Black', 'm'), ('White', 's')]

clothes = [(color, size) for color in colors for size in sizes if (color, size) not in sold_out]
print(clothes)