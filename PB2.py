'''
Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:	NoneType

''' 
# complex data type 
a = 6j 
print(a)
print(type(a))
# basically used  when the humans can only imagine to  count but is quit a bit difficult (kind of  imaginary number) example - no. of times the spinner has been rotated.

# list, tuple, range

# list
shopping_list = ["milk", "bread", "eggs", "eggs"]
shopping_list.append("bananas")  # Add an item
print(shopping_list)  # Output: ['milk', 'bread', 'eggs', 'bananas']
# lists are modifyable ex - it can be used for  creating add to cart from backend 

# tuple
recipe_ingredients = ("flour", "sugar","sugar", 2)  # 2 eggs
# recipe_ingredients[0] = "wheat flour"  # This would cause an error (immutable)
print(recipe_ingredients)  # Output: ('flour', 'sugar', 2)
# tuples are fixed and are not modifyable as well as ex - it can be  used for setting product name, colour which are goin to be  reamined as fixed.

for i in range(1, 11):  # Count from 1 to 10
    print(i)
# ex - if want to count numbers from 1` to 100 than range is usefull
 # Generate numbers in descending order
     
# dict 
# Using curly braces
phonebook = {"Alice": "123-4567", "Bob": "890-1234"}

# Using dict() function
user_info = dict(name="Charlie", age=30)
print(phonebook["Alice"], phonebook["Bob"])  # Output: 123-4567
# basically dict differs to the dictionary and the values are in key:value format which are defined in the dict data type.

# Sets
cars = ["mercedes", "bmw", "range rover", "range rover", "Audi"]
unique_cars = set(cars)
print(unique_cars)

# Frozen Sets
fruits = ["apple", "banana", "orange", "apple", "papaya"]  # Duplicate "apple"
freezed_fruits = frozenset(fruits)  # Create a set to remove duplicates
print(freezed_fruits) 

# only the difference between set and frozenset is that in set the elements can be added, removed & discord
# and the same thing is not possible in the frozenset bcoz it'll display the "attribute error"

# Binary Types - 

# Byte
k = b'hello' 
print(k)
# byte is not modifiable

# byte array - 
ab = bytearray(10)
print(ab)
# byte array is modifiable

# memoryview - 
memory_view = memoryview(k)    



