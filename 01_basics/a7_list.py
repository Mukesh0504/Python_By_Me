fruit_varities = ['apple', 'mango', 'kiwi', 'orange']

print(fruit_varities)

print(fruit_varities[-1])
print(fruit_varities[0:4])
print(fruit_varities[0:4:2])

fruit_varities[3] = 'papaya'
print(fruit_varities)
 

# fruit_varities[1:2] = 'Lemon' # this is not a good practice because it treat the value as an array
fruit_varities[1:2] = ['Lemon'] #this is the right way to assign
print(fruit_varities)


fruit_varities[1:3] = ['Banana', 'Grapes']
print(fruit_varities)



print(fruit_varities[1:1])
fruit_varities[1:1] = ['test','test']  # it insert the values after 0th position
print(fruit_varities)

fruit_varities[1:3] = []  #it removes the value from the given position
print(fruit_varities)


# LOOPS IN LIST
for fruit in fruit_varities:
    print(fruit)