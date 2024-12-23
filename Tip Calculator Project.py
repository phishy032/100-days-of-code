print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15: "))
people = int(input("How many people to split the bill? "))

cal_tips = (tip / 100 + 1)
total_bill = bill * cal_tips
split = round((total_bill / people), 2)

print(f"Each person should pay: ${split}")
