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


# to update the value
new_dict["age"] = 22
print(new_dict)


# Loops in Dict
# for data in new_dict:
#     print(data, new_dict[data])


# for key, value in new_dict.items():
#     print(key, value)



# CONDITION IN DICT
if "companya" in new_dict:
    print("i have company")
else:
    print("i don't have")





