"""
Code Challenge
  Name: 
    Intersection
  Filename: 
    Intersection.py
  Problem Statement:
    With two given lists [1,3,6,78,35,55] and [12,24,35,24,88,120,155]
    Write a program to make a list whose elements are intersection of the above
    given lists.  
"""
################################### Version 1 ############################################
first_list = [1,3,6,78,35,55]

second_list = [12,24,35,24,88,120,155]

# Using set to get the intersection of first and second list
intersection_list = list(set(first_list).intersection(second_list))

print (intersection_list)

################################### Version 2 ############################################


first_list = [1,3,6,78,35,55]

second_list = [12,24,35,24,88,120,155]

intersection_list = []
for i in first_list:
    if i in second_list:
        intersection_list.append(i)
        
print (intersection_list)


################################### Version 3 ############################################

first_list = [1,3,6,78,35,55]

second_list = [12,24,35,24,88,120,155]

intersection_list = list(filter(lambda x: x in second_list,first_list))

print (intersection_list)
