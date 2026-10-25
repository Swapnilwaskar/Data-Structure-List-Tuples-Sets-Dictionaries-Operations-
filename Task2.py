# Task 2: Categories (Sets)

# 1. From your products list, create a set of categories called categories_set. (if product namesdo not contains categories, create a short parallel list categories = [..] with matching length and use that)
products = ["Laptop", "Mobile", "Headphones", "Keyboard", "Mouse", "Monitor"]
categories = ["Electronics", "Electronics", "Electronics", "Accessories", "Accessories", "Electronics"]

# create  a set of unique categories
categories_set = set(categories)
print("Unique Categories: ", categories_set)

# 2. Add new category and demonstrate duplicates are ignored
categories_set.add("Furniture")
print("Categories after adding 'Furniture': ", categories_set)
categories_set.add("Electronics")  # This is a duplicate
print("Categories after adding duplicate 'Electronics': ", categories_set)

# 3. check whether a category existsint the set and print the result
category_to_check = "Electronics"
print(f"Does '{category_to_check}' exist in categories_set? ", category_to_check in categories_set)
print(f"Does 'Toys' exist in categories_set? ", "Toys" in categories_set)

# count the unique categories and print the count
print("Count of unique categories: ", len(categories_set))