#Print a list
## IMPORTANT : Refer below link on Data structures and List operations
# Reference : https://docs.python.org/3/tutorial/datastructures.html

fruits = ["Apple", "Chery", "Pear"]

print(fruits)
print(fruits[2])

fruits[1] = "Cherry"
print(fruits)

#Append Orange
fruits.append("Orange")
print(fruits)

#Extend with new items
fruits.extend(["Mango", "Kiwi"])
print(fruits)

#Count - Return the number of times x appears in the list. 
print(fruits.count("Mango"))

print(len(fruits))

#Add two lists of fruits and Veg

fruits = ["Strawberries","Grapes","Apple"]
vegetables =["Spinach", "Kale", "Tomatoes"]

dirty_dozen = [fruits, vegetables]

print(dirty_dozen)


