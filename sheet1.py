# Problem 1 
# Definition: Practice using Python operators in a real-world scenario. 
# Task: Read food bill and GST %. Calculate GST and final bill. 
# Example Input: (Sample values) 
# Example Output: (Expected result based on input)

food_bill=int(input("Enter bill for your food: "))
gst=int(input("Enter GST percentage: "))
print(f"Your total bill is: {food_bill + food_bill*(gst/100)} rupees only")
# ******************************************************************************

# Problem 2 
# Definition: Practice using Python operators in a real-world scenario. 
# Task: Read mobile price and discount %. Calculate discount and final price. 
# Example Input: (Sample values) 
# Example Output: (Expected result based on input)

mobile_price=int(input("Enter price of the mobile: "))
discount_perc=int(input("Enter discount percentage: "))
discount=mobile_price*(discount_perc/100)
print(f"Your total discount is: {discount} rupees only")
print(f"Your final price is: {mobile_price-discount} rupees only")
# ******************************************************************************

# Problem 3 
# Definition: Practice using Python operators in a real-world scenario. 
# Task: Read liters and price/liter. Find total cost. 
# Example Input: (Sample values) 
# Example Output: (Expected result based on input)

lit=int(input("Enter number of liters: "))
price_per_lit=int(input("Enter price per liter: "))
print(f"Total cost: {lit*price_per_lit}")
# ******************************************************************************

# Problem 4 
# Definition: Practice using Python operators in a real-world scenario. 
# Task: Read units and price/unit. Find bill. 
# Example Input: (Sample values) 
# Example Output: (Expected result based on input)

units=int(input("Enter number of units: "))
per_unit=int(input("Enter price per unit: "))
print(f"Final bill: {units*per_unit}")
# ******************************************************************************

# Problem 5 
# Definition: Practice using Python operators in a real-world scenario. 
# Task: Read runs and balls. Compute (runs*100)/balls. 
# Example Input: (Sample values) 
# Example Output: (Expected result based on input)

runs=int(input("Enter number of runs: "))
balls=int(input("Enter number of balls: "))
print(f"Strike rate: {(runs*100)/balls}")
# ******************************************************************************

# Problem 6 
# Definition: Practice using Python operators in a real-world scenario. 
# Task: Read marks. Check marks>=35. 
# Example Input: (Sample values) 
# Example Output: (Expected result based on input)

marks = int(input("Enter your marks: "))
print(marks>=35)
# ******************************************************************************

# Problem 7 
# Definition: Practice using Python operators in a real-world scenario. 
# Task: Read balance and withdrawal. Check balance>=withdrawal. 
# Example Input: (Sample values)
# Example Output: (Expected result based on input)

bal=int(input("Enter Balance:"))
withdrawl=int(input("Enter withdrawl amount:"))
print(bal>=withdrawl)
# ******************************************************************************

# Problem 8 
# Definition: Practice using Python operators in a real-world scenario. 
# Task: Read age. Check age>=18. 
# Example Input: (Sample values) 
# Example Output: (Expected result based on input)

age=int(input("Enter your age: "))
print(age>=18)
# ******************************************************************************

# Problem 9 
# Definition: Practice using Python operators in a real-world scenario. 
# Task: Read two passwords. Check equality. 
# Example Input: (Sample values) 
# Example Output: (Expected result based on input)

pass1=input("Enter a password: ")
pass2=input("Enter another password: ")
print(pass1==pass2)
# ******************************************************************************

# Problem 10 
# Definition: Practice using Python operators in a real-world scenario. 
# Task: Read order amount. Check >=500. 
# Example Input: (Sample values) 
# Example Output: (Expected result based on input)

amt=int(input("Enter order amount: "))
print(amt>=500)
# ******************************************************************************

# Problem 11 
# Definition: Practice using Python operators in a real-world scenario. 
# Task: Read age and fitness. Eligible if age>=18 and fit. 
# Example Input: (Sample values) 
# Example Output: (Expected result based on input)

age=int(input("Enter age: "))
fit=input("Enter fit or not")
if age>=18 and fit=="yes":
    print("Eligible")
else:
    print("Not Eligible")
# ******************************************************************************

# Problem 12 
# Definition: Practice using Python operators in a real-world scenario. 
# Task: Read percentage and income. Eligible if >=85 and income<300000. 
# Example Input: (Sample values) 
# Example Output: (Expected result based on input)

percentage=int(input("Enter percentage: "))
income=input("Enter income")
if percentage>=85 and income<300000:
    print("Eligible")
else:
    print("Not Eligible")
# ******************************************************************************

# Problem 13 
# Definition: Practice using Python operators in a real-world scenario. 
# Task: Read Saturday and Sunday flags. Weekend if either true. 
# Example Input: (Sample values) 
# Example Output: (Expected result based on input)

sat=int(input("Enter 0 or 1"))
sun=int(input("Enter 0 or 1"))
if sat==0 or sun==0:
    print("Weekend")
else:
    print("Weekday")
# ******************************************************************************

# Problem 14 
# Definition: Practice using Python operators in a real-world scenario.
# Task: Read degree status and age. Eligible if degree and age>=21. 
# Example Input: (Sample values) 
# Example Output: (Expected result based on input)

degree=int(input("Enter degree status: "))
age=int(input("Enter your age: "))
if degree=="yes" and age>=21:
    print("Eligible")
else:
    print("Not Eligible")
# ******************************************************************************

# Problem 15 
# Definition: Practice using Python operators in a real-world scenario. 
# Task: Read current and max level. Check full. 
# Example Input: (Sample values) 
# Example Output: (Expected result based on input)

curr=int(input("enter current level: "))
myax=int(input("enter max level: "))
if curr==myax:
    print("Full")
else:
    print("Not Full")
# ******************************************************************************

# Problem 16 
# Definition: Practice using Python operators in a real-world scenario. 
# Task: Read hours. Cost=40*hours. 
# Example Input: (Sample values) 
# Example Output: (Expected result based on input)

hrs=int(input("Enter number of hours: "))
print(f"Cost = {40*hrs}")
# ******************************************************************************

# Problem 17 
# Definition: Practice using Python operators in a real-world scenario. 
# Task: Read salary. Bonus if <50000. 
# Example Input: (Sample values) 
# Example Output: (Expected result based on input)

sal = int(input("Enter your sal: "))
bonus=int(input("Enter bonus amt: "))
if sal<50000:
    sal+=bonus
print(f"Total sal: {sal}")
# ******************************************************************************

# Problem 18 
# Definition: Practice using Python operators in a real-world scenario. 
# Task: Read loan and months. EMI=loan/months. 
# Example Input: (Sample values) 
# Example Output: (Expected result based on input)

loan=int(input("Enter loan amount: "))
months=int(input("Enter the number of months: "))
print(f"EMI: {loan/months}")
# ******************************************************************************

# Problem 19 
# Definition: Practice using Python operators in a real-world scenario. 
# Task: Read purchase. Cashback 5% if >2000. 
# Example Input: (Sample values) 
# Example Output: (Expected result based on input)

purchase=int(input("Enter the purchase amount: "))
cashback = purchase*0.05
if purchase>2000:
    purchase-=cashback
print(f"Your total amount = {purchase}")
# ******************************************************************************

# Problem 20 
# Definition: Practice using Python operators in a real-world scenario. 
# Task: Read weight and height. BMI=weight/(height*height). 
# Example Input: (Sample values) 
# Example Output: (Expected result based on input)

weight = int(input("Enter your weight: "))
height = int(input("Enter your height: "))
print(f"BMI = {weight/(height*height)}")
# ******************************************************************************

# Problem 21 
# Definition: Practice using Python operators in a real-world scenario. 
# Task: Assign same value to two vars. Check using is. 
# Example Input: (Sample values) 
# Example Output: (Expected result based on input)

a=1
b=1
print(a is b)
# ******************************************************************************

# Problem 22 
# Definition: Practice using Python operators in a real-world scenario. 
# Task: Check coupon in list using in. 
# Example Input: (Sample values) 
# Example Output: (Expected result based on input)

l=[1,2,3,4,5,6,7,8,9]
coup=int(input("Enter a number: "))
print(coup in l)
# ******************************************************************************

# Problem 23 
# Definition: Practice using Python operators in a real-world scenario. 
# Task: Check department in tuple. 
# Example Input: (Sample values) 
# Example Output: (Expected result based on input)

tup=("cse","ece","eee","mech","civil")
dept = input("Enter your dept: ")
print(dept in tup)
# ******************************************************************************

# Problem 24 
# Definition: Practice using Python operators in a real-world scenario. 
# Task: Use & to identify even/odd. 
# Example Input: (Sample values) 
# Example Output: (Expected result based on input)

num=int(input("Enter a number: "))
if num&1:
    print("Odd")
else:
    print("Even")
# ******************************************************************************

# Problem 25 
# Definition: Practice using Python operators in a real-world scenario. 
# Task: Use << to double. 
# Example Input: (Sample values) 
# Example Output: (Expected result based on input)

num = int(input("Enter a number: "))
print(num << 1)
# ******************************************************************************

# Problem 26 
# Definition: Practice using Python operators in a real-world scenario. 
# Task: Use >> to halve. 
# Example Input: (Sample values) 
# Example Output: (Expected result based on input)

num = int(input("Enter a number: "))
print(num >> 1)
# ******************************************************************************

# Problem 27 
# Definition: Practice using Python operators in a real-world scenario. 
# Task: Use & on two permissions. 
# Example Input: (Sample values)
# Example Output: (Expected result based on input)

perm1=int(input("Emter a permission"))
perm2=int(input("Emter a permission"))
print(perm1&perm2)
# ******************************************************************************

# Problem 28 
# Definition: Practice using Python operators in a real-world scenario. 
# Task: Alarm if door or motion. 
# Example Input: (Sample values) 
# Example Output: (Expected result based on input)

door = int(input("Open or not: "))
motion = int(input("Moving or not: "))
if door or motion:
    print("Alarm")
else:
    print("No Alarm")
# ******************************************************************************

# Problem 29 
# Definition: Practice using Python operators in a real-world scenario. 
# Task: Eligible if attendance>=75 or project complete. 
# Example Input: (Sample values) 
# Example Output: (Expected result based on input)

att=int(input("Enter attendance percentage: "))
project=int(input("Is your project complete: "))
if att or project:
    print("Eligible")
else:
    print("Not Eligible")
# ******************************************************************************

# Problem 30 
# Definition: Practice using Python operators in a real-world scenario. 
# Task: Board if passport,ticket,visa all true. 
# Example Input: (Sample values) 
# Example Output: (Expected result based on input)

passport=int(input("Is passport available: "))
ticket=int(input("Is ticket available: "))
visa=int(input("Is visa available: "))

if passport and visa and ticket:
    print("Board")
else:
    print("Do not Board")