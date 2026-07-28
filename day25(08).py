# 1. Zig-Zag Star Pattern 
# Task: Read N and print a zig-zag pattern using *. 
# *       *       *
#  *     * *     *
#   *   *   *   *
#    * *     * *
#     *       *

n = int(input("Enter N: "))
for i in range(n):
    for j in range(4*(n-1)+1):
        if (j==i or j==2*(n-1)-i or j==2*(n-1)+i or j==4*(n-1)-i):
            print("*", end="")
        else:
            print(" ", end="")
    print()
# ******************************************************************************

# 2. Hourglass Pattern 
# Task: Read N (odd) and print an hourglass using *. 
# ******* 
#  ***** 
#   *** 
#    * 
#   *** 
#  ***** 
# *******

n= int(input("Enter an odd number: "))
for i in range(n//2+1):
    print(" "*i,"*"*(n-2*i))
for i in range(n//2-1,-1,-1):
    print(" "*i,"*"*(n-2*i))
# ******************************************************************************

# 3. Hollow Diamond with Border 
# Task: Print a hollow diamond.
#     *
#    * *
#   *   *
#  *     *
# *       *
#  *     *
#   *   *
#    * *
#     *

n=int(input("Enter a number: "))
for i in range(1,n+1):
    print(" "*(n-i),end="")
    for j in range(1,i+1):
        if i==1 or j==1 or j==i:
            print("* ",end="")
        else:
            print("  ",end="")
    print()
for i in range(n-1,0,-1):
    print(" "*(n-i),end="")
    for j in range(1,i+1):
        if i==1 or j==1 or j==i:
            print("* ",end="")
        else:
            print("  ",end="")
    print()
# ******************************************************************************

# 4. Binary Triangle 
# Task: Print alternating 0s and 1s.
#  1
#  01
#  101
#  0101
#  10101

n= int(input("Enter number of rows: "))
for i in range(1,n+1):
    for j in range(1,i+1):
        if (i+j)%2==0:
            print("1",end="")
        else:
            print("0",end="")
    print()
# ******************************************************************************

# 5. Snake Pattern 
# Task: Print numbers in a snake arrangement.
#  1 2 3 4 5
#  10 9 8 7 6
#  11 12 13 14 15
#  20 19 18 17 16
#  21 22 23 24 25

n=int(input("Enter number of rows: "))
start = 1
for i in range(n):
    if i%2==0:
        for j in range(5):
            print(start+j,end=" ")
    else:
        for j in range(4,-1,-1):
            print(start+j,end=" ")
    start +=5
    print()
# ******************************************************************************

# 6. Mirror Number Pyramid Task: Print a mirrored number pyramid.
#         1
#       2 1
#     3 2 1
#   4 3 2 1
# 5 4 3 2 1

n=int(input("Enter number of columns: "))
for i in range(1,n+1):
    print("  "*(n-i+1),end="")
    for j in range(i,0,-1):
        print(j,end=" ")
    print()
# ******************************************************************************

# 7. Cross Number Pattern 
# Task: Print row and column numbers where they intersect.
# 1   1
#  2 2
#   3
#  4 4
# 5   5

n=int(input("Enter number of rows: "))
for i in range(1,n+1):
    for j in range(1,n+1):
        if j==i or j==n-i+1:
            print(i,end="")
        else:
            print(" ",end="")
    print()
# ******************************************************************************

# 8. Hollow Pascal Outline 
# Task: Print only the boundary values of Pascal's triangle.
#  1
#  1 1
#  1   1
#  1     1
#  1 1 1 1 1

n=int(input("Enter number of rows: "))
for i in range(1,n+1):
    for j in range(1,i+1):
        if i==1 or i==n or j==1 or j==i:
            print(1,end=" ")
        else:
            print(" ",end=" ")
    print()
# ******************************************************************************

# 9. Spiral Stars 
# Task: Print a spiral using stars.
#  *******
#        *
#  ***** *
#  *   * *
#  * * * *
#  *     *
#  *******

n = int(input("Enter number of rows: "))
for i in range(n):
    for j in range(n):
        if (i==0 or i==n-1 or (j==n-1 and i<=n-2) or (i==2 and j<=n-3) or
            (j==0 and i>=2) or (j==4 and 2<=i<=4) or
            (i==4 and (j==0 or j==2 or j==4 or j==6))):
            print("*", end="")
        else:
            print(" ", end="")
    print()
# ******************************************************************************

# 10. Wave Number Pattern 
# Task: Print numbers in a vertical wave.
#  1 2 3 4 5
#  10 9 8 7 6
#  11 12 13 14 15
#  20 19 18 17 16
#  21 22 23 24 25

n=int(input("Enter max number: "))
start = 1
for i in range(n):
    if i%2==0:
        for j in range(5):
            print(start+j,end=" ")
    else:
        for j in range(4,-1,-1):
            print(start+j,end=" ")
    start +=5
    print()