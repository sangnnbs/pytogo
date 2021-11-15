# Following the articles on checkme.txt
# Let's focus on basic knowledge of Data Structures (ref: https://pythongeeks.org/python-data-structures/)
# This cheatsheet would help (https://storage.googleapis.com/kaggle-forum-message-attachments/923535/16292/Python%20Data%20Structures%20Cheat-sheet.jpg)



#--------------- Sets -------------
# Create set
from typing import Union


set1 = {'s',1,5,6,(1,22)}       # Syntax
set2 = set(())   # Constructor - double round-brackets

# Accessing an element
    # We cannot use indexing. But we can use 'for' loop 
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x) 
  
    # Check value in set
thisset = {"apple", "banana", "cherry"}

print("banana" in thisset) 


# Operations on sets in Python

set1.union(set2)                #returns the combined values from both the sets
set1.intersection(set2)         #returns the set of common values from both the sets
set1.difference(set2)           #returns the set of values of the first set that are not there in the second one
set1.symmetric_difference(set2) #returns the set of values from both the sets that are not common to the sets.

#  Changing Python set value by using list():
list = list(set1)

# Python Built-in Functions
set1.add('as')          #adds an element to the list at the end.
set1.pop()              #deletes the last element or at the index    => pop() , pop({index})
set1.remove('bs')       #removes the specified value                 => remove({value})
len(set1)               #returns the length or number of elements in the list
set1.clear()            #delete all the elements in set
set1.discard()          #removes the specified element from the set. But this function does not give an error if the element is not present in the set.