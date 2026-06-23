#Q1. Write a program to print multiplication table of a given number using for loop.

n = int(input("Enter the number: "))

for i in range(1,11):
    print(f"{n} X {i} = {n*i}")
    
# Q2. Write a program to greet all the person names stored in a list ‘lʼ and which starts with S.
# l = ["Harry", "Soham", "Sachin", "Rahul"]

l = ["Harry", "Soham", "Sachin", "Rahul"]

for i in l:
    if(i.startswith("S")):
        print(f"Hello {i}")
        
#Q3. Attempt problem 1 using while loop

n = int(input("Enter the number: "))

i = 1
while(i<11):
    print(f"{n} X {i} = {n*i}")
    i += 1
    
#Q4. Write a program to find whether a given number is prime or not.

n = int(input("Enter the number: "))

for i in range(2,n):
    if(n%i) == 0:
        print("No. is not prime")
        break
else:
    print("No. is prime")
    
#Q5. Write a program to find the sum of first n natural numbers using while loop.

n = int(input("Enter the number: "))

i = 1
sum = 0
while(i<=n):
    sum += i
    print(i)
    i +=1
    
print(sum)



#Q6. Write a program to calculate the factorial of a given number using for loop.

n = int(input("Enter the number: "))
product = 1

for i in range(1,n+1):
    product = product *i

print(f"The Factorial of {n} is: {product}")

#Q7. Write a program to print the following star pattern.
# *
# ***
# ***** for n = 3

n = int(input("Enter the number: "))

for i in range(1,n+1):
    print(" "*(n-1),end="")
    print("*"*(2*i-1),end="")
    print("")
    
# #Q8. Write a program to print the following star pattern:
# *
# **
# *** for n = 3

n = int(input("Enter the number: "))

for i in range(1,n+1):
    print("*"*(i),end="")
    print("")
    

#Q9. Write a program to print the following star pattern.
# * * *
# *   * for n = 3
# * * *

n = int(input("Enter the number: "))

for i in range(1,n+1):
    if(i==1 or i==n):
        print("*"* n,end="")
    else:
        print("*",end="")
        print(" "*(n-2),end="")
        print("*",end="")
    print("")

#Q10. Write a program to print multiplication table of n using for loops in reversed order.

n = int(input("Enter the number: "))

for i in range(1,11):
    print(f"{n}X{11-i} = {n*(11-i)}")    