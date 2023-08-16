with open("Hello.txt", "r") as file:
    content = file.read(5)
print(content)

with open("Hello.txt", "r") as file:
    for line in file:
        print(line)

with open("Hello.txt", "r") as file:
    content = file.readlines()
print(content)

line_number = 3  # Specify the line number you want to read
with open("Hello.txt", "r") as file:
    lines = file.readlines()
    if line_number <= len(lines):
        line = lines[line_number - 1]
        print(line)
    else:
        print("Line number out of range.")

with open("test.txt", "w") as file:
    file.write("Hello World")

with open("test.txt", "w") as file:
    file.write("Hello World\n")
    file.write("Hello Python")

fruits = ["Mango", "DragonFruit", "Kiwi"]
with open("fruits.txt", "w") as file:
    for fruit in fruits:
        file.write(fruit + "\n")

import re

txt = "hello world"
pattern = r"he..o"
matches = re.findall(pattern, txt)
print(matches)

txt = "The rain in Spain"
if txt.startswith("The"):
    print("The string starts with 'The'")
else:
    print("The string does not start with 'The'")

txt = "The rain in Spain"
if txt.endswith("Spain"):
    print("The string ends with 'Spain'")
else:
    print("The string does not end with 'Spain'")

txt = "The rain in Spain"
if txt.startswith("The") and txt.endswith("Spain"):
    print("The string starts with 'The' and ends with 'Spain'")
else:
    print("The string does not meet the specified conditions")

import re

txt = "The rain in Spain"
pattern = r"[a-mA-M]"
matches = re.findall(pattern, txt)
print(matches)

txt = "The rain in Spain"
index = txt.index(" ")
print(f"The first whitespace character is at index {index}")

txt = "The rain in Spain"
new_txt = txt.replace(" ", "9")
print(new_txt)

import re

email = "example@example.com"
pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
if re.match(pattern, email):
    print("Valid email ID")
else:
    print("Invalid email ID")

