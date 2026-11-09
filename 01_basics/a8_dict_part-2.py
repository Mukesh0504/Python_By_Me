new_dict = {
    "name": "mukesh", 
    "age": 100, "company": 
    "Wipro", "Program": "Wilp"
    }


# CONDITION IN DICT
if "company" in new_dict:
    print("i have company")
else:
    print("i don't have")


tea_shop = {
    "chai": {"masala": "spicy", "ginger": "zesty"},
    "City": {1: "Rewa", 2: "Delhi", 3: "Bhopal"},
}

print(tea_shop)
print(tea_shop["City"][2])


squared_nums = {x:x**2 for x in range(6)}
print(squared_nums)
squared_nums.clear()  # to clear the keys and values


# To create the dictionary
keys  = ["Masala","ginger","Lemon"]
default_value = 'Delecious'

new_tea  = dict.fromkeys(keys,default_value) 
print(new_tea)