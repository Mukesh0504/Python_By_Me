# Problem: Customize a coffee order: "Small", "Medium", or "Large" with an option for "Extra shot" of espresso.

coffee_size  = input("Please tell me the coffee size: e.g \n 1. small\n 2. medium\n 3. large ---> ")

extra_shot = True

if extra_shot:
    coffee = coffee_size + " coffee with an extra shot"
else:
    coffee = coffee_size + " coffee"


print(coffee)