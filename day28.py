# 1. Remove All Spaces 
# Definition: A space (' ') is a blank character between words. 
# Task: Remove all spaces from the given string. 
# Example Input: Python Programming 
# Example Output: PythonProgramming

string = input("Enter a string: ")
ans=""
i=0
word=""
while i< len(string):
    if string[i]!=" ":
        word += string[i]
    else:
        ans += word
        word=""
    i+=1
if word !="":
    ans += word
print(ans)
# ******************************************************************************

# 2. camelCase to snake_case 
# Definition: camelCase uses capitals after first word; snake_case uses underscores. 
# Task: Convert camelCase to snake_case. 
# Example Input: studentName 
# Example Output: student_name

string = input("Enter a string: ")
i=0
word=""
ans=""
while i<len(string):
    if not(string[i]>="A" and string[i]<="Z"):
        word += string[i]
    else:
        ans += word+"_"+chr(96+ord(string[i])-64)
        word=""
    i+=1
if word !="":
    ans += word
print(ans)
# ******************************************************************************

# 3. snake_case to camelCase 
# Definition: snake_case uses underscores; camelCase capitalizes later words. 
# Task: Convert snake_case to camelCase. 
# Example Input: student_name 
# Example Output: studentName

string = input("Enter a string: ")
i=0
word=""
ans=""
asc_diff=0
while i<len(string):
    if string[i]!="_":
        word += string[i]
    else:
        ans += word+chr(ord(string[i+1])-96+64)
        word=""
        i+=1
    i+=1
if word !="":
    ans +=word
print(ans)
# ******************************************************************************

# 4. Uppercase to Lowercase 
# Definition: Uppercase letters are A-Z. 
# Task: Convert all uppercase letters to lowercase. 
# Example Input: HELLO WORLD 
# Example Output: hello world

string = input("Enter a string: ")
i=0
ans=""
while i<len(string):
    if string[i]==" ":
        ans+=" "
    else:
        ans += chr(ord(string[i])+96-64)
    i+=1
print(ans)
# ******************************************************************************

# 5. Lowercase to Uppercase 
# Definition: Lowercase letters are a-z. 
# Task: Convert all lowercase letters to uppercase. 
# Example Input: python 
# Example Output: PYTHON

string = input("Enter a string: ")
i=0
ans=""
while i<len(string):
    ans += chr(ord(string[i])-96+64)
    i+=1
print(ans)
# ******************************************************************************

# 6. Reverse Every Word 
# Definition: Reverse each word only. 
# Task: Reverse every word. 
# Example Input: Learn Python 
# Example Output: nraeL nohtyP

string = input("Enter a string: ")
i=0
ans=""
word=""
while i<len(string):
    if string[i]!=" ":
        word = string[i]+ word
    else:
        ans+=word+" "
        word=""
    i+=1
if word!="":
    ans += word
print(ans)
# ******************************************************************************

# 7. Remove Duplicate Characters 
# Definition: Keep first occurrence only. 
# Task: Remove duplicate characters. 
# Example Input: programming
# Example Output: progamin

string = input("Enter a string: ")
i=0
ans=""
while i<len(string):
    if string[i] not in ans:
        ans +=string[i]
    i+=1
print(ans)
# ******************************************************************************

# 8. Count Vowels and Consonants 
# Definition: Count vowels and consonants. 
# Task: Print both counts. 
# Example Input: Education 
# Example Output: 
# Vowels:5 
# Consonants:4

string = input("Enter a string: ")
vow = 0
i=0
while i<len(string):
    if string[i] in ["a","e","i","o","u","A","E","I","O","U"]:
        vow +=1
    i+=1
print(f"Vowels:{vow}")
print(f"Consonants:{len(string)-vow}")
# ******************************************************************************

# 9. Replace Multiple Spaces 
# Definition: Extra spaces should become one. 
# Task: Replace multiple spaces with one. 
# Example Input: Python is fun
# Example Output: Python is fun

string = input("Enter a string: ")
i=0
ans=""
word=""
count=0
while i<len(string):
    if string[i]!=" ":
        word += string[i]
        count=0
    else:
        count +=1
        if count==1:
            ans+=word+" "
            word=""
    i+=1
if word!="":
    ans+=word
print(ans)
# ******************************************************************************

# 10. Capitalize Every Word 
# Definition: First letter uppercase. Task: Convert to title case. 
# Example Input: welcome to python 
# Example Output: Welcome To Python

string = input("Enter a string: ")
i=0
ans=""
word=""
while i<len(string):
    if i==0:
        ans += chr(ord(string[i])-96+64)
    else:
        if string[i]!=" ":
            word += string[i]
        else:
            ans +=word + " " +chr(ord(string[i+1])+64-96)
            i+=1
            word=""
    i+=1
if word!="":
    ans += word
print(ans)
# ******************************************************************************

# 11. Print Only Digits 
# Definition: Digits are 0-9. 
# Task: Extract digits. 
# Example Input: AB12CD345 
# Example Output: 12345

string = input("Enter a string: ")
i=0
ans=""
while i<len(string):
    if string[i]>="0" and string[i]<="9":
        ans+=string[i]
    i+=1
print(ans)
# ******************************************************************************

# 12. Print Only Alphabets 
# Definition: Letters only. 
# Task: Remove digits and symbols. 
# Example Input: Pyt#123hon! 
# Example Output: Python

string=input("Enter a string: ")
i=0
ans=""
while i<len(string):
    if (string[i]>="A" and string[i]<="Z")or(string[i]>="a" and string[i]<="z"):
        ans += string[i]
    i+=1
print(ans)
# ******************************************************************************

# 13. Count Words 
# Definition: Words separated by spaces. 
# Task: Count words. 
# Example Input: Python is easy to learn 
# Example Output: 5

string = input("Enter a string: ")
count = 0
i=0
while i<len(string):
    if string[i]==" ":
        count +=1
    i+=1
print(count+1)
# ******************************************************************************

# 14. Check Anagram 
# Definition: Same letters, different order.
# Task: Check anagram. 
# Example Input: listen / silent 
# Example Output: Anagram

string1=input("Enter string 1: ")
freq={}
string2=input("Enter string 2: ")
if len(string1)!=len(string2):
    print("Not an Anagram")
else:
    for i in string1:
        if i not in freq:
            freq[i] = 1
        else:
            freq[i] += 1
    i=0
    anagram = True
    while i<len(string2):
        if string2[i] not in freq or freq[string2[i]]==0:
            anagram = False
            break
        else:
            freq[string2[i]] -=1
        i+=1        
if anagram:
    print("Anagram")
else:
    print("Not an Anagram")
# ******************************************************************************

# 15. Find Longest Word 
# Definition: Longest word has most characters. 
# Task: Print longest word. 
# Example Input: I love programming language 
# Example Output: programming

string = input("Enter a string: ")
longest = ""
i=0
word=""
while i<len(string):
    if string[i]!=" ":
        word+= string[i]
    else:
        if len(word)>len(longest):
            longest = word
        word=""
    i+=1
if word!="":
    if len(word)>len(longest):
        longest = word
print(longest)
# ******************************************************************************

# 16. Remove All Digits 
# Definition: Digits are numeric chars. 
# Task: Remove all digits. 
# Example Input: Room12Block5 
# Example Output: RoomBlock

string = input("Enter a string: ")
i=0
ans=""
while i<len(string):
    if not(string[i]>="0" and string[i]<="9"):
        ans+=string[i]
    i+=1
print(ans)
# ******************************************************************************

# 17. Move Digits to End 
# Definition: Keep letter order. 
# Task: Move digits to end. 
# Example Input: A1B2C34 
# Example Output: ABC1234

string=input("Enter a string: ")
digs=""
chars=""
i=0
while i<len(string):
    if string[i]>="0" and string[i]<="9":
        digs += string[i]
    else:
        chars += string[i]
    i+=1
print(chars+digs)
# ******************************************************************************

# 18. Toggle Case 
# Definition: Swap upper/lower. 
# Task: Toggle every letter. 
# Example Input: PyThOn 
# Example Output: pYtHoN

i=0
ans=""
string=input("Enter a string: ")
while i<len(string):
    if string[i]>="A" and string[i]<="Z":
        ans+=chr(ord(string[i])-64+96)
    else:
        ans+=chr(ord(string[i])+64-96)
    i+=1
print(ans)
# ******************************************************************************

# 19. Palindrome 
# Definition: Reads same both ways. 
# Task: Check palindrome. 
# Example Input: madam 
# Example Output: Palindrome

string=input("Enter a string: ")
left = 0
right = len(string)-1
pal=True
while left<right:
    if string[left]!=string[right]:
        pal = False
        break
    left+=1
    right-=1
if pal:
    print("Palindrome")
else:
    print("Not a Palindrome")
# ******************************************************************************

# 20. Compress Characters 
# Definition: Consecutive repeats become char+count. 
# Task: Compress string. 
# Example Input: aaabbccccdd 
# Example Output: a3b2c4d2

freq={}
string = input("Enter a string: ")
i=0
while i<len(string):
    if string[i] not in freq:
        freq[string[i]] = 1
    else:
        freq[string[i]] += 1
    i+=1
for i in freq:
    print(f"{i}{freq[i]}",end="")