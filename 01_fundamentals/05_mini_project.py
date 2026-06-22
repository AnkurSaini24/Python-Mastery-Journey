# 05_mini_project.py

# डेवलपर्स की लिस्ट (List of Dictionaries)
developers:list[dict] = [
    {"name": "Ankur", "exp": 10, "role": "Senior MERN"},
    {"name": "Anand", "exp": 7, "role": "React Native"},
    {"name": "Rohan", "exp": 2, "role": "Junior Frontend"}
]

print("--- Experience Developers (Exp > 5 years) ---")

# loop 
for dev in developers:
    if dev["exp"] > 5:
        print(f"Name: {dev['name']} | Role: {dev['role']} | Exp: {dev['exp']} years") 

































