# Problem: Compute the factorial of a number using a while loop.

number = int(input("Enter the nth number: "))

fact = 1

while number > 0:
    # fact = fact * number
    # number -= 1
    fact *= number
    number -= 1

print("factorial of given term is ", fact)
