# 1. Harshad Number Definition: A number that is divisible by the sum of its digits. 
# Example Calculation: 
# Number = 18 
# Sum of digits = 1 + 8 = 9 
# Check divisibility: 18 ÷ 9 = 2 (remainder 0) 
# Therefore, 18 is a Harshad number. 
# Task: Check whether a given number is Harshad. 
# Example Input: 18 
# Example Output: 18 is a Harshad number

num = int(input("Enter a number: "))
tot = 0
temp = num
while temp>0:
    tot = tot + temp%10
    temp//=10
if num %tot == 0:
    print(f"{num} is a Harshad number")
else:
    print(f"{num} is not a Harshad number")
# ******************************************************************************

# 2. Strong Number 
# Definition: A number where the sum of factorials of its digits equals the original number. 
# Example Calculation: 
# Number = 145 
# 1! + 4! + 5! = 1 + 24 + 120 = 145 
# Therefore, 145 is a Strong number. 
# Task: Check whether a number is Strong. 
# Example Input: 145 
# Example Output: 145 is a Strong number

num = int(input("Enter a number: "))
tot = 0
temp = num
while temp>0:
    r = temp %10
    temp_prod = 1
    for i in range (1,r+1):
        temp_prod*=i
    tot+=temp_prod
    temp//=10
if num==tot:
    print(f"{num} is a Strong number")
else:
    print(f"{num} is not a Strong number")
# ******************************************************************************

# 3. Neon Number 
# Definition: A number where the sum of digits of its square equals the original number. 
# Example Calculation: 
# Number = 9 
# Square = 9 × 9 = 81 
# Sum of digits = 8 + 1 = 9 
# Therefore, 9 is a Neon number. 
# Task: Check whether a number is Neon. 
# Example Input: 9 
# Example Output: 9 is a Neon number

num = int(input("Enter a number: "))
square = num**2
temp = square
sum_of_dig = 0
while temp>0:
    sum_of_dig = sum_of_dig + temp%10
    temp//=10
if num==sum_of_dig:
    print(f"{num} is a Neon Number.")
else:
    print(f"{num} is not a Neon Number.")
# ******************************************************************************

# 4. Spy Number 
# Definition: A number where the sum of digits equals the product of digits. 
# Example Calculation: 
# Number = 1124 
# Sum = 1+1+2+4 = 8 
# Product = 1×1×2×4 = 8 
# Therefore, 1124 is a Spy number.
# Task: Check whether a number is Spy. 
# Example Input: 1124 
# Example Output: 1124 is a Spy number

num = int(input("Enter a number: "))
sum_of_digits = 0
product_of_digits = 1
temp = num
while temp>0:
    sum_of_digits = sum_of_digits + temp%10
    product_of_digits = product_of_digits * temp%10
    temp//=10
if sum_of_digits == product_of_digits:
    print(f"{num} is a Spy number.")
else:
    print(f"{num} is not a Spy number.")
# ******************************************************************************

# 5. Happy Number 
# Definition: A number that reaches 1 after repeatedly replacing it with the sum of squares of its digits. 
# Example Calculation: 
# 19 → 1²+9²=82 → 8²+2²=68 → 6²+8²=100 → 1²+0²+0²=1 
# Therefore, 19 is a Happy number. 
# Task: Check whether a number is Happy. 
# Example Input: 19 
# Example Output: 19 is a Happy number

num = int(input("Enter a number: "))
happy = 0
temp = num
while True:
    if temp ==1:
        happy +=1
        break
    if temp == 4:
        break
    x=0
    while temp>0:
        x = x+(temp %10)**2
        temp//=10
    temp = x
if happy ==1:
    print(f"{num} is a happy number.")
else:
    print(f"{num} is not a happy number.")
# ******************************************************************************

# 6. Disarium Number 
# Definition: A number where the sum of digits raised to their positions equals the original number. 
# Example Calculation: 135 = 1¹ + 3² + 5³ = 1 + 9 + 125 = 135 
# Therefore, 135 is a Disarium number. 
# Task: Check whether a number is Disarium. 
# Example Input: 135 
# Example Output: 135 is a Disarium number

num = int(input("Enter a number: "))
digits = 0
temp1 = num
temp2 = num
tot = 0
count = 0
while temp1>0:
    temp1//=10
    digits +=1
while temp2>0:
    tot = tot + (temp2%10)**(digits-count)
    temp2//=10
    count +=1
if tot == num:
    print(f"{num} is a Disarium number")
else:
    print(f"{num} is not a Disarium number")
# ******************************************************************************

# 7. Duck Number 
# Definition: A number containing zero digits but not starting with zero. 
# Example Calculation: 1023 contains 0 after the first digit. Therefore, 1023 is a Duck number. 
# Task: Check whether a number is Duck. 
# Example Input: 1023 
# Example Output: 1023 is a Duck number

num = int(input("Enter a number: "))
temp = num
duck = 0
while temp >0:
    x = temp%10
    if x == 0:
        duck +=1
        break
    temp//=10
if duck >0:
    print(f"{num} is a Duck number.")
else:
    print(f"{num} is not a Duck number.")
# ******************************************************************************

# 8. Abundant Number 
# Definition: A number where the sum of proper divisors is greater than the number. 
# Example Calculation: 
# 12 → Proper divisors: 1,2,3,4,6 
# Sum = 1+2+3+4+6 = 16 
# 16 > 12, so 12 is Abundant. 
# Task: Check whether a number is Abundant. 
# Example Input: 12
# Example Output: 12 is an Abundant number

num = int(input("Enter a number: "))
temp = num
sum_of_div = 0
for i in range(1, num):
    if num % i == 0:
        sum_of_div += i
if sum_of_div > num:
    print(f"{num} is an Abundant number.")  
else:
    print(f"{num} is not an Abundant number.")
# ******************************************************************************

# 9. Perfect Number 
# Definition: A number where the sum of proper divisors equals the number. 
# Example Calculation: 
# 6 → Proper divisors: 1,2,3 
# Sum = 1+2+3 = 6 Therefore, 6 is Perfect. 
# Task: Check whether a number is Perfect. 
# Example Input: 6 
# Example Output: 6 is a Perfect number

num = int(input("Enter a number: "))
temp = num
sum_of_div = 0
for i in range(1, num):
    if num % i == 0:
        sum_of_div += i
if sum_of_div == num:
    print(f"{num} is a Perfect number.")  
else:
    print(f"{num} is not a Perfect number.")
# ******************************************************************************

# 10. Automorphic Number 
# Definition: A number whose square ends with the same digits as the original number. 
# Example Calculation: 25² = 625 
# Last two digits of 625 = 25 Therefore, 25 is Automorphic. 
# Task: Check whether a number is Automorphic. 
# Example Input: 25 
# Example Output: 25 is an Automorphic number

num = int(input("Enter a number: "))
digits = 0
square = num**2
temp1 = num
temp2 = square
autom = 0
pos = 1
while temp1>0:
    temp1//=10
    digits +=1
count = 0
autom = 0
while temp2>0:
    if count == digits:
        break
    x = temp2%10
    autom = autom+x*pos
    pos = pos*10
    temp2//=10
    count +=1
if autom == square:
    print(f"{num} is an Automorphic number.")
else:
    print(f"{num} is not an Automorphic number.")