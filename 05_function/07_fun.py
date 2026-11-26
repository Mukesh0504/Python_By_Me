# Problem: Write a function that takes variable number of arguments and returns their sum.


def sum_all(*args):  # *args can hold multiple values
    print(args)  # (1,2,3)

    for i in args:
        print("i =", i * 2)

    return sum(args)


print(sum_all(1, 2, 3))
# print(sum_all(1, 2, 3, 4, 5))
# print(sum_all(1, 2, 3, 4, 5, 6))
