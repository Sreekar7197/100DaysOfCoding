# 1. Area of Square
# Question: Calculate the area of a square. 
# - Formula: Area = side × side 
# - Input: - Side = 5 
# - Output: - Area of square is: 25

side = int(input("Enter lenth of side: "))
print(f"Area of square: {side*side}")
# ________________________________________

# 2. Area of Rectangle
# Question: Calculate the area of a rectangle. 
# - Formula: Area = length × breadth 
# - Input: - Length = 6 - Breadth = 4 - 
# Output: - Area of rectangle is: 24

length=int(input("Enter Length: "))
breadth=int(input("Enter Breadth: "))
print(f"Area of rectangle: {length*breadth}")
# ________________________________________

# 3. Area of Triangle
# Question: Calculate the area of a triangle using base and height. 
# - Formula: Area = (1/2) × base × height 
# - Input: - Base = 8 - Height = 5 
# - Output: - Area of triangle is: 20.0

base=int(input("enter the base length: "))
height = int(input("Enter the height of the triangle: "))
print(f"Area of triangle: {0.5*base*height}")
# ________________________________________

# 4. Perimeter of Square
# Question: Calculate the perimeter of a square. 
# - Formula: Perimeter = 4 × side 
# - Input: - Side = 6 
# - Output: - Perimeter of square is: 24

side = int(input("Enter side length: "))
print(f"Perimeter of square is: {4*side}")
# ________________________________________

# 5. Perimeter of Rectangle
# Question: Calculate the perimeter of a rectangle. 
# - Formula: Perimeter = 2 × (length + breadth) 
# - Input: - Length = 5 - Breadth = 3 
# - Output: - Perimeter of rectangle is: 16

length=int(input("Enter length: "))
breadth=int(input("Enter breadth: "))
print(f"Perimeter of rectangle = {2*(length+breadth)}")
# ________________________________________

# 6. Perimeter of Triangle
# Question: Calculate the perimeter of a triangle. 
# - Formula: Perimeter = side1 + side2 + side3 
# - Input: - Side1 = 5, Side2 = 6, Side3 = 7 
# - Output: - Perimeter of triangle is: 18

side1=int(input("Enter length of a side: "))
side2=int(input("Enter length of a side: "))
side3=int(input("Enter length of a side: "))
print(f"Perimeter of triangle = {side1+side2+side3}")
# ________________________________________

# 7. Break Amount into 1000s, 500s, and Remaining Change
# Question: Break the total amount into denominations. 
# - Input: - Amount = 3700 
# - Output: - 1000s: 3 - 500s: 1 - Remaining: 200

amt = int(input("Enter total amount: "))
thou=0
five_hun=0
thou = amt//1000
amt%=1000
five_hun = amt//500
amt%=500
print(f"1000s: {thou} 500s: {five_hun} Remaining: {amt}")

# ________________________________________
# 8. Convert Seconds into Hours, Minutes, and Seconds
# Question: Convert total seconds into hours, minutes, and seconds. - Input: - Total seconds = 3672 - Output: - Hours: 1 - Minutes: 1 - Seconds: 12

sec = int(input("Enter total seconds: "))
hrs=sec//3600
sec%=3600
min=sec//60
sec%=60
print(f"Hours: {hrs}, Minutes: {min}, Seconds: {sec}")
# ________________________________________
# 9. Sum of Marks (Maths, Physics, Chemistry)
# Question: Calculate the sum of marks in 3 subjects. - Input: - Maths = 85 - Physics = 90 - Chemistry = 88 - Output: - Total marks: 263

mat=int(input("Enter marks in math: "))
phy=int(input("Enter marks in phy: "))
chem=int(input("Enter marks in chem: "))
print(f"Total marks: {mat+phy+chem}")
# ________________________________________
# 10. Average of Marks (Maths, Physics, Chemistry)
# Question: Calculate the average of marks in 3 subjects. - Input: - Maths = 85 - Physics = 90 - Chemistry = 88 - Output: - Average marks: 87.67

mat=int(input("Enter marks in math: "))
phy=int(input("Enter marks in phy: "))
chem=int(input("Enter marks in chem: "))
print(f"Average marks: {(mat+phy+chem)/3}")