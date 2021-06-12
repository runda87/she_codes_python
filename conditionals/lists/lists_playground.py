chilli_wishlist = [
    "igloo",
    "chicken",
    "donut toy",
    "cardboard box"
]

# print(chilli_wishlist)
# print(chilli_wishlist[0])
# print(len(chilli_wishlist))
# print(chilli_wishlist[-1])
# print(chilli_wishlist[0:2])

# chilli_wishlist[1] = "carrot"
# print(chilli_wishlist)

# #print the sublist of items in positions 2 through to 3. 
# print(chilli_wishlist[2:4])
# #print the item in the -3 position.
# print(chilli_wishlist[-3])

#adding items to list 
chilli_wishlist.append("dig mat")
print(chilli_wishlist)
chilli_wishlist.extend(["kong", "tennis ball", "crocodile toy"])
print(chilli_wishlist)
chilli_wishlist.insert(1, "peanut butter")
print(chilli_wishlist)

# remove items 
print(chilli_wishlist.pop())
print(chilli_wishlist)
print(chilli_wishlist.pop(2))
print(chilli_wishlist)
chilli_wishlist.remove("kong")
print(chilli_wishlist)

#add new item to position -2 
chilli_wishlist.insert(-2, "frisbee")
print(chilli_wishlist)
#remove the third item from the list 
print(chilli_wishlist.pop(3))
print(chilli_wishlist)
#add four new items to the end of the list
chilli_wishlist.extend(["ball", "towel", "bed","human"])
print(chilli_wishlist)
#remove the "igloo item from the list "
chilli_wishlist.remove("igloo")
print(chilli_wishlist)


chilli_wishlist = [
    ["igloo"],
    ["donut toy", "tennis ball","crocodile toy"],
    ["chicken", "peanut butter"],
    ["cardboard box", "kong"]
]

print(chilli_wishlist)
print(chilli_wishlist[0][0])
print(chilli_wishlist[3][0])