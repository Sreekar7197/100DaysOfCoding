# 1. Merge Two Sorted Lists Given two lists already sorted in ascending order, create a new sorted list by comparing elements one by one. Do not use sort(), append(), extend(), or slicing. 
# Input List1=[1,4,7,10] List2=[2,3,8,9] 
# Output [1,2,3,4,7,8,9,10]

list1=[1,4,7,10] 
list2=[2,3,8,9]
sorted_list =[]
for i in range(len(list1)):
    for j in range(len(list2)):
        if list1[i] not in sorted_list or list2[i] not in sorted_list:
            if list1[i]<list2[j]:
                sorted_list += [list1[i]]
            else:
                sorted_list += [list2[j]]
print(sorted_list)
# ******************************************************************************

# 2. Find the Second Largest Number Given a list of integers, find the second largest distinct number without using sort(), max(), or min(). 
# Input [12,45,67,23,89,54] 
# Output 67

nums=[12,45,67,23,89,54]
max=nums[0]
for i in range(len(nums)):
    for j in range(i,len(nums)):
        if nums[i]>nums[j]:
            nums[i],nums[j]=nums[j],nums[i]
print(nums[len(nums)-2])
# ******************************************************************************

# 3. Tuple Frequency Counter Given a tuple, count how many times each element appears and store the result in a dictionary. Do not use count(). 
# Input (2,5,2,8,5,5) 
# Output {2:2, 5:3, 8:1}

nums=(2,5,2,8,5,5)
visited = {}
for i in nums:
    if i not in visited:
        visited[i] = 1
    else:
        visited[i] += 1
print(visited)
# ******************************************************************************

# 4. Dictionary Value Sum Given a dictionary whose values are integers, calculate the total of all values manually. Do not use sum(). 
# Input {'A':10,'B':20,'C':30} 
# Output 60

nums={'A':10,'B':20,'C':30}
total = 0
for i in nums:
    total += nums[i]
print(total)
# ******************************************************************************

# 5. Unique Elements from Two Lists Print elements that occur in only one list. Do not use sets.
# Input List1=[1,2,3,4] List2=[3,4,5,6] 
# Output 1 2 5 6

list1=[1,2,3,4]
list2=[3,4,5,6]
visited = {}
for i in range(len(list1)):
    if list1[i] not in visited:
        visited[list1[i]] =1
    else:
        visited[list1[i]] +=1
for i in range(len(list2)):
    if list2[i] not in visited:
        visited[list2[i]] =1
    else:
        visited[list2[i]] +=1
for i in visited:
    if visited[i]==1:
        print(i)
# ******************************************************************************

# 6. Student Marks Analysis Store student names and marks in a dictionary. Find the highest scorer, lowest scorer, and average marks manually.
# Input {'John':78,'Rahul':92,'Priya':85,'Anu':65} 
# Output 
# Highest: Rahul-92 
# Lowest: Anu-65 
# Average: 80

marks = {'John':78,'Rahul':92,'Priya':85,'Anu':65}
high = 0
high_name = ''
low = 100
low_name = ''
total = 0
for i in marks:
    if marks[i]> high:
        high = marks[i]
        high_name = i
    if marks[i]< low:
        low = marks[i]
        low_name = i
    total +=marks[i]
print(f"Highest: {high_name}-{high}")
print(f"Lowest: {low_name}-{low}")
print(f"Average: {int(total/len(marks))}")
# ******************************************************************************

# 7. Remove Duplicate Tuples Given a list of tuples, print only unique tuples while keeping the original order. Do not use set(). 
# Input [(1,2),(3,4),(1,2),(5,6),(3,4)] 
# Output [(1,2),(3,4),(5,6)]

tup = [(1,2),(3,4),(1,2),(5,6),(3,4)]
unq = []
for i in tup:
    if i not in unq:
        unq+=[i]
print(unq)
# ******************************************************************************

# 8. Word Frequency Counter Given a list of words, count occurrences of each word and store them in a dictionary. Do not use count() or Counter. 
# Input ['apple','banana','apple','orange','banana','apple'] 
# Output {'apple':3,'banana':2,'orange':1}

fruits = ['apple','banana','apple','orange','banana','apple']
freq = {}
for i in fruits:
    if i not in freq:
        freq[i] = 1
    else:
        freq[i] += 1
print(freq)
# ******************************************************************************

# 9. Check Whether One Set is a Subset Determine whether every element of the first set exists in the second set without using issubset(). 
# Input Set1={2,4} Set2={1,2,3,4,5} 
# Output Subset

set1={2,4} 
set2={1,2,3,4,5}
sub = 0
for i in set1:
    if i in set2:
        sub +=1
if sub == len(set1):
    print("Subset")
else:
    print("Not a Subset")
# ******************************************************************************

# 10. Inventory Management System Create a menu-driven dictionary program. Keys are product names and values are quantities. Implement Add, Update, Delete, Search, Display, and Exit options. 
# Example Input/Output 
# Choice:1 Add Pen 50 
# Choice:1 Add Book 20 
# Choice:2 Update Pen 75 
# Choice:4 Search Pen -> Pen:75 
# Choice:5 -> Pen:75 Book:20 
# Choice:3 Delete Book 
# Choice:5 -> Pen:75 
# Choice:6 -> Program exited.

inventory = {}
print("====INVENTORY MANAGEMENT SYSTEM====\n 1.Add Product\n 2.Update Product Quantity\n 3.Delete Product\n 4.Search Product Quantity\n 5. Display Inventory\n 6.Exit")
while True:
    choice = int(input("Choice: "))
    if choice == 6:
        print("Program exited.")
        break
    elif choice == 1:
        product = input("Enter Product Name: ")
        quantity = int(input("Enter quantity: "))
        inventory[product] = quantity
    elif choice ==2:
        product = input("Enter Product Name: ")
        quantity = int(input("Enter quantity: "))
        if product in inventory:
            inventory[product] = quantity
        else:
            print("Invalid Product.")
    elif choice == 3:
        product = input("Enter Product Name: ")
        if product in inventory:
            inventory.pop(product)
        else:
            print("Invalid Product.")
    elif choice ==4:
        product = input("Enter Product Name: ")
        if product in inventory:
            print(f"{product}: {inventory[product]}")
        else:
            print("Invalid Product.")
    elif choice ==5:
        print(inventory)
        
