# Following the articles on checkme.txt
# Let's focus on basic knowledge of Objects in Python (ref: https://pythongeeks.org/objects-in-python/)
# This cheatsheet would help (https://piazza.com/class_profile/get_resource/jde6vr6f8rk2b6/je4qxiv06m923z)



#--------------- Objects in Python -------------
# Create Class
class ClassName:      # Syntax
    #---- Some constructors ----
    #---- Some methods ----
    pass
    
    #Example    
class Dog:
   def __init__(self,name,age):
        self.name = name
        self.age = age

# Create Object 
object_name = ClassName(arguments)  

dog1        = Dog("Snoob", 3)


# Accessing Object attributes
object_name.attribute_name  #Syntax

dog1.age
dog1.name


# Unlimited Objects in Python
'''In Python, we can create as many objects as we want from a single class.'''
    # Setting a Limit in Python
class Dog:
    def __new__(cls, *args, **kwargs):
        #-----Still reading. Check document-----#
        pass


# Modifying an Object’s State in Python
    # Using the Python built-in functions
    
getattr()         # getattr({object},{attribute})         - access the attribute of an object using this function, returns the value of the given attribute  
hasattr()         # hasattr({object},{attribute})         - returns True if the passed attribute exists, otherwise False
setattr()         # setattr({object},{attribute},{value}) - modify or create a new attribute
delattr()         # delattr({object},{attribute})         - delete an attribute

# Delete Objects in Python

del dog1

# Object Aliasing in Python
'''In Python, we can give more than one name to an object. This is called Object Aliasing.'''

class Geeks:
    def __init__(self, name):
       self.name = name
website1 = Geeks("PythonGeeks")
website2 = website1             # Here.  Object Aliasing 


# Nested Loops
for i in list:
    for j in range():
        pass