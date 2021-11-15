# Following the articles on checkme.txt
# Let's focus on basic knowledge of Data Structures (ref: https://pythongeeks.org/python-data-structures/)
# This cheatsheet would help (https://storage.googleapis.com/kaggle-forum-message-attachments/923535/16292/Python%20Data%20Structures%20Cheat-sheet.jpg)



#--------------- Dictionaries -------------
# Create Dict
dict1 = {'key': 55,     # Syntax, Must have {key : value}
            1 : "ae"  
                    }       


# Accessing an element using keys
dict1['key']    #---> return 55               
dict1[1]        #---> return "ae"

# Changing and adding the value of Python Dictionary
    # We cannot change the keys but we can change the values using the keys
dict1 = {'a':7,'e':4,"y":6,"ab":10}
dict1['ab'] = 15

# Python Built-in Functions

dict1.get('a')          #get a value of the specified key. get({key})
dict1.pop('e')          #Takes a key as an argument, deletes that key-value, and returns the value.
dict1.popitem()         #Deletes the last key-value and returns the key-value pair as dictionary.
dict1.clear()           #Delete all the elements of a dictionary. It gives an empty dictionary
dict1.keys()            #Get all the keys in the dictionary
dict1.values()          #Get all the values in the dictionary
dict1.items()           #Get all the key-value pairs
