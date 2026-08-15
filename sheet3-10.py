# 1. Print Numbers from 1 to n
# Question: Write a program to print numbers from 1 to n. 
# Explanation: Use a loop starting from 1 to n and print each number. 
# - Input: n = 5 
# - Output: 1 2 3 4 5

n=int(input("Enter a number: "))
for i in range(1,n+1):
    print(i,end=" ")
# ________________________________________
# 2. Print Numbers from m to n
# Question: Write a program to print numbers from m to n. 
# Explanation: Loop from m to n and print values. 
# - Input: m = 3, n = 7 
# - Output: 3 4 5 6 7

m=int(input("Enter starting number: "))
n=int(input("Enter ending number: "))
for i in range(m,n+1):
    print(i,end=" ")
# ________________________________________
# 3. Print Numbers from n to 1 in Reverse
# Question: Write a program to print numbers in reverse from n to 1. 
# Explanation: Use a loop starting from n and decrement to 1. 
# - Input: n = 5 
# - Output: 5 4 3 2 1

n=int(input("Enter a number: "))
for i in range(n,0):
    print(i)
# ________________________________________
# 4. Print Numbers from n to m in Reverse
# Question: Write a program to print numbers from n to m in reverse. 
# Explanation: Start from n and go down to m. 
# - Input: n = 10, m = 6 
# - Output: 10 9 8 7 6

m=int(input("Enter starting number: "))
n=int(input("Enter ending number: "))
for i in range(n,m-1):
    print(i,end=" ")
# ________________________________________
# 5. Sum of n Natural Numbers
# Question: Write a program to calculate the sum of first n natural numbers. 
# Explanation: Use formula or loop to sum from 1 to n. 
# - Input: n = 5 
# - Output: 15

n=int(input("Enter a number: "))
sum=0
for i in range(1,n+1):
    sum+=i
print(sum)
# ________________________________________
# 6. Factorial of a Number
# Question: Write a program to find the factorial of a number. 
# Explanation: Multiply all numbers from 1 to n. 
# - Input: n = 5 
# - Output: 120

n=int(input("Enter a number: "))
prod=1
for i in range(1,n+1):
    prod*=i
print(prod)
# ________________________________________
# 7. Sum of m to n Numbers
# Question: Write a program to find the sum of all numbers from m to n. 
# Explanation: Loop from m to n and add values. 
# - Input: m = 3, n = 6 
# - Output: 18

m=int(input("Enter starting number: "))
n=int(input("Enter ending number: "))
sum=0
for i in range(m,n+1):
    sum+=i
print(sum)
# ________________________________________
# 8. Product of m to n Numbers
# Question: Write a program to find the product of numbers from m to n. 
# Explanation: Loop from m to n and multiply values. 
# - Input: m = 2, n = 4 
# - Output: 24

m=int(input("Enter starting number: "))
n=int(input("Enter ending number: "))
prod=1
for i in range(m,n+1):
    prod*=i
print(prod)
# ________________________________________
# 9. Print Factors of a Number
# Question: Write a program to print all factors of a given number. 
# Explanation: Check divisibility of number from 1 to n. 
# - Input: n = 6 
# - Output: 1 2 3 6

n=int(input("Enter a number: "))
for i in range(1,n+1):
    if n%1==0:
        print(i,end=" ")
# ________________________________________
# 10. Count of Factors
# Question: Write a program to count how many factors a number has. 
# Explanation: Increment count when divisible. 
# - Input: n = 6 
# - Output: 4

count=0
n=int(input("Enter a number: "))
for i in range(1,n+1):
    if n%1==0:
        count+=1
print(count)
# ________________________________________
# 11. Prime Number Check
# Question: Check if a number is prime. 
# Explanation: A number is prime if it has exactly 2 factors. - 
# Input: n = 7 
# - Output: Prime

num=int(input("Enter a number: "))
prime=1
if num<=1:
    prime=0
else:
    for i in range(2,num):
        if num%i==0:
            prime=0
            break
if prime:
    print("Prime")
else:
    print("Not a prime")
# ________________________________________
# 12. Even Numbers from m to n
# Question: Print all even numbers between m and n. 
# Explanation: Use loop and check if divisible by 2. 
# - Input: m = 3, n = 10 
# - Output: 4 6 8 10

m=int(input("Enter starting number: "))
n=int(input("Enter ending number: "))
for i in range(m,n+1):
    if i%2==0:
        print(i)
# ________________________________________
# 13. Odd Numbers from m to n
# Question: Print all odd numbers between m and n. 
# Explanation: Check if number % 2 != 0. 
# - Input: m = 3, n = 10 
# - Output: 3 5 7 9

m=int(input("Enter starting number: "))
n=int(input("Enter ending number: "))
for i in range(m,n+1):
    if i%2==1:
        print(i)
# ________________________________________
# 14. Count of Even and Odd Numbers
# Question: Count how many even and odd numbers are in the range m to n. Explanation: Use counters for even and odd. - Input: m = 3, n = 7 - Output: Even = 2, Odd = 3

m=int(input("Enter starting number: "))
n=int(input("Enter ending number: "))
even=0
odd=0
for i in range(m,n+1):
    if i%2==0:
        even+=1
    else:
        odd+=1
print(f"Even= {even}")
print(f"Odd= {odd}")
# ________________________________________
# 15. Reverse a String
# Question: Reverse a given string. 
# Explanation: Use slicing or loop. 
# - Input: “hello” 
# - Output: “olleh”

string=input("Enter a string: ")
ans=""
for i in range(len(string)):
    ans=string[i]+ans
print(ans)
# ________________________________________
# 16. Check for Palindrome String
# Question: Check if a string is a palindrome. 
# Explanation: Compare string with its reverse. 
# - Input: “madam” 
# - Output: Palindrome

string=input("Enter a string: ")
ans=""
for i in range(len(string)):
    ans=string[i]+ans
if string==ans:
    print("Palindrome")
else:
    print("Not a Palindrome")
# ________________________________________
# 17. Sum of Digits
# Question: Calculate the sum of digits of a number. 
# Explanation: Use loop and % 10 to extract digits. 
# - Input: 123 
# - Output: 6

num=int(input("Enter a number: "))
sum=0
while num>0:
    sum+=num%10
    num//=10
print(sum)
# ________________________________________
# 18. Product of Digits
# Question: Calculate the product of digits. 
# Explanation: Multiply digits extracted from number. 
# - Input: 123 
# - Output: 6

num=int(input("Enter a number: "))
prod=1
while num>0:
    prod*=num%10
    num//=10
print(prod)
# ________________________________________
# 19. Armstrong Number Check
# Question: Check if a number is an Armstrong number. 
# Explanation: Sum of cube of digits equals the number. 
# - Input: 153 
# - Output: Armstrong number

num=int(input("Enter a number: "))
arm=0
count=0
temp1=num
temp2=num
while temp1>0:
    temp1//=10
    count+=1
while temp2>0:
    arm+= (temp2%10) ** count
    temp2//=10
if arm==num:
    print("Armstrong number")
else:
    print("Not an Armstrong number")
# ________________________________________
# 20. Reverse a Number
# Question: Reverse the digits of a number. 
# Explanation: Use loop with % and // to reverse. 
# - Input: 123 
# - Output: 321

num=int(input("Enter a number: "))
rev=0
while num>0:
    r=num%10
    rev=rev*10+r
    num//=10
print(rev)
# ________________________________________
# 21. Palindrome Number Check
# Question: Check if a number is a palindrome. 
# Explanation: Compare number with its reverse. 
# - Input: 121 
# - Output: Palindrome

num=int(input("Enter a number: "))
temp=num
rev=0
while num>0:
    r=num%10
    rev=rev*10+r
    num//=10
if temp==rev:
    print("Palindrome")
else:
    print("Not a Palindrome")
# ________________________________________
# 22. Count Vowels in String
# Question: Count number of vowels in a string. 
# Explanation: Loop and check for a, e, i, o, u. 
# - Input: “apple” 
# - Output: 2

string=input("Enter a string: ")
vowels=["a","e","i","o","u","A","E","I","O","U"]
count=0
for i in string:
    if i in vowels:
        count+=1
print(count)
# ________________________________________
# 23. Count Consonants in String
# Question: Count consonants in a string. 
# Explanation: Check for alphabetic characters not vowels. 
# - Input: “apple” 
# - Output: 3

string=input("Enter a string: ")
vowels=["a","e","i","o","u","A","E","I","O","U"]
count=0
for i in string:
    if i not in vowels:
        count+=1
print(count)
# ________________________________________
# 24. Count Vowels and Consonants
# Question: Count vowels and consonants in input string. 
# Explanation: Maintain two counters. 
# - Input: “apple” 
# - Output: Vowels = 2, Consonants = 3

string=input("Enter a string: ")
vowels=["a","e","i","o","u","A","E","I","O","U"]
vow=0
cons=0
for i in string:
    if i in vowels:
        vow+=1
    else:
        cons+=1
print(f"Vowels= {vow}")
print(f"Consonants= {cons}")
# ________________________________________
# 25. Perfect Number Check
# Question: Check if a number is perfect. 
# Explanation: Sum of proper divisors equals the number. 
# - Input: 28 
# - Output: Perfect number

num=int(input("Enter a number: "))
sum=0
for i in range(1,num):
    if num%i==0:
        sum+=i
if sum==num:
    print("Perfect number")
else:
    print("Not a Perfect number")
# ________________________________________
# 26. Neon Number Check
# Question: Check if a number is a neon number. 
# Explanation: Square the number, sum digits, match original. 
# - Input: 9 
# - Output: Neon number

num=int(input("enter a number: "))
sq=num**2
sum=0
while sq>0:
    sum+=sq%10
    sq//=10
if sum==num:
    print("Neon number")
else:
    print("Not a Neon number")
# ________________________________________
# 27. Strong Number Check
# Question: Check if a number is a strong number. 
# Explanation: Sum of factorial of digits equals the number. 
# - Input: 145 
# - Output: Strong number

num=int(input("Enter a number: "))
temp=num
sum=0
while temp>0:
    fact=1
    for i in range(1,(temp%10)+1):
        fact*=i
    sum+=fact
    temp//=10
if sum==num:
    print("Strong number")
else:
    print("Not a Strong number")
# ________________________________________
# 28. Harshad Number Check
# Question: Check if a number is divisible by the sum of its digits. 
# Explanation: Calculate digit sum and check divisibility. 
# - Input: 18 
# - Output: Harshad number

num=int(input("Enter a number: "))
sum=0
temp=num
while temp>0:
    sum+=temp%10
    temp//=10
if num%sum==0 and sum>0:
    print("Harshad Number")
else:
    print("Not a Harshad Number")
# ________________________________________
# 29. Fibonacci Series
# Question: Print the Fibonacci series up to n terms. 
# Explanation: Start with 0, 1 and continue with sum of last two. 
# - Input: n = 5 
# - Output: 0 1 1 2 3

num=int(input("Enter a number: "))
a=0
b=1
while num>0:
    print(a,end=" ")
    a,b=b,a+b
    num-=1
# ________________________________________
# 30. Check for Neon Number (Repeated)
# Question: Again, check for a neon number (example). 
# Explanation: Square number and sum digits. 
# - Input: 9 
# - Output: Neon number

num=int(input("enter a number: "))
sq=num**2
sum=0
while sq>0:
    sum+=sq%10
    sq//=10
if sum==num:
    print("Neon number")
else:
    print("Not a Neon number")