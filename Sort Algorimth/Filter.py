# Using a hash table to filter out diplicate and count item

# Item declaration
items = ["Orange", "Lime", "Lemon", "Blueberry", "Black Berry",
        "Grape", "Lime", "Orange", "Apple"]

# Filter functions
 counter = dict()

# Add value onto the hash table
 for key in items:
    if key in filter.keys():
       counter[key] += 1
    else:
        counter[key] = 1
# Print the variable
print(counter)




# Item Filter 
filter = dict()
# Looping through the array and add each elements to the hashmap
for key in items:
    filter[key] = 0
# Save all the result onto a single variable
result = set(filter.keys())
print(result)
