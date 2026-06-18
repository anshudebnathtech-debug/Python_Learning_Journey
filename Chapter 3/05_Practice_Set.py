#Q1. Write a python program to display a user entered name followed by Good Afternoon using input() function.

name = input("Enter Your name:")
print(f"Good Afternoon! {name}")

# Q2. Write a program to fill in a letter template given below with name and date.
# letter = '''
# Dear <|Name|>,
# You are selected!
# <|Date|>
# '''

letter = '''
wDear <|Name|>,
You are selected!
<|Date|>
'''
 
print(letter.replace("<|Name|>","Anshu").replace("<|Date|>","17th June 2026"))

#3. Write a program to detect double space in a string. Replace the double space from problem 3 with single spaces.

name = "Anshu is a  good boy  "
name = "Anshu is a  good boy  "
print(name.find("  "))

print(name.replace("  "," "))
# *** Strings are immutable which means that you cannot change them by running functions on them
# Here when we print name it just made a new string and just print that new one but didnt change the original one, so this proves strings are immutable

#4. Write a program to format the following letter using escape sequence characters.
#   letter = "Dear Harry, this python course is nice. Thanks!"

letter = "Dear Harry,\n\tThis python course is nice.\n\tThanks!"
print(letter)