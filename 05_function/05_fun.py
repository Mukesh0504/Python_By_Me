# Problem: Write a function that greets a user. If no name is provided, it should greet with a default name.


def greets(name="Mukesh"):
    return "Good Morning! " + name


print(greets("Nilesh"))
print(greets())
