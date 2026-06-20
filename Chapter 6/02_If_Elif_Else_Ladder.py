# Elif in Python: If else and elif statements are a multiway decision 
# taken by our program due to certain conditions in our code.

b = int(input("Enter the age"))
if(b>18):
    print("You are an Adult") 
    print("Good for you")    # If if condition s matched , it will ignore 
    # the other conditions remember only one condition will be met and 
    # generated and all other will be ignored , it will look for the 
    # condition around every condition and once found it will ignore the 
    # other conditions

elif(b<0):
    print("You are entering an invalid negative age, go check on your maths Teacher")

elif(b==0):
    print("You are entering 0 wtf bruhh!!")

else:
    print("Not an Adult")
    
print("End of program")

# Relational Operators:
# Relational Operators are used to evaluate conditions inside the if statements. Some examples of relational
# operators are:
# ==: equals.
# > =: greater than/ equal to.
# < =: lesser than/ equal to.

# Logical Operators:
# In python logical operators operate on conditional statements. For Example:
# and – true if both operands are true else false.
# or – true if at least one operand is true or else false.
# not – inverts true to false & false to true.