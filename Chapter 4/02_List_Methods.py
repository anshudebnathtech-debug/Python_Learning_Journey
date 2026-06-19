name = ["Apple","Orange",5,3242.42,False,"Akash"]
print(name[0])

name.append("Anshu")
print(name)
name.extend(["Satoshi","Snorlax","pikachu"])
print(name)

l1 = [10,21,34,23,43,12,11]
l1.sort()
print(l1)

l1.reverse()
print(l1)

l1.insert(3, 2434353) # Insert 2434353 such that its index in the list is 3
print(l1)

l1.remove(21)
print(l1)

print(l1.pop(1))
print(l1)

l1.clear()
print(l1) 

l = [1, 2]; l.append(3); print(l)  # Adds an element to the end of the list | Output: l becomes [1, 2, 3]        
l = [1, 2]; l.extend([3, 4]); print(l)    # Adds all elements of an iterable to the end | Output: l becomes [1, 2, 3, 4] 
l = [1, 3]; l.insert(1, 2); print(l)    # Inserts an element at a specific index | Output: l becomes [1, 2, 3]   
l = [1, 2, 3]; l.remove(2); print(l)    # Removes the first occurrence of a specific value | Output: l becomes [1, 3]   
l = [1, 2, 3]; x = l.pop(1); print(f"Removed: {x}, List: {l}")      # Removes and returns the element at the specified index | Output: x is 2, l is [1, 3]
l = [1, 2, 3]; l.clear(); print(l)      # Removes all elements from the list entirely | Output: l becomes []   
l = [3, 1, 2]; l.sort(); print(l)      # Sorts the list in ascending order in-place | Output: l becomes [1, 2, 3]    
l = [1, 2, 3]; l.reverse(); print(l)     # Reverses the order of the list in-place | Output: l becomes [3, 2, 1]  
l = [1, 2, 2]; c = l.count(2); print(c)    # Returns the number of times a specified value appears | Output: c is 2
l = [10, 20]; i = l.index(20); print(i)    # Returns the index of the first occurrence of a value | Output: i is 1
l = [1, 2]; c = l.copy(); print(c)     # Returns a shallow copy of the list | Output: c is [1, 2]
a = [12,2323,232,13]
print(sum(1))   # built-in Function to sum no.s in list