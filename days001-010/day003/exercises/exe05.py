# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
lower_names = (name1 + name2).lower()

t_count = lower_names.count("t")
r_count = lower_names.count("r")
u_count = lower_names.count("u")
e_count = lower_names.count("e")

l_count = lower_names.count("l")
o_count = lower_names.count("o")
v_count = lower_names.count("v")

true_count = t_count + r_count + u_count + e_count
love_count = l_count + o_count + v_count + e_count

true_love_score = int(f'{true_count}{love_count}')

message = f"Your score is {true_love_score}"
if true_love_score < 10 or true_love_score > 90:
    message += ", you go together like coke and mentos"
elif true_love_score > 40 and true_love_score < 50:
    message += ", you are alright together"
message += "."
print(message)
