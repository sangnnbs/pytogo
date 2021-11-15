# Following the articles on checkme.txt
# Let's focus on basic knowledge of Data Structures (ref: https://pythongeeks.org/python-data-structures/)
# This cheatsheet would help (https://storage.googleapis.com/kaggle-forum-message-attachments/923535/16292/Python%20Data%20Structures%20Cheat-sheet.jpg)



#--------------- Tuples -------------
# Create tuple
tuple5 = (1,3,4)       # Syntax
tuple5 = tuple(())   # Constructor - double round-brackets

# Accessing an element
tuple5[0]                 # Accessing 1st element 
tuple5[1]                 # Accessing 2nd element
tuple5[0:5]               # Slicing from 1st to 6th element
tuple5[-2:-6]             # Slicing from last 7th to 3rd element
tuple5[:4]                # Slicing all till 5th element

# Modifying and deleting elements and tuple

    #Tuples do not allow you to change or delete a particular element of a tuple

del tuple5                #Delete tuple

# Addition and multiplication of the tuples in Python

tuple1 = (315,22,315,111,111,233,2)
tuple2 = ('a','b','c',4)
tuple1 + tuple2

#  Changing Python tuple value by using list():
list = list(tuple)

#  Packing and Unpacking tuple:
tup=1,2,3                 #packing
print("The type of ",tup,"is:",type(tup))

a,b,c=tup                 #unpacking
print(a)
print(b)
print(c)


# Python Built-in Functions
        # Can use those functions

tuple5.index()            #finds the index of the element passed
tuple5.count()            #finds the number of times the value occurs in a list
tuple5.len()              #returns the length or number of elements in the list
        
        # Not Supported functions. Need to convert tuple into list
        
list.append('as')       #adds an element to the list at the end.
list.insert(2,'bs')     #inserts the value in the specified location => insert({index}, {value})
list.pop()              #deletes the last element or at the index    => pop() , pop({index})
list.remove('bs')       #removes the specified value                 => remove({value})
list.sort()             #arranges the elements of the list in ascending or descending order

