# Problem: Calculate the sum of even numbers up to a given number n.

n = int(input("Enter the range of n: "))

sum_even = 0

for num in range(1, n + 1):
    if num % 2 == 0:
        sum_even += num

print("The sum of even number is: ", sum_even)
