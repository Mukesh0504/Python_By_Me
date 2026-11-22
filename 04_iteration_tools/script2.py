# =======================Iter in list====================

mylist = [1,2,3]
i = iter(mylist)
i
# <list_iterator object at 0x000001AF1141D180>
i.__next__()
# 1
i
# <list_iterator object at 0x000001AF1141D180>
i.__next__()
# 2
i.__next__()
# 3
i.__next__()
# Traceback (most recent call last):
#   File "<python-input-18>", line 1, in <module>
#     i.__next__()
#     ~~~~~~~~~~^^
# StopIteration




# ++++++++++++++++++ f is iter  +++++++++++++++++++
f =open("01_script.py")
iter(f) is f
# True

iter(f) is f.__iter__()
# True



# =================================================
myNewList = [1,2,3,4,5]
iter(myNewList) == myNewList
# False



# ===++++++++++++++++++++++++++++++++++++++++++++++++++++
new_dict = {"name": "mukesh", "age": 100, "company": "Wipro"}
I = iter(new_dict)
I.__next__()
# 'name'
next(I)
# 'age'
next(I)
# 'company'
next(I)

# Traceback (most recent call last):
#   File "<python-input-36>", line 1, in <module>
#     next(I)
#     ~~~~^^^
# StopIteration






# ++++++++++++++  it is also applied on range()  ++++++++++++++
range(0,5)
range(0, 5)
R = range(0,5)
I = iter(R)
next(I)
0
next(I)
1
