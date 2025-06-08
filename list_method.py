origin_list = [1, 2, 3, 4, 5]

print("Original list:", origin_list)
# append
origin_list.append(6)
print("After appending 6:", origin_list)
# insert
origin_list.insert(0, 0)
print("After inserting 0 at the beginning:", origin_list)
# extend
origin_list.extend([7, 8, 9])
print("After extending with [7, 8, 9]:", origin_list)
# remove
origin_list.remove(3)
print("After removing 3:", origin_list)
# pop
popped_element = origin_list.pop()
print("After popping the last element:", origin_list)
print("Popped element:", popped_element)
# clear
origin_list.clear()
print("After clearing the list:", origin_list)
# copy
copied_list = origin_list.copy()
print("Copied list:", copied_list)
# count
origin_list = [1, 2, 2, 3, 4]
count_of_twos = origin_list.count(2)
print("Count of 2 in the list:", count_of_twos)
# index
index_of_four = origin_list.index(4)
print("Index of 4 in the list:", index_of_four)
# sort
origin_list.sort()
print("After sorting the list:", origin_list)
# reverse 
origin_list.reverse()
print("After reversing the list:", origin_list)
# slicing
sliced_list = origin_list[1:4]
print("Sliced list from index 1 to 4:", sliced_list)
# concatenation
another_list = [10, 11, 12]
concatenated_list = origin_list + another_list
print("Concatenated list with [10, 11, 12]:", concatenated_list)
# repetition
repeated_list = origin_list * 2
print("Repeated list:", repeated_list)
# membership
is_five_in_list = 5 in origin_list
print("Is 5 in the list?", is_five_in_list)