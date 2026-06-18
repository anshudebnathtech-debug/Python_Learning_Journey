# Escape Sequence Characters: Sequence of characters after backslash "\" are called Escape Sequence characters.
                            # These characters represent one special character inside strings.
                            
a = "Anshu is a good boy \n but not a good \tboy"
a = "Anshu is a good boy \n but not a good \"boy\""
a = "Anshu is a good boy \n but not a good 'boy'"
a = 'Anshu is a good boy \n but not a good "boy"'  # All are printable

print(a)

print("Hello\nWorld") # \n (New Line): Moves the cursor to the beginning of the next line.
print("Name:\tAlice") # \t (Horizontal Tab): Inserts a horizontal tab space.
print("C:\\Users\\Admin") # \\ (Backslash): Allows you to include a literal backslash without triggering another escape sequence.
print('It\'s a beautiful day.') # \' (Single Quote): Allows you to include a single quote inside a string enclosed by single quotes.
print("She said, \"Hello!\"") # \" (Double Quote): Allows you to include a double quote inside a string enclosed by double quotes.
print("12345\rABC") # \r (Carriage Return): Moves the cursor back to the start of the current line, overwriting existing characters.
print("Hello \bWorld") # \b (Backspace): Moves the cursor back one space and erases the character there.
print("Page 1\fPage 2") # \f (Form Feed): Historically forced a printer to the next page; in modern terminals, it usually forces a downward line break.
print("Item 1\vItem 2") # \v (Vertical Tab): Historically advanced to the next vertical tab stop; usually acts as a downward line break today.
print("Error!\a") # \a (ASCII Bell): Triggers the system alert sound (a "beep") in supported terminals.
print("\110\151") # \ooo (Octal Value): Represents a character using its 1-to-3 digit octal (base-8) value.
print("\x48\x69") # \xhh (Hexadecimal Value): Represents a character using exactly 2 hexadecimal (base-16) digits.
print("\N{WAVING HAND SIGN}") # \N{name} (Unicode Name): Prints a Unicode character by its official database name.
print("I \u2764 Python") # \uxxxx (16-bit Unicode): Prints a Unicode character using exactly 4 hexadecimal digits.
print("\U0001F600") # \Uxxxxxxxx (32-bit Unicode): Prints a Unicode character using exactly 8 hex digits (often used for emojis).









