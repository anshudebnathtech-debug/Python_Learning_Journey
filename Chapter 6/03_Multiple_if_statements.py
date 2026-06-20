b = int(input("Enter the age"))

if(b%2==0):   # if statement no.1
    print("It is even")

if(b>18):  # if statement no.2
    print("You are an Adult") 
    print("Good for you")    # If if condition s matched , it will ignore 
    # the other conditions remember only one condition will be met and 
    # generated and all other will be ignored , it will look for the 
    # condition around every condition and once found it will ignore the 
    # other conditions

# if(b%6==0):   # if statement no.3
#     print("Divisible by 6")

elif(b<0):
    print("You are entering an invalid negative age, go check on your maths Teacher")

elif(b==0):
    print("You are entering 0 wtf bruhh!!")

else:
    print("Not an Adult")
    
print("End of program")


# ***Suppose multiple ifs are there, like # if statement no.1 ,2 ,3 so if 
# we run the code the first if gonna run individually as there is no elif
# or else present and then the 2nd no. if gonna run now if there is no 
# if no.3 it will be connected together with elif and else but if if no.3
# is present if no. 2 gonna run individually and if no.3 will be connected
# together with elif else

# Also if can be individual but elif else cant be individually runned 
# they need if at first , another if else and if elif else can be runned 
# together but if you run if elif it will show syntax error
