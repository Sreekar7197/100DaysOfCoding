# Problem 1: Student Grade 
# Definition: Use if, elif, and else statements to classify a student's marks into grades. 
# Task: Read the student's marks (0–100). 
# 90–100 → Grade A 
# 75–89 → Grade B 
# 60–74 → Grade C 
# 35–59 → Grade D 
# Below 35 → Fail 
# Example Input: 82 
# Example Output: Grade B 

mar=int(input("Enter students marks: "))
if mar>=90 and mar<=100:
    print("Grade A")
elif mar>=75 and mar<=89:
    print("Grade B")
elif mar>=60 and mar<=74:
    print("Grade C")
elif mar>=35 and mar<=59:
    print("Grade D")
else:
    print("Fail")
# ******************************************************************************

# Problem 2: Traffic Signal 
# Definition: Use conditional statements to decide the action based on the traffic signal color. 
# Task: Read the traffic signal color. 
# Red → Stop 
# Yelow → Get Ready 
# Green → Go 
# Any other color → Invalid Signal 
# Example Input: Green 
# Example Output: Go 

light=int(input("Enter signal colour: "))
if light=="Red":
    print("Stop")
elif light=="Yellow":
    print("Get Ready")
elif light=="Green":
    print("Go")
else:
    print("Invalid Signal")
# ******************************************************************************

# Problem 3: Movie Ticket Price 
# Definition: Use conditions to determine the ticket price based on age. 
# Task: Read age. 
# Below 5 → Free 
# 5–17 → ₹100 
# 18–59 → ₹200 
# 60 and above → ₹120 
# Example Input: 25 
# Example Output: Ticket Price: ₹200 

age=int(input("Enter age: "))
if age<5:
    price=0
elif age>=5 and age<=17:
    price =100
elif age>=18 and age<=59:
    price =200
else:
    price = 120
if age<5:
    print("Free")
else:
    print("Ticket Price:",price)
# ******************************************************************************

# Problem 4: Electricity Bill Category 
# Definition: Use conditional statements to classify electricity usage. 
# Task: Read units consumed. 
# 0–100 → Domestic 
# 101–300 → Standard 
# 301–500 → Premium 
# Above 500 → Heavy User 
# Example Input: 280 
# Example Output: Standard 

units=int(input("Enter units consumed: "))
if units <=0 and units<=100:
    print("Domestic")
elif units <=101 and units<=300:
    print("Standard")
elif units <=301 and units<=500:
    print("Premium")
else:
    print("Heavy User")
# ******************************************************************************

# Problem 5: Bank Loan Eligibility 
# Definition: Use conditions to classify a customer's credit score. 
# Task: Read the credit score. 
# 750 and above → Excelent 
# 650–749 → Good 
# 550–649 → Average 
# Below 550 → Not Eligible 
# Example Input: 720 
# Example Output: Good 

cr=int(input("Enter customer's credit score: "))
if cr>=750:
    print("Excellent")
elif cr<=749 and cr>=650:
    print("Good")
elif cr<=649 and cr>=550:
    print("Average")
else:
    print("Not Eligible")
# ******************************************************************************

# Problem 6: BMI Category 
# Definition: Use conditions to determine BMI status. 
# Task: Read BMI value. 
# Below 18.5 → Underweight 
# 18.5–24.9 → Normal 
# 25–29.9 → Overweight 
# 30 and above → Obese 
# Example Input: 27.4 
# Example Output: Overweight 

bmi = float(input("Enter BMI value: "))
if bmi<18.5:
    print("Underweight")
elif bmi>=18.5 and bmi<=24.9:
    print("Normal")
elif bmi>=25 and bmi<=29.9:
    print("Overweight")
else:
    print("Obese")
# ******************************************************************************

# Problem 7: Internet Speed Rating 
# Definition: Classify internet speed using conditional statements. 
# Task: Read internet speed (Mbps). 
# Below 10 → Slow 
# 10–50 → Average 
# 51–100 → Fast 
# Above 100 → Very Fast 
# Example Input: 75 
# Example Output: Fast 

speed=int(input("Enter internet speed in mbps: "))
if speed<10:
    print("Slow")
elif speed>=10 and speed<=50:
    print("Average")
elif speed>=51 and speed<=100:
    print("Fast")
else:
    print("Very fast")
# ******************************************************************************

# Problem 8: Restaurant Feedback 
# Definition: Display feedback based on the customer's rating. 
# Task: Read rating (1–5). 
# Example Input: 5 
# Example Output: Excelent 

rating = int(input("Enter your rating: "))
if rating ==5:
    print("Excellent")
elif rating==4:
    print("Very Good")
elif rating==3:
    print("Good")
elif rating==2:
    print("Average")
else:
    print("Bad")
# ******************************************************************************

# Problem 9: Cricket Score 
# Definition: Determine batting performance using runs scored. 
# Task: Read runs. 
# 0 → Duck 
# 1–49 → Good 
# 50–99 → Half Century 
# 100 or more → Century 
# Example Input: 108 
# Example Output: Century 

runs=int(input("Enter runs: "))
if runs==0:
    print("Duck")
elif runs>=1 and runs<=49:
    print("Good")
elif runs>=50 and runs<=99:
    print("Half Century")
else:
    print("Century")
# ******************************************************************************

# Problem 10: Attendance Status 
# Definition: Check eligibility based on attendance percentage. 
# Task: Read attendance percentage. 
# 90–100 → Excelent 
# 75–89 → Eligible 
# 60–74 → Warning 
# Below 60 → Not Eligible 
# Example Input: 78 
# Example Output: Eligible 

att=int(input("Enter Attendance Percentage: "))
if att>=90 and att<=100:
    print("Excellent")
elif att>=75 and att<=89:
    print("Eligible")
elif att>=64 and att<=74:
    print("Warning")
else:
    print("Not Eligible")
# ******************************************************************************

# Problem 11: Courier Weight Charge 
# Definition: Use conditions to determine the courier category. 
# Task: Read parcel weight and display the shipping category. 
# Example Input: 8 
# Example Output: Medium Parcel 

wt=int(input("Enter parcel weight: "))
if wt<=5:
    print("Small Parcel")
elif wt<=10:
    print("Medium Parcel")
else:
    print("Large Parcel")
# ******************************************************************************

# Problem 12: Mobile Battery Status 
# Definition: Display battery status based on battery percentage. 
# Task: Read battery percentage. 
# Example Input: 18 
# Example Output: Low Battery 

bat=int(input("Enter battery percentage: "))
if bat<=30:
    print("Low Battery")
elif bat<=80:
    print("Medium Battery")
else:
    print("High Battery")
# ******************************************************************************

# Problem 13: Air Conditioner Mode 
# Definition: Suggest the AC mode based on room temperature. 
# Task: Read room temperature. 
# Example Input: 35 
# Example Output: Cooling Mode 

temp=int(input("Enter room temperature: "))
if temp>=26:
    print("Low mode")
elif temp>=29:
    print("Medium mode")
else:
    print("Cooling mode")
# ******************************************************************************

# Problem 14: Rainfall Level 
# Definition: Determine rainfall intensity. 
# Task: Read rainfall in millimeters. 
# Example Input: 55 
# Example Output: Heavy Rain 

mm=int(input("Enter rainfall level in mm: "))
if mm<=20:
    print("Low rain")
elif mm<=35:
    print("Medium rain")
else:
    print("Heavy rain")
# ******************************************************************************

# Problem 15: Water Tank Status 
# Definition: Display the water tank status. 
# Task: Read water level percentage. 
# Example Input: 95 
# Example Output: Ful 

stat = int(input("enter water level percentage: "))
if stat>=80:
    print("Full")
elif stat>=30:
    print("Medium")
else:
    print("Low")
# ******************************************************************************

# Problem 16: Exam Rank 
# Definition: Assign a class based on total marks. 
# Task: Read marks and display the class. 
# Example Input: 88 
# Example Output: First Class 

mar=int(input("Enter marks: "))
if mar>=85:
    print("First class")
elif mar>=75 and mar<=84:
    print("Second Class")
elif mar>=50 and mar<=74:
    print("Third class")
elif mar>=35 and mar<=49:
    print("Fourth Class")
else:
    print("Fail")
# ******************************************************************************

# Problem 17: Salary Tax Slab 
# Definition: Determine the salary tax slab. 
# Task: Read annual salary. 
# Example Input: 850000 
# Example Output: Medium Tax Slab 

sal=int(input("Enter Annual Sal: "))
if sal<=500000:
    print("Low Tax Slab")
elif sal<=1200000:
    print("Medium Tax Slab")
else:
    print("High Tax Slab")
# ******************************************************************************

# Problem 18: Hotel Room Type 
# Definition: Suggest a room based on the customer's budget. 
# Task: Read the budget. 
# Example Input: 3500 
# Example Output: Deluxe Room 

amt=int(input("Enter your budget amount: "))
if amt<=1200:
    print("Normal Room")
elif amt<=4000:
    print("Deluxe Room")
else:
    print("Luxury Room")
# ******************************************************************************

# Problem 19: Vehicle Speed Warning 
# Definition: Display a warning based on vehicle speed. 
# Task: Read vehicle speed. 
# Example Input: 110 
# Example Output: Overspeed 

speed=int(input("Enter Vehicle speed: "))
if speed<=50:
    print("Low Speed")
elif speed<=100:
    print("Medium Speed")
else:
    print("Overspeed")
# ******************************************************************************

# Problem 20: Employee Performance 
# Definition: Classify employee performance. 
# Task: Read performance score. 
# Example Input: 92 
# Example Output: Outstanding 

score=int(input("Enter performance score: "))
if score>=90:
    print("Outstanding")
elif score>=30 and score<=89:
    print("Good")
else:
    print("Bad")
# ******************************************************************************

# Problem 21: Online Shopping Discount 
# Definition: Determine the discount percentage based on purchase amount. 
# Task: Read purchase amount. 
# Example Input: 4500 
# Example Output: 15% Discount 

amt = int(input("Enter the purchase amount: "))
if amt<=3000 and amt>=1001:
    discount=10
elif amt<=5000 and amt>=3001:
    discount=15
else:
    discount=20
print(f"{discount}% discount")
# ******************************************************************************

# Problem 22: Data Usage Alert 
# Definition: Display internet usage status. 
# Task: Read data usage in GB. 
# Example Input: 95 
# Example Output: High Usage 

usage=int(input("enter uaage in GB: "))
if usage>=75:
    print("High usage")
elif usage <=74 and usage>=30:
    print("Medium usage")
else:
    print("Low usage")
# ******************************************************************************

# Problem 23: Fuel Level Indicator 
# Definition: Display the vehicle fuel status. 
# Task: Read fuel percentage. 
# Example Input: 12 
# Example Output: Low Fuel 

fuel = int(input("Enter fuel percentage: "))
if fuel<30:
    print("Low fuel")
elif fuel <70:
    print("Medium Fuel")
else:
    print("High fuel")
# ******************************************************************************

# Problem 24: ATM Cash Withdrawal 
# Definition: Categorize the withdrawal amount. 
# Task: Read withdrawal amount. 
# Example Input: 15000 
# Example Output: Large Withdrawal 

amt = int(input("Enter withdrawal amount: "))
if amt>10000:
    print("Large withdrawl")
elif amt<10000 and amt>3000:
    print("Medium withdrawl")
else:
    print("Small withdrawl")
# ******************************************************************************

# Problem 25: Library Fine 
# Definition: Determine the fine category based on overdue days. 
# Task: Read overdue days. 
# Example Input: 7 
# Example Output: Medium Fine 

overdue=int(input("Enter overdue days: "))
if overdue>=10:
    print("Huge")
elif overdue<10 and overdue>=4:
    print("Medium")
else:
    print("Low")
# ******************************************************************************

# Problem 26: Delivery Priority 
# Definition: Assign a delivery type based on parcel weight. 
# Task: Read parcel weight. 
# Example Input: 15 
# Example Output: Standard Delivery 

wt=int(input("Enter parcel weight: "))
if wt<=10:
    print("Small Parcel")
elif wt<=25:
    print("Medium Parcel")
else:
    print("Large Parcel")
# ******************************************************************************

# Problem 27: Internet Data Plan 
# Definition: Recommend a data plan. 
# Task: Read monthly data usage. 
# Example Input: 180 
# Example Output: Premium Plan 

data=int(input("Enter monthly data usage: "))
if data>150:
    print("Premium plan")
elif data<150 and data>=80:
    print("Medium plan")
else:
    print("Low plan")
# ******************************************************************************

# Problem 28: Hospital Emergency Level 
# Definition: Determine emergency priority. 
# Task: Read priority level (1–4). 
# Example Input: 2 
# Example Output: High Priority 

priority=int(input("Enter priority level: "))
if priority<=2:
    print("High priority")
elif priority>2:
    print("Low Priority")
# ******************************************************************************

# Problem 29: Hotel Star Rating 
# Definition: Display a description based on hotel rating. 
# Task: Read hotel rating (1–5). 
# Example Input: 4 
# Example Output: Very Good Hotel 

rating=int(input("Enter your rating: "))
if rating==5:
    print("Excellent Hotel")
elif rating==1:
    print("Worst Hotel")
else:
    print("Average Hotel")
# ******************************************************************************

# Problem 30: E-commerce Membership 
# Definition: Assign a membership level based on yearly purchases. 
# Task: Read yearly purchase amount. 
# Example Input: 125000 
# Example Output: Gold Membership 

amt=int(input("Enter annual purchase amount: "))
if amt>200000:
    print("Diamond Membership")
elif amt>=80000 and amt<200000:
    print("Gold Membership")
else:
    print("Silver Membership")