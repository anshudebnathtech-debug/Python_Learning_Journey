# For Loop With Else: An optional else can be used with a for loop if the code is to be executed when the loops exhausts.

l = [1,"Anshu","rima",False]

for i in l:
    print(i)
    
else:
    print("All done")  # This is printed when for loop exhausts
# ---------------------------------------------------
    
# The Break Statement: ‘breakʼ is used to come out of the loop when encountered. It instructs the program to – exit the loop now

for i  in range(100):
    if(i==34):
        break  # Exit the loop right now
    
    print(i)
# ---------------------------------------------------

# The Continue Statement: ‘continueʼ is used to stop the current iteration of the loop and continue with the next one. It instructs the
# Program to “skip this iteration”.

for i  in range(100):
    if(i==34):
        continue  # Skip this iteration right now
    
    print(i)

# -----------------------------------------------------

# Pass Statement: pass is a null statement in python. It instructs to “do nothing”

for i  in range(100):
    pass # Suppose i want to dow hile fast and want to do for later so i want it to be skipped for now for that we can use "pass" that allows me to skip for loop and go directly to while to execute it

i = 0
while(i<100):
    print(i)
    i +=1
    
    print(i)

