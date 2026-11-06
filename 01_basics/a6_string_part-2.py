# Change the list to string
chai_variety = ['lemon', 'masala', 'ginger']



print("".join(chai_variety))
print(", ".join(chai_variety))
print(" - ".join(chai_variety))
print(".".join(chai_variety))



new_chai = 'Masala Chai'
for letter in new_chai:
    print(letter)



intro = "He said, \"His name is mukesh Dwivedi\""    #if we want to treat this under quote as string so we have use '\' before the quote.
print(intro)



new_text = 'Mukesh\nDwivedi' #it print the text in two line to remove this we can use 'r' before the quote.
print(new_text)

new_text = r'Mukesh\nDwivedi'
print(new_text)



win_path1 = r'c:\user\mukesh\project'   # these are the two way to solve this error
win_path2 = 'c:\\user\\mukesh\\project'
print(win_path1,'=====',win_path2)



# we can also search keyword in string it will return true or false
print('Masala' in new_chai)




