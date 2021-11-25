#Read and print your name:
print("Hello " + input("What`s your name : ") + " !")

# Write a program that prints the number of characters in a user's name.

print(len(input("What`s your name : ")))
# OR

strl= len(input("What`s your name : "))
print(strl)

#OR If you need the size of the string in bytes, you need sys.getsizeof():
import sys
print(sys.getsizeof(input("What`s your name ? ")))




