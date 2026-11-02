import random
print(random.random())  #it gives a random number between 0-1

print(random.randint(1,100)) #it gives a random number between gievn parameter 1,100


l1 = ['lemon', 'masala chai', 'ginger tea', 'mint']
print(random.choice(l1)) # it gives a random choice of given list, number or anything


random.shuffle(l1) # it shuffles the values of list
print(l1)

# ===========decimal problem==============

print(0.1 + 0.1 + 0.1 -0.3) #it is giving a wrong value
print((0.1 + 0.1 + 0.1 )-0.3)

from decimal import Decimal
print(Decimal('0.1') + Decimal('0.1') + Decimal('0.1') - Decimal('0.3')) # it gives a right answer


# = == ==== === = FRACTION ===== === == ===
from fractions import Fraction
myfra = Fraction(2,7)
print(myfra)


# =========== SET ============

setone = {1,2,3,4}
print (setone & {1, 2, 4})  # intersection
print (setone | {1,2,4})    # uninon
print (setone - {1,2,4})    # difference


print(setone - {1, 2, 3, 4}) # it returns the empty value 'set()' but not empty {}, because {} denoted the empty dict

print(type(()))
print(type({}))


print(type(True))
print(True == 1)
print(True is 1)
print(True + 4)

