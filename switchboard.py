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

while True:
    # printing option
    print('Welcome to the Sales lucky dip switchboard! Please choose option 1, 2, 3 or 4 to learn a fun fact today!')

    # ask for an option
    user_input = input('Please choose an option')

    if user_input == '1':
        print('Thanks, you chose option 1')
        print('This is a list of all of the sales:', sales_list)

    elif user_input == '2':
        print('Thanks, you chose option 2')
        print('The lowest monthly sales were:', min(sales_list))

    elif user_input == '3':
        print('Thanks, you chose option 3')
        print('The highest monthly sales were:', max(sales_list))

    elif user_input == '4':
        print('Thanks, you chose option 4')
        print('The average sales per month were:', sum(sales_list) / len(sales_list))

    elif user_input == '0':
        break








