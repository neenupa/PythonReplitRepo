#Positional vs Keyword Arguments

def myFunction(a, b, c):
  print(f"a = {a}")
  print(f"b = {b}")
  print(f"c = {c}")

# myFunction(1,2,3)

myFunction(c=10,b=1,a=9)