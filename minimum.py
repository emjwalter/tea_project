### MINIMUM ###

import csv

sales = []

with open('sales.csv', 'r') as sales_csv:
    spreadsheet = csv.DictReader(sales_csv)

    for row in spreadsheet:
        sales_csv = row['sales']
        sales.append(sales_csv)

    lowest_sale = min(sales)
    print(lowest_sale)

print('The lowest sales are: {}'. format(lowest_sale))