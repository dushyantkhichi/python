
"""
Code Challenge
  Name: 
    Romeo and Juliet
  Filename: 
    romeo.py
  Problem Statement:
    Let’s start with a very simple file of words taken from the text of 
    Romeo and Juliet. (romeo.txt)
    We will write a Python program to read through the lines of the file
    break each line into a list of words
    and then loop through each of the words in the line,
    and count each word using a dictionary.    
"""

#version 1

list1=[]
file=open('data/romeo.txt',"r",encoding="utf8")

count=dict()
for line in file:
    words = line.split()
    list1.append(words)
    for word in words:
        if word not in count:
            count[word] = 1
        else:
            count[word] += 1
print("\nList of Words: ")
print("----------------------------------------------")
print(list1)
print("\nWord counts are: ")
print("----------------------------------------------")
print(count)


#version 2

import re
file2=open('data/romeo2.txt',"r",encoding="utf8")
data=file2.read()
result=re.sub('[^A-Za-z\s]','',data)
print(result)
dict_=dict()
for line in result.split():
        if line not in dict_:
            dict_[line]=1
        else:
            dict_[line]+=1

print("\nWord counts :")
print(dict_)
            

#version 3

# To open the file
with open("romeo.txt", "rt") as fileobj:

    content = fileobj.readlines()
    
    # List to hold the list of the words
    req_content = []
    for var in content:
        req_content.append(var.split())
    
    # To count the words using dictionary
    dict1 = {}
    for var2 in req_content:
        for var3 in var2:
            if var3 not in dict1:
                dict1[var3] = 1
            else:
                dict1[var3]+=1
            
       