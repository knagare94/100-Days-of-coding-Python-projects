#If the bill was $150.00, split between 5 people, with 12% tip.

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to the tip calculator.")
total_bill = input("What was the total bill? ")
tip_pert = input("What percentage tip would you like to give? 10, 20, or 15? ")
split_bill = input("How many people to split the bill? ")5
tip_calculate = float(total_bill) * float(tip_pert) / 100
tip_added_to_bill = float(total_bill) + tip_calculate
each_person_pay = tip_added_to_bill / int(split_bill)
each_person_pay = round(each_person_pay, 2)
print(f"Each person should pay: {each_person_pay}")