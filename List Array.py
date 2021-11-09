import math

######### List ###########
## Note: List is the another notation to the Array in C++ and C# ##
# Constructor
cars = ["Ford", "KYA", "Honda", "Toyota"]

## We can get the length of the array by using the len(*ArrayName*)
print(len(cars))

## Looping through the Array using
for x in cars:
  print(x)

## Unlike C++ Array, Python list size is adaptive so you can
## easily insert an element into the List without worry about
## getting out of high bound
cars.append("Subasa")

## The function Pop in the List ressemble the pop function in
## Stack but it can used with an index.
## Meanwhile the we can specify the value of the data to delete
## it in the list with the remove function
cars.remove("Honda")
cars.pop(0)
print("--------------------------------")
for x in cars:
  print(x)

## The list of all functions that can be used in Python Array
## append()	Adds an element at the end of the list
## clear()	Removes all the elements from the list
## copy()	Returns a copy of the list
vehicle = cars.copy()
print(vehicle)
## count()	Returns the number of elements with the specified value
print(cars.count("Subasa"))
## extend()	Add the elements of a list (or any iterable), to the end of the current list
cars.extend(["Chevolet", "Wolkasen", "BWM"])
print(vehicle)
## index()	Returns the index of the first element with the specified value
print(cars.index("Toyota"))
## insert()	Adds an element at the specified position
cars.insert(4,"Bongo")
## pop()	Removes the element at the specified position
cars.pop(1)
## remove()	Removes the first item with the specified value
cars.remove("KYA")
## reverse()	Reverses the order of the list
cars.reverse()
print(cars)
## sort()	Sorts the list
cars.sort()
print(cars)
