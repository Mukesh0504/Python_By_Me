# Problem: Create a function that accepts any number of keyword arguments and prints them in the format key: value.


def print_kwargs(**kwargs):  # **kwargs can hold the value in dict type
    for key, value in kwargs.items():
        print(f"{key} : {value}")


print_kwargs(name="Mukesh", course="B.C.A")  # we can pass the arguments like this also

print_kwargs(name="Mukesh", course="B.C.A", org="Wipro")
