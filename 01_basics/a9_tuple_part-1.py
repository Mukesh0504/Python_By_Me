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


