# Recursive algorimth to find the maximum value

# Big O Notation
# Time 0(n)
# Space 0(n)
items = [21, 24, 12, 112, 61, 12, 1124, 12245,645754, 767, 1111111]

# Recursive function to find maximum value
def find_max(items):
    if len(items) == 1:
        return items[0]
    op1 = items[0]
    op2 = find_max(items[1:])

    if op1 > op2:
        return op1
    else:
        return op2

print(find_max(items))