# Following the articles on checkme.txt
# Let's focus on basic knowledge of Data Structures (ref: https://pythongeeks.org/python-data-structures/)
# This cheatsheet would help ()

#--------------- Linked Lists -------------

# Advantages

'''
1) Dynamic size 
2) Ease of insertion/deletion

'''

# Drawbacks

'''
1) Random access is not allowed. We have to access elements sequentially starting from the first node. So we cannot do binary search with linked lists efficiently with its default implementation. Read about it here. 
2) Extra memory space for a pointer is required with each element of the list. 
3) Not cache friendly. Since array elements are contiguous locations, there is locality of reference which is not there in case of linked lists.
'''