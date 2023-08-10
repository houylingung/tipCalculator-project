#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to tip calculator \n" ) 

total_bill =input("What was the total bill? ")
tip_percentage = input("How many percent would you like to give? ")
people = input("How many people you want to split with? ")

total_bill_as_int = int(total_bill)
tip_percentage_as_int = int(tip_percentage)
people_as_int = int(people)

total_for_each_person = round((total_bill_as_int / people_as_int) * (1 + (tip_percentage_as_int / 100)), 2)

print(f"Each person should pay: {total_for_each_person}")