# Task 1: Product Collections (Lists & Tuples)

# 1. Create a list containing at least 6 product names
products = ["Laptop", "Mobile", "Headphones", "Keyboard", "Mouse", "Monitor"]

# 2. Create a tuple for one product
sample_product=("Laptop",55000,"Electronics")

# 3. Print the 2nd and last product
print("Second Product: ", products[2])
print("Last Product: ",products[-1])

# 4. Append two new product names and print the updated list
products.append("Tablet")
products.append("Smartwatch")
print("Updated Product List: ", products)

# Extra (Optional): Convert tuple to list, change price, and convert back
sample_product_list = list(sample_product)
print("Original Sample Product: ", sample_product)
sample_product_list[1] = 60000  # Change the price
sample_product = tuple(sample_product_list)
print("Updated Sample Product: ", sample_product)