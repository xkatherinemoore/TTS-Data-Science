# 1. Accept user's first/last name and reverse
# User input
firstname = input("Enter your first name:")
lastname = input("Enter your last name:")
# Slice string, starting at the end of the string and moving backwards
print(lastname[::-1], " ", firstname[::-1])
# Katherine Moore returns erooM enirehtaK

# 2. Accept input integer n and add n + nn + nnn
n = input("Enter a number:")
# Runs the loop if the user input was not a digit
while not(n.isdigit()):
    print("You did not enter a number.")
    n = input("Enter a number:")
# Converts user input strings to integers
n1 = int(n)
n2 = int(n + n)
n3 = int(n + n + n)
answer = n1 + n2 + n3
# input of 8 returns 984

# 3. Take user input of country and print statement
country = input("What country are you from?")
country = country.strip().lower().capitalize()
print("I've heard that ", country, " is a beautiful country!")

# 4. What is the output?
x = 10
y = 50
if (x ** 2 > 100 and y < 100): 
    print(x, y)
# x**2 = 100 so if statement returns false and no output printed

# 5. What is the output?
a = [10, 20]
b = a
b += [30, 40]   # Same as b = b + [30, 40]
print(a)    # prints [10, 20]
print(b)    # prints [10, 20, 30, 40]
# Prior to the addition assignment operator, b = [10, 20]. Addition with lists will combine them

# 6. What is the output?
print(2%6)
# Modulus is the same as remainder; 2/6 = 0r2
# Output is 2

# 7. What is the output?
print(2 * 3 ** 3 * 4)
# Multiplication and exponentation
# 3**3 = 27, 2 * 27 * 4 = 216
# Output is 216

# 8. What is a text editor
# Text editor is a program for reading and making changes to text files. Text editors operate in plaintext unlike Word Processors. Word Processors then have additional binary components encoded into the file (specify font style, font size, special characters, etc.)

# 9. What is Python?
# Python is a cross-platform programming language. It is popular because of its readability and versatility.

# 10. What is Jupyter Notebook?
# Jupyter Notebook is a web-based application for writing code with an integrated interpretor. This means that users can write and execute code in the same environment. It runs python code blocks individually (instead of running the entire program as a whole). Alternatives to Jupyter Notebook include Noteable, Google Colab, Kaggle Notebooks, and Apache Zeppelin. 