# 1. Count Numbers Divisible by the Sum of Their Digits 
# Problem Definition: Some numbers are divisible by the sum of their own digits. 
# Task: Read N. Count how many numbers from 1 to N are divisible by the sum of their digits. 
# Example Input: 20 
# Example Output: 13

n = int(input("Enter maximum number: "))
i=1
count = 0
while i<=n:
    r=i
    sum=0
    while r>0:
        sum += r%10
        r//=10
    if i%sum == 0:
        count +=1
    i+=1
print(count)
# ******************************************************************************

# 2. Print Numbers Whose First and Last Digits Are the Same 
# Problem Definition: A number may begin and end with the same digit. 
# Task: Read N. Print all numbers from 1 to N whose first and last digits are the same. 
# Example Input: 25 
# Example Output: 
# 1 
# 2 
# 3 
# 4 
# 5 
# 6 
# 7 
# 8 
# 9 
# 11 
# 22

n=int(input("Enter max number: "))
i=1
while i<=n:
    j=i
    r=i%10
    while j>10:
        j//=10
    if r==j:
        print(i)
    i+=1
# ******************************************************************************

# 3. Count Numbers Having More Factors Than 4 
# Problem Definition: Some numbers have many factors. Task: Read N. Count how many numbers from 1 to N have more than 4 factors. 
# Example Input: 
# 15 
# Example Output: 
# 5

n=int(input("Enter a number: "))
i=1
tot=0
while i<=n:
    count = 0
    j=1
    while j<=i:
        if i%j==0:
            count +=1
        j+=1
    if count>4:
        tot +=1
    i+=1
print(tot)
# ******************************************************************************

# 4. Print Numbers Whose Product of Digits is Even 
# Problem Definition: The product of a number's digits can classify it. 
# Task: Read N. Print all numbers from 1 to N whose product of digits is even. 
# Example Input: 
# 15
# Example Output: 
# 2 
# 4 
# 6 
# 8 
# 12 
# 14 
# 15

n=int(input("Enter max number: "))
i=1
while i<=n:
    j=i
    prod = 1
    while j>0:
        prod = prod*(j%10)
        j//=10
    if prod%2==0:
        print(i)
    i+=1
# ******************************************************************************

# 5. Count Numbers Ending with an Even Digit 
# Problem Definition: The last digit determines whether a number ends evenly. 
# Task: Read N. Count how many numbers from 1 to N end with an even digit. 
# Example Input: 
# 20 
# Example Output: 
# 10

n=int(input("Enter max number: "))
i=1
count = 0
while i<=n:
    r=i%10
    if r%2==0:
        count+=1
    i+=1
print(count)
# ******************************************************************************

# 6. Find the Greatest Common Factor of Three Numbers 
# Problem Definition: A common factor can exist among three numbers. 
# Task: Read three numbers and print their greatest common factor. 
# Example Input: 
# 24 
# 36 
# 60 
# Example Output: 
# 12

n1=int(input("Enter n1: "))
n2=int(input("Enter n2: "))
n3=int(input("Enter n3: "))
gcf=0
i=1
if n1<n2 and n1<n3:
    while i<=n1:
        if n1%i==0 and n2%i==0 and n3%i==0:
            gcf=i
        i+=1
elif n2<n1:
    while i<=n2:
        if n1%i==0 and n2%i==0 and n3%i==0:
            gcf=i
        i+=1
else:
    while i<=n3:
        if n1%i==0 and n2%i==0 and n3%i==0:
            gcf=i
        i+=1
print(gcf)
# ******************************************************************************

# 7. Print Numbers Whose Digit Sum is Greater Than 10 
# Problem Definition: The sum of digits can be compared against a limit. 
# Task: Read N. Print all numbers from 1 to N whose digit sum is greater than 10. 
# Example Input: 
# 30 
# Example Output: 
# 29 
# 30

n=int(input("Enter max number: "))
i=1    
while i<=n:
    j=i
    tot=0
    while j>0:
        tot += j%10
        j//=10
    if tot>10:
        print(i)
    i+=1
# ******************************************************************************

# 8. Count Numbers That Have Exactly Two Even Digits 
# Problem Definition: Compare even and odd digits. Task: Read N numbers and count how many contain exactly two even digits. 
# Example Input: 
# 4 
# 248 
# 357 
# 4821
# 406
# Example Output: 
# 3

n=int(input("Enter max numbers: "))
count = 0
while n>0:
    num = int(input("Enter a number: "))
    even = 0
    temp=num
    while temp>0:
        r=temp%10
        if r%2==0:
            even +=1
        temp//=10
    if even ==2:
        count +=1
    n-=1
print(count)
# ******************************************************************************

# 9. Print Factors That Are Multiples of 3 
# Problem Definition: Filter factors divisible by 3. 
# Task: Read a number and print all factors that are multiples of 3. 
# Example Input: 
# 36 
# Example Output: 
# 3 
# 6 
# 9 
# 12 
# 18 
# 36

n=int(input("Enter a number: "))
i=1
while i<=n:
    if n%i==0 and i%3==0:
        print(i)
    i+=1
# ******************************************************************************

# 10. Read Numbers Until the Product Exceeds 500 
# Problem Definition: A loop can stop based on the running product. 
# Task: Keep reading numbers until the product exceeds 500 and print the final product. 
# Example Input: 
# 2 
# 5 
# 8 
# 7 
# Example Output: 
# 560

tot=1
while True:
    if tot >500:
        print(tot)
        break
    n=int(input("Enter a number: "))
    tot *= n