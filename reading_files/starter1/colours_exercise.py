#Q1)Write a program that reads incolours_20_simple.csvand output the colour data
# import csv

# colours = []

# with open("colours_20_simple.csv", encoding="utf-8") as csv_file:
#     reader = csv. reader(csv_file)
#     for line in reader:
#         colours.append(line)

# i = 0
# while i < len(colours):
#     print(f"{colours[i][0]} {colours[i][1]} {colours[i][2]}")
#     i = i + 1


#Q2)Writeaprogramthatreadsincolours_20_simple.csvandoutputsthecolourdatainorderEnglish,Hexthen RGB.

# i = 0
# while i < len(colours):
    # print(f"{colours[i][2]} {colours[i][1]} {colours[i][0]}")
    # i = i + 1

# Q3)Write a program that reads incolours_20.csvand output the colour data in order English, Hex thenRGB

# import csv

# colours = []

# with open("colours_20.csv", encoding="utf-8") as csv_file:
#     reader = csv. reader(csv_file)
#     for line in reader:
#         colours.append(line)

# i = 1
# while i < len(colours):
#     print(f"{colours[i][4]}: Hex {colours[i][2]}: RGB {colours[i][1]}")
#     i = i + 1


#Q4)Using the same colour csv files, write a program that out puts the number 
# of times each of the following colours appear in the English 
# Name:
# ●red
# ●green
# ●blue

import csv

colours = []

with open("colours_20.csv", encoding="utf-8") as csv_file:
    reader = csv. reader(csv_file)
    for line in reader:
        colours.append(line)

print(colours)


# red = 
# green = 
# blue = 
# yellow = 
