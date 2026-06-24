from collections import defaultdict,Counter

# 1. defaultdict: डेटा को ग्रुप करने के लिए बहुत यूज़फुल
data = [('fruit','apple'),('veg','carrot'),('fruit','banana')]
grouped_data = defaultdict(list)

for category,item in data:
     grouped_data[category].append(item)

print(f"Grouped Data:{dict(grouped_data)}")


# 2. Counter: डेटा काउंटिंग के लिए
items = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
counts = Counter(items)
print(f"Item Counts: {counts}")











