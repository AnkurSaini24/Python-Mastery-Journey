# 03_lists_and_loops.py

# List of integers with type hinting
marks_lists:list[int] = [20,45,80,30,95]

def check_result(marks:list) -> str:
    if marks >= 33:
       return "Pass"
    return "Fail" 

# Iterating through the list 
print("--- Result ---")
for mark in marks_lists:
    status:str = check_result(mark)
    print(f"Marks:{mark} ->Status: {status}")  