
# main.py

from read import read_products
from operations import display_products, make_sale, restock

def main():
    products = read_products()

    while True:
        print("\n--- WeCare Skin Care System ---")
        print("1. View Products\n2. Make Sale\n3. Restock\n4. Exit")
        option = input("Enter choice: ")

        if option == '1':
            #products will be displayed while entering 
            display_products(products)
        elif option == '2':
            make_sale(products)
            #if we enter option 2 we will be able to make sale
        elif option == '3':
            restock(products)
            #while entering 3 we will bw able to restock products
        elif option == '4':
            print("Goodbye!")
            #if we enter option 4 the loop will break and will exit and pint goodbye!
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
