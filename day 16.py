from prettytable import PrettyTable
table = PrettyTable()
table.add_column('Pokemon Name', ['Pikachu', 'Hazer', 'Ismail'])
table.add_column('Type', ['Dry', 'Human', 'Water'])
table.align = 'c'
print(table)
