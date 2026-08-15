# 1. Check Even or Odd
# Question: Determine whether a number is even or odd. 
# Explanation: A number is even if it is divisible by 2. Otherwise, it’s odd. 
# - Input: Number = 6 
# - Output: Even number

num=int(input("Enter a number: "))
if num%2==0:
    print("Even number")
else:
    print("Odd number")
# ________________________________________
# 2. Divisible by 5 but Not by 10
# Question: Check if a number is divisible by 5 but not by 10. 
# Explanation: Use modulo (%) to check if the number % 5 == 0 and number % 10 != 0. 
# - Input: Number = 25 
# - Output: Satisfy

num=int(input("Enter a number: "))
if num%10!=0 and num%5==0:
    print("Satisfy")
else:
    print("Not Satisfy")
# ________________________________________
# 3. Biggest Among Two Numbers
# Question: Find the biggest number among two. Explanation: Use comparison operators (>) to check which number is greater. - Input: A = 4, B = 7 - Output: Biggest is: 7

num1=int(input("Enter num1: "))
num2=int(input("Enter num2: "))
if num1>num2:
    print(f"Biggest is {num1}")
else:
    print(f"Biggest is {num2}")
# ________________________________________
# 4. Smallest Among Two Numbers
# Question: Find the smallest number among two. Explanation: Use comparison operators (<) to find the smaller value. - Input: A = 4, B = 7 - Output: Smallest is: 4

num1=int(input("Enter num1: "))
num2=int(input("Enter num2: "))
if num1<num2:
    print(f"Smallest is {num1}")
else:
    print(f"Smallest is {num2}")
# ________________________________________
# 5. Divisible by 2, 3, and 6
# Question: Check if a number is divisible by 2, 3, and 6. Explanation: If a number is divisible by both 2 and 3, it is also divisible by 6. - Input: Number = 18 - Output: Satisfy

num = int(input("Enter a number: "))
if num%2==0 and num%3==0:
    print("Satisfy")
else:
    print("Not Satisfy")
# ________________________________________
# 6. Voting Eligibility
# Question: Check if a person is eligible to vote (age >= 18). Explanation: A person is eligible to vote if their age is 18 or above. - Input: Age = 19 - Output: Eligible to vote
age=int(input("Enter Your age: "))
if age>=18:
    print("Eligible to vote")
else:
    print("Not Eligible to vote")
# ________________________________________
# 7. Student Pass/Fail Based on All Subjects >= 35
# Question: Check if a student passed all subjects (maths, physics, chemistry). Explanation: Student passes only if marks in all subjects are 35 or more. - Input: Maths = 40, Physics = 36, Chemistry = 30 - Output: Fail

mat=int(input("Enter marks in Maths: "))
phy=int(input("Enter marks in Physics: "))
chem=int(input("Enter marks in Chemistry: "))
if mat>=35 and phy>=35 and chem>35:
    print("Pass")
else:
    print("Fail")
# ________________________________________
# 8. Student Pass if Passed Any One Subject (>= 35)
# Question: Check if the student passed at least one subject. Explanation: Use logical OR to check if any one subject has marks >= 35. - Input: Maths = 20, Physics = 38, Chemistry = 25 - Output: Pass

mat=int(input("Enter marks in Maths: "))
phy=int(input("Enter marks in Physics: "))
chem=int(input("Enter marks in Chemistry: "))
if mat>=35 or phy>=35 or chem>35:
    print("Pass")
else:
    print("Fail")
# ________________________________________
# 9. Student Pass if Passed Any Two Subjects
# Question: Check if the student passed any two out of three subjects. Explanation: Use a counter or logical conditions to verify two subjects >= 35. - Input: Maths = 40, Physics = 20, Chemistry = 36 - Output: Pass

mat=int(input("Enter marks in Maths: "))
phy=int(input("Enter marks in Physics: "))
chem=int(input("Enter marks in Chemistry: "))
if (mat>=35 and phy>=35) or (phy>=35 and chem>35) or (mat>=35 or chem>=35):
    print("Pass")
else:
    print("Fail")
# ________________________________________
# 10. Biggest Among Three Numbers
# Question: Find the biggest number among three. Explanation: Compare each pair of numbers using if-else conditions. - Input: A = 7, B = 4, C = 9 - Output: Biggest is: 9

num1=int(input("Enter num1: "))
num2=int(input("Enter num2: "))
num3=int(input("Enter num3: "))
if num1>num2:
    if num1>num3:
        print(f"Biggest is {num1}")
    else:
        print(f"Biggest is {num3}")
else:
    if num2>num3:
        print(f"Biggest is {num2}")
    else:
        print(f"Biggest is {num3}")
# ________________________________________
# 11. Smallest Among Three Numbers
# Question: Find the smallest number among three. Explanation: Use comparison logic to determine the minimum value. - Input: A = 7, B = 4, C = 9 - Output: Smallest is: 4

num1=int(input("Enter num1: "))
num2=int(input("Enter num2: "))
num3=int(input("Enter num3: "))
if num1<num2:
    if num1<num3:
        print(f"Smallest is {num1}")
    else:
        print(f"Smallest is {num3}")
else:
    if num2<num3:
        print(f"Smallest is {num2}")
    else:
        print(f"Smallest is {num3}")
# ________________________________________
# 12. Perfect Square or Not
# Question: Check if a number is a perfect square. Explanation: A number is a perfect square if the square of its square root equals the number. - Input: Number = 49 - Output: Perfect square


num=int(input("Enter a number: "))
i=0
while i*i<num:
    i+=1
if i*i==num:
    print("Perfect square")
else:
    print("Not a Perfect square")
# ________________________________________
# 13. Cars Required for Members (Max 5 per car)
# Question: Calculate how many cars are needed for a given number of people. Explanation: Divide total people by 5 and round up using ceiling logic. - Input: Members = 17 - Output: Cars needed = 4

num=int(input("Enter number of people: "))
print(f"Cars needed: {(num//5)+1}")
# ________________________________________
# 14. Second Biggest Among Three Numbers
# Question: Find the second largest number among three inputs. Explanation: Use sorting or nested conditions to find the second largest value. - Input: A = 10, B = 25, C = 18 - Output: Second biggest: 18

num1=int(input("Enter num1: "))
num2=int(input("Enter num2: "))
num3=int(input("Enter num3: "))
if num1>=num2 and num1>=num3:
    if num2>num3:
        print(f"Second biggest: {num2}")
    else:
        print(f"Second biggest: {num3}")
elif num2>=num1 and num2>=num3:
    if num1>num3:
        print(f"Second biggest: {num1}")
    else:
        print(f"Second biggest: {num3}")
else:
    if num1>num2:
        print(f"Second biggest: {num1}")
    else:
        print(f"Second biggest: {num2}")
# ________________________________________
# 15. Leap Year or Not
# Question: Check if a given year is a leap year. Explanation: A year is a leap year if it is divisible by 4, and (not divisible by 100 unless divisible by 400). - Input: Year = 2024 - Output: Leap year

year=int(input("Enter the year: "))
if (year%100!=0 and year%4==0) or year%400==0:
    print("Leap Year")
else:
    print("Not a Leap Year")