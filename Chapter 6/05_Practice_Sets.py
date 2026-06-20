#Q1. Write a program to find the greatest of four numbers entered by the user.

a1 = int(input("enter the no.1 "))
a2 = int(input("enter the no.2 "))
a3 = int(input("enter the no.3 "))
a4 = int(input("enter the no.4 "))

if(a1>a2 and a1>a3 and a1>a4):
    print("a1 is the greatest no",a1)
elif(a2>a1 and a2>a3 and a2>a4):
    print("a2 is the greatest no",a2)
elif(a3>a1 and a3>a2 and a3>a4):
    print("a3 is the greatest no",a3)
elif(a4>a1 and a4>a2 and a4>a2):
    print("a4 is the greatest no",a4)
    
# #Q2. Write a program to find out whether a student has passed or failed if it requires a total of
# 40% and at least 33% in each subject to pass. Assume 3 subjects and take marks as an
# input from the user.
    
marks1 = int(input("enter the marks 1: "))
marks2 = int(input("enter the marks 2: "))
marks3 = int(input("enter the marks 3: "))

total_percentage = (100*(marks1 + marks2 + marks3))/300 

if(total_percentage>=40 and marks1>=33 and marks2>=33 and marks3>=33):
    print("You are passed",total_percentage)
else:
    print("You failed!",total_percentage)
    
#Q3. A spam comment is defined as a text containing following keywords:
# “Make a lot of money”, “buy now”, “subscribe this”, “click this”. 
# Write a program to detect these spams.

p1 = "Make a lot of money"
p2 = "buy now"
p3 = "subscribe this"
p4 = "click this"

p = input("Enter your comment")

if(p1 in p or p2 in p or p3 in p or p4 in p):
    print("Your comment is fraud")
else:
    print("Your comment is not a fraud")
    
#Q4. Write a program to find whether a given username contains less than 10 characters or not.

username = input("Enter the username: ")

if(len(username)<10):
    print("Ypur username has less than 10 characters")
else:
    print("Everything is fine")
    
#Q5. Write a program which finds out whether a given name is present in a list or not

name = ["Anshu","Snorlax","Rima","Satoshi"]

n = input("enter your name: ")
if(n in name):
    print("Your name is on the list")
else:
    print("Your name not in the list")
    
# #Q6. Write a program to calculate the grade of a student from his marks from the following
# scheme:
# 90 – 100 => Ex
# 80 – 90 => A
# 70 – 80 => B
# 60 – 70 => C
# 50 – 60 => D
# <50 => F

marks = int(input("Enter your marks: "))

if(marks>=90):
    print("Your are EX")
if(marks>=80 and marks<90):
    print("Your are A")
if(marks>=70 and marks<80):
    print("Your are B")
if(marks>=60 and marks<70):
    print("Your are C")
if(marks>=50 and marks<60):
    print("Your are D")
if(marks<50):
    print("Your are F")
    
#7. Write a program to find out whether a given post is talking about “Harry” or not.

post = input("Enter the post: ")

if("Harry" in post):    # if("Harry".lower() in post.lower()): this covers all possible types of harry that can be written in upper lower middle letter upper or lower evrything covers it
    print("Post is talking about 'Harry'")
else:
    print("This post not talking about 'Harry'")