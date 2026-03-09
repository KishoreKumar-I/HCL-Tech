def shopping_cart(prices):
    print("\n Items in the cart: ")
    for items, price in enumerate(prices, start = 1):
        print(f"Item : {items} , ₹{price}")
    
    Total_cost = sum(prices)
    print(f"\nTotal cost : ₹{Total_cost}")

    max_price = prices[0]
    for price in prices:
        if price > max_price:

            max_price = price
    print(f"\nExpensive item cost =₹{max_price}")

    choice = input("\nPlease confirm the items in the cart, if you want to cancel any item, please type 'yes/no' : ")
    if choice.lower() == 'yes':
        pos = int(input("Enter the item number to remove:"))
        if pos >=1 and pos<=len(prices):
            removed = prices.pop(pos-1)
            print(f"Item with price ₹{removed} removed from your shopping cart.")
        else:
            print("Invalid item number.")
        print("\n Updated cart:",prices)
        print("\nUpdated total cost : ₹",sum(prices))
    else:
        print("\nThank you for shopping with us! Your total cost is ₹", Total_cost)

prices = []
n = int(input("Enter the number of items in the cart: "))

for i in range(n):
    item = input("Enter the name of the item:")
    price = float(input("Enter the price of the item: ₹"))
    prices.append(price)

shopping_cart(prices)


#Output:
# Enter the number of items in the cart: 3
# Enter the name of the item : milk
# Enter the price of the item: ₹50
# Enter the name of the item : bread
# Enter the price of the item: ₹60
# Enter the name of the item : perfume
# Enter the price of the item: ₹115

#  Items in the cart:
# Item : 1 , ₹50.0
# Item : 2 , ₹60.0
# Item : 3 , ₹115.0

# Total cost : ₹225.0

# Expensive item cost = ₹115.0

# Please confirm the items in the cart, if you want to cancel any item, please type 'yes/no' : yes
# Enter the item number to remove:2
# Item with price ₹60.0 removed from your shopping cart.

# Updated cart: [50.0, 115.0]

# Updated total cost : ₹ 165.0