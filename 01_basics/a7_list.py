fruit_varities = ['apple', 'mango', 'kiwi', 'orange']

print(fruit_varities)

print(fruit_varities[-1])
print(fruit_varities[0:4])
print(fruit_varities[0:4:2])

fruit_varities[3] = 'papaya'
print(fruit_varities)


fruit_varities[1:2] = 'Lemon' # this is not a good practice because it treat the value as an array
print(fruit_varities)
fruit_varities[1:2] = ['Lemon'] #this is the right way to assign