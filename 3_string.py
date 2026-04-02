# String is a sequence of charatcers enclosed within quotes

str1 = 'Akshit'

# Letters , Numbers , Special symbol,whitespace characters
# Unicode characters

language = 'python'
print(language)
print(language[3])


print(1 + 2 + 3)
print("1 + 2 * 3")
print('1 + 2 * 3')

name1 = "Python"
name2 = "Python"

print(name1==name2)

# String can be stored in single quote or double quote
# Multiple string can be stored with ''' ....''' or """..."""

poem = '''sabko hai tension , par sab hasta dikhna zaroori hai,
gukuldham mein problems bhi scripted comedy hai
popatlal ka dard TRP ki majboori hai.'''

print(poem)

# C:\Users\prathmesh\Documents

directory = "C:\\Users\\prathmesh\\Documents"
print(directory)

# \ escape character

# String concatenation 
# + connects 2 Strings

a = "1"
b = "2"

print(a+b)

first_name = "shubham"
last_name = "Sharma"

print(first_name + " " + last_name)

# Convert int to stirng

age = 45
message = "My age is " + str(age)
print(message)


city = " new york"
temp = 75
weather_report = "The temperature in " + city + " is " + str(temp) +" degrees"
print(weather_report)

# f string

weather_report= f"The temparature in {city} is {temp} degrees"
print(weather_report)

a = 5
b = 10

print(f"The sum of {a} and {b} is {a + b}")

name = "Vipul"

print(f"First character of {name} is {name[0]}")

print(f"This is a curly brace : {{")

# when we multiply string to the integer it will repeat 
a = "python"
res = a * 3
print(res)

# Helpful to solve * patterns problems

star = "*"
print(5 * ((star * 5) + "\n"))

# Empty String

a = "python"
print(a*0)
print(a)
print(a * -1)

# PyPythonthon

print("py" * 2 + "thon" * 2)

# End of Print Function

# len function -  to calculate string lenght

a = "Python"
length = len(a)
print(length)

print(len(""))
print(len("@"))
print(len("Hello\nWorld"))

print(len("😊"))
print(len("😆"))
print("\u2764") # Unicode


msg="Help!"
res=len(msg)>=5
print(res)

# compare the string

print("apple" == "apple")
print("apple"=="Apple")
print("apple"!="Orange")
print(1<2)
print(11 > 2)
print(15<=8)
print(23>=9)

print("-------------clear---------------")
# Compare strings with operators
print("a" < "b")
print("apple" < "banana")
print("apple" > "Apple")
print("apple" < "Ape")

# String Indexing and Slicing

txt = "PYTHON"
# print(txt[len(txt)]) - this will give error txt[6]

# If you want to find location of n from python

print(txt[len(txt)-1]) # txt[5] = n

# Negative Indexing for python - to l0cate from last

print(txt[-3])

# Slicing - string[start:end:step]
# start - inclusive
# end exclusive

txt = "Python Programming"
print(txt[0:6]) # Last index is exclusive in python
print(txt[:6]) # if first index is not mentioned - then it will take it from start

print(txt[7:18])
print(txt[7:]) # if last index is not mentioned - then it will take it till end of string

# To print complete string
print(txt[:])

# to print pro

print(txt[7:10])

# Using negative

print(txt[-11:-8])

#string[start:end:step] - step = to skip the characters in between if it is 2 - then it will skip every second char
# to print pto
print(txt[:6:2])

# A negative step traverses the string in reverse direction

print(txt[::-2])

# Reverse a string
print(txt[::-1])

# String Methods 
# Methods are same like functions - but calling them is bit different


print(txt)  # function call

print(txt.upper())  # method call using .
print(txt.lower())

txt = "hello python programming"
print(txt.title())

new_txt=txt.title()
print(new_txt)

print(txt.capitalize())

# to trim the spaces from start and end

txt = "           hello python programming       "
print(txt)
print(txt.strip())
print(txt.lstrip())
print(txt.rstrip())

# to find something in string
# find syntax string.find(substring, strart, end)
txt = "Python is amazing, Python is fun"
idx = txt.find("Python")
print(idx)

print(txt.find("fun"))
# find syntax string.find(substring, strart, end)
# to find the index of is

print(txt.find("is"))
print(txt.find(",")) # , is at 17th place

print(txt.find("is",19)) #(substring, strart) - seareched from pth index

# count the occurances  - string.count(substring, strart, end)
print(txt.count("Python"))
print(txt.count("Python",19))

# to find the index - string.index(substring, strart, end)
# The .index() method is similar to .find() but raises a value error if not found


print(txt.find("java"))
#print(txt.index("java")) # throws the error

# replace method 
# string.replace(old, new, count)

txt="Hello world"
idx=txt.replace("Hello","tello")
print(idx)

txt= "banana banana banana"
idx=print(txt.replace("banana","apple",2))


# to check strings contains alphabets , digits , alphanumeric 
text1= "Python"
text2= "Python3"
print(text1.isalpha()) # True
print(text2.isalpha()) # false

# alphanumeric
print(text1.isalnum())
print(text2.isalnum())

text1= "2322"
text2= "2python" 

print(text1.isdigit())
print(text2.isdigit())


# islower(), isupper()

txt ="   "
print(txt.isspace())

# startswith endswith

text = "python is amazing"
print(text.startswith("python")) # True
print(text.startswith("is")) # False

print(text.endswith("amazing")) # True
print(text.endswith("python")) # False

print(text.endswith("is", 0, 9)) # False







