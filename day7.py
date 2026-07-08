# 1. Electricity Bill Using Slab Rates

# Task: Write a Python program to calculate the electricity bill based on the following conditions:
# * First 100 units → ₹5 per unit
# * Next 100 units → ₹7 per unit
# * Above 200 units → ₹10 per unit

# Things to use:
# * Variables
# * Input/output
# * If-elif-else
# * Arithmetic operators

# Example Input:
# Enter units: 250

# Example Output:
# Electricity bill = 1700

units = int(input("Enter units: "))
bill = 0
if units <= 100:
    bill = units * 5
elif units <= 200:
    bill = (100 * 5) + ((units - 100) * 7)
else:
    bill = (100 * 5) + (100 * 7) + ((units - 200)*10)
print(f"Electricity Bill = {bill}")
# ******************************************************************************

# 2. Check Whether a Number is Armstrong Number
# Task:
# Write a Python program to check whether a given number is an Armstrong number.

# Things to use:
# * While loop
# * Modulus (%)
# * Integer division (//)
# * If statement

# Example Input:
# Enter number: 153


# Example Output:
# 153 is an Armstrong number

num = int(input("Enter a number: "))
arm = 0
temp1 = num
temp2 = num
count = 0
while temp1 >0:
    temp1 //=10
    count +=1
while temp2 >0:
    x = temp2 % 10
    arm += x ** count
    temp2 //= 10
if arm == num:
    print(f"{num} is an Armstrong number")
else:
    print(f"{num} is not an Armstrong number")
# ******************************************************************************

# 3. Reverse a Number and Check Palindrome
# Task:
# Write a Python program to reverse a number and determine whether it is a palindrome number.

# Things to use:
# * While loop
# * Variables
# * Modulus (%)
# * If statement

# Example Input:
# Enter number: 1221

# Example Output:
# Reversed number = 1221
# Palindrome number

num = int (input("Enter a number: "))
temp = num
rev = 0
while temp>0:
    x = temp%10
    rev = rev*10+x
    temp//=10
print(f"Reversed number = {rev}")
if rev == num:
    print("Palindrome number")
else:
    print("Not a Palindrome number")
# ******************************************************************************

# 4. Count Even and Odd Digits in a Number
# Task:
# Write a Python program to count the number of even digits and odd digits in a given number.

# Things to use:
# * While loop
# * Modulus operator
# * If condition

# Example Input:
# Enter number: 256843

# Example Output:
# Even digits = 4
# Odd digits = 2

num = int(input("Enter a number: "))
temp = num
even = 0
odd = 0
while temp>0:
    x = temp % 10
    if x %2==0:
        even +=1
    else:
        odd +=1
    temp //= 10
print(f"Even digits: {even}")
print(f"Odd digits: {odd}")
# ******************************************************************************

# 5. ATM Cash Withdrawal System
# Task:
# Write a Python program to simulate an ATM withdrawal system with the following conditions:
# * User enters account balance and withdrawal amount
# * Withdrawal amount should be a multiple of 100
# * Withdrawal amount should not exceed account balance
# * Display updated balance if transaction is successful; otherwise show an appropriate message

# Things to use:
# * Variables
# * If-elif-else
# * Arithmetic operators
# * Multiple conditions

# Example Input:
# Enter account balance: 10000
# Enter withdrawal amount: 2500

# Example Output:
# Transaction Successful
# Remaining balance = 7500

bal = int(input("Enter account balance: "))
withdraw = int(input("Enter withdrawl amount: "))
if withdraw > bal:
    print("Withdrawal amount should not exceed account balance.")
elif withdraw %100 != 0:
    print("Withdrawal amount should be a multiple of 100.")
else:
    bal -= withdraw
    print("Transaction Successful")
    print(f"Remaining balance = {bal}")
# ******************************************************************************

# 6. Strong Number Checker
# Task:
# Write a Python program to check whether a given number is a Strong number.
# A Strong number is a number whose sum of factorials of its digits equals the original number.

# Example:
# 145 = 1! + 4! + 5!

# Things to use:
# * While loop
# * Nested loop
# * Variables
# * Factorial logic
# * Modulus (%) and integer division (//)

# Example Input:
# Enter number: 145

# Example Output:
# 145 is a Strong number

num = int(input("Enter a number: "))
temp = num
strong = 0
while temp >0:
    x =  temp %10
    fact = 1
    while x>=1:
        fact *= x
        x-=1
    strong += fact
    temp //=10
if strong == num:
    print(f"{num} is a strong number")
else:
    print(f"{num} is not a strong number")
# ******************************************************************************

# 7. Sum of Squares Series
# Task:
# Write a Python program to find the sum of the following series:
# 1² + 2² + 3² + ... + n²

# Things to use:
# * For loop
# * Variables
# * Arithmetic operators

# Example Input:
# Enter n: 5

# Example Output:
# Sum = 55

n = int(input("Enter n: "))
sum = 0
for i in range(1,n+1):
    sum+= i**2
print(f"Sum = {sum}")
# ******************************************************************************

# 8. Find Frequency of Digits in a Number
# Task:
# Write a Python program to count the frequency of each digit in a given number.

# Things to use:
# * While loop
# * Dictionary or list
# * Modulus operator
# * Loops

# Example Input:
# Enter number: 22334452

# Example Output:
# 2 occurs 3 times
# 3 occurs 2 times
# 4 occurs 2 times
# 5 occurs 1 time

num = int(input("Enter a number: "))
digits = {}
while num > 0:
    x = num%10
    if x in digits:
        digits[x] +=1
    else:
        digits[x] =1
    num //=10
for x in sorted(digits):
    print(f"{x} occurs {digits[x]} times")
# ******************************************************************************

# 9. Find Prime Numbers in a Given Range
# Task:
# Write a Python program to display all prime numbers between two given numbers.

# Things to use:
# * Nested loops
# * If condition
# * Range function

# Example Input:
# Enter start number: 10
# Enter end number: 30

# Example Output:
# Prime numbers:
# 11
# 13
# 17
# 19
# 23
# 29

a = int(input("Enter start number: "))
b = int(input("Enter end number: "))
for i in range(a,b):
    check = 0
    for j in range(2,i):
        if i%j ==0:
            check +=1
    if check ==0:
        print(i)
# ******************************************************************************

# 10. Employee Payroll System with Bonus Calculation
# Task:
# Write a Python program to accept details of 5 employees (name, basic salary, and years of experience).

# Calculate:
# * HRA = 15% of basic salary
# * TA = 10% of basic salary
# * Bonus:
#   * Experience ≥ 5 years → 20% of salary
#   * Experience < 5 years → 10% of salary
# * Gross Salary = Basic + HRA + TA + Bonus

# Display:
# * Gross salary of each employee
# * Employee with highest gross salary

# Things to use:
# * Lists
# * Loops
# * Conditions
# * Variables
# * Percentage calculations

# Example Input:
# Employee Name: Ravi
# Basic Salary: 30000
# Experience: 6

# Employee Name: Priya
# Basic Salary: 40000
# Experience: 4

# Example Output:
# Ravi Gross Salary = 43500
# Priya Gross Salary = 54000

high_name = ''
high_gross = 0
for i in range(5):
    n = input("Employee name: ")
    s = int(input("Basic Salary: "))
    e = int(input("Experience: "))

    gross = s + 0.1*s + 0.15*s
    if e>=5:
        gross +=0.2*s 
    else:
        gross += 0.1*s 
    print(f"{n} gross salary = {int(gross)}")
    if gross>high_gross:
        high_gross= gross
        high_name = n 
print(f"Highest gross salary is of {high_name} with sal of {int(high_gross)}")     
