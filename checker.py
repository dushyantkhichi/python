"""
Code Challenge
  Name: 
    Name Printing Checkerboard pattern
  Filename: 
    checker.py
  Problem Statement:
    Print the checkerboard pattern using escape Codes and Unicode 
    with multiple print statements and the multiplication operator 
  Hint: 
    Eight characters sequence in a line and 
    the next line should start with a space
    try to use the * operator for printing
  Input:
    No input required
  Output:
    * * * * * * * *
     * * * * * * * *
    * * * * * * * *
     * * * * * * * *
    * * * * * * * *
     * * * * * * * *

"""

print("* "*8) # printing pattern line starting with star('*')
print(" *"*8) # printing pattern line starting with space(' ')
print("* "*8) # printing pattern line starting with star('*')
print(" *"*8) # printing pattern line starting with space(' ')
print("* "*8) # printing pattern line starting with star('*')
print(" *"*8) # printing pattern line starting with space(' ')
print("* "*8) # printing pattern line starting with star('*')

###################### OR ################

print(("* "*8+"\n"+" *"*8+"\n")*3)