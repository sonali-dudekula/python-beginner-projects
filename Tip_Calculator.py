# Tip calculator
print("Welcome to the Tip Calculator")
total_bill = float(input("What was the total bill? "))
percent_tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))
divided_bill = (total_bill * (1 + percent_tip / 100)) / people
# rounded_bill = round(divided_bill, 2)
rounded_bill = "{:0.2f}".format(divided_bill)
print(f"Each person should pay: {rounded_bill}")
