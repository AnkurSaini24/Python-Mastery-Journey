# 02_comprehensions.py


# list comprehension:  find the square of the number from 0 to 9 
squares = [x**2 for x in range(10)] 
print(f"Squares List: {squares}") 

# Dictionary Comprehension
square_dict = {x: x**2 for x in range(10)}
print(f"Squares Dictionary :{square_dict}")

# MERN-style data
users = [
    {"id": 1, "name": "Ankur", "age": 28},
    {"id": 2, "name": "Rohan", "age": 22},
    {"id": 3, "name": "Amit", "age": 30}
]

# use Dictionary Comprehension  for filtering and mapping
filtered_users = {user["id"]:user["name"] for user in users if user["age"] > 25 }

print(f"Filtered Users: {filtered_users}")

















