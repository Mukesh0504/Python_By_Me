# Problem: Write a generator function that yields even numbers up to a specified limit.


def even_generator(limit):
    for i in range(2, limit + 1, 2):
        yield i


# for num in even_generator(10):
#     print(num)

num = even_generator(10)
print(next(num))
print(next(num))






print("================================")
# FOR BETTER UNDERSTANDING

def my_generator():
    print("Start")
    yield 10

    print("Middle")
    yield 20

    print("End")
    yield 30


gen = my_generator()

print(next(gen))
print(next(gen))
print(next(gen))
