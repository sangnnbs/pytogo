# Following the articles on checkme.txt
# Let's focus on basic knowledge of Data Structures (ref: https://pythongeeks.org/python-data-structures/)
# This cheatsheet would help (https://storage.googleapis.com/kaggle-forum-message-attachments/923535/16292/Python%20Data%20Structures%20Cheat-sheet.jpg)



#--------------- Lists -------------
# Create list
list = []       # Syntax
list = list()   # Constructor

# Accessing an element
list[0]                 # Accessing 1st element 
list[1]                 # Accessing 2nd element
list[0:5]               # Slicing from 1st to 6th element
list[-2:-6]             # Slicing from last 7th to 3rd element
list[:4]                # Slicing all till 5th element

# Modifying and deleting elements and list

list[1:3]=[3.5,8]       #Modify elements

del list[1:3]           #Delete elements

list = [41,22,315,6]    #Modify whole list

del list                #Delete list

# Addition and multiplication of the lists in Python

list1 = [315,22,315,111,111,233,2]
list2 = ['a','b','c',4]
list1 + list2

list2*3                 #Multiply list



# Python Built-in Functions

list.append('as')       #adds an element to the list at the end.
list.insert(2,'bs')     #inserts the value in the specified location => insert({index}, {value})
list.pop()              #deletes the last element or at the index    => pop() , pop({index})
list.remove('bs')       #removes the specified value                 => remove({value})
list.len()              #returns the length or number of elements in the list
list.sort()             #arranges the elements of the list in ascending or descending order
list.index()            #finds the index of the element passed
list.count()            #finds the number of times the value occurs in a list

#List Comprehension in Python
list2=[x**2 for x in list1]


# Nested Loops
for i in list:
    for j in range():
        pass