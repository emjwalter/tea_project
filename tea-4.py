import csv

def get_sales():
    data = []
    sales = []
    with open('/Users/emilywalter/Downloads/sales.csv', 'r') as sales_csv:
        spreadsheet = csv.DictReader(sales_csv)
        for row in spreadsheet:
            sales.append(int(row['sales']))
    return sales

sales_list = get_sales()

print('This is a list of all of the sales:', sales_list)
print('The lowest sales were:', min(sales_list))
print('The highest sales were:', max(sales_list))
print('The average sales were:', sum(sales_list) / len(sales_list))