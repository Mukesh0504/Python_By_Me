my_tuple = ("Black", "Green", "Oolong") # it is immutable
print(my_tuple, type(my_tuple))

print(my_tuple[1])
print(my_tuple[-1])
print(my_tuple[0:])

# my_tuple[0] = 'Lemon'  # it is showing error because tuple is immutable
print(len(my_tuple))


more_tea = ("herbal", "Earl Grey")
all_tea = my_tuple + more_tea
print(all_tea)



# Condition in Tuple
if "Green" in my_tuple:
    print("I have green")


more_tea = ("Herbal", "Earl Grey", "Herbal")
print(more_tea)
print(more_tea.count("Herbal"))
print(more_tea.count("Herb"))  #it returns 0 when no value will be found



# To unrap the tuple with tuple
tea_types = ("BLACK", "MASALA", "GREEN")
(black, masala, green) = tea_types  #it extract tuple value in variable
print(tea_types)
print(black, masala, green)   




nest_tuple = ("Phone", (1,2,3,4,5), "Charger")
print(nest_tuple)