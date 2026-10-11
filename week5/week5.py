class ShoppingCart:
    def __init__(self):
        # Har cart ki apni items list hogi
        self.items = []

    def add_item(self, product, price, quantity):
        # Product, price aur quantity ko cart mein add karna
        item = {
            "product": product,
            "price": price,
            "quantity": quantity
        }
        self.items.append(item)

    def calculate_total(self):
        # Cart ke tamam items ka total calculate karna
        total = 0
        for item in self.items:
            total += item["price"] * item["quantity"]
        return total


# First cart
cart1 = ShoppingCart()
cart1.add_item("Laptop", 100000, 1)
cart1.add_item("Mouse", 1500, 2)

# Second cart
cart2 = ShoppingCart()
cart2.add_item("Keyboard", 3000, 1)
cart2.add_item("Headphones", 2500, 2)

# Display results
print("Cart 1 Items:", cart1.items)
print("Cart 1 Total: Rs.", cart1.calculate_total())

print("\nCart 2 Items:", cart2.items)
print("Cart 2 Total: Rs.", cart2.calculate_total())