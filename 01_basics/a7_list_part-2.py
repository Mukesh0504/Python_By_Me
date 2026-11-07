# conditioning in list
city = ['Rewa', 'Bhopal', 'Noida', 'Pune', 'Delhi'] 

city.append('mauganj')  #it add value in the last

# if 'mauganj' in city:
#     print('I have this city')
# else:
#     print('i don\'t have this city')

pop_result = city.pop() # it removed the last value
# print(pop_result)

city.insert(1, 'Mayur Vihar')  #it insert the value at given position
city.remove('Bhopal')  #it remove the given value
# print(city)




city_copy  = city.copy()  # it copied the value without giving it own reference
print(city_copy)



# loops under the list
squared_nums  = [x**2 for x in range(10)]
print(squared_nums)

cube_num = [y**3 for y in range(10)]
print(cube_num)