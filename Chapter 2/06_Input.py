# Input() Function:
# This function allows the user to take input from the keyboard as a string

a = input("enter no. 1: ")
b = input("enter no. 2: ")
print("Number a is: ", a)
print("Number b is: ", b)
print("Sum of a and b:", a + b)  # Suppose a=1 b=2, then Sum = 12, since input takes value in string format, so values of a and b will concatinate

#Suppose i want to add instead of concatinate:
c = int(input("enter no. 1: "))
d = int(input("enter no. 2: "))
print("Number c is: ", c)
print("Number d is: ", d)
print("Sum of c and d:", c + d) # Here i changed the type with int before input