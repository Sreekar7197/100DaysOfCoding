# 1. Grocery Store Billing with Discount
# Concepts to Use: for loop, if 
# Example Data: prices = [500, 1200, 800, 1500] 
# Task: 
# Calculate the total bill. If an item price is greater than 1000, give a 10% discount on that item. Calculate the final bill after discount. 
# Expected Output: 
# Total Bill = 4000 
# Discount = 270 
# Final Bill = 3730

prices = [500, 1200, 800, 1500]
total = 0
disc = 0
for item_price in prices:
    total += item_price
    if item_price > 1000:
        disc+=item_price*0.1
print(f"Total Bill = {total}")
print(f"Discount = {disc}")
print(f"Final Bill = {total-disc}")
# ****************************************************************************

# 2. Employee Attendance Percentage 
# Concepts to Use: for loop, counting 
# Example Data: attendance = ['P', 'A', 'P', 'P', 'A', 'P'] 
# Task: Calculate the total present days and attendance percentage.
# Expected Output: 
# Present Days = 4 
# Attendance Percentage = 66.67

attendance = ['P', 'A', 'P', 'P', 'A', 'P'] 
present = 0
for check in attendance:
    if check == 'P':
        present += 1
print(f"Present Days = {present}")
print(f"Attendance Percentage = {(present/len(attendance))*100}")
# *****************************************************************************

# 3. Online Shopping Cart 
# Concepts to Use: for loop, continue 
# Example Data: cart = [500, -1, 700, 1200, -1, 300] 
# Task: -1 means item removed from cart. Ignore removed items and calculate the total amount.
# Expected Output:
# Total Amount = 2700

cart = [500, -1, 700, 1200, -1, 300]
total = 0
for item in cart:
    if item == -1:
        continue
    total += item
print(f"Total Amount: {total}")
# ******************************************************************************

# 4. Bank Transactions 
# Concepts to Use: for loop, break 
# Example Data: 
# transactions = [5000, -2000, -3000, -4000]
# balance = 6000 
# Task: Process transactions one by one. Stop if the balance becomes negative. Display the final balance. 
# Expected Output: 
# Insufficient Balance 
# Final Balance = 1000

transactions = [5000, -2000, -3000, -4000]
balance = 6000 
for money in transactions:
    if balance + money < 0:
        print("Insufficient Balance")
        break
    balance += money
print(f"Final Balance = {balance}")
# ******************************************************************************

# 5. Cricket Tournament Analysis 
# Concepts to Use: for loop 
# Example Data: runs = [45, 80, 22, 95, 60] 
# Task: Find the total runs, highest score, and average score. 
# Expected Output: 
# Total = 302 
# Highest = 95 
# Average = 60.4

runs = [45, 80, 22, 95, 60] 
total= 0
highest = 0 
for score in runs:
    if score>highest:
        highest = score
    total += score
print(f"Total = {total}")
print(f"Highest = {highest}")
print(f"Average = {total/len(runs)}")
# ******************************************************************************

# 6. Electricity Consumption Billing 
# Concepts to Use: while loop 
# Example Data: units = [120, 150, 200, 180] 
# Task: Calculate the electricity bill using: First 100 units = 5/unit Remaining units = 8/unit 
# Expected Output: 
# Calculate Total Bill

units = [120, 150, 200, 180]
ind = 0
total = 0
while ind< len(units):
    if (units[ind]) <100:
        total += units[ind]*5
    total += units[ind]*8
    ind +=1
print(f"Total Bill = {total}")
# ******************************************************************************

# 7. Exam Result Processing 
# Concepts to Use: for loop, counting 
# Example Data: marks = [75, 30, 82, 40, 95, 28] 
# Task: Count how many students passed and failed. Pass mark = 35.
# Expected Output: 
# Passed = 4 
# Failed = 2

marks = [75, 30, 82, 40, 95, 28]
passed = 0
for mark in marks:
    if mark >= 35:
        passed += 1
print(f"Passed = {passed}")
print(f"Failed = {len(marks)-passed}")
#*******************************************************************************

# 8. Food Delivery Performance
# Concepts to Use: for loop, continue 
# Example Data: ratings = [5, 4, 0, 3, 5, 0, 4] 
# Task: 0 means not rated. Ignore those ratings and calculate the average rating. Expected Output: 
# Average Rating = 4.2

ratings = [5, 4, 0, 3, 5, 0, 4]
total = 0
count = 0
for rating in ratings:
    if rating == 0:
        continue
    total += rating
    count += 1
print(f"Average Rating: {total/count}")
# ******************************************************************************

# 9. ATM Cash Dispensing 
# Concepts to Use: while loop 
# Example Data: amount = 3700 
# Task: Calculate the minimum number of notes required using 2000, 500, 200, and 100 notes. 
# Expected Output: 
# 2000 x 1 
# 500 x 3 
# 200 x 1

amount = 3700
while amount > 0:
    if amount >= 2000:
        count1 = amount // 2000
        print(f"2000 x {count1}")
        amount %= 2000
    elif amount >= 500:
        count2 = amount // 500
        print(f"500 x {count2}")
        amount %= 500
    elif amount >= 200:
        count3 = amount // 200
        print(f"200 x {count3}")
        amount %= 200

# ******************************************************************************

# 10. Sales Report Generator 
# Concepts to Use: for loop, break, continue 
# Example Data: sales = [5000, 7000, -1, 9000, 0, 8000] 
# Task: -1 means holiday (skip it). 0 means system crash (stop processing). Calculate total sales before crash. 
# Expected Output: 
# Total Sales = 21000

sales = [5000, 7000, -1, 9000, 0, 8000]
total = 0
for sale in sales:
    if sale == 0:
        break
    elif sale == -1:
        continue
    total += sale
print(f"Total Sales = {total}")
# ******************************************************************************
