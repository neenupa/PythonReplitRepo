## Your Life in Weeks

# Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old. 
# It will take your current age as the input and output a message with our time left in this format:
# > You have x days, y weeks, and z months left. Where x, y and z are replaced with the actual calculated numbers. 
# Reference :[https://waitbutwhy.com/2014/05/life-weeks.html](https://waitbutwhy.com/2014/05/life-weeks.html)

# # Example Input : 56
# # Example Output : You have 12410 days, 1768 weeks, and 408 months left.
# # Hint : There are 365 days in a year, 52 weeks in a year and 12 months in a year.

# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

yearsleft = 90 - int(age)
monthsleft = yearsleft * 12
weeksleft = yearsleft * 52
daysleft = yearsleft * 365

print(f"You have {daysleft} days, {weeksleft} weeks, and {monthsleft} months left.")













