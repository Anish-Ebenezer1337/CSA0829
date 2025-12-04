#Creating a List
col=["red", "yellow", "blue"]
print(col)
print()

#Accessing Elements
print("First Element ", col[0]) #First Element
print("Last Element", col[-1]) #Last Element
print()

#Update Element
col[1]="green"
print("Updated list", col)
print()

#Append Element
col.append("orange")
print("After appending ", col)
print()

#Inserting an element
col.insert(4, "black")
print("After Inserting ", col)
print()

#Remove Element
col.remove("orange")
print("After removing ", col)
print()

#Popping Element
col.pop(0)
print("After popping 0th element ", col)
print()

#Length of list
print("The length of list", col, " is ", len(col))
print()

#List slicing
print("col[0:2] gives ", col[0:2])
print()

#Iterating through a list
print("Iteration")
for i in col:
    print(i)
print()


#Largest and smallest
l=[10,30,50,50,55,92,50]
print("New list- ", l)
print("Largest number- ", max(l))
print("Smallest number- ", min(l))
print()

#Sorting
print("Sorting the list- ", l.sort())
print()

#Reversing a List
print("Reversing a list- ", l.reverse())
print()

#Count occurence
print("The occurence of 50 in the list ", l.count(50))
print()

#Find index
print("Index of 55 in list-", l.index(55))
print()

#List comprehension
print("List Comprehension")
squares=[x*x for x in range(1,6)]
print(squares)
print()

#Merge two lists
a=[1,2,3]
b=[4,5,6]
print("a= ", a)
print("b= ", b)
print("After merging- ", a+b)
print()

#Remove duplicates
print(l)
unique=list(set(l))
print("After removing duplicates- ", unique)
print()

#Copying a list
copy_list=a.copy()
print("Copied list from list a", copy_list)
