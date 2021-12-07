# Review: 
# Create a function called greet(). 
# Write 3 print statements inside the function.
# Call the greet() function and run your code.


# Example : name = Tom 
# name : Paramter and Tom : Argument 

def greet(name, region):
  print(f"Hello {name}")
  print(f"How is weather at {region}")

friends_name = input("What`s your friends name ?")
region = input("Where he live ?")

greet(friends_name, region)