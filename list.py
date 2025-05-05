'''Python list method are built in function that allow as to perform various operations on lists
such as adding, removing, and modifying elements. 

append(): Adds an element to the end of the list.
copy() : Returns a shallow copy of the list.
clear(): Removes all elements from the list.
count() :Returns the number of occurrences of a specified element in the list.
extend() : Adds the elements of a list (or any iterable) to the end of the current list.
index() : Returns the index of the first occurrence of a specified element
insert(): Adds an element at a specified position in the list.
pop(): Removes the element at the specified position in the list, and returns it.
remove(): Removes the first occurrence of a specified element from the list.
reverse(): Reverses the order of the list.
sort(): Sorts the list in ascending order by default.'''

myList = [45,56,23,45,23]
print("My Original list is", myList)

myList.append(35)
print("My list after appending 35 is", myList)

lcount=myList.count(45)
print("The count of 45 in my list is", lcount)
print(myList)

print("The count of 23 in my list is",myList.index(23))
print(myList)

myList.pop()
print("Remove last element ",myList)