# Day 2 Practice - Python Basics (Continued)

# Question 1: If-else statement
x = 10
y = 20
if x > y:
    print("x is greater")
else:
    print("y is greater")  # Output: y is greater

# Question 2: Loops (for and while)
# Using a for loop to print numbers 1 to 5
for i in range(1, 6):
    print(i)

# Using a while loop to print numbers 1 to 5
i = 1
while i <= 5:
    print(i)
    i += 1

# Question 3: List operations
numbers = [1, 2, 3, 4, 5]
numbers.append(6)
print(numbers)  # Output: [1, 2, 3, 4, 5, 6]

# Question 4: Dictionary example
person = {"name": "John", "age": 30}
print(person["name"])  # Output: John

# Question 5: Function to add two numbers
def add(a, b):
    return a + b

print(add(5, 3))  # Output: 8

# Question 6: Handling exceptions
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")  # Output: Cannot divide by zero
