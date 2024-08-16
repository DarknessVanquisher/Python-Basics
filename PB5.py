# list syntax [normally displaying the list]
list1 = ['deep','raj','ujjval','dev', 'helee', 'rani','snehal']
print(list1)

# allow duplicates 
list2 = ['deep','deep','ujjval','ujjval', 'helee', 'helee','snehal','snehal']
print(list2) #List also allows duplicate values 

# list length
list3 = ['deep','deep','ujjval','ujjval', 'helee', 'helee','snehal','snehal']
print(len(list3))

# list items - data types 
list4 = ['deep',25,True ]
print(list4) #it allows all the date types 

# list items - type()
list5 = ['deep',25,True ]
print(type(list5))

# list constructor 
list6 = list(("deep",25,True))
print(list6)

# list items
# access list items  - 
# index [can acces using index]
list7 = ['Deep','Raj','Rahul','Rohan','Milan','Mitsu','Palak']
print(list7[3])
print(list7[-1])
print(list7[0:4])
print(list7[-3])
print(list7[0:])
print(list7[:-2])
print('Rahul' in list7)

# changeable
# change item value 
list8 = ['apple','orange','banana','guava','straw berry','crem berry']
list8[1] = 'lemon'
list8[0:3] = 'red','grey'
print(list8)
# this is how we can replace the value of the current value.
list9 = ['deep','deepa','janvi']
list9[1:2] = 'zeel','drashti'
# if the data is in limited amount than it will be displayed like this 
print(list9)

# ordered
   




