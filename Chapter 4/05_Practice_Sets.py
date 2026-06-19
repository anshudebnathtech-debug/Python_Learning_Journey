#Q1. Write a program to store seven fruits in a list entered by the user.

Fruits = []
f1 = input("Enter fruit name:")
Fruits.append(f1)
f2 = input("Enter fruit name:")
Fruits.append(f2)
f3 = input("Enter fruit name:")
Fruits.append(f3)
f4 = input("Enter fruit name:")
Fruits.append(f4)
f5 = input("Enter fruit name:")
Fruits.append(f5)
f6 = input("Enter fruit name:")
Fruits.append(f6)
f7 = input("Enter fruit name:")
Fruits.append(f7)

print(Fruits)

#Q2. Write a program to accept marks of 6 students and display them in a sorted manner.

Marks = []
f1 = int(input("Enter Marks score:"))
Marks.append(f1)
f2 = int(input("Enter Marks score:"))
Marks.append(f2)
f3 = int(input("Enter Marks score:"))
Marks.append(f3)
f4 = int(input("Enter Marks score:"))
Marks.append(f4)
f5 = int(input("Enter Marks score:"))
Marks.append(f5)
f6 = int(input("Enter Marks score:"))
Marks.append(f6)
f7 = int(input("Enter Marks score:"))
Marks.append(f7)

Marks.sort()
print(Marks)

#Q3. Check that a tuple type cannot be changed in python.

a = ("Anshu",23,False,"Akash")
a[0] = "Larry"   # Will generate error since it can't be done we cant change the tuple type

#4. Write a program to sum a list with 4 numbers.

a = [12,2323,232,13]
print(sum(1))

#5. Write a program to count the number of zeros in the following tuple:
# a = (7, 0, 8, 0, 0, 9)

a = (7, 0, 8, 0, 0, 9)
print(a.count(0))


