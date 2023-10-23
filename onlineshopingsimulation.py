#create a new account
user = input("Enter you first name")
email = input("Enter you email address")

#available products
products = [
    {"name": "Phone", "price": 500, "quantity": 10},
    {"name": "Laptop", "price": 1200, "quantity": 5},
    {"name": "Headphones", "price": 100, "quantity": 20},
    # Add more products here
]
def display_product_list(products):
    print("Available Products:")
    print("-------------------")
    for product in products:
        print(f"Product: {product['name']}")
        print(f"Price: ${product['price']}")
        print(f"Quantity Available: {product['quantity']}")
        print("-------------------")

if products['quantity'] <= 5:
    print("product is not available")

# Call the function to display the product list
display_product_list(products)
