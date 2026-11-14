fruit = "Banana"
fruit_color = input("Enter the fruit color: ").lower()


if fruit == "Banana":
    if fruit_color == "green":
        print("Unripe")
    elif fruit_color == "yellow":
        print("ripe")
    elif fruit_color == "Brown":
        print("Overripe")
    else:
        print("Please provide a valid color")

    