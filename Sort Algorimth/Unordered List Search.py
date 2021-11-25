# Unordered list search

# Declare an array of items
items = [24, 12, 21, 1, 53, 16, 88]

def find_item(item, itemList):
    for i in range(0, len(itemList)):
        if item == itemList[i]:
            return i
    return None

print(find_item(21, items))
print(find_item(44, items))