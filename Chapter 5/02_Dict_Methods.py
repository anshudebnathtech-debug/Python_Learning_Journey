# Dictionary Methods :

marks = {
    "Harry": 100,
    "Subham": 56,
    "Rohan": 23,
    0 : "Norway"
}

print(marks.items())
print(marks.keys())
print(marks.values())
marks.update({"Harry":99, "Snorlax":100}), print(marks)
print(marks.get("Shivika")) # If the key not present will output none
print(marks.get("Harry")) # Will give Output

# ***Now one important question what is difference between marks.get("Harry") and marks["Harry"] as both gonna give me the same output 99
print(marks.get("Harry2")) # The difference is : If the key is not present marks.get("Harry2") will give none as output 
print(marks["Harry2"]) # While marks["Harry2"] will give error (***Msotly asked in interviewers)

d = {'a': 1}; d.clear(); print(d)                               # Removes all key-value pairs from the dictionary | Output: {}
d = {'a': 1}; c = d.copy(); print(c)                            # Returns a shallow copy of the dictionary | Output: {'a': 1}
k = ('x', 'y'); d = dict.fromkeys(k, 0); print(d)               # Creates a new dictionary with specified keys and a single value | Output: {'x': 0, 'y': 0}
d = {'a': 1}; v = d.get('a'); print(v)                          # Returns the value of a key safely (returns None if not found instead of an error) | Output: 1
d = {'a': 1}; i = d.items(); print(i)                           # Returns a view object containing tuples of all key-value pairs | Output: dict_items([('a', 1)])
d = {'a': 1}; k = d.keys(); print(k)                            # Returns a view object containing all the keys in the dictionary | Output: dict_keys(['a'])
d = {'a': 1}; v = d.values(); print(v)                          # Returns a view object containing all the values in the dictionary | Output: dict_values([1])
d = {'a': 1, 'b': 2}; v = d.pop('a'); print(f"{v}, {d}")        # Removes the specified key and returns its value | Output: 1, {'b': 2}
d = {'a': 1, 'b': 2}; kv = d.popitem(); print(f"{kv}, {d}")     # Removes and returns the last inserted key-value pair as a tuple | Output: ('b', 2), {'a': 1}
d = {'a': 1}; v = d.setdefault('b', 2); print(f"{v}, {d}")      # Returns the value if key exists; if not, inserts the key with a default value | Output: 2, {'a': 1, 'b': 2}
d = {'a': 1}; d.update({'b': 2, 'c': 3}); print(d)              # Updates the dictionary by adding/overwriting with new key-value pairs | Output: {'a': 1, 'b': 2, 'c': 3}

# (Note: In older versions of Python, dictionaries were unordered, so popitem() would remove a random item. But since Python 3.7, dictionaries remember the order items were added, so popitem() always removes the very last item you put in!)