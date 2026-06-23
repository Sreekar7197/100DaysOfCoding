# 1. Longest Login Streak 
# Concepts to Use: for loop, counting
# Example Data: logins = [1, 1, 0, 1, 1, 1, 0, 1]
# Task: 1 means logged in and 0 means missed day. Find the longest continuous login streak.
# Expected Output: 
# Longest Streak = 3

logins = [1, 1, 0, 1, 1, 1, 0, 1]
streak = 0
count = 0
for login in logins:
    if login == 0:
        count = 0
        continue
    count += 1
    if count > streak:
        streak = count
print(f"Longest Streak = {streak}")
# ******************************************************************************

# 2. Password Strength Checker 
# Concepts to Use: for loop, counting 
# Example Data: password = "Abc123X" 
# Task: Count uppercase letters, lowercase letters, and digits. Print Strong Password if it contains at least one uppercase letter, one lowercase letter, and one digit. 
# Expected Output: 
# Uppercase = 2 
# Lowercase = 3 
# Digits = 3 
# Strong Password

password = "Abc123X"
uppercase = 0
lowercase = 0
digits = 0
for character in password:
    if "A"<=character<="Z":
        uppercase += 1
    elif "a"<=character<="z":
        lowercase += 1
    elif "0"<=character<="9":
        digits += 1
print(f"Uppercase = {uppercase} \nLowercase = {lowercase} \nDigits = {digits}")
if uppercase>0 and lowercase>0 and digits>0:
    print("Strong Password")
# ******************************************************************************

# Concepts to Use: for loop, continue 
# Example Data: stock = [25, 5, 0, 18, 3, 40] 
# Task: Ignore products with stock 0. Count how many products need restocking (stock less than 10). 
# Expected Output:
# Products To Restock = 2

stock = [25, 5, 0, 18, 3, 40]
restock = 0
for product in stock:
    if product == 0:
        continue
    elif product < 10:
        restock += 1
print(f"Products To Restock = {restock}")
# ******************************************************************************

# 4. Bus Seat Occupancy 
# Concepts to Use: while loop 
# Example Data: seats = [1, 0, 1, 1, 0, 0, 1] 
# Task: 1 means occupied and 0 means empty. Calculate occupied seats, empty seats, and occupancy percentage. 
# Expected Output: 
# Occupied = 4 
# Empty = 3 
# Occupancy = 57.14%

seats = [1, 0, 1, 1, 0, 0, 1]
occupied = 0
for seat in seats:
    if seat == 1:
        occupied += 1
print(f"Occupied = {occupied}\nEmpty = {len(seats)-occupied}\nOccupancy = {(occupied / len(seats))*100:.2f}%")
# ******************************************************************************

# 5. Consecutive Failures Detector
# Concepts to Use: for loop, break 
# Example Data: results = ['P', 'P', 'F', 'F', 'F', 'P'] 
# Task: Stop processing when 3 consecutive failures occur. 
# Expected Output: 
# 3 Consecutive Failures Found

results = ['P', 'P', 'F', 'F', 'F', 'P']
consec = 0
for result in results:
    if consec == 3:
        break
    if result == "P":
        consec = 0
        continue
    elif result == "F":
        consec += 1
print(f"{consec} Consecutive Failures Found")
# ******************************************************************************

# 6. Product Return Analysis 
# Concepts to Use: for loop 
# Example Data: orders = [500, 800, -500, 1000, -800]
# Task: Positive values are sales and negative values are returns. Calculate total sales, total returns, and net revenue. 
# Expected Output: 
# Sales = 2300 
# Returns = 1300 
# Net Revenue = 1000

orders = [500, 800, -500, 1000, -800]
sales = 0
returns = 0
for data in orders:
    if data > 0:
        sales += data
    elif data < 0:
        returns += data
print(f"Sales = {sales} \nReturns = {returns} \nNet Revenue = {sales+returns}")
# ******************************************************************************

# 7. Mobile Data Usage Tracker 
# Concepts to Use: while loop 
# Example Data: usage = [450, 600, 700, 550], limit = 2000 
# Task: Process usage day by day and stop when the limit is exceeded.
# Expected Output:
# Limit Exceeded On Day 4
# Used = 2300 MB

usage = [450, 600, 700, 550]
limit = 2000
day = 0
used = 0
while day < len(usage):
    if used >limit:
        break
    used += usage[day]
    day +=1
print(f"Limit Exceeded On Day {day} \nUsed = {used}MB")
# ******************************************************************************

# 8. Voting Machine Result
# Concepts to Use: for loop 
# Example Data: votes = ['A', 'B', 'A', 'C', 'A', 'B', 'A']
# Task: Count votes for each candidate and find the winner. 
# Expected Output: 
# A = 4
# B = 2 
# C = 1
# Winner = A

votes = ['A', 'B', 'A', 'C', 'A', 'B', 'A']
vote_a = 0 
vote_b = 0 
vote_c = 0 
for vote in votes:
    if vote == "A":
        vote_a += 1
    elif vote == "B":
        vote_b += 1
    elif vote == "C":
        vote_c += 1
print(f"A = {vote_a} \nB = {vote_b} \nC = {vote_c}")
if vote_a> vote_b and vote_a > vote_c:
    print("Winner = A")
elif vote_b> vote_a and vote_b > vote_c:
    print("Winner = B")
else:
    print("Winner = C")
# ******************************************************************************

# 9. Parking Lot Management
# Concepts to Use: for loop, counting 
# Example Data: vehicles = ['C', 'B', 'C', 'T', 'B', 'C'] 
# Task: Count Cars, Bikes, and Trucks.
# Expected Output:
# Cars = 3
# Bikes = 2
# Trucks = 1

vehicles = ['C', 'B', 'C', 'T', 'B', 'C']
cars = 0
bikes = 0
trucks = 0
for vehicle in vehicles:
    if vehicle == "C":
        cars += 1
    elif vehicle == "B":
        bikes += 1
    elif vehicle == "T":
        trucks += 1
print(f"Cars = {cars} \nBikes = {bikes} \ntrucks = {trucks}")
# ******************************************************************************

# 10. Number Sequence Analyzer 
# Concepts to Use: for loop 
# Example Data: numbers = [12, 5, 8, 21, 14, 7] 
# Task: Find number of even numbers, odd numbers, largest number, and smallest number. 
# Expected Output:
# Even = 3
# Odd = 3 
# Largest = 21
# Smallest = 5

numbers = [12, 5, 8, 21, 14, 7]
even = 0
odd = 0
largest = numbers[0]
smallest = numbers[0]
for num in numbers:
    if num % 2 == 0:
        even += 1
    elif num % 2 == 1:
        odd += 1
    if num > largest:
        largest = num
    elif num < smallest:
        smallest = num
print(f"Even = {even} \nOdd = {odd} \nLargest = {largest} \nSmallest = {smallest}")