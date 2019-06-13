
"""
Code Challenge
  Name: 
    copy command
  Filename: 
    copy_file.py
  Problem Statement:
    Make a program that create a copy of a file    
"""

# copy 'words.txt' into 'abc.txt'

another_file = open('abc.txt','wt')
with open('words.txt','rt') as file:
    for text in file.readlines():
        another_file.write(text)
another_file.close()