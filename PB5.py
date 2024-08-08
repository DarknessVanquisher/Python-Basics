# Python Lists 
names = ['Deep','Rahul','Sagar','pradeep']
# ordered
names.append('Rahul') #addable but order remain the same new data will be added at the end.
# changeable 
names.insert(0,'Krishna') #data addable via index, [index number is alloted to each data in list.]
# even the  redundant[duplicate] data is also allowed by the list. 
print(names)
# op - ['Krishna','Deep','Rahul','Sagar','Pradeep','Rahul']

lastname = 'Panchal' 
lastnames = ['Panchal','Bhavsar','Sagar','Bharwad']
print(len(lastname)) # this will calculate the characters in the string.op - 7
print(len(lastnames)) # this will calculate the string inside this list.op - 4

# any value can be inserted in the list
list1 = [1,2,3,4,5]
list2 = ['deep','rahul','sagar','pradeep']
list3 = [True,False,True,False]
print(type(list1))
print(type(list2))
print(type(list3))

# data type specifier
listname = list(('deep','rahul','sagar')) #its also termed as 'list constructor defining'
print(listname)

# accessing list items 
print(list2[2])
print(list2[-1]) # -ve indexing
print(list1[0:4]) #it will exclude the 4th index will display [1,2,3,4]
print(list1[0:-1]) #it will exclude 4th index will display [1,2,3,4]
print(list1[0:]) #this for considering the complete elements in the list.
print(list1[:5])

if "deep" in list2 : 
       print("There is such an element in the list :-)")
else:
       print("There is no such element in the list :-(")

# change list items 
listname.append('raj') 
print(listname)
print('*' * 20)
listname.insert(0,'raj')
print(listname)
print('*' * 20)
# ^^ >> this will only be used for adding the elements in the list
listname[1] = 'rohan'
print(listname)
listname[1:4] = 'harshada','helee'
#^^there is a twist in this bcoz its even replacing the element as well as slicing the elements.
print(listname)
# using this we can replace the element in the list.


