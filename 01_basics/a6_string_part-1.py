# STRING

chai = 'Masala chai'
first_char = chai[0]
print(first_char)

print(chai[0:6])
print(chai[-3:])


num_list = '0123456789'
print(num_list[4:7])
print(num_list[0:8:2])


newStr = '  Masala Chai Chai Chai  '
print(newStr.lower())
print(newStr.upper())
print(newStr.strip()) #it removes the extra spaces
print(newStr.replace("Masala", "Lemon"))


listStr = 'lemon, ginger, masala, mint'
print(listStr.split(', '))
print(newStr.find('Masala'))
print(newStr.count('Chai'))

quantity = 2
order = 'I ordered {} cups of {}'
print(order.format(quantity, newStr))
