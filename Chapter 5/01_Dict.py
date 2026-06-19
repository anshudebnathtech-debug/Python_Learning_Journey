# Dictionary is a collection of keys-value pairs.

dict = {} # Empty dictionaries
print(dict)

marks = {
    "Harry": 100,
    "Subham": 56,
    "Rohan": 23,
    0 : "Norway"
}

print(marks,type(marks))
# print(marks[0]) , will show error since cant be done with indexing but you can do with Key values like: "Harry"
print(marks["Harry"])

# Properties Of Python Dictionaries
# It is unordered.
# It is mutable.
# It is indexed.
# Cannot contain duplicate keys.
