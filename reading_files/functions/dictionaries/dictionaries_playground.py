groceries = {
    "Baby Spinach": 2.78,
    "Hot Chocolate": 3.70,
    "Crackers": 2.10,
    "Bacon": 9.00,
    "Carrots":0.56,
    "Oranges":3.08
    }

print(groceries)
print(groceries["Baby Spinach"])
print(groceries["Crackers"])

groceries["Crackers"] = 1.5
print(groceries)

groceries["Avacadoes"] = 3.0
print(groceries)

del groceries["Bacon"]
print(groceries)

for item in groceries:
    # print(item)
    print(f"{item}: ${groceries[item]}")

print()

for item, price in groceries.items():
    print(f"{item}: ${price}")