print("\n  ")
print(" ")

#Basic data structures in Python
#Invalid names to variables
#1age = 5 # cannot start with a number
#test-var = 10 # cannot contain hyphens
#current user = "John" # cannot contain spaces  

#Creating a list 
#stores ordered indexed, collections of itemos allowing duplicate values

#creating lists []
nums = [1,2,3]#Square brackets
multi_type = ["Hi",5,True] #Multi-typed
matrix = [1,2,3],[4,5,6] #Multidimensional

#accesing elements 
print(nums[0]) #prints first element
print(matrix [1][2]) #Prints 6
print(matrix [1][0]) #Prints 4

#modifiying Listis

nums [1] =20 # Assign new value
nums.append(30) #add value to end
nums.insert(1,25) #insert value at index
print(nums)

#tuples are inmutable 
point= (1,2) 
book = ("Python 101",2020, 4.5)

#trying to modify will give you error
point[0] = 2 #gives error
print(point)

#Dictionaries 
#store mapping of unique keys to values, similiar to map/has table Keysmust be inmmutabletypes

#create dictionaries
user = {"name":"john","id":1,"verified":True}
products= {} #empty dict

Acces & modify

print(user["name"]) # Get value of "name " key

user["id"] = 2
print(users)

#tuples
#those are inmutable list 

point = (1,2)
book = ("Python 101",2020,4.5)

#Trying to modify raise error
#point[0] = 2 #Gives error

#Dictionaries
#stores mapping of unique keys to values
user={'name':'John','id':1,'verified':True}
print(user)

# Accessing and modifying 
print(user['name'])#get value of "name" Key)

user["id"] = 2 #Update value of "id"
print (user)   #  prints {'name': 'John', 'id': 2, 'verified': True}




