#Adding Even Numbers in range of 1 to 100

#Write your code below this row 👇
total = 0
for i in range(1, 101):
  if i%2 == 0:
   total += i

print(f"Total = {total}")

total2 = 0
for i in range(2, 101, 2):
  total2 += i

print(total2)
 
