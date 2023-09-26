#Create a shopping cart app using Python
#Laudro Pineda
#Python 3.8.1 on Visual Studio code macOS

def display_cart(cart):
    if not cart:
        print("Your cart is empty.")
    else:
        print("Shopping cart.")
    total_price = 0
    for item in cart:
        print(f"{item['name']}: ${item['price']}")
        total_price += item['price']
    print(f"Total: ${total_price:.2f}")

def main():
    cart = []
    while(True):
        print("\nShopping Cart Application")
        print("1. Add item to cart")
        print("2. View Cart")
        print("3. Remove item from Cart")
        print("4. Exit")

        choice = input("Enter your choice: \n")
        if(choice == '1'):
            item_name = input("Enter item name: ")
            item_price = float(input("Enter item price: "))
            item = {"name": item_name, "price": item_price}
            cart.append(item)
            print("Item added to cart!")

        elif choice == '2':
            display_cart(cart)

        elif choice == '3':
            if not cart:
                print("Your cart is already empty!")
            else:
                display_cart(cart)
                item_index = int(input("Enter the item number to remove: ")) - 1
                if 0 <= item_index < len(cart):
                    removed_item = cart.pop(item_index)
                    print(f"Removed item: {removed_item['name']}")
                else: 
                    print("Invalid item number.")
        
        elif choice == '4':
            print("Exiting the Application......")
            break
        else:
            print("Invalid choice, please select a valid option")

if __name__ == "__main__":
    main()
