# 1. Running Sum Triangle 
# Concepts to Use: Nested for loop, Addition 
# Example Data: n = 5
# Task: For each row, add numbers from 1 up to that row number. 
# Expected Output:
# 1 = 1 
# 1+2 = 3 
# 1+2+3 = 6 
# 1+2+3+4 = 10 
# 1+2+3+4+5 = 15
# :::: WRONG CODE ::::
n = 5
for i in range (1,n+1):
    total = 0
    for j in range (1,i+1):
        total +=j
        print(j, end="")
        if j<i:
            print(end="+")
    print(" =",total)
# ******************************************************************************

# 2. Multiplication Table Statistics 
# Concepts to Use: Nested for loop, Counting 
# Example Data: Tables 2 to 10 
# Task: Count how many multiplication results are less than 20, between 20 and 50, and greater than 50. 
# Expected Output: 
# Less than 20 = ? 
# 20 to 50 = ?
# Greater than 50 = ?

greater = 0
rang = 0
lesser = 0
for num in range (2,11):
    for table in range(1,11):
        if num*table > 50:
            greater += 1 
        elif num*table <=50 and num*table >=20:
            rang += 1
        elif num*table <20:
            lesser +=1
print(f"Lesser than 20 = {lesser}")
print(f"20 to 50 = {rang}")
print(f"Greater than 50 = {greater}")
# ******************************************************************************

# 3. Student Marks Competition 
# Concepts to Use: Nested for loop, Comparison 
# Example Data: marks = [85, 70, 92, 78, 88]
# Task: For each student count how many students scored more than them.
# Expected Output: 
# 85 -> 2
# 70 -> 4 
# 92 -> 0
# 78 -> 3
# 88 -> 1 
#  
marks = [85, 70, 92, 78, 88]
count = 0
for i in (marks):
    count = 0
    for j in (marks):
        if j > i:
            count +=1
    print(f"{i} -> {count}")
# ******************************************************************************

# 4. Sales Leaderboard
# Concepts to Use: Nested for loop, Ranking 
# Example Data: sales = [500, 900, 700, 1200]
# Task: Find rank of every salesperson.
# Expected Output:
# 500 -> Rank 4
# 900 -> Rank 2 
# 700 -> Rank 3
# 1200 -> Rank 1

sales = [500, 900, 700, 1200]
for i in sales:
    count = 0
    for j in sales:
        if j>i:
            count += 1
    print(f"{i} -> Rank {count+1}")
# ******************************************************************************

# 5. Pair Sum Finder
# Concepts to Use: Nested for loop 
# Example Data: 
# numbers = [2, 5, 7, 8, 3] 
# target = 10 
# Task: Print all pairs whose sum is 10.
# Expected Output: 
# 2 + 8
# 7 + 3

numbers = [2, 5, 7, 8, 3] 
target = 10 
for i in range(len(numbers)):
    for j in range(i+1,len(numbers)):
        if numbers[i]+numbers[j] == target:
            print(numbers[i],"+",numbers[j])
# ******************************************************************************

# 6. Pair Product Finder
# Concepts to Use: Nested for loop 
# Example Data: numbers = [2, 3, 4, 6, 8] target = 24
# Task: Print all pairs whose product is 24. 
# Expected Output:
# 3 x 8 
# 4 x 6

numbers = [2, 3, 4, 6, 8] 
target = 24
for i in range(len(numbers)):
    for j in range(i+1, len(numbers)):
        if numbers[i]*numbers[j] == target:
            print(numbers[i],'x',numbers[j])
# ******************************************************************************

# 7. Matrix Total
# Concepts to Use: Nested for loop 
# Example Data: [[10,20,30],[40,50,60],[70,80,90]]
# Task: Find total of all values.
# Expected Output:
# Total = 450

mat = [[10,20,30],[40,50,60],[70,80,90]]
total = 0
for i in mat:
    for j in i:
        total += j
print('Total =',total)
# ******************************************************************************

# 8. Row Wise Totals
# Concepts to Use: Nested for loop
# Example Data: [[10,20,30],[40,50,60],[70,80,90]]
# Task: Find sum of every row. 
# Expected Output:
# Row 1 = 60
# Row 2 = 150 
# Row 3 = 240

mat = [[10,20,30],[40,50,60],[70,80,90]]
total = 0
row_num = 0
for i in mat:
    total = 0
    row_num +=1
    for j in i:
        total += j
    print(f"Row {row_num} = {total}")
# ******************************************************************************

# 9. Match Schedule Generator
# Concepts to Use: Nested for loop
# Example Data: teams = ['A', 'B', 'C', 'D']
# Task: Generate all matches. 
# Expected Output:
# A vs B
# A vs C
# A vs D
# B vs C
# B vs D
# C vs D

teams = ['A', 'B', 'C', 'D']
for i in range(len(teams)):
    for j in range(i+1, len(teams)):
        print(teams[i],'vs',teams[j])
# ******************************************************************************

# 10. Highest Row Total 
# Concepts to Use: Nested for loop, Comparison
# Example Data: [[10,20,30],[50,60,70],[15,25,35]]
# Task: Find row having highest total. 
# Expected Output: 
# Row 2
# Total = 180

rows = [[10,20,30],[50,60,70],[15,25,35]]
max_tot = 0
row = 0
for i in rows:
    total = 0
    for j in i:
        total += j
    if total> max_tot:
        max_tot = total
        row +=1
print("Row",row)
print("Total =",max_tot)
# ******************************************************************************