# 1. Print Numbers Divisible by Both 3 and 5 
# Problem Definition: Some numbers satisfy multiple conditions at the same time. 
# Task: Read N and print all numbers from 1 to N divisible by both 3 and 5. 
# Example Input: 50 
# Example Output: 
# 15 
# 30 
# 45

n=int(input("Enter a number: "))
i=1
while i<=n:
    if i%3==0 and i%5==0:
        print(i)
    i+=1
# ******************************************************************************

# 2. Count Numbers Ending with 5 
# Problem Definition: The last digit helps identify patterns. 
# Task: Read N and count numbers from 1 to N ending with 5. 
# Example Input: 
# 35 
# Example Output: 
# 4

n=int(input("Enter a number: "))
i=1
count = 0
while i<=n:
    r=i%10
    if r==5:
        count+=1
    i+=1
print(count)
# ******************************************************************************

# 3. Sum Numbers Whose Last Digit is Even 
# Problem Definition: Check only the last digit before adding. 
# Task: Read N and find the sum of numbers whose last digit is even. 
# Example Input: 
# 10 
# Example Output: 
# 30

n=int(input("Enter a numnber: "))
tot=0
i=0
while i<=n:
    r=i%10
    if r%2==0:
        tot +=i
    i+=1
print(tot)
# ******************************************************************************

# 4. Print Numbers Whose Square is Less Than N 
# Problem Definition: Print numbers only if their square is less than N. 
# Task: Read N and print such numbers. 
# Example Input: 
# 30 
# Example Output: 
# 1 
# 2 
# 3 
# 4 
# 5

num = int(input("Enter a number: "))
i=1
while i<=num:
    if i**2 <num:
        print(i)
    i+=1
# ******************************************************************************

# 5. Count Numbers Divisible by 4 but Not by 6
# Problem Definition: Combine two divisibility conditions. 
# Task: Read N and count numbers divisible by 4 but not 6. 
# Example Input: 
# 30 
# Example Output: 
# 6

n = int(input("Enter a number: "))
count = 0
i=1
while i<=n:
    if i%4==0 and i%6!=0:
        count +=1
    i+=1
print(count)
# ******************************************************************************

# 6. Reverse Every Alternate Number 
# Problem Definition: Process alternate inputs differently. 
# Task: Read N numbers. Reverse only the 2nd, 4th, 6th... numbers. 
# Example Input: 
# 4 
# 123 
# 456 
# 789 
# 654 
# Example Output: 
# 123 
# 654 
# 789 
# 456

n=int(input("Enter max numbers: "))
count = 0
while count<n:
    num=int(input("Enter a number: "))
    count+=1
    if count %2==0:
        rev=0
        while num>0:
            r=num%10
            rev=rev*10+r
            num//=10
        print(rev)
    else:
        print(num)
# ******************************************************************************

# 7. First Number Divisible by Both 7 and 9 
# Problem Definition: Stop when the required number is found. 
# Task: Read N and print the first number greater than N divisible by both 7 and 9. 
# Example Input: 
# 50 
# Example Output: 
# 63

num = int(input("Enter a number: "))
while True:
    num+=1
    if num%7==0 and num%9==0:
        print(num)
        break
# ******************************************************************************

# 8. Count Numbers Having More Even Digits Than Odd Digits 
# Problem Definition: Compare even and odd digits in each number. 
# Task: Read N numbers and count such numbers. 
# Example Input: 
# 3 
# 2481 
# 1357 
# 8246 
# Example Output:
# 2

n = int(input("Enter max number: "))
i = 0
count = 0
while i<n:
    num = int(input("Enter a number: "))
    even = 0
    odd = 0
    while num>0:
        r=num%10
        if r%2==0:
            even +=1
        else:
            odd +=1
        num//=10
    if even>odd:
        count +=1
    i+=1
print(count)
# ******************************************************************************

# 9. Print Factors Greater Than 5 
# Problem Definition: Filter factors using a condition.
# Task: Read a number and print only factors greater than 5. 
# Example Input: 
# 60 
# Example Output: 
# 6 
# 10 
# 12 
# 15 
# 20 
# 30 
# 60

num = int(input("Enter a number: "))
i=1
while i<=num:
    if i>5 and num%i==0:
        print(i)
    i+=1
# ******************************************************************************

# 10. Sum Until a Negative Number Appears 
# Problem Definition: Use a negative number as the stopping condition. 
# Task: Read numbers until a negative appears and print the sum. 
# Example Input: 
# 10 
# 20 
# 15 
# 8
#-1 
# Example Output: 
# 53

tot = 0
while True:
    n=int(input("Enter a number: "))
    if n==-1:
        break
    tot+=n
print(tot)