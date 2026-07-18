# 1. Count Even and Odd Numbers from 1 to N 
# Problem Definition: A program can classify numbers as even or odd. 
# Task: Read N. Count even and odd numbers from 1 to N. 
# Example Input: 10 
# Example Output: 
# Even Numbers = 5 
# Odd Numbers = 5

n=int(input("Enter a number: "))
i=1
even = 0
odd = 0
while i<=n:
    if i%2==0:
        even+=1
    else:
        odd+=1
    i+=1
print(f"Even Numbers = {even}")
print(f"Odd Numbers = {odd}")
# ******************************************************************************

# 2. Sum of Numbers Divisible by 3 
# Problem Definition: Process only numbers that satisfy a condition. 
# Task: Read N. Find the sum of numbers divisible by 3. 
# Example Input: 10 
# Example Output: 18

n=int(input("Enter a number: "))
i=0
tot=0
while i<=10:
    if i%3==0:
        tot+=i
    i+=1
print(tot)
# ******************************************************************************

# 3. Print Leap Years in a Range 
# Problem Definition: Leap years follow specific rules. 
# Task: Read start year and end year. Print all leap years. 
# Example Input: 
# 2000 
# 2020
# Example Output: 
# 2000 
# 2004 
# 2008 
# 2012 
# 2016 
# 2020

start = int(input("Enter start year: "))
last = int(input("Enter end year: "))
while start<=last:
    if start%4==0 and start%100!=0 or start%400==0:
        print(start)
    start +=1
# ******************************************************************************

# 4. Count Multiples of 5 and 7 
# Problem Definition: Numbers may satisfy multiple divisibility rules. 
# Task: Read N. Count multiples of 5, 7 and both. 
# Example Input: 50 
# Example Output: 
# 5=10 
# 7=7 
# Both=1

n=int(input("Enter a number: "))
mul_5=0
mul_7=0
both=0
i=1
while i<=n:
    if i%5==0 and i%7==0:
        both +=1
    if i%5==0:
        mul_5+=1
    if i%7==0:
        mul_7+=1
    i+=1
print(f"5={mul_5}")
print(f"7={mul_7}")
print(f"Both={both}")
# ******************************************************************************

# 5. Print All Factors and Their Count 
# Problem Definition: Factors divide a number exactly. 
# Task: Print all factors and total count. 
# Example Input: 12 
# Example Output: 
# 1 2 3 4 6 12 
# Total Factors = 6

n=int(input("Enter a number: "))
i=1
count = 0
while i<=n:
    if n%i==0:
        print(i)
        count+=1
    i+=1
print(f"Total Factors = {count}")
# ******************************************************************************

# 6. Largest Digit 
# Problem Definition: Find the greatest digit. 
# Task: Read a number and print the largest digit. 
# Example Input: 
# 583920 
# Example Output: 
# Largest Digit = 9

num = int(input("Enter a number: "))
lar = 0
while num>0:
    r = num%10
    if r>lar:
        lar = r
    num//=10
print(f"Largest Digit = {lar}")
# ******************************************************************************

# 7. Smallest Digit 
# Problem Definition: Find the smallest digit. 
# Task: Read a number and print the smallest digit. 
# Example Input: 
# 583920 
# Example Output: 
# Smallest Digit = 0

num = int(input("Enter a number: "))
small=num%10
while num>0:
    r = num%10
    if r<small:
        small=r
    num//=10
print(f"Smallest Digit = {small}")
# ******************************************************************************

# 8. Count Digits Greater Than 5 
# Problem Definition: Count digits meeting a condition. 
# Task: Read a number and count digits > 5. 
# Example Input: 
# 589762 
# Example Output: 
# 4

n=int(input("Enter a number: "))
count = 0
while n>0:
    r=n%10
    if r>5:
        count+=1
    n//=10
print(count)
# ******************************************************************************

# 9. Sum Only Even Digits 
# Problem Definition: Add only even digits. 
# Task: Read a number and print the sum of even digits. 
# Example Input: 
# 58294 
# Example Output: 
# 14

num = int(input("Enter a number: "))
tot = 0
while num>0:
    r=num%10
    if r%2==0:
        tot +=r
    num//=10
print(tot)
# ******************************************************************************

# 10. Divisible by 3 but Not 5 
# Problem Definition: Filter numbers using two conditions. 
# Task: Read N and print numbers divisible by 3 but not 5. 
# Example Input: 
# 30 
# Example Output: 
# 3 6 9 12 18 21 24 27

num = int(input("Enter a number: "))
i=1
while i<=num:
    if i%3==0 and i%5!=0:
        print(i)
    i+=1