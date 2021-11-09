import numpy as np

# List construction
key_words=["Cat", "Dog", "Rabbit", "Tiger" ]
# List Indexing
print(key_words[1])
# List Slicing
print(key_words[1:3])
# Negative Indexing
print(key_words[:-1])
print(key_words[:-2])

# Nesting
search_result_index = [45, [23,561,617], [1.5,8.654,53.43,112.42]]
print(max(search_result_index[2]))

# Iteration

for words in key_words:
    print("Search for " + words)

# Lambda Function

random_Number = np.random.rand(1,6)
print(random_Number)

# Data Filtering
print(list(filter(lambda x: x > 333 , [3214, 515, 21, 421, 332, 231, 4412])))

# Data Transformation
# Using the map function with a lambda function provides quite powerful
# functionality. When used with the map function, the lambda function can be used
# to specify a transformer that transforms each element of the given sequence.
print(list(map(lambda x: x ** 2, [1, 2, 3, 4, 5, 6])))

# Data aggregation: For data aggregation, the reduce() function can be used,
# which recursively runs a function to pairs of values on each element of the list
from functools import reduce
def doSum(x1,x2):
    return x1+x2
x = reduce(doSum, [100, 2, 3, 1231, 451])
print(x)
# Note that the reduce function needs a data aggregation function to be defined.
# That data aggregation function in the preceding code is functools. It defines
# how it will aggregate the items of the given list. The aggregation will start from
# the first two elements and the result will replace the first two elements. This
# process of reduction is repeated until we reach the end, resulting in one
# aggregated number

# Range function
# The range function can be used to easily generate a large list of numbers.
# It is used to autopopulate sequences of numbers in a list.

z = range(3,29,2)
print(z)
# This range function does not function properly
account = [[1,4], [5,5,71], [2,23,1,45], [1,4,5,2,1,5]]
for c in range(len(account)):
            accumulatedWealth = 0
            for m in range(len(account[c])):
                    accumulatedWealth[c] += m
            print(accumulatedWealth[c])
#
