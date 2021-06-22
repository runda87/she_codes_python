# Q1)Below is a list of foods and their prices perunit:groceries. Ask the user how many units of each item they bought,
# then output the corresponding receipt.For the input below, assume that the input is providedin the same order as defined in the list

groceries = [
    ["Baby Spinach", 2.78],
    ["Hot Chocolate", 3.70],
    ["Crackers", 2.10],
    ["Bacon", 9.00],
    ["Carrots", 0.56],
    ["Oranges", 3.08]
]

till = [   
]

for item in range(len(groceries)):
    amount = float(input("how many did you buy"))
    line_1 = (groceries[item][0])
    line_2 = float(groceries[item][1])
    calc = (line_2* amount)
    print((line_1),calc)

sum=sum(till)
print(f"subtotal: ${sum}")

