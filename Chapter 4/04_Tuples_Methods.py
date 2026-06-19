# Tuple Methods: Only two 
# a.count(1): a count (1) will return number of times 1 occurs in a.
# a.index(1) will return the index of first occurrence of 1 in a.

a = (1,2,2,3,2,3,4, False, 2342.2,"Rohan") # in bracket with commas " , " means tuple
print(type(a)) 

no = a.count(2)
print(no)

i = a.index(False) # once it finds it wont go for another same value False
print(i)

# Tuple Functions we can use to get info :
t = (1, 2, 3); l = len(t); print(l)        # Returns the total number of items in the tuple | Output: 3
t = (3, 1, 2); s = sorted(t); print(s)     # Evaluates the tuple and returns a new sorted LIST | Output: [1, 2, 3]
t = (1, 2, 3); m = max(t); print(m)        # Returns the highest value item | Output: 3
t = (1, 2, 3); s = sum(t); print(s)        # Adds all numeric values together | Output: 6
t1 = (1, 2); t2 = t1 + (3, 4); print(t2)   # Concatenation: Joins them to create a completely NEW tuple | Output: (1, 2, 3, 4)
t = (1, 2); t2 = t * 3; print(t2)          # Repetition: Repeats the tuple elements into a NEW tuple | Output: (1, 2, 1, 2, 1, 2)
t = (1, 2, 3); b = 2 in t; print(b)        # Membership: Checks if a value exists inside (Returns Boolean) | Output: True