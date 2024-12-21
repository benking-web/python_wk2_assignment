#NO1: Create an empty list called my_list

my_list = []   # Create an empty list


#NO2: Append the following elements to my_list: 10, 20, 30, 40.

# Create an empty list
my_list = []

# Append the elements to the list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

# Print the list to check the result
print(my_list)
#output: [10, 20, 30, 40]


#NO3: Insert the value 15 at the second position in the list.

# Create a list with elements
my_list = [10, 20, 30, 40]

# Insert the value 15 at the second position (index 1)
my_list.insert(1, 15)

# Print the list to check the result
print(my_list)

""" insert(1, 15) inserts 15 at index 1.  list indices are zero-based, so index 1 refers to the second position.
output : [10, 15, 20, 30, 40] """


#NO4: Extend my_list with another list: [50, 60, 70].

# Existing list
my_list = [10, 15, 20, 30, 40]

# List to extend with
new_elements = [50, 60, 70]

# Extend my_list with new_elements
my_list.extend(new_elements)

# Print the updated list
print(my_list)
#output: [10, 15, 20, 30, 40, 50, 60, 70]
""" The extend() method adds all elements from the list new_elements to the end of my_list.
After this operation, my_list will contain the original elements plus the new elements [50, 60, 70]."""

#NO5: Remove the last element from my_list.

# Existing list
my_list = [10, 15, 20, 30, 40, 50, 60, 70]

# Remove the last element
my_list.pop()

# Print the updated list
print(my_list)
#output: [10, 15, 20, 30, 40, 50, 60]
""" The pop() method removes and returns the last element of the list. Since we don't provide an index, it removes the last element by default.
After calling pop(), the list will no longer contain the last element, which was 70 in this case."""

#NO6: Sort my_list in ascending order.

# Existing list
my_list = [10, 15, 20, 30, 40, 50, 60, 70]

# Sort the list in ascending order
my_list.sort()

# Print the sorted list
print(my_list)
#output: [10, 15, 20, 30, 40, 50, 60, 70]
#my_list.sort() sorts the list in place in ascending order by default.


#NO7: Find and print the index of the value 30 in my_list.

# Existing list
my_list = [10, 15, 20, 30, 40, 50, 60, 70]

# Find and print the index of the value 30
index_of_30 = my_list.index(30)

# Print the index
print(index_of_30)
#output: 3
""" The index(30) method searches for the value 30 in the list and returns its index. In this case, the index of 30 is 3 because list indices are zero-based."""



