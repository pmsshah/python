dict = {}
dict['one'] = "This is one"
dict[2]     = "This is two"

tinydict = {'name': 'john','code':6734, 'dept': 'sales'}


print (dict['one'])       # Prints value for 'one' key
print (dict[2])           # Prints value for 2 key
print (tinydict)          # Prints complete dictionary
print (tinydict.keys())   # Prints all the keys
print (tinydict.values()) # Prints all the values

dict1 = {'Name': 'Zara', 'Age': 7, 'Name': 'Manni'}
print ("dict1['Name']: ", dict1['Name'])


import time;  # This is required to include time module.
ticks = time.time()
print ("Number of ticks since 12:00am, January 1, 1970:", ticks)

ItemDict = {}
newList=[]
newList.append(3)
newList.append("HomeItem1")
newList.append("HomeItem2")
newList.append("HomeItem3")
ItemDict["Home"]=newList

newList=[]
newList.append(4)
newList.append("WorkItem1")
newList.append("WorkItem2")
newList.append("WorkItem3")
newList.append("WorkItem4")
ItemDict["Work"]=newList

for key in ItemDict:
	print("\n:",key,":")
	myList=ItemDict[key]
	[print (i) for i in myList] # one line for loop

list = [1, 3, 5, 7, 9] 
for i in list: 
    print(i) 
print ("\n")
for i in range(len(list)): 
    print(list[i]) 
print ("\n")
while i < len(list): 
    print(list[i]) 
    i += 1
print ("\n")
[print(i) for i in list] 
print ("\n")
for i, val in enumerate(list): 
    print (i, ",",val) 