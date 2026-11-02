# NUMBERS IN PYTHON

print(1 + 2)
print(1 - 2)
print(1 * 2)
print(1 / 2)
print(1 % 2)  #modulos
print(1 ** 2) #exponentiation
print(2 // 4) #floor division

40 + 2.3  # this is not a good practice, we always have to play with the same datatype

print(int(2.3))
print(float(40))

x = 2
y = 3
z = 4
print('chai' + 'code')
print(x,y,z)
print(x+2, y*3)
print(y % 2)

print(2 ** 1000)


print(repr('chai'))  # "'chai'"
print(str('chai'))   # 'chai'
print('chai')        # chai


# *****************Comparison****************************
print(1 < 2)
print(1 > 2)
print(1 <= 2)
print(1 >= 2)
print(5.0 == 5.0)
print(4.0 != 5.0)

print(x < y < z) # this is not good practice
print(x < y and y < z)

print("or :- ",x < y or y < z)
print('and :-',x < y and y < z)


print( 1 == 2 < 3 ) #false - 1==2 and 2<3

#****************************

import math
print(math.floor(3.6)) # always going to the smallest one
print(math.floor(-3.3))

print(math.trunc(2.8)) # it always goes to the nearest zero
print(math.trunc(-2.8)) 


# ==========imaginery number===============
print((3 + 1j)*3)






# ==============
print(0o20) #octal
print(0xff) #hexa
print(0b1000) #binary
print(oct(64))
print(hex(64))
print(bin(64))

print(int('64',8))
print(int('64',16))
print(int('10000',2))
