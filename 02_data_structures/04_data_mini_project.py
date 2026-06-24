from collections import defaultdict, Counter

# Dummy Data
logs = [
    {"level": "INFO", "message": "User logged in"},
    {"level": "ERROR", "message": "Database connection failed"},
    {"level": "INFO", "message": "Page loaded"},
    {"level": "ERROR", "message": "Timeout error"},
    {"level": "ERROR", "message": "Database connection failed"},
    {"level": "WARNING", "message": "High memory usage"}
]

levels = [log["level"] for log in logs]
levels_count= Counter(levels)
print(f"--- (Log Level Summary) ---")
print(levels_count)


#using default Dict
error_messages = defaultdict(int)

for log in logs:
     if log["level"] == "ERROR" :
          error_messages[log["message"]] += 1
   

print(f"\n--- (Detailed Error Report) ---")
for error, count in error_messages.items():
    print(f"Error: '{error}' :: {count} ")    