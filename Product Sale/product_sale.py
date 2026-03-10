class Store:
    def __init__(self):
        self.products = {}

    def add_product(self,product_name,quantity):
        if product_name in self.products:
            print(f"Product : {product_name} is already exists. updating quantity.")

            self.products[product_name] +=quantity
        else:
            self.products[product_name] = quantity
        
        print(f"Product : {product_name} added with quantity {self.products[product_name]}")

    def update_quantity(self,product_name,quantity_sold):
        available = self.products[product_name]
        if quantity_sold > available:
            print(f"Insufficent stock!! Available = {available} | Requested  = {quantity_sold}")
        else:
            self.products[product_name] -= quantity_sold
            print(f"All done.! Remaining {product_name} Stock {self.products[product_name]} ")

    def check_stock(self,product_name):
        quantity = self.products[product_name]
        if quantity == 0:
            print(f"Product {product_name} is OUT OF STOCK.")
        else:
            print(f"Product is available. Quantity : {quantity}")

    def display(self):
        if not self.products:
            print("Store is empty.")

        else:
            print("Products in store")
            for product,qty in self.products.items():
                print(f"{product} : {qty} ")

store = Store()

while True:
    print("\n =====STORE MENU=====")
    print("1. Add product")
    print("2. Update quantity After sale")
    print("3. Check stock status ")
    print("4. Display All Products")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        name = input("Enter product name: ")
        qty = int(input("Enter quantity: "))
        store.add_product(name,qty)

    elif choice == '2':
        name = input("Enter product name: ")
        sold = int(input("Enter quantity sold: "))
        store.update_quantity(name,sold)

    elif choice == '3':
        name = input("Enter product name: ")
        store.check_stock(name)
    
    elif choice == '4':
        store.display()
    
    elif choice == '5':
        print("Exiting...")
        break

    else:
        print("Invalid choice.")

#  =====STORE MENU=====
# 1. Add product
# 2. Update quantity After sale
# 3. Check stock status 
# 4. Display All Products
# 5. Exit
# Enter your choice: 1
# Enter product name: bread
# Enter quantity: 4
# Product : bread added with quantity 4

#  =====STORE MENU=====
# 1. Add product
# 2. Update quantity After sale
# 3. Check stock status
# 4. Display All Products
# 5. Exit
# Enter your choice: 1
# Enter product name: milk
# Enter quantity: 6
# Product : milk added with quantity 6

#  =====STORE MENU=====
# 1. Add product
# 2. Update quantity After sale
# 3. Check stock status
# 4. Display All Products
# 5. Exit
# Enter your choice: 2
# Enter product name: milk
# Enter quantity sold: 2
# All done.! Remaining milk Stock 4 

#  =====STORE MENU=====
# 1. Add product
# 2. Update quantity After sale
# 3. Check stock status
# 4. Display All Products
# 5. Exit
# Enter your choice: 3
# Enter product name: milk
# Product is available. Quantity : 4

#  =====STORE MENU=====
# 1. Add product
# 2. Update quantity After sale
# 3. Check stock status
# 4. Display All Products
# 5. Exit
# Enter your choice: 3   
# Enter product name: bread
# Product is available. Quantity : 4

#  =====STORE MENU=====
# 1. Add product
# 2. Update quantity After sale
# 3. Check stock status
# 4. Display All Products
# 5. Exit
# Enter your choice: 4
# Products in store
# bread : 4
# milk : 4

#  =====STORE MENU=====
# 1. Add product
# 2. Update quantity After sale
# 3. Check stock status
# 4. Display All Products
# 5. Exit
# Enter your choice: 5
# Exiting...