#Q1) Continuously ask the user to enter a number until they provide a blank input. Output the sum of all the numbers

sum = 0
number = 1
while number > 0:
    number = int(input("Enter a number: "))
    if number > 0:
        sum = sum + float(number)
print("The total sum of all number entered is {sum}")


#Q2) Ask the user to enter a number. Print all the odd numbers between 0 and that number (inclusive).

# n=int(input("Enter n value:"))
# for i in range(1,n+1,2):
#     print(i,end=" ")


#Q3) Select a number. Ask the user to enter a number, output whether their number is less than or greater than
#the selected number. Repeat this process until the user guesses the correct number

# guess =""
# while guess !="33":
#     guess = int(input("Guess a number between 0-50 - "))
#     if guess < 32:
#         print("Too Low")
#     elif guess > 34:
#         print("Too High")
#     else :
#         print("Great Guess ! ")