from collections import defaultdict,Counter

# 1. defaultdict: helpful in grouuping data 
data = [('fruit','apple'),('veg','carrot'),('fruit','banana')]
grouped_data = defaultdict(list)

for category,item in data:
     grouped_data[category].append(item)

print(f"Grouped Data:{dict(grouped_data)}")


# 2. Counter: use for data counting
items = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
counts = Counter(items)
print(f"Item Counts: {counts}")











