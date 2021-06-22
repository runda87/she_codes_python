from typing import ItemsView


prices = {
    "Baby Spinach": 2.78,
    "Hot Chocolate": 3.70,
    "Crackers": 2.10,
    "Bacon": 9.00,
    "Carrots": 0.56,
    "Oranges": 3.08
}

quantity1 = {
    "Baby Spinach": 1,
    "Hot Chocolate": 3,
    "Crackers": 2,
    "Bacon": 1,
    "Carrots": 4,
    "Oranges": 2
}

quantity2 = {
    "Baby Spinach": 2,
    "Hot Chocolate": 1,
    "Crackers": 4,
    "Bacon": 0,
    "Carrots": 8,
    "Oranges": 5
}

for item, quantity1 in quantity1.items():
    print(f"{quantity1} {item} @ $ {prices[item]} = ${(quantity1 * prices[item])}")

print()

for item, quantity2 in quantity2.items():
    print(f"{quantity2} {item} @ $ {prices[item]} = ${(quantity2 * prices[item])} ")


