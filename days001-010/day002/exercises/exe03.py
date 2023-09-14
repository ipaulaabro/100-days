# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
age_int = int(age)

remaining_years = 90 - age_int
remaining_months = 12 * remaining_years
remaining_weeks = 52 * remaining_years
remaining_days = 365 * remaining_years

print(f"You have {remaining_days} days, {remaining_weeks} weeks, and {remaining_months} months left.")
