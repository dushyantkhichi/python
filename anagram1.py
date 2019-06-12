# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 17:36:47 2019

@author: User
"""

"""
Code Challenge
  Name: 
    Anagram
  Filename: 
    anagram.py
  Problem Statement:
   Two words are anagrams if you can rearrange the letters of one to spell the second.  
   For example, the following words are anagrams:
   ['abets', 'baste', 'bates', 'beast', 'beats', 'betas', 'tabes']
   
  Create a function which takes two arguments and return whether they are angram or no ( True or False)
  
  Hint: 
   How can you tell quickly if two words are anagrams?  
   Dictionaries allow you to find a key quickly.  

"""

################################################## Version 1 ##########################################################################################

def anagram(w1,w2):
    dict1 = {}
    dict2 = {}
    for i in w1:
        if i not in dict1:
            dict1[i] = 1
        else:
            dict1[i] =+ 1
    for z in w2:
        if z not in dict2:
            dict2[z] = 1
        else:
            dict2[z] =+ 1
    if len(dict1.keys()) == len(dict2.keys()) and sorted(list(dict1.keys()))==sorted(list(dict2.keys())):
        return ("Words {0} and {1} are anagram".format(w1,w2))
    else:
        return ("Words {0} and {1} are not  anagram".format(w1,w2))
    
user_1 = input("Enter the first word>>")
user_2 = input("Enter the second word>>")

anagram(user_1,user_2)        
################################################# Version 2 ############################################################################################

# Function to check the given words are anagram or not
def anagram_filter(word_1, word_2):
    if len(word_1) == len(word_2):
        if sorted(word_1) == sorted(word_2):
            return True
        else:
            return False
    else:
        return False
        

# Taking the words as input that are needed to be checked
first_word = input("Enter your first word here:")
second_word = input("Enter your second word here:")

# Final conclusion returned by function
final_result = anagram_filter(first_word, second_word)

if final_result == True :
    print ("Its Anagram")
else:
    print ("Not Anagram")
    
############################################### Version 3 #############################################################################################
    
    
    
def anagram_word(w1,w2):
    if set(w1) == set(w2):
        return ("Words {0} and {1} are anagram".format(w1,w2))
    else:
        return ("Words {0} and {1} are not  anagram".format(w1,w2))
    
    
user_1 = input("Enter the first word>>")
user_2 = input("Enter the second word>>")

anagram_word(user_1,user_2)    













