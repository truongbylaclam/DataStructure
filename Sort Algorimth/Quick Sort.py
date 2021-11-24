items = [12, 45, 10, 5, 54, 99, 7, 75]

def quickShort(dataset, first, last):
    if first < last:
        # Calculate the split point
        pivotIdx = partition(dataset, first, last)

        # Sort the two partition
        partition(dataset, first, pivotIdx - 1)
        partition(dataset, pivotIdx, last)
def partition(datavalues, first, last):

    # Chose the first value as a pivot value
    pivotvalue = datavalues[first]

    # Declare the upper and lower indexes (as know as i and j)
    upper = first + 1
    lower = last

    # Set the loop for the partitioning
    done = False
    ## Be
    while not done:
        while lower <= upper and datavalues[lower] <= pivotvalue:
            lower += 1








print(items)
quickShort(items, 0, len(items) - 1)
print(items)