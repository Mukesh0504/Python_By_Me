# Problem: Reverse a string using a loop.

name = "Mukesh"
reverse_string = ""

# FIRST METHOD
for char in range(-1, -len(name) - 1, -1):
    # print(name[char])
    reverse_string = reverse_string + name[char]
print("1st method", reverse_string)



# SECOND METHOD
rev_string = ""
for char in name:
    rev_string = char + rev_string
print("2nd method", rev_string)
