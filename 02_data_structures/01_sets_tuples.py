# 01_sets_tuples.py

# Tuple: Immutable(can't be changed)
user_roles:tuple[str,str,str] = ("admin","editor","viewer")
print(f"Roles (Tuple) :{user_roles}")


# Set: Uniques items only (it's remove Duplicate Values)
active_users:set[str] = {"ankur","anand","ankur","rohan"}
print(f"Unqiue Active Users (Set): {active_users}")

# Set uses in Membership testing 
if "ankur" in active_users:
    print("Ankur is in the set!")