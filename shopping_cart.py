"""
E-commerce Cart System
-------------------------
This program simulates an e-commerce shopping cart system where users can:
- View a product catalog
- Add/remove items to/from the cart
- View the current contents of the cart
- Checkout and purchase the items in the cart

Features:
- Adds and removes items dynamically.
- Displays total cost of items in the cart.
- Allows users to cancel or complete the checkout process.

"""

class Item1:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} **** ${self.price:.2f}"

class Cart:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)
        print(f"✅ Added '{item.name}' to the cart.")

    def remove_item(self, item_name):
        for i, item in enumerate(self.items):
            if item.name.lower() == item_name.lower():
                del self.items[i]
                print(f"❌ Removed '{item.name}' from the cart.")
                return
        print("⚠️ Item not found in cart.")

    def view_cart(self):
        if not self.items:
            print("🛒 Your cart is empty.")
            return
        print("\n🛒 Your Cart:")
        for item in self.items:
            print(f"  - {item}")
        print(f"Total: ${self.total_cost():.2f}\n")

    def total_cost(self):
        return sum(item.price for item in self.items)

    def checkout(self):
        if not self.items:
            print("🚫 Cart is empty. Add items before checking out.")
            return
        self.view_cart()
        confirm = input("Proceed to checkout? (yes/no): ").strip().lower()
        if confirm == 'yes':
            print("✅ Checkout complete. Thank you for your purchase!")
            self.items.clear()
        else:
            print("⏳ Checkout cancelled.")

def main():
    # Sample product catalog
    catalog = {
        "laptop": 999.99,
        "phone": 499.99,
        "headphones": 89.99,
        "mouse": 29.99,
        "keyboard": 49.99
    }

    cart = Cart()

    while True:
        print("\n--- E-commerce Cart Menu ---")
        print("1. View Catalog")
        print("2. Add Item to Cart")
        print("3. Remove Item from Cart")
        print("4. View Cart")
        print("5. Checkout")
        print("6. Exit")

        choice = input("Choose an option (1-6): ").strip()

        if choice == '1':
            print("\n🛍️ Product Catalog:")
            for name, price in catalog.items():
                print(f"  - {name.title()} : ${price:.2f}")

        elif choice == '2':
            item_name = input("Enter item name to add: ").strip().lower()
            if item_name in catalog:
                item = Item1(item_name.title(), catalog[item_name])
                cart.add_item(item)
            else:
                print("❌ Item not found in catalog.")

        elif choice == '3':
            item_name = input("Enter item name to remove: ").strip()
            cart.remove_item(item_name)

        elif choice == '4':
            cart.view_cart()

        elif choice == '5':
            cart.checkout()

        elif choice == '6':
            print("👋 Exiting. Thank you for visiting!")
            break

        else:
            print("⚠️ Invalid choice. Please select from 1-6.")


if __name__ == "__main__":
    main()
