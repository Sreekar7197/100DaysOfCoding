# 1. Consecutive Pass Count 
# Definition: A consecutive pass means students pass one after another without any failure in between. 
# Task: Read marks of N students and find the longest consecutive sequence of students scoring 35 or more. 
# Example Input: 
# 8 
# 40 
# 55 
# 20 
# 36 
# 70 
# 90 
# 15 
# 45 
# Example Output: 
# Longest Consecutive Passes = 3

n=int(input("Enter max length: "))
longest = 0
cons = 0
while n>0:
    marks = int(input("Enter student marks: "))
    if marks<35:
        cons=0
    else:
        cons +=1
    if cons>longest:
        longest=cons
    n-=1
print("Longest Connsecutive Passes =",longest)
# ******************************************************************************

# 2. Largest Prime Entered 
# Definition: A prime number has exactly two positive divisors. 
# Task: Read N numbers and print the largest prime. 
# Example Input: 
# 6 
# 12 
# 17 
# 21 
# 29 
# 18 
# 7 
# Example Output: 
# Largest Prime = 29

n=int(input("Enter max numbers: "))
lar = 0
while n>0:
    num = int(input("Enter a number: "))
    i=2
    while i<=num*0.5:
        if num%i!=0 and num>lar:
            lar = num
        i+=1
    n-=1
print("Largest Prime =",lar)
# ******************************************************************************

# 3. Sum of Even Digits 
# Definition: Even digits are 0,2,4,6,8. 
# Task: Read a number and print the sum of even digits. 
# Example Input: 
# 4827316 
# Example Output:
# 20

n=int(input("Enter a number: "))
even_sum = 0
while n>0:
    if (n%10)%2==0:
        even_sum+=n%10
    n//=10
print(even_sum)
# ******************************************************************************

# 4. Factory Quality Check 
# Definition: Quality below 50 is defective. 
# Task: Read N scores and print defective and good counts. 
# Example Input: 
# 6 
# 45 
# 60
# 72 
# 38 
# 80 
# 49 
# Example Output: 
# Defective = 3 
# Good = 3

n=int(input("Enter max scores: "))
defective = 0
good = 0
while n>0:
    score = int(input("Enter a score: "))
    if score<50:
        defective +=1
    else:
        good +=1
    n-=1
print(f"Defective = {defective}")
print(f"Good = {good}")
# ******************************************************************************

# 5. Maximum Sales Increase 
# Definition: Increase is today's sales minus yesterday's. 
# Task: Find the maximum increase between consecutive days. 
# Example Input: 
# 5 
# 100 
# 130 
# 110 
# 180 
# 200 
# Example Output: 
# Maximum Increase = 70

n = int(input("Enter number of days: "))
max_increase = 0
num = int(input("Enter today sales: "))
prev_sales=0
while n>1:
    prev_sales = num
    num = int(input("Enter today sales: "))
    increase = 0
    if num>prev_sales:
        increase = num-prev_sales
    else:
        increase = prev_sales-num
    if increase>max_increase:
        max_increase=increase
    n-=1
print(f"Maximum Increase = {max_increase}")
# ******************************************************************************

# 6. Number with Most Digits 
# Definition: Digit count is the number of digits. 
# Task: Print the number with the most digits. 
# Example Input: 
# 5 
# 23 
# 9876 
# 105 
# 123456 
# 89 
# Example Output: 
# 123456

n=int(input("Enter max numbers: "))
max_dig = 0
max_dig_num = 0
while n>0:
    num = int(input("Enter a number: "))
    temp = num
    dig = 0
    while temp>0:
        temp//=10
        dig +=1
    if dig>max_dig:
        max_dig = dig
        max_dig_num = num
    n-=1
print(max_dig_num)
# ******************************************************************************

# 7. Count Numbers Divisible by Both 4 and 6 
# Definition: Such numbers are divisible by 12. 
# Task: Count such numbers. 
# Example Input: 
# 6 
# 12 
# 24 
# 18 
# 36 
# 40 
# 48 
# Example Output: 
# 4

n= int(input("Enter max numbers: "))
count = 0
while n>0:
    num = int(input("Enter a number: "))
    if num%12==0:
        count +=1
    n-=1
print(count)
# ******************************************************************************

# 8. Longest Odd Streak 
# Definition: An odd streak is consecutive odd numbers. 
# Task: Find the longest odd streak. 
# Example Input: 
# 8 
# 3 
# 5 
# 8 
# 7 
# 9 
# 11 
# 4 
# 13 
# Example Output: 
# 3

n=int(input("Enter max number: "))
odd_streak = 0
streak = 0
while n>0:
    num = int(input("Enter a number: "))
    if num %2 ==1:
        streak +=1
    else:
        streak = 0
    if streak > odd_streak:
        odd_streak=streak
    n-=1
print(odd_streak)
# ******************************************************************************

# 9. Smallest Digit Sum 
# Definition: Digit sum is the sum of a number's digits. 
# Task: Print the number with the smallest digit sum. 
# Example Input: 
# 4 
# 123 
# 81 
# 44 
# 70 
# Example Output: 
# 70

n=int(input("Enter max numbers: "))
smallest_dig_sum = 0
num = int(input("Enter a number: "))
smallest_dig = num
while n>1:
    num = int(input("Enter a number: "))
    dig_sum = 0
    temp = num
    while temp>0:
        dig_sum+=temp%10
        temp//=10
    if dig_sum<smallest_dig_sum:
        smallest_dig_sum=dig_sum
        smallest_dig=num
    n-=1
print(smallest_dig)
# ******************************************************************************

# 10. Running Balance 
# Definition: Running balance updates after each transaction. 
# Task: Print balance after each transaction and final balance. 
# Example Input: 
# 1000 
# 4 
# 500
# -200 
# 300
# -100 
# Example Output: 
# Balance=1500 
# Balance=1300 
# Balance=1600 
# Balance=1500 
# Final Balance=1500

bal = int(input("Enter Balance"))
n=int(input("Enter total no. of transactions: "))
while n>0:
    transaction = int(input("Enter transaction amount: "))
    bal += transaction
    print(f"Balance = {bal}")
    n-=1
print(f"Final Balance = {bal}")