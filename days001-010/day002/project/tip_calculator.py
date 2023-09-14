print("💰 Tip Calculator 💰")

total_bill = float(input("What was the total bill? $"))
tip_percentage = int(input("What percentage would you like to tip? ")) / 100
num_people = int(input("How many people to split the bill? "))

bill = total_bill * (1 + tip_percentage)
bill_per_person = bill / num_people
print(f"💰 Each person should pay: ${bill_per_person:.2f} 💰")
