# Binary Search (Ordered List Search)

item = [24, 12, 21, 1, 53, 16, 88]
items = [12, 22, 24, 44, 66, 88, 111]

# Binary Search function
def BinarySearch(item, itemList):
    # Get the List size
    listsize = len(itemList) - 1

    # Start at the two end of the list
    lowerIdx = 0
    upperIdx = listsize

    while lowerIdx < upperIdx:
        # Caluclate midpoint
        midPoint = (lowerIdx + upperIdx) // 2

        # If midpoint is equak to the searching target, return the index
        if itemList[midPoint] == item:
            return midPoint
        
        # Otherwise move the lower index above the midpoint if the searching value is greater
        # than the midpoint value
        if item > itemList[midPoint]:
            lowerIdx = midPoint + 1
        # Or move the upper index below the midpoint of the item is lower than midpoint value
        else:
            upperIdx = midPoint - 1

    if lowerIdx > upperIdx:
        return None

print(BinarySearch(24, items))
print(BinarySearch(2, items))
