# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 17:10:53 2023

@author: Sultan
"""

# In order to use alphabets and digits I import string library.
import string

# I take inputs from user to use in decryption function.
initial_text = str(input("Please enter the encrypted text: "))
shift_number = int(input("Please enter the shift number: "))

# I create a function with two parameters: encrypted text and shift number.
def decryption(text , shift):
   
   # with string library functions I make lists of lower case letters , upper case letters and digits.
   # I make list because i want to find and convert each letter and digit.
    alphabet_lower = list(string.ascii_lowercase)
    alphabet_upper = list(string.ascii_uppercase)
    digits = list(string.digits)
    
    # I make empty output list which is new decyrpted text.
    new_text = []
    
    # I make a loop that runs while checking every character in input text and ends after that.
    for ch in text:
    
        # If character is space it remains same and function adds it to new text list.
        if ch == ' ':
            new_text.append(' ')
        
        # If it is lower case letter function finds its order, adds shift number, 
        # mods with 26 in order to reduct it to alphabet range after that it finds back
        #  its place in alphabet and adds to the text list.
        elif ch in alphabet_lower :
            position = alphabet_lower.index(ch)
            new_position = (position + shift) % 26
            new_letter = alphabet_lower[new_position]
            new_text.append(new_letter)
        
        #Does same thing with lower case one .   
        elif ch in alphabet_upper :
            position = alphabet_upper.index(ch)
            new_position = (position + shift) % 26
            new_letter = alphabet_upper[new_position]
            new_text.append(new_letter)
        
        # Also does same but this time I mod with 10 because there are 10 characters in digits list.
        elif ch in digits :
            position = digits.index(ch)
            new_position = (position + shift) % 10
            new_text.append(digits[new_position])

    #Now I have a list full of new characters so I add them one after.
    new_text = ''.join(new_text)
    
    #Getting feedback
    return new_text

print(decryption(initial_text , shift_number))       
       
