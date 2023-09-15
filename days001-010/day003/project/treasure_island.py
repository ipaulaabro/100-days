print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

print("🏝 Treasure Island 🏝️")
print("Your mission is to find the treasure.")

print("\n🚏You stand at a crossroads.")
print("\nOptions:")
print("[left] 👈 Go left")
print("[right] 👉 Go right")
option = input("Which way will you go? ").lower()

if option == "left":
    print("\n🏞️ You arrive at a serene lake.")
    print("\nOptions:")
    print("[wait] 🚤 Wait for a boat")
    print("[swim] 🏊‍️ Swim across the lake")
    option = input("What will you do? ").lower()
    if option == "wait":
        print("\n🏡 You arrive at a house with three doors.")
        print("\nOptions:")
        print("[yellow] 🟡 Yellow door.")
        print("[red] 🔴 Red door.")
        print("[blue] 🔵 Red door.")
        option = input("Which door will you open? ").lower()
        if option == "yellow":
            print("\n🏆 Congratulations! You found the treasure!")
        elif option == "red":
            print("\n🔥 Room engulfed in flame trap you. GAME OVER!")
        elif option == "blue":
            print("\n🦁 Beasts attack you. GAME OVER!")
        else:
            print("\n❌ Invalid option. GAME OVER!")
    elif option == "swim":
        print("\n🐟Enraged piranhas attack you. GAME OVER!")
    else:
        print("\n❌ Invalid option. GAME OVER!")
elif option == "right":
    print("\n🚊Train hits you. GAME OVER!")
else:
    print("\n❌ Invalid option. GAME OVER!")
