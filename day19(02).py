# 1. Print Numbers from 1 to N 
# Definition: Loops allow a program to repeat the same task multiple times. 
# Task: Read a number N and print all numbers from 1 to N using a loop. 
# Example Input: N = 5 
# Example Output: 1 2 3 4 5

n = int(input("Enter a number: "))
i=1 
while i<=n:
    print(i)
    i+=1
# ******************************************************************************

# 2. Print Numbers from N to 1 
# Definition: Reverse counting is useful in many programming problems. 
# Task: Read a number N and print numbers from N to 1 using a loop. 
# Example Input: N = 5 
# Example Output: 5 4 3 2 1

n=int(input("Enter a number: "))
while n>0:
    print(n)
    n-=1
# ******************************************************************************

# 3. Sum of First N Natural Numbers 
# Definition: Natural numbers start from 1. 
# Task: Find the sum of numbers from 1 to N using a loop. 
# Example Input: N = 5 
# Example Output: 15

n=int(input("Enter a number: "))
i=1
sum = 0
while i<=n:
    sum += i
    i+=1
print(sum)
# ******************************************************************************

# 4. Factorial of a Number 
# Definition: The factorial of a number is the product of all positive integers from 1 to that number. 
# Task: Calculate the factorial using a loop. 
# Example Input: N = 5 
# Example Output: 120

n=int(input("Enter a number: "))
fact=1
i=1
while i<=n:
    fact*=i
    i+=1
print(fact)
# ******************************************************************************

# 5. Multiplication Table 
# Definition: A multiplication table shows the multiples of a number. 
# Task: Print the multiplication table of a given number up to 10. 
# Example Input: N = 3 
# Example Output: 3 x 1 = 3 ... 3 x 10 = 30

n = int(input("Enter a number: "))
i=1
while i<=10:
    print(f"{n}x{i}={n*i}")
    i+=1
# ******************************************************************************

# 6. Count Digits 
# Definition: Every number contains one or more digits. 
# Task: Count the total number of digits using a loop.
# Example Input: 45892 
# Example Output: 5

n=int(input("Enter a number: "))
dig = 0
while n>0:
    n//=10
    dig+=1
print(dig)
# ******************************************************************************

# 7. Reverse a Number 
# Definition: Reversing digits is a common number problem. 
# Task: Reverse the given number using a loop. 
# Example Input: 1234 
# Example Output: 4321

n=int(input("Enter a number: "))
rev = 0
while n>0:
    r=n%10
    rev=rev*10+r
    n//=10
print(rev)
# ******************************************************************************

# 8. Sum of Digits 
# Definition: Add all digits present in the number. 
# Task: Calculate the sum of digits using a loop. 
# Example Input: 572 
# Example Output: 14

n=int(input("Enter a number: "))
sum=0
while n>0:
    sum+=n%10
    n//=10
print(sum)
# ******************************************************************************

# 9. Product of Digits 
# Definition: Multiply all digits present in the number. 
# Task: Calculate the product of digits using a loop. 
# Example Input: 572 
# Example Output: 70

n=int(input("Enter a number: "))
prod=1
while n>0:
    prod*=n%10
    n//=10
print(prod)
# ******************************************************************************

# 10. Count Even and Odd Digits 
# Definition: Separate digits based on whether they are even or odd. 
# Task: Count even digits and odd digits using a loop. 
# Example Input: 583920 
# Example Output: 
# Even Digits = 3 
# Odd Digits = 3

n=int(input("Enter a number: "))
even=0
odd=0
while n>0:
    r=n%10
    if r%2==0:
        even +=1
    else:
        odd+=1
    n//=10
print(f"Even={even}")
print(f"Odd={odd}")