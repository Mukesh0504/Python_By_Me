# Problem: Recommend a type of pet food based on the pet's species and age. (e.g., Dog: <2 years - Puppy food, Cat: >5 years - Senior cat food).

species = input("Enter the pet species: ")
age = int(input("Enter the Age - "))

if species == "dog":
    if age < 2:
        food = "puppy food"
    else:
        print("Please enter the correct age")
        exit()
  
elif species == "cat":
    if age > 5:
            food = "Senior cat food"
    else:
        print("Please enter the correct age")
        exit()

else:
     print("Please enter the correct species")
     exit()
    

print("I recommend the", food)