# For loops: Exercise

# #Question 1 -  Ask the user for a number. Use a for loop to print the times tables for that number
# number = input("enter a number = ")

# for item in range(0,int(number)):
#     product = item * int(number)
#     print(f"{number} * {item} = {product}")

# number = input(" enter a number = ")

# for item in range(1,int(number)):
#     product = item * int(number)
#     print(f"{number} * {item} = {product}")

# number = input("enter a number = ")

# for item in range(0):
#     product = item * int(number)
#     print(f"{number} * {item} = {product}")

#Question 2 - Ask the user for a number. Use a for loop to sum from 0 to that number

# addition = int(input("Enter a number."))
# sum = 0
# for i in range(addition + 1):
#   sum = sum + i
#   i = i + 1
# print("Sum is ", sum)

#Question 3 - Given a list, use a for loop to sum all the numbers in the list.

# list = []
# num = int(input("how many numbers : "))
# for n in range(num):
#     numbers = int(input("Enter number : "))
#     list.append(numbers)
# print ("Sum of elements in given list is :", sum(list))

#Question 4  Use a for loop to format and print the following list:
mailing_list = [
["Chilli", "chilli@thechihuahua.com"],
["Roary", "roary@moth.catchers"],
["Remus", "remus@kapers.dog"],
["Prince Thomas of Whitepaw", "hrh.thomas@royalty.wp"],
["Ivy", "noreply@goldendreamers.xyz"],
]

i = 0
while i < len(mailing_list):
    print(f"{mailing_list[i][0]}: {mailing_list[i][1]}")
    i = i + 1
