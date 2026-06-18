# type() function is used to find the data type of a given variable in python

a = 31
t = type(a)
print(t)

a = 31.23
t = type(a)
print(t)

a = "Anshu"
t = type(a)
print(t)

a = True
t = type(a)
print(t)

a = None
t = type(a)
print(t)

a = "31.3"
t = type(a) # can also change one type from to another
print(t)

a = "31.23"
b = float(a) # b = a but the type should be float
t = type(b)
print(t)

# str(31) , integer to string conversion
# int("32") , string to integer conversion
# float(32) , integer to float conversion and so on......