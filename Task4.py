# Task 4: Combined Operations
# Using the products list and price_dict, create a list of tuples where each tuple contains a product name, price, category.
products = ["Laptop", "Mobile", "Headphones", "Keyboard", "Mouse", "Monitor", "Tablet"]
categories = ["Electronics", "Electronics", "Electronics", "Accessories", "Accessories", "Electronics", "Electronics"]
price_dict = {"Laptop": 55000, "Mobile": 22000, "Headphones": 1500, "Keyboard": 1200, "Mouse": 800, "Monitor": 10000, "Tablet": 25000}

combined_list = list(zip(products, [price_dict.get(product) for product in products], categories))
print("Combined List of Products:", combined_list)

# from catalog , create anew dictionary category_to_products that maps each category to a list of products in that category.
category_to_products = {}
for product, category in zip(products, categories):
    if category not in category_to_products:
        category_to_products[category] = []
    category_to_products[category].append(product)

print("Category to Products Mapping:", category_to_products)

# print all products that belong  to the category that has the maximum number of products.
max_category = max(category_to_products, key=lambda k: len(category_to_products[k]))
print(f"Category with Maximum Products: {max_category}, Products: {category_to_products[max_category]}")