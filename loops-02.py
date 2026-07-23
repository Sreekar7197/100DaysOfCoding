# 1. Highest Profit Month 
# Definition: Find the maximum value and its position while reading inputs. 
# Task: A shop owner records the profit for N months. Print the highest profit and its month number. 
# Example Input: 
# 5 
# 12000 
# 15000 
# 9800 
# 17500 
# 16000 
# Example Output: 
# Highest Profit = 17500 
# Month = 4

n=int(input("Enter max months: "))
highest = 0
month = 0
high_month = 0
while month<n:
    profit = int(input("Enter profit: "))
    month +=1
    if profit > highest:
        highest = profit
        high_month = month
print(f"Highest Profit = {highest}")
print(f"Month = {high_month}")
# ******************************************************************************

# 2. Perfect Square Counter 
# Definition: A perfect square is the square of an integer. 
# Task: Read N numbers and count how many are perfect squares. 
# Example Input: 
# 5 
# 16
# 20 
# 25 
# 18 
# 49 
# Example Output: 
# 3

n= int(input("Enter max number: "))
count = 0
while n>0:
    num = int(input("Enter a number: "))
    i=1
    while i*i <num:
        i+=1
    if i*i == num:
        count +=1
    n-=1
print(count)
# ******************************************************************************

# 3. Sum of Multiples of 7 
# Definition: Multiples of 7 are numbers divisible by 7. 
# Task: Read A and B. Sum all multiples of 7 between them. 
# Example Input: 
# 10 
# 35 
# Example Output: 
# 84

a=int(input("Enter a number: "))
b=int(input("Enter a number: "))
tot = 0
while a<=b:
    if a%7==0:
        tot += a    
    a+=1
print(tot)
# ******************************************************************************

# 4. Longest Positive Streak 
# Definition: A streak is consecutive values satisfying a condition. 
# Task: Read N numbers and find the longest positive streak. 
# Example Input: 
# 8 
# 5 
# 7
# -2 
# 4 
# 9 
# 10
# 12
# -5 
# Example Output: 
# 4

n= int(input("Enter max number: "))
long_count = 0
count = 0
while n>0:
    num = int(input("Enter a number: "))
    if num <0:
        if count>long_count:
            long_count = count
        count = 0
    else:
        count +=1
    n-=1
print(long_count)
# ******************************************************************************

# 5. Count Numbers with Exactly Three Divisors 
# Definition: Some numbers have exactly three positive divisors. 
# Task: Read N numbers and count them. 
# Example Input: 
# 5 
# 4 
# 9 
# 8 
# 16 
# 25 
# Example Output: 
# 3

n=int(input("Enter max numbers: "))
count = 0
while n>0:
    num = int(input("Enter a number: "))
    div = 0
    i=1
    while i<=num:
        if num%i==0:
            div +=1
        i+=1
    if div ==3:
        count +=1
    n-=1
print(count)
# ******************************************************************************

# 6. Largest Difference 
# Definition: Difference is the gap between two values. 
# Task: Find the largest difference between consecutive inputs. 
# Example Input: 
# 5 
# 10 
# 25 
# 18 
# 40 
# 32 
# Example Output: 
# 22

n= int(input("Enter max numbers: "))
largest = 0
num = int(input("Enter a number: "))
while n>1:
    prev_num=num
    num = int(input("Enter a number: "))
    if num>prev_num:
        diff = num-prev_num
    else:
        diff = prev_num-num
    if diff>largest:
        largest=diff
    n-=1
print(largest)
# ******************************************************************************

# 7. Salary Bonus 
# Definition: Employees below a threshold qualify. 
# Task: Count salaries below Rs.30000. 
# Example Input: 
# 5 
# 25000 
# 40000 
# 18000 
# 32000 
# 29000 
# Example Output: 
# 3

n=int(input("Enter max employees: "))
thr=int(input("Enter the Threshold salary: "))
count = 0
while n>0:
    sal = int(input("Enter the salary: "))
    if sal < thr:
        count +=1
    n-=1
print(count)
# ******************************************************************************

# 8. Largest Digit Sum 
# Definition: Digit sum is the sum of all digits.
# Task: Print the number having the largest digit sum. 
# Example Input: 
# 4 
# 123 
# 98 
# 555 
# 71 
# Example Output:
# 555

n=int(input("Enter max numbers: "))
largest_tot = 0
lar=0
while n>0:
    num = int(input("Enter a number: "))
    temp = num
    tot=0
    while temp>0:
        tot +=temp%10
        temp//=10
    if tot>largest_tot:
        largest_tot=tot
        lar=num
    n-=1
print(lar)
# ******************************************************************************

# 9. Average Until Zero 
# Definition: Average equals total divided by count. 
# Task: Read numbers until 0 and print the average. 
# Example Input: 
# 8 
# 12 
# 20 
# 0 
# Example Output: 
# 13.33

count = 0
tot = 0
while True:
    num = int(input("Enter a number: "))
    if num == 0:
        avg = tot/count
        print(f"{avg:.2f}")
        break
    count +=1
    tot += num
# ******************************************************************************

# 10. Count Numbers Greater Than Average 
# Definition: Compare values with the calculated average. 
# Task: Read N numbers, compute average, then count numbers above it. 
# Example Input: 
# 5 
# 10 
# 20 
# 30 
# 40 
# 50 
# Example Output:
# 2

n=int(input("Enter max numbers: "))
nums = []
count = 0
tot = 0
while n>0:
    num = int(input("Enter a number: "))
    tot+=num
    nums += [num]
    count +=1
    n-=1
avg = tot/count
i=0
greater=0
while i<count:
    if nums[i]>avg:
        greater +=1
    i+=1
print(greater)