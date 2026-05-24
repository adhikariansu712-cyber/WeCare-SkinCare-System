
# write.py

def write_products(products, filename='inventary.txt'):
    with open(filename, 'w') as file:
        for p in products:
            file.write(f"{p['name']},{p['brand']},{p['quantity']},{p['price']},{p['country']}\n")
