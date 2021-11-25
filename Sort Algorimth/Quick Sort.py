# Declare items array

items = [12, 45, 10, 5, 54, 99, 7, 75]

def quickSort(dataset, first, last):
    if first < last:
        # Calculate the split point
        pivotIdx = partition(dataset, first, last)

        # Sort the two partition
        quickSort(dataset, first, pivotIdx - 1)
        quickSort(dataset, pivotIdx + 1, last)
def partition(datavalues, first, last):

    # Chose the first value as a pivot value
    pivotvalue = datavalues[first]

    # Declare the upper and lower indexes (as know as i and j)
    lower = first + 1
    upper = last

    # Set the loop for the partitioning
    done = False
    # Loop to incremen the upper and lower index
    while not done:
    # Increment the lower index
        while lower <= upper and datavalues[lower] <= pivotvalue:
            lower += 1
    # Decrement the upper index
        while datavalues[upper] >= pivotvalue and upper >= lower:
            upper -= 1
    # If two indexes cross, we have found the split point
        if upper < lower:
            done = True
        else:
            # temp = datavalues[lower]
            # datavalues[lower] = datavalues[upper]
            # datavalues[upper] = temp
            datavalues[lower], datavalues[upper] = datavalues[upper], datavalues[lower]
    # When the split point is found, exhchange the pivot value
    # temp = datavalues[first]
    # datavalues[first] = datavalues[upper]
    # datavalues[upper] = temp
    datavalues[first], datavalues[upper] = datavalues[upper], datavalues[first]
    # Return the plit point index
    return upper

print(items)
quickSort(items, 0, len(items) - 1)
print(items)