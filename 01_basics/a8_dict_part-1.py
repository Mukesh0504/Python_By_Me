new_dict = {
    "name": "mukesh",
    "age": 100,
    "company": "Wipro"
    }

print(new_dict)
print(new_dict["company"])
# print(new_dict['naming'])   #it is showing key error

print(new_dict.get('name'))  #it return the vlue of given key
print(new_dict.get('compan'))  #it returns "none"  without any key error


# To insert the value
new_dict["program"] = "Wilp"
# print(new_dict)


# to update the value
new_dict["age"] = 22
print(new_dict)


# To delete the key / value
new_dict.pop("age") # it removes the item and return the removed value
new_dict.popitem()  # it removes the last item

del new_dict['company']  #it delete the item of given key
print(new_dict)



dict_copy  = new_dict.copy()  # it copied the dict without its reference


# Loops in Dict
for data in new_dict:
    print(data, new_dict[data])


for key, value in new_dict.items():
    print(key, value)









