num = 10
import  sys

print(sys.getrefcount(num)) #it always shows a  random value 

num = 'mukesh'
num = 10.5


# NOTE:-
# garbage collection does not removes the reference of num and string immedietly
myListOne = [1,2,3]
myListTwo =myListOne

myListOne = 'chai' #--------1
myListOne = [1,2,3] # ---------2

myListOne[0] = 55  # ---------3
print (myListOne,myListTwo)


#--------second senario
h1 = [10,20,30]
h2 = h1[:]

# print(h1, h2)
h1[0] = 55
# print(h1,h2)        # if we change any value of h1 it does change the value of h2 because h2 = [:] this syntax didn't take the reference of h1, it only store a copied value


#--------------------
box1  = [1000, 2000, 3000]

import copy
box2 = copy.copy(box1)
# box2 = copy.deepcopy(box1)  #it will copy the nested list

# print(box1, box2)



#----------------------------------
n = [30, 40, 50]
m = n

print(m==n)
print (m is n)   #true
m = [30,40,50]  # if we assign the value explicitly the reference of both the variable will be changed
print(m is n)  #false





