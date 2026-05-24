

import datetime
from write import write_products

def display_products(products):
    print("\n{:<15} {:<10} {:<6} {:<10} {:<10}".format('Name', 'Brand', 'Qty', 'Price', 'Country'))
    print("-" * 55)
    for p in products:
        print("{:<15} {:<10} {:<6} Rs {:<8.2f} {:<10}".format(p['name'], p['brand'], p['quantity'], p['price'], p['country']))

def find_product(products, name):
    return next((p for p in products if p['name'].lower() == name.lower()), None)

def make_sale(products):
    customer = input("Customer name: ")
    items, total = [], 0

    while True:
        pname = input("Enter product name (or '4' to exit): ")
        if pname.lower() == '4': break
        product = find_product(products, pname)
        if not product:
            print("Not found."); continue

        qty = input("Enter quantity: ")
        if not qty.isdigit(): print("Invalid quantity."); continue
        qty = int(qty)

        if qty > product['quantity']:
            print("Not enough stock."); continue



        free = qty //3
        #if we buy 3 or more than 3 we will get buy 3 get one free offer
        total_units = qty + free
        product['quantity'] -= total_units
        sell_price = product['price'] * 2
        line_total = qty * sell_price
        total += line_total

        items.append((product['name'], product['brand'], qty, free, sell_price, line_total))
        print("Added {} + {} free.".format(qty, free))

    now = datetime.datetime.now()
    fname = "sale_invoice_{}_{}.txt".format(customer, now.strftime('%Y%m%d%H%M%S'))
    with open(fname, 'w') as f:
        f.write("Customer: {}\nDate: {}\n\nItems:\n".format(customer, now))
        for i in items:
            f.write("{} ({}) - {} + {} free @Rs {:.2f} = Rs {:.2f}\n".format(i[0], i[1], i[2], i[3], i[4], i[5]))
        f.write("\nTotal: Rs {:.2f}\n".format(total))
    print("Invoice saved: {}".format(fname))
    write_products(products)

def restock(products):
    supplier = input("Supplier name: ")
    items, total = [], 0

    while True:
        pname = input("Enter product name to restock (or '4'): ")
        if pname.lower() == '4': break
        product = find_product(products, pname)
        if not product:
            print("Not found."); continue

        qty = input("Enter quantity: ")
        if not qty.isdigit(): print("Invalid qty."); continue
        qty = int(qty)

        new_price = input("Enter new price (or 0 to keep current): ")
        try:
            new_price = float(new_price)
            if new_price > 0:
                product['price'] = new_price
        except:
            print("Invalid price."); continue

        product['quantity'] += qty
        cost = qty * product['price']
        total += cost
        items.append((product['name'], product['brand'], qty, product['price'], cost))
        print("Restocked {} of {}.".format(qty, product['name']))

    now = datetime.datetime.now()
    fname = "restock_invoice_{}_{}.txt".format(supplier, now.strftime('%Y%m%d%H%M%S'))
    with open(fname, 'w') as f:
        f.write("Supplier: {}\nDate: {}\n\nRestocked Items:\n".format(supplier, now))
        for i in items:
            f.write("{} ({}) - {} @Rs {:.2f} = Rs {:.2f}\n".format(i[0], i[1], i[2], i[3], i[4]))
        f.write("\nTotal Restock: Rs {:.2f}\n".format(total))
    print("Restock invoice saved: {}".format(fname))
    write_products(products)

