# Python Boolean Values
# Smaller than and Greater than
print(10 < 8)
print(56 < 85)
print(90 > 78)
# With date and with no data 
print(bool(0))
print(bool(0))
print(bool("deep"))

# Python Operators 
# Arithmatic operators
# + addition
a = 10
b = 20
c = a+b
print(c)

# - Substraction
d = 10
e = 20
f = d-e
print(f)

# * Multiplication
g = 10
h = 20
i = g*h
print(i)

# / Division
j = 10
k = 20
l = k/j
print(l)

# % Modules
m = 10
n = 20
o = n%m
print(o)

# ** Exponentiation
p = 10
q = 20
r = p**q
print(r)

# // Floor Division
s = 10.0
t = 20
u = t//s
print(u)

# Assignment operators 

#  = operator 
number1 = 10
print(number1)
# this is how the = operator is used as assignment operator.

# += operator
# normal way 
number2 = 20
number2 = number2 + 10
print(number2)
# using operator 
number2 += 10 #this will be consider as number2 = number2 + 10 if we use this assignment operator.
print(number2)

# -= operator
number3 = 10
number3 -= 5
print(number3)

# *= operator
number4 = 10
number4 *= 10
print(number4)

# /= operator 
number5 = 10
number5 /= 5
print(number5)

# %= operator 
number6 = 10
number6 %= 5
print(number6)

# **= operator
number7 = 10
number7 **= 5
print(number7)

# //= operator 
number8 = 10
number8 //= 5
print(number8)

# logical operators 
# not operator 
# it revereses the result or the op
# it means that if the result should be false than it'll display true and if false than will return true.
number9 = 5
print(not(number9 > 3 & number9 < 10))
# it'll return false instead of true, this is how it reverses the results.
print('*' * 20)

# Identity operators
# 'is' operator 
# basically it checks the object variable whether they are same or not  
identity1 = ['orange','apple']
identity2 = ['orange','apple']
identity3 = identity1

print(identity1 is identity2)
print(identity2 is identity3)
print(identity3 is identity1)

print('*' * 20)

# 'is not' operator 
identity4 = ['green','blue']
identity5 = ['grey','blue']
identity6 = identity4
print(identity4 is not identity5)
print(identity5 is not identity6 )
print(identity6 is not identity4)
# this too will consider object in the code and not the value 
# so it is said to be the logical operators

print('*' * 20)

# membership operators 
# 'in' operators 
member1 = ['blue','grey']
member2 = ['blue','grey'] 
member3 = member1
print(member1 in member2)
print(member2 in member3)
print(member3 in member1)
# this is not how the method is used 
# the method is used in a different way.
# will show you the right way for this method 
member4 = ['blue','grey']
print('blue' in member4)
# here this operator will check whether the value is in the object or not.

print('*' * 20)

# 'not in' operator 
member5 = ['blue','grey']
print('red' not in member5)

# exp 1
# Operator Precedence
# Operator precedence describes the order in which operations are performed.
# Parentheses has the highest precedence, meaning that expressions inside parentheses must be evaluated first
print((6 + 3) - (6 + 3))

# exp 2 
# Multiplication * has higher precedence than addition +, and therefor multiplications are evaluated before additions:
print(100 + 5 * 3)


