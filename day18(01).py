# 1. Swap Two Numbers Without Third Variable 
# Definition: Exchange values of two variables without using an extra variable. 
# Task: Swap using arithmetic operators and bitwise XOR. 
# Example Input: A=15, B=25 
# Example Output: A=25, B=15
a= int(input("A="))
b= int(input("B="))
a=a^b
b=a^b
a=a^b
print(f"A={a}")
print(f"B={b}")

# ******************************************************************************

# 2. Convert Seconds Into Hours, Minutes and Seconds
# Definition: Convert total seconds into time units. 
# Task: Find hours, minutes and remaining seconds. 
# Example Input: Total seconds=7384 
# Example Output: Hours=2, Minutes=3, Seconds=4 

sec = int(input("Total seconds = "))
if sec>=3600:
    h = sec//3600
    sec%=3600
else:
    h=0
if sec>=60:
    m=sec//60
    sec%=60
else:
    m=0
print(f"Hours = {h}")
print(f"Minutes = {m}")
print(f"Seconds = {sec}")
# ******************************************************************************

# 3. Temperature Conversion System 
# Definition: Convert temperature values between Celsius and Fahrenheit. 
# Task: Convert Celsius to Fahrenheit and Fahrenheit to Celsius. 
# Example Input: Celsius=30 
# Example Output: Fahrenheit=86

temp = int(input("Enter the temperature: "))
deg = input("c or f: ")
if deg == 'c' or "C":
    f= temp*(9/5)+32
    print(f"Farenheit = {f}")
elif deg == 'f' or "F":
    c = (temp-32)*(5/9)
    print(f"Celcius = {c}")
# ******************************************************************************

# 4. Calculate Compound Amount 
# Definition: Compound interest calculates interest on both the original amount and previously earned interest. 
# Task: Calculate final amount using the compound interest formula. 
# Formula: Amount = P × (1 + R/100)^T Where: P = Principal amount R = Rate of interest T = Time period 
# Example Input: 
# Principal = 10000 
# Rate = 10 
# Time = 2 years 
# Example Output: Final Amount = 12100

p = int(input("Principal = "))
r = int(input("Rate = "))
t = int(input("Time = "))
amount = p*(1+r/100)**t
print(f"Final Amount = {amount:.0f}")
# ******************************************************************************

# 5. Split Bill Among Friends 
# Definition: Divide a total bill equally among people. 
# Task: Find each person's share and remaining amount.
# Example Input: Bill=2455, Friends=5 
# Example Output: Each pays=491, Remaining=0

bill = int(input(f"Bill="))
frnds = int(input("Friends="))
per_person = bill//frnds
rem = bill%frnds
print(f"Each Pays={per_person}")
print(f"Remaining={rem}")
# ******************************************************************************

# 6. Convert Distance Units 
# Definition: Convert kilometers into smaller units. 
# Task: Convert km into meters, centimeters and millimeters. 
# Example Input: Distance=5 km 
# Example Output: 
# Meters=5000, 
# Centimeters=500000, 
# Millimeters=5000000

km = int(input("Distance in km = "))
m=km*1000
cm = m*100
mm = cm*10
print(f"Meters={m}")
print(f"Centieters={cm}")
print(f"Millimeters={mm}")
# ******************************************************************************

# 7. Digital Storage Conversion 
# Definition: Convert storage units from GB to smaller units. 
# Task: Convert GB into MB, KB and Bytes. 
# Example Input: Storage=2 GB 
# Example Output: MB=2048, KB=2097152, Bytes=2147483648

gb = int(input("Storage in GB = "))
mb=gb*1024
kb=mb*1024
byte = kb *1024
print(f"MB={mb}")
print(f"KB={kb}")
print(f"Bytes={byte}")
# ******************************************************************************

# 8. Minimum Currency Notes 
# Definition: Find the number of currency notes required for an amount. 
# Task: Use 500, 200, 100 and 50 denomination notes. 
# Example Input: Amount=1850 
# Example Output: 500 notes=3, 200 notes=1, 100 notes=1, 50 notes=1

amt = int(input("Amount="))
fivehun=0
twohun=0
hun=0
fifty = 0
if amt>=500:
    fivehun=amt//500
    amt%=500
if amt>=200:
    twohun=amt//200
    amt%=200
if amt>=100:
    hun=amt//100
    amt%=100
fifty = amt//50
print(f"500 notes = {fivehun}")
print(f"200 notes = {twohun}")
print(f"100 notes = {hun}")
print(f"500 notes = {fifty}")
# ******************************************************************************

# 9. Salary Calculation System 
# Definition: Calculate final salary after adding bonus and deducting tax. 
# Task: Calculate the final salary. 
# Example Input: Salary=40000, Bonus=5000, Tax=10% 
# Example Output: Final Salary=40500

sal = int(input("Salary="))
bonus = int(input("Bonus="))
tax = int(input("Tax="))
bon_sal = sal+bonus
final_sal = bon_sal-(bon_sal*0.1)
print(f"Final Salary={final_sal}")
# ******************************************************************************

# 10. Travel Time Calculator 
# Definition: Calculate travel duration using distance and speed. 
# Task: Find time for two journeys and total time. 
# Formula: Time = Distance / Speed 
# Example Input: Distance1=120, Speed1=60, Distance2=100, Speed2=50 
# Example Output: Journey1=2 hours, Journey2=2 hours, Total=4 hours

d1=int(input("Distance1 = "))
s1=int(input("Speed1 = "))
d2=int(input("Distance2 = "))
s2=int(input("Speed2 = "))
j1 = d1/s1
j2 = d2/s2
print(f"Journey1={j1} hours")
print(f"Journey2={j2} hours")
print(f"Total = {j1+j2} hours")