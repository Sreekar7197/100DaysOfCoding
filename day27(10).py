# 1. Find the First Unique Word 
# Problem Definition: A unique word appears exactly once in a sentence. 
# Task: Read a sentence and print the first word that occurs only once. 
# Example Input: 
# cat dog cat fish dog bird 
# Example Output: fish

sent = input("Enter a sentence: ")
word = ""
freq={}
i=0
while i<len(sent):
    if sent[i] != " ":
        word += sent[i]
    else:
        if word not in freq:
            freq[word] = 1
        else:
            freq[word] += 1
        word=""
    i+=1
if word != "":
    if word not in freq:
        freq[word] = 1
    else:
        freq[word] += 1
for i in freq:
    if freq[i]==1:
        print(i)
        break
# ******************************************************************************

# 2. Student Marks Analyzer 
# Problem Definition: Store students and their marks in a dictionary. 
# Task: Read names and marks of N students. Print highest and lowest. 
# Example Input: 
# 4
# Rahul 85 
# Anu 92 
# Kiran 78 
# Meena 90 
# Example Output: 
# Highest : Anu 
# Lowest : Kiran

n=int(input("Enter max students: "))
rec = {}
while n>0:
    name = input("Enter student name: ")
    mar = int(input("Enter marks: "))
    rec[name] = mar
    n-=1
highest = 0
high_name = ""
lowest = list(rec.values())[0]
low_name =""
for i in rec:
    if rec[i]>highest:
        highest = rec[i]
        high_name = i
    if rec[i]<lowest:
        lowest = rec[i]
        low_name = i
print("Highest :",high_name)
print("Lowest :",low_name)
# ******************************************************************************

# 3. Find Missing Alphabets 
# Problem Definition: Determine which lowercase letters are absent. 
# Task: Read a string and print missing lowercase letters. 
# Example Input: 
# abcdefxyz 
# Example Output: 
# g h i j k l m n o p q r s t u v w

string = input("Enter alphabets: ")
for i in range(97,123):
    if chr(i) in string:
        continue
    else:
        print(chr(i),end=" ")
# ******************************************************************************

# 4. Find Common Words Between Two Sentences 
# Problem Definition: Some words may appear in both sentences. 
# Task: Read two sentences and print common words. 
# Example Input: 
# python is easy 
# learning python is fun 
# Example Output: 
# python 
# is

sent1 = input("Enter first sentence: ")
dict1 = {}
i=0
word1=""
while i<len(sent1):
    if sent1[i] !=" ":
        word1 += sent1[i]
    else:
        if word1 not in dict1:
            dict1[word1] = 1
        else:
            dict1[word1] += 1
        word1 = ""
    i+=1
if word1 != "":
    if word1 not in dict1:
        dict1[word1] = 1
    else:
        dict1[word1] += 1
sent2 = input("Enter second sentence: ")
dict2 = {}
j=0
word2=""
while j<len(sent2):
    if sent2[j] !=" ":
        word2 += sent2[j]
    else:
        if word2 not in dict2:
            dict2[word2] = 1
        else:
            dict2[word2] += 1
        word2 = ""
    j+=1
if word2 != "":
    if word2 not in dict2:
        dict2[word2] = 1
    else:
        dict2[word2] += 1
for i in dict1:
    for j in dict2:
        if i == j:
            print(i)
# ******************************************************************************

# 5. Print Words in Descending Frequency 
# Problem Definition: Order words by frequency. 
# Task: Read a sentence and print frequencies.
# Example Input: 
# red blue red green blue red 
# Example Output: 
# red : 3 
# blue : 2 
# green : 1

sent = input("Enter a sentence: ")
freq = {}
i=0
word=""
while i< len(sent):
    if sent[i]!=" ":
        word +=sent[i]
    else:
        if word not in freq:
            freq[word] = 1
        else:
            freq[word] += 1
        word=""
    i+=1
if word !="":
    if word not in freq:
        freq[word] = 1
    else:
        freq[word] += 1
high = 0
for i in freq:
    if freq[i]>high:
        high = freq[i]
for i in range(high,0,-1):
    for word in freq:
        if freq[word] == i:
            print(word,":",freq[word])
# ******************************************************************************

# 6. Detect Duplicate Values 
# Problem Definition: Different keys may share the same value. 
# Task: Read a dictionary and print duplicate values. 
# Example Input:
# A 10 
# B 20 
# C 10 
# D 40 
# E 20 
# Example Output: 
# 10 
# 20

n= int(input("Enter max keys: "))
freq={}
while n>0:
    key = input("Enter a key: ")
    val = int(input("Enter a value: "))
    freq[key] = val
    n-=1
printed={}
for i in freq:
    for j in freq:
        if freq[i] == freq[j] and i!=j and freq[i] not in printed:
            print(freq[i])
            printed[freq[i]] = 1
# ******************************************************************************

# 7. Count Words Starting with Each Alphabet 
# Problem Definition: Group words by first letter. 
# Task: Read a sentence and count words by first letter. 
# Example Input: 
# apple ant ball bat banana cat 
# Example Output: 
# a : 2 
# b : 3 
# c : 1

sent = input("Enter a sentence: ")
freq = {}
i=0
word=""
while i<len(sent):
    if sent[i]!=" ":
        word += sent[i]
    else:
        if word[0] not in freq:
            freq[word[0]] = 1
        else:
            freq[word[0]] += 1
        word = ""
    i+=1
if word !="":
    if word[0] not in freq:
        freq[word[0]] = 1
    else:
        freq[word[0]] += 1
for i in freq:
    print(f"{i} : {freq[i]}")
# ******************************************************************************

# 8. Build a Character Position Dictionary 
# Problem Definition: Store positions of each character. 
# Task: Read a string and print positions. 
# Example Input: 
# banana 
# Example Output: 
# b : 0 
# a : 1 3 5 
# n : 2 4

string = input("Enter a word: ")
i=0
pos={}
count =0
while i<len(string):
    if string[i] not in pos:
        pos[string[i]]=str(count)
    else:
        pos[string[i]]+= " "+str(count)
    count +=1
    i+=1
for i in pos:
    print(i,":",pos[i])
# ******************************************************************************

# 9. Find the Longest Word(s) 
# Problem Definition: More than one longest word may exist. 
# Task: Read a sentence and print every longest word.
# Example Input: 
# python programming java development 
# Example Output: 
# programming 
# development

sent = input("Enter a sentence: ")
i=0
freq={}
word=""
count=0
while i < len(sent):
    if sent[i] !=" ":
        word +=sent[i]
    else:
        freq[word] = count
        word = ""
        count=0
    count +=1
    i+=1
if word !="":
    freq[word] = count
for i in freq:
    for j in freq:
        if freq[i]==freq[j] and i!=j:
            print(i)
# ******************************************************************************

# 10. Mini Inventory Manager 
# Problem Definition: Search products using a dictionary. 
# Task: Read products then search for one. 
# Example Input: 3 
# Pen 20 
# Book 15 
# Pencil 40 
# Book 
# Example Output: 
# 15

n=int(input("Enter max products: "))
prod={}
while n>0:
    name = input("Enter product name: ")
    price =int(input("Enter the price: "))
    prod[name] = price
    n-=1
search = input("Enter the item you want the price for: ")
print(prod[search])