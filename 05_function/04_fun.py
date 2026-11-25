# Problem: Create a function that returns both the area and circumference of a circle given its radius.

import math


def circle_stats(radius):
    area = math.pi * radius * radius
    circum = 2 * math.pi * radius
    return area, circum


area, circum = circle_stats(2)
print("Area:", area)
print("Circumference :", circum)

print(round(area, 2))  # to get a presision of two digit after decimal
