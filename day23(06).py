# 1. Count Numbers Whose Last Digit is Greater Than First Digit Problem 
# Definition: Every number has a first digit and a last digit. Compare them. 
# Task: Read N numbers. Count how many have the last digit greater than the first digit. 
# Example Input: 
# 5 
# 123 
# 482 
# 91 
# 3456 
# 78 
# Example Output: 
# 2

num = int(input("Enter max numbers: "))
i=0
count = 0
while i<num:
    n=int(input("Enter a number: "))
    a=n%10
    while n>10:
        n//=10
    if a>n:
        count +=1
    i+=1
print(count)
# ******************************************************************************

# 2. Print Common Factors of Two Numbers 
# Problem Definition: A common factor divides both numbers exactly. 
# Task: Read two numbers and print all their common factors. 
# Example Input: 
# 24 
# 36 
# Example Output: 
# 1 
# 2 
# 3 
# 4 
# 6 
# 12

num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))
i=1
if num1>num2:
    while i<num2:
        if num1%i==0 and num2%i==0:
            print(i)
        i+=1
if num2>num1:
    while i<num1:
        if num1%i==0 and num2%i==0:
            print(i)
        i+=1
# ******************************************************************************

# 3. Count Numbers Having Exactly Three Digits 
# Problem Definition: A three-digit number lies between 100 and 999. 
# Task: Read N numbers and count how many are exactly three digits. 
# Example Input: 
# 5 
# 23 
# 456 
# 890 
# 1000 
# 145 
# Example Output: 
# 3

n= int(input("Enter max numbers: "))
count = 0
while n>0:
    num = int(input("Enter a number: "))
    if num>=100 and num <=999:
        count +=1
    n-=1
print(count)
# ******************************************************************************

# 4. Print Numbers Whose Digit Sum is Even
# Problem Definition: The sum of the digits can be used as a condition. 
# Task: Read N. Print all numbers from 1 to N whose digit sum is even. 
# Example Input: 
# 15 
# Example Output: 
# 2 
# 4 
# 6
# 8 
# 11 
# 13 
# 15

n= int(input("Enter a number: "))
i=1
while i<=n:
    dig_sum = 0
    r=i
    while r>0:
        dig_sum+=r%10
        r//=10
    if dig_sum %2 == 0:
        print(i)
    i+=1
# ******************************************************************************

# 5. Count Factors That Are Even 
# Problem Definition: Not every factor is even. 
# Task: Read a number and count how many of its factors are even. 
# Example Input: 
# 24 
# Example Output: 
# 6

n=int(input("Enter a number: "))
i=1
count = 0
while i<=n:
    if n%i==0 and i%2==0:
        count +=1
    i+=1
print(count)
# ******************************************************************************

# 6. Reverse Only Even Numbers 
# Problem Definition: Different inputs may require different processing. 
# Task: Read N numbers. Reverse only even numbers and print odd numbers unchanged. 
# Example Input: 
# 4 
# 123 
# 246 
# 789 
# 820 
# Example Output: 
# 123 
# 642 
# 789 
# 28

n= int(input("Enter max numbers: "))
while n>0:
    num = int(input("Enter a number: "))
    if num %2==0:
        rev=0
        while num >0:
            r = num %10
            rev = rev*10+r
            num //=10
        num = rev
    print(num)
    n-=1
# ******************************************************************************

# 7. Find the Smallest Multiple of 7 Greater Than N 
# Problem Definition: Search until the required condition is met. 
# Task: Read N and print the smallest multiple of 7 greater than N. 
# Example Input: 
# 50 
# Example Output: 
# 56

n= int(input("Enter a number: "))
a=n+1
while True:
    if a%7==0:
        print(a)
        break
    a+=1
# ******************************************************************************

# 8. Count Numbers Having Equal Even and Odd Digits 
# Problem Definition: Compare the number of even and odd digits. 
# Task: Read N numbers and count how many have equal even and odd digits. 
# Example Input: 
# 4
# 1234 
# 2468 
# 1357 
# 4521 
# Example Output: 
# 2

n = int(input("Enter max numbers: "))
count = 0
while n>0:
    num = int(input("Enter a number: "))
    even = 0
    odd = 0
    while num>0:
        if (num%10)%2==0:
            even +=1
        else:
            odd +=1
        num //=10
    if even == odd:
        count +=1
    n-=1
print(count)
# ******************************************************************************

# 9. Print Factors Between 5 and 20 
# Problem Definition: Filter factors within a range. 
# Task: Read a number and print only the factors between 5 and 20. 
# Example Input: 
# 120 
# Example Output: 
# 5 
# 6 
# 8 
# 10 
# 12 
# 15 
# 20

n = int(input("Enter a number: "))
i=5
while i<=20:
    if n%i==0:
        print(i)
    i+=1
# ******************************************************************************

# 10. Read Numbers Until Their Sum Exceeds 100 
# Problem Definition: A loop can stop based on the running total. 
# Task: Keep reading numbers until the sum exceeds 100. Print the final sum. 
# Example Input: 
# 20 
# 35 
# 18 
# 40 
# Example Output: 
# 113

sum=0
while True:
    if sum >100:
        print(sum)
        break
    n=int(input("Enter a number: "))
    sum +=n
