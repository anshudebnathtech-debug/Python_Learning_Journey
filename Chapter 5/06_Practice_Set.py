#Q1. Write a program to create a dictionary of Hindi words with values as their English
# translation. Provide user with an option to look it up!   

a = {"Madad": "Help",
     "Jao Yaha se": "Go Away",
     "Kha Jah rhe ho": "Where are you going"}

b = input("Enter Your WOrd you need the meaning for:")
print(a[b])

#Q2. Write a program to input eight numbers from the user and display all the unique numbers(once).

s = set()

n = input("Enter the no.")
s.add(n)
n = input("Enter the no.")
s.add(n)
n = input("Enter the no.")
s.add(n)
n = input("Enter the no.")
s.add(n)
n = input("Enter the no.")
s.add(n)
n = input("Enter the no.")
s.add(n)
n = input("Enter the no.")
s.add(n)
n = input("Enter the no.")
s.add(n)

print(s)

#Q3. Can we have a set with 18 (int) and '18' (str) as a value in it?

s = set()
s.add(18)
s.add("18")
print(s)

# #Q4. What will be the length of following set s:
# s = set()
# s.add(20)
# s.add(20.0)
# s.add('20') # length of s after these operations?

s = set()
s.add(20)
s.add(20.0)
s.add('20') 

len(s)



# #Q4. What will be the length of following set s:
# s = set()
# s.add(20)
# s.add(20.0)
# s.add('20') # length of s after these operations?

s = set()
s.add(20)
s.add(20.0)
s.add('20') 

print(len(s)) # ***Output will be 2 instead of 3 because in Python 20 adn 20.0 are both same because of their equal numerical value, due to which python gives True and list gives output 2 since same no.s cant be done

#Q5. s = {}
# What is the type of 's'?

s = {} # is tuple since set(), i.e. empty set can be done only in set()
print(type(s))

#Q6. Create an empty dictionary. Allow 4 friends to enter their favorite language as value and
# use key as their names. Assume that the names are unique.

d = {}

name = input("Enter Your Name: ")
lang = input("Enter Your Fav Language: ")
d.update({name: lang})

name = input("Enter Your Name: ")
lang = input("Enter Your Fav Language: ")
d.update({name: lang})

name = input("Enter Your Name: ")
lang = input("Enter Your Fav Language: ")
d.update({name: lang})

name = input("Enter Your Name: ")
lang = input("Enter Your Fav Language: ")
d.update({name: lang}) 

print(d)

#Q7. If the names of 2 friends are same; what will happen to the program
# in problem 6? If languages of two friends are same; what will happen to the 
# program in problem 6?

g = {}

name = input("Enter Your Name: ")
lang = input("Enter Your Fav Language: ")
g.update({name: lang})

name = input("Enter Your Name: ")
lang = input("Enter Your Fav Language: ")
g.update({name: lang})
 
print(g)  
# If key is same it will just update the value of the new one like
# Anshu:Python , so after update Anshu:C++ , it will give Anshu:C++ only
# If the value is same in two keys then it will give the two keys with same
# value i.e. Anshu:Python and Rima:Python both keys will be given as output 
# with same value 

#Q9. Can you change the values inside a list which is contained in set S?
# f = {8, 7, 12, "Harry", [1,2]}

# Ans: You cant update or change the values of list inside set because set 
# always wants the data to be immutable and list is mutable due to which set 
# thinks its unsafe for its inside organization due to which it gives error 
# also it rely on hashing another reason 
