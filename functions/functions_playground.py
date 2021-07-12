def create_greeting(name):
    greeting = f" Hello, {name}!"
    return greeting

# print(create_greeting("Chilli"))
# print(create_greeting("kaye"))
# print(create_greeting("Paul"))
# print(create_greeting("Ben"))


# def convert_cm_to_in(length_cm):
#     length_in_inches = round (length_cm / 2.54, 2)
#     return length_in_inches

# print(convert_cm_to_in(20))


# def convert_in_to_cm(length_in):
#     length_in_cm = round (length_in  * 2.54, 2)
#     return length_in_cm

# print(convert_in_to_cm(2))


def calculate_mean(a, b):
    total = a + b
    mean = total / 2
    return mean 

print(calculate_mean(2, 4))
print(calculate_mean(3, 4))
print(calculate_mean(5, 10))
