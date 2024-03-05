# Program that accept user input to create two sets of integers and find their intersection
set1 = set(input("Enter integers separated by spaces for the first set: ").split())
set2 = set(input("Enter integers separated by spaces for the second set: ").split())
common_elements = set1.intersection(set2)
print("Common elements in the sets:", common_elements)