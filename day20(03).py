# 1. Find the Largest of N Numbers Problem 
# Definition: Find the greatest value from a sequence of numbers. 
# Task: Read N, then read N numbers one by one and print the largest. 
# Example Input: N=5 
# 12 
# 45 
# 8 
# 90 
# 34 
# Example Output: Largest = 90

n = int(input("How many numbers?: "))
i=0
largest=0
while i<n:
    num=int(input("Enter a number: "))
    if num>largest:
        largest = num
    i+=1
print(f"Largest = {largest}")
# ******************************************************************************

# 2. Find the Smallest of N Numbers Problem 
# Definition: Find the smallest value from a sequence of numbers. 
# Task: Read N numbers and print the smallest. 
# Example Input: N=5 
# 18
# 3 
# 45 
# 7 
# 12 
# Example Output: Smallest = 3

n = int(input("How many numbers?: "))
i=1
num=int(input("Enter a number: "))
smallest=num
while i<n:
    num=int(input("Enter a number: "))
    if num<smallest:
        smallest = num
    i+=1
print(f"Smallest = {smallest}")
# ******************************************************************************

# 3. Find the Second Largest Number Problem 
# Definition: Find the second highest value without sorting. 
# Task: Read N numbers and print the second largest. 
# Example Input: N=5 
# 25 
# 60 
# 15 
# 80 
# 50 
# Example Output: Second Largest = 60

n=int(input("Enter max numbers: "))
lar=0
sec_lar=0
i=0
while i<n:
    num=int(input("Enter a number: "))
    if num>lar:
        sec_lar=lar
        lar=num
    elif num>sec_lar and num<lar:
        sec_lar=num
    i+=1
print(f"Second Largest = {sec_lar}")
# ******************************************************************************

# 4. Find the Second Smallest Number 
# Problem Definition: Find the second lowest value without sorting.
# Task: Read N numbers and print the second smallest. 
# Example Input: 
# N=5 
# 25 
# 60 
# 15 
# 80 
# 50 
# Example Output: 
# Second Smallest = 25

n=int(input("Max number: "))
num=int(input("Enter a number: "))
smallest=num
sec_smallest=num
i=1
while i<n:
    num=int(input("Enter a number: "))
    if num<smallest:
        sec_smallest = smallest
        smallest = num
    elif num>smallest and num<sec_smallest:
        sec_smallest=num
    i+=1
print(f"Second Smallest = {sec_smallest}")
# ******************************************************************************

# 5. Count Positive, Negative and Zero Values 
# Problem Definition: Classify numbers based on their sign. 
# Task: Read N numbers and count positives, negatives and zeros. 
# Example Input: 
# N=6 
# 10
# -5 
# 0 
# 18
# -2 
# 0 
# Example Output: 
# Positive = 2 
# Negative = 2 
# Zero = 2

n=int(input("Max numbers: "))
pos=0
neg=0
zer=0
i=0
while i<n:
    num=int(input("Enter a number"))
    if num>0:
        pos += 1
    elif num==0:
        zer += 1
    else:
        neg += 1
    i+=1
print(f"Positive = {pos}")
print(f"Negative = {neg}")
print(f"Zero = {zer}")
# ******************************************************************************

# 6. Find the Missing Number 
# Problem Definition: One number from 1 to N is missing. 
# Task: Read N and the remaining numbers, then find the missing number. 
# Example Input: 
# N=6 
# 1 
# 2 
# 3 
# 5 
# 6 
# Example Output: 
# Missing Number = 4

n=int(input("Max number: "))
i=1
tot = 0
while i<=n:
    tot += i
    i+=1
giv_tot = 0
j=1
while j<n:
    num = int(input("Enter a number: "))
    giv_tot+=num
    j+=1
print(tot-giv_tot)
# ******************************************************************************

# 7. Check Whether a Number is Perfect 
# Problem Definition: A perfect number equals the sum of its proper factors. 
# Task: Determine whether the given number is perfect. 
# Example Input: 28
# Example Output: Perfect Number

num = int(input("Enter a number: "))
i=1
sum=0
while i<num:
    if num%i==0:
        sum +=i
    i+=1
if sum == num:
    print("Perfect Number")
else:
    print("Not a Perfect Number")
# ******************************************************************************

# 8. Find the GCD of Two Numbers 
# Problem Definition: The GCD is the greatest number that divides both numbers. 
# Task: Find the GCD using loops. 
# Example Input: 
# 24 
# 36 
# Example Output: 
# GCD = 12

num1=int(input("Enter first num: "))
num2=int(input("Enter first num: "))
i=1
gcd=0
if num1<num2:
    while i<num1:
        if num1%i==0 and num2%i==0:
            gcd = i
        i+=1
else:
    while i<num2:
        if num1%i==0 and num2%i==0:
            gcd = i
        i+=1
print(f"GCD = {gcd}")
# ******************************************************************************

# 9. Find the LCM of Two Numbers 
# Problem Definition: The LCM is the smallest number divisible by both numbers. 
# Task: Find the LCM using loops. 
# Example Input: 
# 12 
# 18 
# Example Output: 
# LCM = 36

n1=int(input("Enter first number: "))
n2=int(input("Enter second number: "))
lcm=0
if n1>n2:
    i=n1
    while i<=n1*n2:
        if i%n1==0 and i%n2==0:
            lcm = i
            break
        i+=1
else:
    i=n2
    while i<=n1*n2:
        if i%n1==0 and i%n2==0:
            lcm = i
            break
        i+=1
print(f"LCM =",lcm)
# ******************************************************************************

# 10. Power Without Using ** 
# Problem Definition: Calculate a power using repeated multiplication. 
# Task: Read the base and exponent, then compute the result using a loop. 
# Example Input: 
# Base = 3 
# Exponent = 4 
# Example Output:
# 81

base = int(input("Base = "))
exp = int(input("Exponext = "))
pow=1
i=1
while i<=exp:
    pow *= base
    i+=1
print(pow)