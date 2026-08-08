# 1. Rotate Digits Left 
# Definition: Left rotation moves the first digit to the end. 
# Task: Rotate the given number one position to the left. 
# Example Input: 12345 
# Example Output: 23451

num = int(input("Enter a number: "))
temp=num
count = 0
while temp>=10:
    temp//=10
    count +=1
first = temp
print(num%(10**count)*10+first)
# ******************************************************************************

# 2. Rotate Digits Right 
# Definition: Right rotation moves the last digit to the beginning. 
# Task: Rotate the given number one position to the right. 
# Example Input: 12345 
# Example Output: 51234

num=int(input("Enter a number: "))
temp=num
temp//=10
count =0
while temp>0:
    temp//=10
    count +=1
last=num%10
print(last*(10**count)+num//10)
# ******************************************************************************

# 3. Swap First and Last Digits 
# Definition: Exchange the first and last digits. 
# Task: Print the modified number. 
# Example Input: 58391 
# Example Output: 18395

num = int(input("Enter a number: "))
temp = num
mid_count = 0
while temp>10:
    temp//=10
    mid_count +=1
first = temp
last = num%10
mid_num = num%(10**mid_count)//10
print(last*(10**mid_count)+mid_num*10+first)
# ******************************************************************************

# 4. Replace Every Even Digit with 0 
# Definition: Every even digit becomes 0. 
# Task: Transform the number. 
# Example Input: 482763 
# Example Output: 003703

num = int(input("Enter a number: "))
ans=0
place=1
while num>0:
    dig=num%10
    if dig%2==0:
        dig = 0
    ans+=dig*place
    place*=10
    num//=10
print(ans)
# ******************************************************************************

# 5. Replace Every Odd Digit with 9 
# Definition: Every odd digit becomes 9. 
# Task: Transform the number. 
# Example Input: 482763 
# Example Output: 492769

num = int(input("Enter a number: "))
ans=0
place=1
while num>0:
    r=num%10
    if r%2==1:
        r=9
    ans+=r*place
    place*=10
    num//=10
print(ans)
# ******************************************************************************

# 6. Reverse Only Even Digits 
# Definition: Reverse only even digits, keep odd digits fixed. 
# Task: Print transformed number. 
# Example Input: 284673 
# Example Output: 684273

num=int(input("Enter a number: "))
even=[]
temp=num
while temp>0:
    r=temp%10
    if r%2==0:
        even+=[r]
    temp//=10
temp=num
ans=0
place=1
i=0
while temp>0:
    r=temp%10
    if r%2==0:
        r=even[-1-i]
        i+=1
    ans+=r*place
    place*=10
    temp//=10
print(ans)
# ******************************************************************************

# 7. Reverse Only Odd Digits 
# Definition: Reverse only odd digits, keep even digits fixed. 
# Task: Print transformed number. 
# Example Input: 583921
# Example Output: 123985

num = int(input("Enter a number: "))
odd=[]
temp=num
while temp>0:
    r=temp%10
    if r%2==1:
        odd+=[r]
    temp//=10
print(odd)
temp=num
place=1
i=0
ans=0
while temp>0:
    r=temp%10
    if r%2==1:
        r=odd[-1-i]
        i+=1
    ans+=r*place
    place*=10
    temp//=10
print(ans)
# ******************************************************************************

# 8. Move All Zeros to the Front 
# Definition: Move every zero to the beginning. 
# Task: Transform the number. 
# Example Input: 5020301 
# Example Output: 0005231   

num = int(input("Enter a number: "))
temp=num
zeroes=0
while temp>0:
    r=temp%10
    if r==0:
        zeroes+=1
    temp//=10
for i in range(zeroes):
    print(0,end="")
temp=num
dig=[]
while temp>0:
    r=temp%10
    if r!=0:
        dig+=[r]
    temp//=10
for i in range(len(dig)-1,-1,-1):
    print(dig[i],end="")
# ******************************************************************************

# 9. Move All Zeros to the End 
# Definition: Move every zero to the end. 
# Task: Transform the number. 
# Example Input: 5020301 
# Example Output: 5231000

num = int(input("Enter a number: "))
temp=num
zeroes=0
while temp>0:
    r=temp%10
    if r==0:
        zeroes+=1
    temp//=10
temp=num
dig=[]
while temp>0:
    r=temp%10
    if r!=0:
        dig+=[r]
    temp//=10
for i in range(len(dig)-1,-1,-1):
    print(dig[i],end="")
for i in range(zeroes):
    print(0,end="")
# ******************************************************************************

# 10. Remove Every Alternate Digit 
# Definition: Keep only the 1st, 3rd, 5th... digits. 
# Task: Print resulting number. 
# Example Input: 98765432 
# Example Output: 9753

num= int(input("Enter a number: "))
digs=[]
while num>0:
    digs+=[num%10]
    num//=10
print(digs)
for i in range(len(digs)-1,-1,-2):
    print(digs[i],end="")
# ******************************************************************************

# 11. Duplicate Every Digit 
# Definition: Every digit appears twice consecutively. 
# Task: Print transformed number. 
# Example Input: 483 
# Example Output: 448833

num = int(input("Enter a number: "))
dig=[]
while num>0:
    dig += [num%10]
    num//=10
for i in range(len(dig)-1,-1,-1):
    print(dig[i],end="")
    print(dig[i],end="")
# ******************************************************************************

# 12. Insert 0 Between Every Pair of Digits 
# Definition: Insert one zero between consecutive digits. 
# Task: Transform the number. 
# Example Input: 5678 
# Example Output: 5060708

num = int(input("Enter a number: "))
dig=[]
while num>0:
    dig += [num%10]
    num//=10
for i in range(len(dig)-1,0,-1):
    print(dig[i],end="")
    print(0,end="")
print(dig[0])
# ******************************************************************************

# 13. Mirror the Number 
# Definition: Append the reverse to itself. 
# Task: Print mirrored number. .
# Example Input: 357 
# Example Output: 357753

num=int(input("Enter a number: "))
dig=[]
while num>0:
    dig+=[num%10]
    num//=10
for i in range(len(dig)-1,-1,-1):
    print(dig[i],end="")
for i in range(len(dig)):
    print(dig[i],end="")
# ******************************************************************************

# 14. Compress Consecutive Digits 
# Definition: Replace repeated consecutive digits with digit+count.
# Task: Compress the number. 
# Example Input: 11122333344 
# Example Output: 13224342

num=int(input("Enter a number: "))
digs=[]
while num>0:
    r=num%10
    digs+=[r]
    num//=10
count = 1
for i in range(len(digs)-1,0,-1):
    if  digs[i]== digs[i-1]:
        count +=1
    else:
        print(digs[i],end="")
        print(count,end="")
        count=1
print(digs[0],end="")
print(count)
# ******************************************************************************

# 15. Print Digits in Wave Order 
# Definition: First,last,second,second-last... 
# Task: Rearrange digits. 
# Example Input: 123456 
# Example Output: 162534

num = input("Enter a number: ")
left = 0
right = len(num)-1
ans=""
while left<=right:
    ans+=num[left]
    ans+=num[right]
    left+=1
    right-=1
    if left==right:
        ans+=num[left]
        break
print(ans)
# ******************************************************************************

