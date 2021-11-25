# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
name=(name1+name2).lower()

T=name.count('t')
R=name.count('r')
U=name.count('u')
E=name.count('e')
L=name.count('l') 
O=name.count('o') 
V=name.count('v') 
E=name.count('e')    

lovescore=str(T+R+U+E) + str(L+O+V+E)

if int(lovescore) <10 or int(lovescore) >90 :
 print(f"Your score is {lovescore}, you go together like coke and mentos")
elif int(lovescore) >=40 and int(lovescore)<=50 :
  print(f"Your score is {lovescore}, you are alright together")
else :
  print(f"Your score is {lovescore}")

#Using FOR Loop 
# for i in name :
#   if i==T :
#    T+=1
#   elif i==R :
#     R+=1
#   elif i==U :
#     U+=1
#   elif i==E :
#     E+=1
#   elif i==L :
#     L+=1
#   elif i==O :
#     O+=1
#   elif i==V :
#     V+=1
#   elif i==E :
#     E+=1   
