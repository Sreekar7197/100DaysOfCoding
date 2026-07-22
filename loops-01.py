# 1. Count Passing Students 
# Task: Read marks of N students. Count how many scored 35 or more. 
# Example Input: 
# 5 
# 45 
# 20 
# 67 
# 35 
# 18 
# Example Output: 
# 3

n=int(input("Enter no. of students: "))
count=0
while n>0:
    marks = int(input("Enter marks: "))
    if marks>=35:
        count +=1
    n-=1
print(count)
# ******************************************************************************

# 2. Shop Profit Days 
# Task: Read profit for N days. Count days with profit greater than Rs.1000. 
# Example Input: 
# 5 
# 800 
# 1200 
# 1500 
# 950 
# 2000 
# Example Output: 
# 3

n=int(input("Enter number of days: "))
count =0
while n>0:
    profit = int(input("Enter profit for the day: "))
    if profit>1000:
        count +=1
    n-=1
print(count)
# ******************************************************************************

# 3. Largest Multiple of 5 
# Task: Read N numbers. Print the largest divisible by 5, else 'No Multiple of 5'. 
# Example Input: 
# 5 
# 12 
# 25 
# 18 
# 40 
# 7 
# Example Output: 
# 40

n=int(input("Max numbers: "))
lar = 0
while n>0:
    num = int(input("Enter a number: "))
    if num%5==0 and num>lar:
        lar = num
    n-=1
print(lar)
# ******************************************************************************

# 4. Average of Even Numbers 
# Task: Read N numbers. Print average of even numbers, else 'No Even Numbers'. 
# Example Input: 
# 5 
# 2 
# 5 
# 8 
# 7 
# 10 
# Example Output: 
# Average = 6.67

n=int(input("Enter max numbers: "))
count = 0
tot = 0
while n>0:
    num = int(input("Enter a number: "))
    if num%2==0:
        count +=1
        tot +=num
    n-=1
print(f"Average = {(tot/count):.2f}")
# ******************************************************************************

# 5. Student Improvement 
# Task: Read marks in N tests. Count how many times marks increased. 
# Example Input: 
# 5 
# 50
# 55 
# 52 
# 60 
# 70 
# Example Output: 
# 3

n=int(input("Enter total no. of tests: "))
count = 0
prev_marks = 0
while n>0:
    marks= int(input("Enter marks: "))
    if marks > prev_marks:
        count +=1
    prev_marks = marks
    n-=1
print(count-1)
# ******************************************************************************

# 6. Divisors Count 
# Task: Read a number and count its divisors.
# Example Input: 
# 12 
# Example Output:
# 6

n= int(input("Enter a number: "))
i=1
count = 0
while i<=n:
    if n%i==0:
        count +=1
    i+=1
print(count)
# ******************************************************************************

# 7. Smallest Odd Number 
# Task: Read N numbers. Print smallest odd number or 'No Odd Number'. 
# Example Input: 
# 5 
# 8 
# 13 
# 6 
# 5 
# 10 
# Example Output: 
# 5

n = int(input("Enter max number: "))
num = int(input("Enter a number"))
small = num
while n>1:
    if num<small and num%2==1:
        small = num
    num = int(input("Enter a number: "))
    n-=1
print(small)
# ******************************************************************************

# 8. Count Numbers Ending with 7 
# Task: Read N numbers. Count numbers ending with digit 7. 
# Example Input: 
# 5 
# 27 
# 15 
# 97 
# 120 
# 47 
# Example Output: 
# 3

n=int(input("Enter max numbers: "))
count = 0
while n>0:
    num = int(input("Enter a number: "))
    if num%10==7:
        count +=1
    n-=1
print(count)
# ******************************************************************************

# 9. Multiplication Table 
# Task: Read a number and print table from 1 to 15. 
# Example Input: 
# 7
# Example Output: 
# 7 x 1 = 7 ... 7 x 15 = 105

num = int(input("Enter a number: "))
i=1
while i<=15:
    print(f"{num} x {i} = {num*i}")
    i+=1
# ******************************************************************************

# 10. Sum Until Negative Number 
# Task: Read numbers until a negative number is entered. Print sum of positive numbers. 
# Example Input: 
# 5 
# 10 
# 8 
# 2
# -1 
# Example Output: 
# 25

tot=0
while True:
    num = int(input("Enter a number: "))
    if num <0:
        print(tot)
        break
    tot +=num