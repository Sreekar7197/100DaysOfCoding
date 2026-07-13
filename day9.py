# 1. Digit Mirror Sum 
# Task: Given a number, add digits from opposite ends and store the results. If one digit remains in the middle, keep it as it is. 
# Example Input: 
# Input: 48391 
# Calculation: 
# 4+1=5 
# 8+9=17 
# 3 stays as it is 
# Example Output: Output: [5,17,3]

num = input("Enter a number: ")
calc = []
i = 0
j = len(num)-1
while i<j:
    calc+= [int(num[i])+int(num[j])]
    i+=1
    j-=1
    if i==j:
        calc+=[int(num[i])]
print(calc)
# ******************************************************************************

# 2. Lonely Digit Finder 
# Task: Find the digit that appears exactly once in a number. 
# Example Input: 
# Input: 122334455 
# Example Output: 
# Output: 1

num = input("Enter a number: ")
freq ={}
for i in num:
    if i in freq:
        freq[i]+=1
    else:
        freq[i] = 1
for i in freq:
    if freq[i] == 1:
        print(i)
# ******************************************************************************

# 3. Mountain Number Checker 
# Task: Check whether digits strictly increase and then strictly decrease. Example Input: 
# Input: 123454321 
# Example Output: 
# Output: True 
# Input: 123456 
# Output: False

num = input("Enter a number: ")
i = 0
j = len(num)-1
not_mount = 0
while i<j:
    if num[i] != num[j]:
        not_mount +=1
        break
    i+=1
    j-=1  
if not_mount == 0:
    print("True")
else:
    print("False")
# ******************************************************************************

# 4. Circular Digit Rotation Maximum 
# Task: Generate all circular rotations of a number and return the largest rotation. 
# Example Input:
# Input: 1973 
# Rotations: 1973 9731 7319 3197 
# Example Output: 
# Output: 9731

num = input("Enter a number: ")
rotations = []
for i in num:
    temp_rot = i
    for j in num:
        if i !=j :
            temp_rot += j
    rotations += [int(temp_rot)]
max = 0
for i in rotations:
    if i > max:
        max = i
print(max)
# ******************************************************************************

# 5. Digit Distance Sum 
# Task: Find the sum of absolute differences between neighboring digits. 
# Example Input: 
# Input: 82746 
# |8−2| + |2−7| + |7−4| + |4−6| 
# Example Output: 
# Output: 18

num = input("Enter a number: ")
dist_sum = 0
for i in range(len(num) - 1):
    dist_sum += abs(int(num[i]) - int(num[i + 1]))
print(dist_sum)
# ******************************************************************************

# 6. Hidden Pair Product 
# Task: Multiply each pair of neighboring digits and combine the results into one number. 
# Example Input: 
# Input: 2345 
# 2×3=6 3×4=12 4×5=20 
# Example Output:
# Output: 61220

num = input("Enter a number: ")
tot=''
for i in range(len(num)-1):
    tot += str(int(num[i])*int(num[i+1]))
print(tot)
# ******************************************************************************

# 7. Digit Wave Number 
# Task: Check whether digits form a wave pattern: 
# 1st < 2nd 
# 2nd > 3rd 
# 3rd < 4th and so on 
# Example Input: 
# Input: 163849 
# 1<6 
# 6>3 
# 3<8 
# 8>4 
# 4<9 
# Example Output: 
# Output: True

num = input("Enter a number: ")
check = 0
for i in range(len(num)-1):
    if i % 2 == 0:
        if num[i] >= num[i + 1]:
            check += 1
            break
    else:
        if num[i] <= num[i + 1]:
            check += 1
            break
if check>0:
    print("False")
else:
    print("True")
# ******************************************************************************

# 8. Number DNA Match 
# Task: Given two numbers of equal length, count how many digits match in the same positions. 
# Example Input: 
# Input: 
# 123456 
# 153406 
# Example Output: 
# Output: 4

num1=input("Enter a number: ")
num2=input("Enter a number: ")
count = 0    
for i in range(len(num1)):
    for j in range(len(num2)):
        if num1[i] == num2[j] and i==j:
            count+=1
print(count)
# ******************************************************************************

# 9. Prime Gap Digit Number
# Task: Find absolute differences between adjacent digits and check whether all differences are prime numbers. 
# Example Input: 
# Input: 1638 
# Differences: 
# |1−6|=5 
# |6−3|=3 
# |3−8|=5 
# Example Output: 
# Output: True

num = input("Enter a number: ")
result = True
for i in range(len(num)-1):
    diff = abs(int(num[i]) - int(num[i + 1]))
    if diff < 2:
        result = False
        break
    for j in range(2, int(diff//2)):
        if diff % j == 0:
            result = False
            break
print(result)
# ******************************************************************************

# 10. Digit Gravity Simulation 
# Task: Move all 0s to the left while keeping the order of all other digits unchanged. 
# Example Input: 
# Input: 12030405 
# Example Output: 
# Output: 0012345

num = input("Enter a number: ")
zeroes = ""
digits = ""
for i in num:
    if i == '0':
        zeroes +=i
    else:
        digits +=i
print(zeroes+digits)
# ******************************************************************************