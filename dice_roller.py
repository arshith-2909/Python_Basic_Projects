import random 

#print("\u25CF \u250C \u2500 \u2510 \u2502 \u2514 \u2518")
# ● ┌ ─ ┐ │ └ ┘
"""
┌─────────┐
│         │
│         │
│         │
└─────────┘
"""

dice_art = {
    1:("┌─────────┐",
       "│         │",
       "│    ●    │",
       "│         │",
       "└─────────┘"),
    2:("┌─────────┐",
       "│  ●      │",
       "│         │",
       "│      ●  │",
       "└─────────┘"),
    3:("┌─────────┐",
       "│  ●      │",
       "│    ●    │",
       "│      ●  │",
       "└─────────┘"),
    4:("┌─────────┐",
       "│  ●   ●  │",
       "│         │",
       "│  ●   ●  │",
       "└─────────┘"),
    5:("┌─────────┐",
       "│  ●   ●  │",
       "│    ●    │",
       "│  ●   ●  │",
       "└─────────┘"),
    6:("┌─────────┐",
       "│  ●   ●  │",
       "│  ●   ●  │",
       "│  ●   ●  │",
       "└─────────┘")
}

dice = []
total = 0
no_of_dice = int(input("How many dice?: "))

for die in range(no_of_dice):
    dice.append(random.randint(1,6))

for die in dice:
    total += die

print("Vertically placed")
for i in range(no_of_dice):
    for die in dice_art.get(dice[i]):
        print(die)

print("Horizontally placed")
for i in range(5):
    for die in dice:
        print(dice_art.get(die)[i],end=" ")
    print()

print(dice)
print(f"Total : {total}")