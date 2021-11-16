def print_to_val(val):
    if (val == 0):
        print("Done!!!")
        return
    print("its", val)
    print_to_val(val - 1)

print_to_val(10)