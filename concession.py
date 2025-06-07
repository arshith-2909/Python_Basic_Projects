menu = {
    "burger":199,
    "pizza":349,
    "potato":99,
    "french fries":149,
    "popcorn":49,
    "coke":80,
    "soda":30
}
print("-----------MENU-----------")
for key,value in menu.items():
    print(f"{key:15}:{value:.2f}Rs")
print("-----------MENU-----------")
cart = []
total = 0

while True:
    food = input("Enter the item you want to buy(q to quit) : ").lower()
    if food == "q":
        break
    elif food in menu:
        cart.append(food)
print()
print("-------YOUR ORDER-------")
for food in cart:
    total += menu.get(food)
    print(food,end=" ")

print()
print(f"The Total cost is : {total:.1f}Rs")