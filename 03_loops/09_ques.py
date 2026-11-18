# Problem: Check if all elements in a list are unique. If a duplicate is found, exit the loop and print the duplicate.

items1 = ["apple", "banana", "orange", "banana", "mango"]

unique_item = set()

for item in items1:
    if item in unique_item:
        print("unique item is: ", item)
    else:
        unique_item.add(item)




# items2 = ["apple", "banana", "orange", "banana", "mango"]

# for item in items2:
#     if items2.count(item) > 1:
#         print(item)
#         break
