### MAXIMUM ###

import csv

sales = []

with open('sales.csv', 'r') as sales_csv:
    spreadsheet = csv.DictReader(sales_csv)

    for row in spreadsheet:
        sales_csv = row['sales']
        sales.append(sales_csv)

    highest_sale = max(sales)
    print(highest_sale)

print('The highest sales are: {}'. format(highest_sale))