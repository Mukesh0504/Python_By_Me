# Problem: Check if a number is prime.

number = int(input("Enter any  number: "))

count = 0
if number > 1:
    for i in range(1, number + 1):
        if (number % i) == 0:
            count += 1

if count == 2:
    print(number, "is prime number")
else:
    print(number, "is not a prime number")





# 2nd method

num = 5
is_prime = True

if num > 1:
    for i in range(2,num):
        if (num %i) ==0 :
            is_prime = False


if is_prime:
    print("this is prime number")
else:
    print("this is not a prime number")



