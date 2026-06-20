# 1. Can we run if and elif without else?
# Yes, absolutely! The else statement is completely optional in Python. You can have an if block followed by as many elif blocks as you want, and you are never forced to include an else at the end.

# If neither the if nor the elif conditions are met, Python simply skips the entire block and moves on to the next line of code.
# Here is an example you can run:
# Python

score = 85

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
    
# We didn't include an 'else'. Since 85 is >= 80, the elif runs!
# Output: Grade: B
# If the score was 50, this code would produce absolutely no output and 
# just finish running, because there is no catch-all else to handle it.

# 2. Can we run something like if, else, elif?
# No, this will cause a syntax error.
# In Python (and almost all programming languages), the order of conditional 
# statements is strictly enforced. The else block acts as the final 
# "catch-all" bucket. If you include it, it must be the very last thing in 
# the chain. You cannot check for another specific condition (elif) after 
# you have already declared the final catch-all (else).

# The WRONG way (Throws an error):


# x = 5

# if x == 1:
#     print("One")
# else:
#     print("Not one")
# elif x == 5:         # ERROR: SyntaxError: invalid syntax
#     print("Five")
# The CORRECT order:

x = 5

if x == 1:           # 1. Start with 'if'
    print("One")
elif x == 5:         # 2. Put all 'elif's in the middle
    print("Five")
else:                # 3. Always end with 'else' (if you need it)
    print("Not one or five")

# Output: Five