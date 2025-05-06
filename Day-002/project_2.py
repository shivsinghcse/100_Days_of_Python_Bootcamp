# Tip calculator project

print("Welcome to the tip calculator!")
bill = float(input("What was the total bill?$ "))
tip_percent = int(input("How much tip would you like to give? 10, 12, or 15? "))
number_of_people = int(input("How many people to split the bill? "))

tip_amount = bill * tip_percent / 100
total_bill = bill + tip_amount
per_person_bill = round(total_bill / number_of_people, 2)

print(f"Each person should pay: ${per_person_bill}")
