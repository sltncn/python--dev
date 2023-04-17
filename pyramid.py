# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 17:17:09 2023

@author: Sultan
"""

# A function that takes row as a parameter. Row is the desired row value in the sample.
def draw(row):

    # row number is divided by two because i will print same line two times, eventually row number remains same.
  n = int(row/2)

  # for each number from 0 to n; it prints n-i-1 times space, 2*i+2 times * and creates new line; this process repeats 2 times for each i value in n.
  for i in range(n):  
      for a in range(2):
          for j in range(n-i-1): 
              print(" ", end = "  ")
          
          for j in range(2*i+2):
              print("*", end="  ")
          print()
    
draw(10)
