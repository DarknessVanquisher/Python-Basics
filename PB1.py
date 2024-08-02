import sys
print(sys.version)

print('hello world !')

# this  an single line comment.
'''
With this sign we can give multi line comments in the python.
it is also said the multi line string which can be displayed by using the print function 
but has to be s1o
red in  the variable thats what it is.
'''
#  variables in python 

a = 2
b = "Deepu"
print ('hi there ! this is ' + b + ' here and my id number is' ,a )

c = 2
c = "Chamanprash"
print(c)

# type casting
d = float(1)
e = float(2)
f = float(3)
print (d , e ,f)

# get the type of the variable.
g = "deepu"
h = 0.45
i = 1
print(g)
print(type(g))
print(h)
print(type(h))
print(i)
print(type(i))

# single qoute and double quotes...

j = "deepu"
j = 'Rihya'
print(j)

# case sensitive variables
k = "Deepu"
K = "Rihya"
print(K + ' weds ' + k)

# legal ways of declaring variables in python 

myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

# illegal variable names
# has tyo comment variable names as those were illegal and throwing the  error.
# 2myvar = "John"
# my-var = "John"
# my var = "John"

'''
Camel Case
Each word, except the first, starts with a capital letter:
myVariableName = "John"

Pascal Case
Each word starts with a capital letter:
MyVariableName = "John"

Snake Case
Each word is separated by an underscore character:
my_variable_name = "John"
'''
# many values to multiple variables can be assigned.
l,m,n = "orange","red","blue"
print (l,m,n)

# single value  to multiple variables can be assigned.
o=p=q = 'red'
print (o,p,q)
# store the values in the separate variables
# it is said  [unpack a list]
fruits = ["orange","apple","banana"]
r,s,t = fruits
print(r)
print(s)
print(t)

# python output variables

u = 5
v = 10
print(u + v)

# 1 python global  keywords
w = "awesome"

def myfunc():
  print("Python is " + w)

myfunc()

# 2
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)

# 3 the global keyword
def myfunc():
  global y
  y = "fantastic"

myfunc()

print("Python is " + y)

# 4 the global keyword
z = "awesome"

def myfunc():
  global z
  z = "fantastic"

myfunc()

print("Python is " + z)
  