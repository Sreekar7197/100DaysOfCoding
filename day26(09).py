# 1. Count Frequency of Each Character 
# Problem Definition: A dictionary can store how many times each character appears. 
# Task: Read a string and print the frequency of every character. 
# Example Input: programming Example Output:
#  p : 1
#  r : 2
#  o : 1
#  g : 2
#  a : 1
#  m : 2
#  i : 1
#  n : 1

string = input("Enter a string: ")
freq = {}
i=0
while i<len(string):
    if string[i] not in freq:
        freq[string[i]]=1
    else:
        freq[string[i]]+=1
    i+=1
print(freq)
# ******************************************************************************

# 2. Find the First Repeating Character 
# Problem Definition: The first repeating character appears more than once. 
# Task: Read a string and print the first repeating character. 
# Example Input: datastructure 
# Example Output: a

string = input("Enter a string: ")
freq = {}
i=0
while i<len(string):
    if string[i] not in freq:
        freq[string[i]] = 1
    else:
        freq[string[i]] +=1
        print(string[i])
        break
    i+=1
# ******************************************************************************

# 3. Group Students by Grade 
# Problem Definition: Store multiple values under the same category. 
# Task: Read student names and grades. Print students grouped by grade. 
# Example Input:
# 5 
# Rahul A 
# Anu B 
# Kiran A 
# Meena C 
# Ajay B 
# Example Output:
# A : Rahul Kiran 
# B : Anu Ajay 
# C : Meena

n=int(input("Enter max students: "))
freq={}
while n>0:
    name = input("Enter student name: ")
    grade = input("Enter student grade: ")
    if grade not in freq:
        freq[grade] = name
    else:
        freq[grade] += " "+name
    n-=1
print(freq)
# ******************************************************************************

# 4. Find the Most Frequent Word 
# Problem Definition: Words may repeat. 
# Task: Read a sentence and print the word with the highest frequency. 
# Example Input: python is easy python is powerful python 
# Example Output: python

freq = {}
sent=input("Enter a sentence: ")
word = ""
i=0
while i < len(sent):
    if sent[i] != " ":
        word += sent[i]
    else:
        if word not in freq:
            freq[word] = 1
        else:
            freq[word] += 1
        word = ""
    i+=1
if word !="":
    if word not in freq:
        freq[word] = 1
    else:
        freq[word] += 1
high_word = ""
max_count = 0 
j=0
for j in freq:
    if freq[j] > max_count:
        max_count= freq[j]
        max_word = j
print(max_word)
# ******************************************************************************

# 5. Merge Two Dictionaries 
# Problem Definition: Add values for duplicate keys. 
# Task: Read two dictionaries and merge them. 
# Example Input: 
# A 10, B 20
# B 30, C 40 
# Example Output: 
# A : 10 
# B : 50 
# C : 40

n1=int(input("Enter number of elements in dict1: "))
dict1={}
dict2={}
while n1>0:
    key = input("Enter the key: ")
    val = int(input("Enter the value: "))
    dict1[key] = val
    n1-=1
n2=int(input("Enter number of elements in dict2: "))
while n2>0:
    key = input("Enter the key: ")
    val = int(input("Enter the value: "))
    dict2[key] = val
    n2-=1
for i in dict2:
    if i in dict1:
        dict1[i] += dict2[i]
    else:
        dict1[i] = dict2[i]
print(dict1)
# ******************************************************************************

# 6. Find Employees Having the Same Salary 
# Problem Definition: Different keys can share the same value. 
# Task: Read employee names and salaries. Print employees having identical salaries. 
# Example Input: 
# Rahul 30000 
# Anu 25000 
# Kiran 30000 
# Meena 40000 
# Example Output: 
# 30000 : Rahul Kiran

n=int(input("Enter number of employees: "))
data = {}
while n>0:
    name = input("Enter name of employee: ")
    sal = int(input("Enter salary of employee: "))
    data[name] = sal
    n-=1
for i in data:
    for j in data:
        if data[i]==data[j] and i!=j:
            print(f"{data[i]} : {i}")
# ******************************************************************************

# 7. Build an Inverted Dictionary 
# Problem Definition: Swap every key with its value. 
# Task: Read a dictionary and create its inverse. 
# Example Input: 
# A : Apple 
# B : Ball 
# C : Cat 
# Example Output: 
# Apple : A 
# Ball : B 
# Cat : C

n=int(input("Enter max values: "))
dictionary = {}
while n>0:
    key = input("Enter a key: ")
    val = input("Enter its value: ")
    dictionary[key]=val
    n-=1
for i in dictionary:
    print(dictionary[i],":",i)
# ******************************************************************************

# 8. Count the Frequency of Each Number 
# Problem Definition: Count integers using a dictionary. 
# Task: Read N integers and print frequencies. 
# Example Input: 
# 8 
# 4 
# 2 
# 4 
# 1 
# 2 
# 4 
# 5 
# 1 
# Example Output: 
# 1 : 2 
# 2 : 2
# 4 : 3 
# 5 : 1

n=int(input("Enter max number:"))
freq={}
while n>0:
    num = int(input("Enter a number: "))
    if num not in freq:
        freq[num]=1
    else:
        freq[num]+=1
    n-=1
print(freq)
# ******************************************************************************

# 9. Find Keys Having the Maximum Value 
# Problem Definition: More than one key can have the maximum value. 
# Task: Read a dictionary and print all keys with the maximum value. 
# Example Input: 
# Math : 95 
# Science : 90 
# English : 95 
# Example Output: 
# Math 
# English

n=int(input("Enter max subjects: "))
marks = {}
while n>0:
    sub = input("Enter the subject name: ")
    mar = int(input("Enter marks: "))
    marks[sub] = mar
    n-=1
highest = 0
for i in marks:
    if marks[i]>highest:
        highest = marks[i]
for i in marks:
    if marks[i] == highest:
        print(i)
# ******************************************************************************

# 10. Build a Phone Directory 
# Problem Definition: Search efficiently using a dictionary. 
# Task: Store names and phone numbers, then search by name. 
# Example Input: 
# 3 
# Rahul 9876543210 
# Anu 9123456789 
# Kiran 9988776655 
# 
# Anu 
# Example Output: 
# 9123456789

n=int(input("Enter max people: "))
dir = {}
while n>0:
    name = input("Enter the name: ")
    phno = int(input("Enter the phone number: "))
    dir[name] = phno
    n-=1
search = input("Enter the name to search: ")
for i in dir:
    if i == search:
        print(dir[i])