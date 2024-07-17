# Python Strings....

# quotes inside quotes
print ("Hello there ! this is 'deepu' here.") # Single quotes
print ('Hello there ! this is "deepu" here.') # Double quotes

#  Assign string to a variable 
a = "Deepu"
b = "Hi there this is > " + a + " < here"
print(b)

# Multi line strings 
c = """
Hi there this is deepu here
Hi there this is deepu here
Hi there this is deepu here
""" # using double quotes
'''
Hi there this is deepu here
Hi there this is deepu here
Hi there this is deepu here
''' # using single quotes

# Strings are arrays 
d = "Hello There This is 'Deepu' Here !"
print(d[5])
# remember most important thing that is >> index also considers the whitespaces between the sentences.

# looping through a string 
for e in "JAY SIYA RAM":
    print(e)
# in "for in" characters are displayed in rows and it also considers the space.

# Determine the length of the string 
f = "Hello There This is 'Deepu' Here!"
print(len(f))
# note string len() functions even counts the whitespace between the sentences.

# Check  string 

g = """
Paragraphs are the building blocks of papers. Many students define paragraphs in terms of length: a paragraph is a group of at least five sentences, a paragraph is half a page long, etc. In reality, though, the unity and coherence of ideas among sentences is what constitutes a paragraph
"""
# note - press Alt + Z for word wrap in vs code.
print("constitutes" in g)
# Note - If "Constitutes" word's 1st character is written in capital still it would display false.
# Note - if want to check any word so for that we have to right in the same way as we written in the paragraph.
# Note - same we can test in case of "if the searched name is not found in the para" >> it would display "false".

# Following are the methods of the string >> 

# 1 Slicing method >>
h = "Hello there ! this is deepu here."
print(h[2:12])
# note - here it would skip the 12th character and will display only till the 11th character of the sentence.
# it also considers the whitespace in counting range.
print(h[1:-1]) 
print(h[4:-5])
print(h[:-1])
print(h[:5])
print(h[1:])
print(h[-6:-1])
# slicing method can return the range of the characters by using the slice syntax where start and end index are mentioned.

# 2 Modify method >>
# a. Upper Case [upper()]
# b. Lower Case [lower()]
# c. Remove White spaces [strip()]
# d. Replace string [replace()]
# e. Split String [split()]

# a. Upper Case - 
i = "deepu panchal"
print(i.upper())
# converts the sentence into the uppercase.

# b. Lower Case - 
j = "DEEPU PANCHAL"
print(i.lower())
# converts the sentence into the lower case.

# c. Remove White Spaces - 
k = "     Hello There!     " # whitespace on both the ends.
print(k.strip() + "< with using the strip() method") 
print(k + "< without using the strip() method")
# Note - this method removes the whitespaces from the outerside of the sentence like on both the ends >> as mentioned in the example above.

# d. Replace String - 
l = "Hi there ! this is Deepu Here !"
print(l.replace("!", ';')) #Replaced a special character of the sentence.
print(l.replace("Hi","bye")) # Replaced a word of the sentence.
print(l.replace("Deepu", "Prachi")) #Replaced the name of the candidate.
print(l.replace(" ", "")) #Removed the whitespaces
# To replace something in the string this method is used for the same.

# e. Split String - 

m = "Hello.There.this.is.deepu.here !"
print(m.split("."))
# Note - Split is all about spliting the word from the sentence.

# 3 Concatenation - 
o = "   Deepu         "
p = " here !      "
q = o.strip()
r = p.strip()
print(q + r)

s = "hello"
t = "world"
print(s+t)
u = s + " " + t # this is how i have added the space.
print(u)
# Basically this method is used for adding 2 different strings and displaying them as one sentence as the output...

# 4 Format Strings
Name = "Deepu"
Age = 25

print("Hi There ! This is " + Name + " here and i am ", Age ,  "Years old") 
txt = f"Hi There ! This is  {Name}  here and i am {Age} Years old" # Example of the format strings. 
txt1 = f"Hi There ! This is  {Name}  here and i am {Age:.2f} Years old" # Using modifier in placeholder
txt3 = f"hi there the price {50 * 50}" # Calculation in the placeholder itself.
print(txt)
print(txt1)
print(txt3)

