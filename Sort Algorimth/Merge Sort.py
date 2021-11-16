# Merge Sort

items = [6, 20, 8, 19, 56, 23, 87, 41, 49, 53]

def mergeSort(dataset):
    # Break down the array by half as long as the array size is greater than 1
    if len(dataset) > 1:
        mid = len(dataset) // 2
        leftarr = dataset[:mid]
        rightarr = dataset[mid:]
        # Recursively break down the array
        mergeSort(leftarr)
        mergeSort(rightarr)
        # Merge the array
        i = 0 #Left arr index
        j = 0 #Right arr index
        k = 0 #Merged arr index
        
        # Add the sorted result into the array  
        while i < len(leftarr) and j < len(rightarr):
            if leftarr[i] < rightarr[j]:
                dataset[k] = leftarr[i]
                i += 1
            else:
                dataset[k] = rightarr[j]
                j += 1
            k += 1          

        # Add the leftover left array value   
        while i < len(leftarr):
            dataset[k] = leftarr[i]
            k += 1
            i += 1

        # Add the leftover left array value   
        while j < len(rightarr):
            dataset[k] = rightarr[j]
            k += 1
            j += 1


print(items)
mergeSort(items)
print(items)