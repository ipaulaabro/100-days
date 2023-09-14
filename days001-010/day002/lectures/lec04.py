print(8 / 3)
print(int(8 / 3))
print(round(8 / 3))
print(round(8 / 3, 2))
print(round(2.666666666666, 2))
print()

print(8 // 3)
print(type(8 // 3))
print(type(8 / 3))
print(type(4 / 2))
print(4 / 2)
print()

result = 4 / 2
result /= 2
print(result)
print()

score = 0
score += 7
print(score)

score -= 2
print(score)

score *= 3
print(score)

# TypeError
# print("Your score is: " + score)

print("Your score is: " + str(score))
print()

age = 27
height = 1.62
is_winner = True

print(f"Your age is {age}, your height is {height} and are you the winner? {is_winner}")
