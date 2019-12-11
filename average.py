# ### AVERAGE ###

import csv

sales = []

with open('sales.csv', 'r') as sales_csv:
    spreadsheet = csv.DictReader(sales_csv)

    for row in spreadsheet:
        sales_csv = row['sales']
        sales.append(sales_csv)

    average = total_sales() / len(sales)
    print(average)

print('The average sales are: {}'.format(average))