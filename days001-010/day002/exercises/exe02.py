# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
height_m = float(height)
weight_kg = float(weight)

bmi = weight_kg / height_m ** 2
bmi_int = int(bmi)
print(bmi_int)
