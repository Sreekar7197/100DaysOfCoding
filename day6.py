# Task 1: Student Grade Checker (Beginner) 
# Topics to Use: if, elif, else 
# Problem: A school wants to automatically assign grades based on student marks. 
# A→90 and above, B→75–89, C→60–74, D→35–59, Fail→Below 35. 
# Example Input: Enter marks: 82 
# Expected Output: Grade: B

marks = int(input("Enter your marks: "))
if marks >= 90:
    print("Grade: A")
elif marks >=75 and marks <=89:
    print("Grade: B")
elif marks >=60 and marks <=74:
    print("Grade: C")
elif marks >=35 and marks <=59:
    print("Grade: D")
else:
    print("Failed.")
# ******************************************************************************

# Task 2: ATM PIN Verification (Beginner) 
# Topics: while, if-else 
# Problem: Allow only 3 PIN attempts. Correct PIN: Login Successful. After 3 wrong attempts: Card Blocked. 
# Example Input: 1111, 2345, 1234 
# Expected Output: Login Successful

corr_pin = 7197
max_attempts = 3
while max_attempts>0:
    pin = int(input("Please enter your 4 digit pin: "))
    if pin == corr_pin:
        print("Login Successful")
        break
    else:
        max_attempts-=1
        if max_attempts==0:
            print("Card Blocked.")
# ******************************************************************************

# Task 3: Multiplication Tables (Beginner)
# Topics: for loop 
# Problem: Print multiplication table up to 10. 
# Example Input: 7 
# Expected Output: 
# 7 x 1 = 7 
# 7 x 2 = 14 
# ...
# 7 x 10 = 70

num = int(input("Enter a number: "))
for i in range(1,11):
    print(num,'x',i,'=',num*i)
# ******************************************************************************

# Task 4: Number Guess Validation (Beginner) 
# Topics: while, if 
# Problem: Keep asking until number is between 1 and 100.
# Example Input: 150, -5, 45 
# Expected Output: Invalid, Invalid, Valid Number

while True:
    num = int(input("Enter a number: "))
    if num >1 and num<100:
        print("Valid Number")
        break
    print("Invalid ")
# ******************************************************************************

# Task 5: Number Pattern (Beginner) 
# Topics: Nested for loops 
# Problem: Print pattern: 
# 1 
# 12 
# 123 
# 1234 
# 12345

for i in range(1,6):
    for j in range(1,i+1):
        print(j,end="")
    print()
# ******************************************************************************

# Task 6: Bus Seat Booking Display (Beginner) 
# Topics: Nested loops 
# Problem: Display seats: 
# R1C1 R1C2 R1C3 R1C4 R1C5 
# R2C1 R2C2 R2C3 R2C4 R2C5 
# R3C1 R3C2 R3C3 R3C4 R3C5 
# R4C1 R4C2 R4C3 R4C4 R4C5

for row in range(1,6):
    for col in range(1,6):
        print(f"R{row}C{col}", end=" ")
    print()
# ******************************************************************************

# Task 7: Restaurant Ordering System (Beginner) 
# Topics: while, if-elif, menu-driven programming 
# Menu: 1.Pizza 2.Burger 3.Sandwich 4.Exit 
# Keep ordering until Exit. Display Total Items Ordered = X. 
# Example Input: 1 2 2 3 4 
# Expected Output: Pizza Ordered, Burger Ordered, Burger Ordered, Sandwich Ordered, 
# Total Items Ordered = 4

total = 0
while True:
    order = int(input("Menu: 1.Pizza 2.Burger 3.Sandwich 4.Exit\n"))
    if order == 1:
        print("Pizza Ordered,")
    elif order ==2:
        print("Burger Ordered,")
    elif order ==3:
        print("Sandwich Ordered,")
    elif order ==4:
        break
    total+=1
print("Total Items Ordered =", total)
# ******************************************************************************

# Task 8: Cinema Seat Booking (Intermediate) 
# Topics: Nested loops, if, break, continue 
# Problem: Theatre has 5 rows and 6 seats. If seat already booked print Already Booked else Seat Booked Successfully. Continue until 5 seats booked. 
# Example: (2,4),(2,4),(3,5) 
# Output: Seat Booked Successfully, Already Booked, Seat Booked Successfully.

booked = []
count = 0
while count <= 5:
    row = int(input("Enter the row number: "))
    column = int(input("Enter the column number: "))
    seat = (row,column)
    if row < 1 or row > 5 or column < 1 or column > 6:
        print("Invalid seat number. Please try again.")
        continue
    if seat in booked :
        print("Already Booked")
        continue
    booked += [seat]
    print("Seat Booked Successfully")
    count+=1
#         ++++++++++++++++++++  OR  +++++++++++++++++++++++++++
available = []
count = 0
for i in range (1,6):
    for j in range (1,7):
        available += [(i,j)]
while count < 5:
    row = int(input("Enter the row number: "))
    seat = int(input("Enter the seat number: "))
    if row < 1 or row > 5 or seat < 1 or seat > 6:
        print("Invalid seat number. Please try again.")
        continue
    check = (row,seat)
    if check not in available:
        print("Already booked")
        continue
    available.remove(check)
    print("Seat Booked Successfully")
    count+=1
# ******************************************************************************

# Task 9: Employee Attendance Report (Intermediate) 
# Topics: Cross nested loops, if-else 
# Problem: 3 departments, 5 employees each. Attendance: 1=Present, 0=Absent. Display department-wise Present and Absent counts.

for dept in range(1,4):
    print("Department",dept)
    present = 0
    for emp in range(1,6):
        attendance = int(input(f"Employee {emp}:"))
        if attendance == 1:
            present +=1
    print()
    print("Present =",present)
    print("Absent =",5-present)
    print()
# ******************************************************************************

# Task 10: Bank Transaction Simulator (Intermediate - Interview Level) 
# Topics: while, nested loops, if-elif, cross nested loops, break, continue
#  Menu: Deposit, Withdraw, Balance, Mini Statement, Exit. 
# Rules: Login with PIN (3 attempts), continue until Exit, withdrawal cannot exceed balance, maintain transaction count, display total deposits and withdrawals. 
# Example Input: PIN1234, Deposit5000, Withdraw1200, Balance, Mini Statement, Exit. 
# Expected Output: Deposit Successful, Withdrawal Successful, Balance=3800, Transactions=2, Thank You.

count = 0
pin = 7197
max_attempt = 3
balance = 0
tot_dep = 0
tot_wthdrw = 0
while max_attempt >0:
    login = int(input(f"Enter your 4 digit pin. Only {max_attempt} attempts: "))
    if login == pin:
        print("Login Successful.")
        while True:
            print('\nMenu: 1.Deposit, 2.Withdraw, 3.Balance, 4.Mini Statement, 5.Exit.')
            do = int(input("Choose from 1-5: "))
            print()
            if do == 1:
                deposit = int(input("Enter the amount you want to Deposit: "))
                if deposit <0:
                    print("Invalid amount.")
                    continue
                balance += deposit
                tot_dep += deposit
                print(f"{deposit} rupees Deposited..")
                count +=1
            elif do == 2:
                withdraw = int(input("Enter the amount you want to Withdraw: "))
                if withdraw <0:
                    print("Invalid amount.")
                    continue
                elif withdraw < balance:
                    balance -= withdraw
                    tot_wthdrw += withdraw
                    print(f"{withdraw} rupees Withdrawn..")
                    count +=1
                else:
                    print(f"Insufficient Balance! Your Total Balance is = {balance}")
                    continue
            elif do == 3:
                print(f"The remaining Balance is rupees {balance}.")
            elif do == 4:
                print(f"\n*************************\nCurrent Balance: {balance}\nTotal Deposits: {tot_dep}\nTotal Withdrawals: {tot_wthdrw}\nTransactions: {count}\n*************************\n")
            elif do == 5:
                print("--THANK YOU--")
                print()
                break
            else:
                print("ERROR OCCURED!!! Please enter the correct number...")
            print()
        break
    else:
        max_attempt -=1
        if max_attempt == 0:
            print("Error! You have entered The Wrong Pin 3 times. Card Blocked")
            break