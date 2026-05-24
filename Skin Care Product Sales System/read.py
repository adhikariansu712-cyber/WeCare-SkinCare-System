


def read_products(filename='inventary.txt'):
    products = []
    try:
        file = open(filename, 'r')
        for line in file:
            line = line.replace('\n', '')
            data = line.split(',')
            if len(data) != 5: #skip invalid lines
                continue  
            name = data[0]
            brand = data[1]
            qty = int(data[2])
            price = float(data[3])
            country = data[4]
            products.append({
                'name': name,
                'brand': brand,
                'quantity': qty,
                'price': price,
                'country': country
            })
        file.close()
    except:
        print("File not found.")
    return products
