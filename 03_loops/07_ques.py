# Problem: Keep asking the user for input until they enter a number between 1 and 10.


while True:
    user_input = int(input("Enter the value btw 1-10: "))
    if 1 <= user_input <= 10:
        print("Now you are choosing the right one")
        break
    else:
        print("invalid numbe try again")
