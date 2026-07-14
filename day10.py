# 1. Grocery Bill Write a function that takes the prices of 5 items and returns the total bill. 
# Example Input: 
# 10 
# 25 
# 15 
# 30 
# 20 
# Output: 
# Total Bill = 100

def grocery_bill():
    total = 0
    for i in range(5):
        total+=int(input(f"Enter price of item {i+1}: "))
    return total
print(f"Total Bill = {grocery_bill()}")
# ******************************************************************************

# 2. Student Percentage 
# Write a function that takes marks in 5 subjects and returns the percentage. 
# Example Input: 
# 80 
# 75 
# 90 
# 85 
# 70 
# Output: 
# Percentage = 80.0

def stu_percent():
    total = 0
    for i in range(5):
        total += int(input(f"Enter marks of subject {i+1}: "))
    return ((total/500)*100)
print(f"Percentage = {stu_percent()}")
# ******************************************************************************

# 3. Restaurant Bill Split 
# Write a function that takes the total restaurant bill and the number of friends and returns how much each person should pay.
# Example Input: 
# 1200 
# 4 
# Output: 
# Each Person Pays = 300.0

def bill_split():
    bill = int(input("Enter the total bill amount: "))
    mems = int(input("Enter the total number of members: "))
    return (bill/mems)
print(f"Each person pays = {bill_split()}")
# ******************************************************************************

# 4. Monthly Salary 
# Write a function that takes daily wage and number of working days and returns the monthly salary. 
# Example Input: 
# 800 
# 26 
# Output: 
# Monthly Salary = 20800

def monthly_sal():
    daily = int(input("Enter the daily wage: "))
    present = int(input("Enter the number of working days: "))
    return daily*present
print(f"Monthly Salary = {monthly_sal()}") 
# ******************************************************************************

# 5. Cricket Strike Rate 
# Write a function that takes runs scored and balls faced and returns the strike rate. 
# Formula: (runs × 100) / balls
# Example Input: 
# 72 
# 48 
# Output: 
# Strike Rate = 150.0

def strike_rate():
    runs = int(input("Enter the runs scored: "))
    balls = int(input("Enter the number of balls played: "))
    return (runs/balls)*100
print(f"Strike Rate = {strike_rate()}")
# ******************************************************************************

# 6. Area and Perimeter of a Rectangle 
# Write a function that takes length and breadth and returns both area and perimeter. 
# Example Input: 
# 12 
# 8 
# Output: 
# Area = 96 
# Perimeter = 40

def mens_rect():
    length = int(input("Enter the length of rectangle: "))
    breadth = int(input("Enter the breadth of rectangle: "))
    return 2*(length+breadth),length*breadth
perimeter,area = mens_rect()
print(f"Perimeter = {perimeter}")
print(f"Area = {area}")
# ******************************************************************************

# 7. Electricity Bill 
# Write a function that takes units consumed and price per unit and returns the total bill. 
# Example Input: 
# 150 
# 8 
# Output: 
# Electricity Bill = 1200

def ele_bill():
    units=int(input("Enter no. of units consumed: "))
    price = int(input("Enter price per unit: "))
    return units*price
print(f"Electricity Bill = {ele_bill()}")
# ******************************************************************************

# 8. Simple Interest 
# Write a function that takes principal, rate, and time and returns the simple interest. 
# Formula: (P × R × T) / 100 
# Example Input: 
# 50000 
# 8 
# 2 
# Output: 
# Simple Interest = 8000.0

def simple_interest():
    p = int(input("Principle Amount : "))
    t = int(input("Time in yrs : "))
    r = int(input("Rate of Interest : "))
    return p*t*r/100
print(f"Simple Interest = {simple_interest()}")
# ******************************************************************************

# 9. Bike Mileage Write a function that takes distance traveled and fuel used and returns the mileage. 
# Formula: Distance / Fuel 
# Example Input: 
# 240 
# 6
# Output: 
# Mileage = 40.0 km/l

def mileage():
    dist = int(input("Enter distance: "))
    fuel = int(input("Enter fuel: "))
    return dist/fuel
print(f"Mileage = {mileage()} km/l")
# ******************************************************************************

# 10. Exam Remaining Marks 
# Write a function that takes total marks and obtained marks and returns the remaining marks. 
# Example Input: 
# 600 
# 482
# Output: 
# Remaining Marks = 118

def remaining_marks():
    tot = int(input("Enter total marks: "))
    obt = int(input("Enter obtained marks: "))
    return tot-obt
print(f"Remaining Marks = {remaining_marks()}")