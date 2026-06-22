# 04_dictionaries.py

# Dictionary में Key-Value pairs होते हैं (JSON की तरह)
user_profile:dict[str,any] = {
     "name":"Ankur",
     "experience_years":10,
     "role":"Senior Mern Developer",
     "is_active":True
}

# डेटा एक्सेस करना
print(f"Developer: {user_profile['name']}")
print(f"Experience:{user_profile['experience_years']} years")

# नया डेटा अपडेट करना
user_profile['location'] = "Uttarakhand"

# लूप के ज़रिए डिक्शनरी को एक्सेस करना
print("\n--- Profile details ---")
for key,value in user_profile.items():
    print(f"{key.capitalize()}: {value}")