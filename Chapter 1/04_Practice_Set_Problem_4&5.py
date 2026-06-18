# # Q. Write a python program to print the contents of a directory using the os module. Search
# online for the function which does that.

import os

# Ask the user to enter the folder path
folder_path = input("Enter the folder path to list: ")

try:
    print(f"\n--- Contents of '{folder_path}' ---")
    for item in os.listdir(folder_path):
        print(item)
except FileNotFoundError:
    print("Oops! That folder doesn't seem to exist. Check the spelling.")
except NotADirectoryError:
    print("That's a file, not a folder!")
    
    # Give example like: C:\Users\ramad\Videos\Movies and it will generate
    
    
# Q5. Label the program written in problem 4 with comments.
#Ans: Already commented using #