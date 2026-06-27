# 1. Find Common Elements Between Two Lists
# Given: a=[4,7,2,9,1] b=[8,2,1,6,4]
# Explanation: Compare each element of first list with every element of second list using nested loops. Print common values and avoid duplicates. 
# Expected Output: 
# 4 
# 2 
# 1

a=[4,7,2,9,1] 
b=[8,2,1,6,4]
for i in a:
    for j in b:
        if i==j:
            print(i)
# ******************************************************************************

# 2. Find First Pair with Target Sum 
# Given: arr=[2,5,7,9,1,4] target=11 
# Explanation: Compare each element with all remaining elements and stop immediately after finding first matching pair. 
# Expected Output:
# 2 9

arr=[2,5,7,9,1,4] 
target=11
for i in arr:
    for j in arr:
        if i+j == target:
            print(i,j)
    break
# ******************************************************************************

# 3. Frequency Count Without count()
# Given: arr=["apple","banana","apple","orange","banana","apple"] 
# Explanation: Count occurrences manually using nested loops without dictionary or count(). 
# Expected Output: 
# apple : 3 
# banana : 2 
# orange : 1

arr=["apple","banana","apple","orange","banana","apple"]
occ=[]
for i in  arr:
    count = 0
    if i in occ:
        continue
    for j in arr:
        if i==j:
            count+=1
    occ += [i]
    print(f"{i} : {count}")
# ******************************************************************************

# 4. Find Duplicate Strings 
# Given: 
# names=["Raj","John","Raj","Mike","John","Raj"]
# Explanation: Traverse and identify repeated strings. Print duplicates once only. 
# Expected Output: 
# Raj 
# John

names=["Raj","John","Raj","Mike","John","Raj"]
done = []
for i in names:
    count = 0
    if i in done:
        continue
    for j in names:
        if i==j:
            count+=1
    done += [i]
    if count>1:
        print(i)
# ******************************************************************************

# 5. Matrix Equality Check 
# Given: m1=[[1,2,3],[4,5,6]] m2=[[1,2,3],[4,5,6]] 
# Explanation: Compare every row and column value. 
# Expected Output:
# Matrices are equal

m1=[[1,2,3],[4,5,6]] 
m2=[[1,2,3],[4,5,6]]
equal = 0
for i in range(len(m1)):
    for j in range(len(m1[0])):
        if m1[i][j]==m2[i][j]:
            equal +=1
if equal >0:
    print("Matrices are equal")
# ******************************************************************************

# 6. Find Missing Elements Between Two Lists 
# Given: a=[1,2,3,4,5,6] b=[2,4,6] 
# Explanation: Print values from first list that do not exist in second list. Expected Output: 
# 1 
# 3 
# 5

a=[1,2,3,4,5,6] 
b=[2,4,6]
for i in a:
    count = 0
    for j in b:
        if i == j:
            count+=1
    if count==0:
        print(i)
# ******************************************************************************

# 7. Longest Matching Consecutive Characters 
# Given: s1="ABCDXYZEF" s2="XYZABCDPQ" 
# Explanation: Find longest consecutive matching sequence using nested loops. Expected Output: 
# 4

s1="ABCDXYZEF" 
s2="XYZABCDPQ"
match = 0
for i in range(len(s1)):
    for j in range(len(s2)):        
        if s1[i] == s2[j]:
            count = 0
            while s1[i] == s2[j]:
                count+=1
                i+=1
                j+=1    
    if count>match:
        match = count
print(match)
# ******************************************************************************

# 8. Find All Pairs With Same Sum 
# Given: arr=[1,2,3,4,5] 
# Explanation: Compare pair sums and identify equal sums. 
# Example Output: 
# 1 4 = 5 
# 2 3 = 5

arr=[1,2,3,4,5]
same = []
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        s = arr[i]+arr[j]
        same += [[arr[i],arr[j],s]]
for i in range(len(same)):
    for j in range(i+1,len(same)):
        if same[i][2] == same[j][2]:
            print(same[i][0],same[i][1],"=",same[i][2])
            print(same[j][0],same[j][1],"=",same[j][2])
# ******************************************************************************

# 9. Check Subsequence 
# Given: a=[1,3,5,7,9,11] b=[3,7,11]
# Explanation: Verify whether second list appears in same order inside first list. 
# Expected Output: 
# Subsequence exists

a=[1,3,5,7,9,11]
b=[3,7,11]                
order_list = []
for i in a:
    for j in b:
        if i==j and i not in order_list:
            order_list += [i]
if order_list == b:
    print("Subsequence exists")
else:
    print("Subsequence does not exist")
# ******************************************************************************

# 10. Find Maximum Repeating String 
# Given: words=["cat","dog","cat","bird","cat","dog"] 
# Explanation: Find string with highest occurrence without using dictionary. Expected Output: 
# cat 
# 3

words=["cat","dog","cat","bird","cat","dog"]
done=[]
max_rep = 0
max_word = ''
for i in words:
    if i in done:
        continue
    count = 0
    for j in words:
        if i == j:
            count+=1
    done +=[i]
    if count>max_rep:
        max_rep=count
        max_word = i
print(max_word)
print(max_rep)