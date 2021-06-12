# boolean - only 2 states true / false
# is_rainig = False
# is_cold = True
# print(type(is_rainig))
# print(type(is_cold))

# print(is_rainig) # true
# print(not is_rainig) # false
# print(is_rainig or is_cold) #true
# print(is_rainig and not is_cold) # false
# print(is_rainig or not is_cold) # false = true
# print(not is_rainig and not is_cold) # false

# print()
# temp = 16
# print(temp < 18)
# print(temp > 18)

# wind_chill = 3
# print(wind_chill > 4)
# print( temp - wind_chill < 16)


# code = "freeticket"
# print(code == "freeticket")
# print(code != "freeticket")


# is_raining = True
# if is_raining:
#     print("Take an umbrella")
# else: 
#     print("Do not takes an umbrella")
# print("cats")


# temp = 16 
# wind_chill = 4

# if temp - wind_chill < 16:
#     print("take a jumper.")
# elif temp - wind_chill > 30:
#     print("It is hot. Stay home")
# else:
#     print("wow, what a lovely day!")

# if temp < 16:
#     if is_raining:
#         print("Just stay home")
#     else:
#         print("It's ok today")    
# else:
#     print()        

# moths_in_house = True
# if moths_in_house:
#     print("Get the moths!")
# else:
#     print("No threats detected")

# moths_in_house = False
# mitch_is_home = True

# if moths_in_house and mitch_is_home:
#     print("Hooman! Help me get the moths!")
# elif moths_in_house and not mitch_is_home:
#     print("Meoooooooow! Hissssssss!")
# elif not moths_in_house and mitch_is_home:
#     print("Climb on Mitch.")
# else: 
#     print("No threats detetced.")


# light_colour = "Amber"
# car_detected = True

# if light_colour == "Red" and car_detected:
#     print("Flash!")
# else:
#     print("Do nothing")

# height = 135
# if height > 50:
#     print("Sorry, not today :(")
# elif height < 120:
#     print("Hop on!")

#question 5 
# username = input("Enter username - ")
# password = input("Enter pasword - ")

# if username =="fleur" and password =="password123":
#     print("Correct!")
# else:
#     print("Incorrect!")


#question 6
email = input("Enter email - ")

if "@" in email and "." in email:
    print("Valid email address.")
else:
    print("Invalid email address.")

    