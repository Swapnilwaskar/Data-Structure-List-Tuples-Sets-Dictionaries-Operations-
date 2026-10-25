# Task 3: Product Pricing (Dictionaries)

# 1.Create a dictionary price_dict where keys are product names and values are prices
price_dict = {"Laptop": 55000, "Mobile": 20000, "Headphones": 1500, "Keyboard": 1200, "Mouse": 800, "Monitor": 10000}
print("Product Prices:", price_dict)

# 2.1 Add new product with price and print the updated dictionary
price_dict["Tablet"] = 25000
print("Updated Product Prices:", price_dict)

# 2.2 Update the price of an existing product and print the updated dictionary
price_dict["Mobile"] = 22000
print("Updated Product Prices after changing Mobile price:", price_dict)

# 3 print average price of all products
average_price = sum(price_dict.values())/len(price_dict)
print("Average Price of Products:", average_price)

# print the product with max and min price
max_price_product = max(price_dict, key=price_dict.get)
min_price_product = min(price_dict, key=price_dict.get)
print("Product with Maximum Price:", max_price_product, "Price:", price_dict[max_price_product])
print("Product with Minimum Price:", min_price_product, "Price:", price_dict[min_price_product])