# Determine whether the list is sorted or not
item1 = [1, 3, 5, 7, 8, 12, 124, 555]
item2 = [6, 7, 8, 3, 1, 1122, 12]

def is_list_sort(itemList):
    # Using brute force
    # for i in range(1,len(itemList)):
    #     if itemList[i - 1] > itemList[i]:
    #         return False
    # return True
    # More simplified solutions
    return all(itemList[i] <= itemList[i + 1] for i in range(0, len(itemList) - 1))

if not is_list_sort(item1):
    print("Item1 is not sorted")
else:
    print("Item1 is sorted")
if not is_list_sort(item2):
    print("Item2 is not sorted")
else:
    print("Item2 is sorted")
    