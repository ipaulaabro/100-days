import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

rps = [rock, paper, scissors]
win = "🥳 User wins!"
tie = "😐 It's a tie!"
lose = "😭 Computer wins!"

print("🕹 Rock Paper Scissors 🕹")
computer = random.randint(0, 2)

print("\nChoose one of the options below:")
print("[0] Rock")
print("[1] Paper")
print("[2] Scissors")

user = int(input("Choice: "))

if not (0 <= user <= 2):
    print("Invalid choice, so I'm choosing for you!")
    user = random.randint(0, 2)

print(f"\nYou chose:\n{rps[user]}")
print(f"Computer chose:\n{rps[computer]}")

if user == computer:
    print(tie)
elif user == 0:
    if computer == 1:
        print(lose)
    else:
        print(win)
elif user == 1:
    if computer == 0:
        print(win)
    else:
        print(lose)
else:
    if computer == 0:
        print(lose)
    else:
        print(win)
