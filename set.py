# set demos
set_demo = set()
# add elements to the set
set_demo.add(1)
set_demo.add(2)
set_demo.add(3)
set_demo.add(4)

# add a duplicate element
set_demo.add(1)

# add a string element
set_demo.add("hello")

# print the set
print(set_demo)

# loop through the set
for item in set_demo:
    print(item)

# check if an element is in the set
if 1 in set_demo:
    print("1 is in the set")
else:
    print("1 is not in the set")  

# check if an element is in the set using contains
print(set_demo.__contains__(1))  

# size
print("Size of the set:", len(set_demo))

# clear the set
set_demo.clear()
print("Set after clearing:", set_demo)
print("Length of the set after clearing:", len(set_demo))

# union of two sets
set_a = {1, 2, 3}
set_b = {3, 4, 5}
set_union = set_a.union(set_b)
print("Union of set_a and set_b:", set_union)

# intersection of two sets
set_intersection = set_a.intersection(set_b)
print("Intersection of set_a and set_b:", set_intersection)

# difference of two sets
set_difference = set_a.difference(set_b)
print("Difference of set_a and set_b:", set_difference)