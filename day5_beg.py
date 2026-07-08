# 1. Seating Arrangement Checker 
# Task: Find occupied seats, empty seats, and row with maximum occupancy. Input: seats=[[1,0,1,1],[0,1,1,0],[1,1,1,1]] 
# Output: Occupied Seats=9, Empty Seats=3, Row with Maximum Occupancy=Row 3

seats=[[1,0,1,1],[0,1,1,0],[1,1,1,1]]
count = 0
max_row = 0
total=0
for i in range (3):
    max = 0
    for j in range(4):
        if seats[i][j] == 1:
            count +=1
        total +=1
    if count>max:
        max = count
        max_row = i+1
print(f"Occupied Seats={count}")
print(f"Empty Seats={total-count}")
print(f"Row with Maximum Occupancy=Row {max_row}")
# ******************************************************************************

# 2. Product Price Comparison 
# Task: Find cheapest price for each product and store. 
# Input: prices=[[100,120,90],[250,200,300],[50,70,60]] 
# Output: Product 1=90(Store 3), Product 2=200(Store 2), Product 3=50(Store 1)

prices=[[100,120,90],[250,200,300],[50,70,60]]
for i in range(3):
    min_price =prices[i][0]
    min_store = 1
    for j in range(3):
        if prices[i][j]< min_price:
            min_price =  prices[i][j]
            min_store = j+1
    print(f"Product {i+1}={min_price}(Store {min_store})")
# ******************************************************************************

# 3. Word Search in a Grid 
# Task: Count occurrences of a given character. 
# Input: grid=[['p','y','t'],['h','o','n'],['p','y','t']], character='p' Output: p found 2 times

grid=[['p','y','t'],['h','o','n'],['p','y','t']]
character='p'
visited = {}
for i in range(3):
    count = 0
    for j in range(3):
        if grid[i][j] in visited:
            visited[grid[i][j]] += 1
        else:
            visited[grid[i][j]] = 1
for i in visited:
    print(f"{i} found {visited[i]} times")
# ******************************************************************************

# 4. Matrix Diagonal Analyzer 
# Task: Find diagonal sums and compare them. 
# Input: matrix=[[5,2,3],[1,6,4],[7,8,9]] 
# Output: Main=20, Opposite=16, Equal=False

matrix=[[5,2,3],[1,6,4],[7,8,9]]
main = 0
opp =0
for i in range(3):
    for j in range(3):
        if i==j:
            main += matrix[i][j]
    opp += matrix[i][len(matrix[i])-1-i]
print(f"Main={main}")
print(f"Opposite={opp}")
if main==opp:
    print(f"Equal=True")
else:
    print(f"Equal=False")
# ******************************************************************************

# 5. Password Strength Analyzer 
# Task: Count uppercase, lowercase and digits and classify password. 
# Input: passwords=['Abc123','hello','P@55'] 
# Output: Abc123 Strong, hello Weak, P@55 Strong

passwords=['Abc123','hello','P@55']
for i in range(len(passwords)):
    up=0
    low=0
    dig=0
    char=0
    for j in range(len(passwords[i])):
        if passwords[i][j] >= "A" and passwords[i][j] <="Z":
            up+=1
        elif passwords[i][j] >= "a" and passwords[i][j] <="z":
            low+=1
        elif passwords[i][j] >= "0" and passwords[i][j] <="9":
            dig +=1
        else:
            char +=1
    if up>0 and dig >0:
        print(passwords[i], "Strong")
    else:
        print(passwords[i], "Weak")
# ******************************************************************************

# 6. Image Pixel Brightness Analyzer 
# Task: Count dark, medium and bright pixels. 
# Input: image=[[20,80,200],[40,150,220]] 
# Output: Dark=2, Medium=2, Bright=2

image=[[20,80,200],[40,150,220]]
dark = 0
med = 0
bright = 0
for i in range(len(image)):
    for j in range(len(image[i])):
        if image[i][j]<=49:
            dark +=1
        elif image[i][j]<=150:
            med +=1
        else:
            bright +=1
print(f"Dark={dark}")
print(f"Medium={med}")
print(f"Bright={bright}")
# ******************************************************************************

# 7. Find Duplicate Rows in Data 
# Task: Find rows containing identical data. 
# Input: data=[[10,20,30],[40,50,60],[10,20,30]] 
# Output: Duplicate Row Found: Row 1 and Row 3

data=[[10,20,30],[40,50,60],[10,20,30]]
for i in range(len(data)):
    for j in range(i+1,len(data)):
        if data[i]==data[j]:
            print(f"Duplicate Row Found: Row {i+1} and Row {j+1}")
# ******************************************************************************

# 8. Bus Route Analyzer 
# Task: Find common stops and total unique stops.
# Input: routes=[['A','B','C'],['B','C','D'],['C','D','E']] 
# Output: Common Stop=C, Total Unique Stops=5

routes=[['A','B','C'],['B','C','D'],['C','D','E']]
unq = {}
common = ''
for i in range(len(routes)):
    common = ''
    for j in range(len(routes[i])):
        if routes[i][j] in unq:
            unq[routes[i][j]] += 1
        else:
            unq[routes[i][j]] = 1
for i in unq:
    if unq[i] == len(routes):
        common = i
print(f"Common Stop={common}")
print(f"Total Unique Stops={len(unq)}")
# ******************************************************************************

# 9. Monthly Expense Category Tracker 
# Task: Find highest expense and categories above limit. 
# Input: expenses=[[500,200,800],[300,700,100],[900,400,600]], limit=500
#  Output: Person 1 Highest=800, Categories Above Limit=4

expenses=[[500,200,800],[300,700,100],[900,400,600]]
limit=500
abv=0
for i in range(len(expenses)):
    high = 0
    for j in range(len(expenses[i])):
        if expenses[i][j] > high:
            high = expenses[i][j]
        if expenses[i][j] >limit:
            abv +=1
    print(f"Person {i+1} Highest={high}")
print(f"Categories Above Limit={abv}")
# ******************************************************************************

# 10. Chess Board Analyzer 
# Task: Count white pieces, black pieces and empty positions. 
# Input: board=[['W','B','-'],['B','W','-'],['-','W','B']] 
# Output: White=3, Black=3, Empty=3

board=[['W','B','-'],['B','W','-'],['-','W','B']]
pieces = {}
for i in range(len(board)):
    for j in range(len(board[i])):
        if board[i][j] in pieces:
            pieces[board[i][j]] += 1
        else:
            pieces[board[i][j]] = 1
print (f"White={pieces['W']}")
print (f"Black={pieces['B']}")
print (f"Empty={pieces['-']}")