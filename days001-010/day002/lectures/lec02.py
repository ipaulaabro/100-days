# TypeError
# len(4837)

num_chars = len(input("What is your name? "))

# TypeError
# print("Your name has " + num_chars + " characters.")

print(type(num_chars))

num_chars_str = str(num_chars)
print("Your name has " + num_chars_str + " characters.")
print()

a = 123
print(type(a))

a = str(123)
print(type(a))

a = float(123)
print(type(a))
print()

print(70 + float("100.5"))
print(str(70) + str(100))
