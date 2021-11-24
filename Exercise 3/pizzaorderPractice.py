# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

if size == "S" :
  bill_amt = 15
elif size == "M" :
  bill_amt = 20
elif size == "L" :
  bill_amt = 25 

if add_pepperoni == "Y" : 
  if(size == "S") :
   bill_amt += 3
  elif(size =="M" or size == "L") : 
   bill_amt += 3

if extra_cheese == "Y" :
  bill_amt += 1

print(f"Your Final Bill Amount = ${bill_amt}")