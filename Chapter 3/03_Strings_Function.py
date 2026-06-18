name = "anshu are siuuuu"
print(len(name)) # len will find the length of string that is 5
# print(name.endswith(rry)) , will show error if you give any other string then the given one
print(name.endswith("nshu"))
print(name.endswith("hu"))
print(name.endswith("Ans"))

print(name.startswith("Ans"))
print(name.capitalize()) # remember only First letter is gonna be capitalize and other will small ex- Anshu are siuuu, only a will be capital


# All String FUnctions From Gemini:
# Changing Methods:-
print("hello world".capitalize()) # capitalize(): Converts the first character to uppercase and the rest to lowercase.
print("HELLO WORLD".lower()) # lower(): Converts all characters to lowercase.
print("hello world".upper()) # upper(): Converts all characters to uppercase.
print("hello world".title()) # title(): Converts the first character of each word to uppercase.
print("HelLo WoRlD".swapcase()) # swapcase(): Swaps lowercase to uppercase and vice versa.
print("ΟΔΥΣΣΕΥΣ".casefold()) # casefold(): Converts to lowercase, but is more aggressive than lower() 
                                # (useful for caseless matching in different languages).


# Searching and Replacing:-
print("Moshi Moshi okasan".count("Moshi")) # count(substring): Returns the number of times a substring appears.
print("Moshi Moshi okasan".count("o")) # count(substring): Returns the number of times a substring appears.
print("Moshi Moshi okasan".find("okasan")) # find(substring): Returns the lowest index where the substring is found. Returns -1 if not found.
print("Moshi Moshi okasan".rfind("Moshi")) # rfind(substring): Returns the highest index where the substring is found 
                                           # (searches from the right). Returns -1 if not found.

print("Anshu is a good good boy".replace("good","bad")) # replace(old, new, [count]): Replaces occurrences of a substring with a new string.

# Splitting and Joining:-
print("Anshu loves coding".split("s",2)) #split(separator): Splits the string at the specified separator and returns a list.
print("Anshu, loves, coding".rsplit(",",1)) #split(separator): Splits the string at the specified separator and returns a list.
print("Anshu debnath".splitlines()) # splitlines(): Splits the string at line breaks and returns a list. if Anshu\ndebnath then 'Anshu' 'debnath'
print("+".join(['4','5','9'])) # join(iterable): Joins elements of an iterable (like a list) into a single string, using the string as a separator.
print("Anshu Debnath Tech is a ffefe Industry expert".partition("Tech")) # partition(separator): Splits the string at the first occurrence of the separator and returns a 3-tuple (before, separator, after). 
print("Anshu Debnath is a Tech Industry expert".rpartition("Tech")) # partition(separator): Splits the string at the first occurrence of the separator and returns a 3-tuple (before, separator, after).
 
# Stripping and Formatting:-
print("   000 helloH11 ##   ".strip()) # strip([chars]): Removes leading and trailing whitespace (or specified characters).
print(" 000 helloH11 #".lstrip("0")) # lstrip([chars]): Removes leading (left) whitespace or characters. doesnt apply if trailing and leading string has space
print("000 helloH11 ##".rstrip("#")) # rstrip([chars]): Removes trailing (right) whitespace or characters. doesnt apply if trailing and leading string has space


print("Anshu_Debnath123".removeprefix("Ans")) # removeprefix(prefix) (Python 3.9+): Removes a prefix if present.
print("Anshu_Debnath123".removesuffix("_Debnath123")) # removesuffix(suffix) (Python 3.9+): Removes a suffix if present.
print("Anshu".center(20,"-")) # center(width, [fillchar]): Centers the string within a specified width, padding with a character.
print("Anshu".ljust(20,"*")) # ljust(width, [fillchar]): Left-aligns the string within a specified width.
print("Anshu".rjust(20,"*")) # rjust(width, [fillchar]): Right-aligns the string within a specified width.
print("Anshu".zfill(8)) # zfill(width): Pads the string on the left with zeros to fill the specified width.
print("Anshu\tDebnath".expandtabs()) # expandtabs(tabsize): Replaces tab characters (\t) with spaces.  

# String Validation (Boolean Returns):-
print("ANshu1Deb".startswith("ANshu")) # startswith(prefix): Checks if the string starts with a specific prefix.
print("ANshu1Deb".endswith("Deb")) # endswith(suffix): Checks if the string ends with a specific suffix.
print("ANshu1Deb".isalnum()) # isalnum(): Checks if all characters are alphanumeric (letters and numbers).
print("AnshuDeb".isalpha()) # isalpha(): Checks if all characters are in the alphabet.
print("AnshuDeb".isascii()) # isascii(): Checks if all characters are ASCII characters.
print("1323122".isdecimal()) # isdecimal(): Checks if all characters are decimals (0-9).
print("13123".isdigit()) # isdigit(): Checks if all characters are digits (includes superscripts like ²).
print("131".isnumeric()) # isnumeric(): Checks if all characters are numeric (includes fractions like ½).
print("Char".isidentifier()) # isidentifier(): Checks if the string is a valid Python identifier/variable name.
print("harry".islower()) # islower(): Checks if all alphabetic characters are lowercase.
print("HARRY".isupper()) # isupper(): Checks if all alphabetic characters are uppercase, false if one letter of the string is small or lowercase
print("\t".isspace()) # isspace(): Checks if all characters are whitespace. like "\n", " " (space between quotation), "\t"
print("Anshu Debnath".istitle()) # istitle(): Checks if the string follows title case rules.
print("hello\nsweatheart".isprintable()) # isprintable(): Checks if all characters are printable (e.g., skips escape characters like \n).

# Advanced and Formatting Methods:-
print("My name is {} and I am {}".format("Anshu",25)) # format(*args, kwargs): Formats string values into placeholders {}.
print("") # format_map(mapping): Similar to format(), but takes a dictionary directly.
print("") # encode(encoding='utf-8'): Returns an encoded version of the string as a bytes object.
print("") # maketrans(x, y, z) & translate(table): maketrans creates a mapping table, and translate applies it to replace characters.

