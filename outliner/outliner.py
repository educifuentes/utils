import pyperclip

# saves text copied to clipboard
text = pyperclip.paste()
# print("Before Modification:")
# print(text)

# stores different lines of text
# in a list named lines
lines = text.split("\n")

# adds - to every line stored
for i in range(len(lines)):
    lines[i] = "- " + lines[i].strip().replace(". ", " - ")

# converts the list of different
# lines to single text
text = "\n".join(lines)

# copies new modified text
# to the clipboard
pyperclip.copy(text)
print("\nAfter Modification:")
print(pyperclip.paste())
