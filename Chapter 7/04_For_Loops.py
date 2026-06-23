# For Loop: A for loop is used to iterate through a sequence like list, tuple, or string [iterables]

for i in range(4):
    print(i)
    
# Range Function In Python
# The range() function in python is used to generate a sequence of number.
# We can also specify the start, stop and step-size as follows:
# range(start, stop, step_size)
# # step_size is usually not used with range()

i = 0
for i in range(0,100,4):
    print(i)   # Will print output from 0 to 100 with 4 as gap just like string slicing 
               # Ex : 0 1 2 3 4 5 6 7 8 9 => 0 4 8 12 ..... as output