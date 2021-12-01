# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()

print(student_heights)

for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

# 🚨 Don't change the code above 👆

#Write your code below this row 👇

# Without FOR LOOP

# avg_height= round(sum(student_heights)/len(student_heights))
# print(f"Average height = {avg_height}")

#With FOR LOOP

total_height=0
for height in student_heights:
  total_height += height

avg_height=round(total_height/len(student_heights))
print(f"Average height = {avg_height}")

