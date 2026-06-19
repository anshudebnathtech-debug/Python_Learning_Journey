# Properties Of Sets
# Sets are unordered => Elementʼs order doesnʼt matter
# Sets are unindexed => Cannot access elements by index
# There is no way to change items in sets.
# Sets cannot contain duplicate values.

# Set 17 built-in methods :

s = {1}; s.add(2); print(s)                                           # Adds a single element to the set | Output: {1, 2}
s = {1}; s.update([2, 3]); print(s)                                   # Adds multiple elements from an iterable | Output: {1, 2, 3}
s = {1, 2}; s.remove(2); print(s)                                     # Removes a specific element (raises KeyError if not found) | Output: {1}
s = {1, 2}; s.discard(3); print(s)                                    # Removes a specific element safely (does nothing if not found) | Output: {1, 2}
s = {'a', 'b'}; x = s.pop(); print(f"{x}, {s}")                       # Removes and returns an arbitrary element (sets are unordered) | Output: a, {'b'}
s = {1, 2}; s.clear(); print(s)                                       # Removes all elements from the set | Output: set()
s = {1, 2}; c = s.copy(); print(c)                                    # Returns a shallow copy of the set | Output: {1, 2}
s1 = {1, 2}; s2 = {2, 3}; u = s1.union(s2); print(u)                  # Returns a new set with all elements from both sets | Output: {1, 2, 3}
s1 = {1, 2}; s2 = {2, 3}; i = s1.intersection(s2); print(i)           # Returns a new set with only the common elements | Output: {2}
s1 = {1, 2}; s2 = {2, 3}; d = s1.difference(s2); print(d)             # Returns a new set with elements in s1 but not in s2 | Output: {1}
s1 = {1, 2}; s2 = {2, 3}; sd = s1.symmetric_difference(s2); print(sd) # Returns a new set with elements in either set, but NOT both | Output: {1, 3}
s1 = {1, 2}; s1.intersection_update({2, 3}); print(s1)                # Updates s1, keeping only elements found in both sets | Output: {2}
s1 = {1, 2}; s1.difference_update({2, 3}); print(s1)                  # Updates s1, removing elements found in the other set | Output: {1}
s1 = {1, 2}; s1.symmetric_difference_update({2, 3}); print(s1)        # Updates s1, keeping only elements found in one set but not both | Output: {1, 3}
s1 = {1}; s2 = {1, 2}; b = s1.issubset(s2); print(b)                  # Returns True if all elements of s1 are in s2 | Output: True
s1 = {1, 2}; s2 = {1}; b = s1.issuperset(s2); print(b)                # Returns True if s1 contains all elements of s2 | Output: True
s1 = {1}; s2 = {2}; b = s1.isdisjoint(s2); print(b)                   # Returns True if the sets have absolutely no common elements | Output: True

s = {1 , 2, 3, 7 , "Harry"}
print(len(s))