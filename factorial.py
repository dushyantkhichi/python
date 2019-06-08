"""
Code Challenge
  Name: 
    Facorial
  Filename: 
    factorial.py
  Problem Statement:
    Find the factorial of a number. 
  Hint: 
    Factorial of 3 = 3 * 2 * 1= 6 
    Try to first find the function from math module using dir and help 
  Input:
    Take the number from the keyboard as input from the user.
"""

from math import factorial

input_number = int(input("Enter the number >"))
Factorial_of_input_number = factorial(input_number)
print ("Factorial of {0} is {1}".format(input_number,Factorial_of_input_number))

############################# OR ###################################
counter = 1
input_number = int(input("Enter the number >"))
for i in range(1,input_number+1):
    counter = counter*i
print ("Factorial of {0} is {1}".format(input_number,counter))


############################ OR ####################################


counter = 1
input_number = int(input("Enter the number >"))
for i in range(input_number,1,-1):
    counter = counter*i
print ("Factorial of {0} is {1}".format(input_number,counter))


############################ OR ####################################

counter = 1

input_number = int(input("Enter the number >"))

counter1  = input_number
while counter1 >0:
    counter *= counter1
    counter1 -=1

print ("Factorial of {0} is {1}".format(input_number,counter))