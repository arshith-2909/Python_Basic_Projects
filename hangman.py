import random

words = ("rice", "sugar", "salt", "flour", "bread", "milk", "eggs", "butter", "cheese", "yogurt",
"coffee", "tea", "pasta", "oil", "vinegar", "jam", "honey", "ketchup", "mustard", "cereal",
"chair", "table", "sofa", "bed", "mattress", "pillow", "blanket", "wardrobe", "dresser", "bookshelf",
"apple", "banana", "orange", "mango", "grapes", "pineapple", "watermelon", "papaya", "kiwi", "strawberry",
"potato", "tomato", "onion", "carrot", "cabbage", "spinach", "broccoli", "cauliflower", "peas", "garlic",
"detergent", "mop", "broom", "bucket", "sponge", "bleach", "duster",
"hammer", "screwdriver", "wrench", "pliers", "nails", "screws", "drill", "tapemeasure", "level", "saw",
"refrigerator", "washingmachine", "microwave", "oven", "toaster", "blender", "fan", "heater", "airconditioner", "iron",
"toothpaste", "toothbrush", "shampoo", "soap", "conditioner", "lotion", "razor", "towel", "comb", "tissue",
"pen", "pencil", "notebook", "eraser", "sharpener", "ruler", "marker", "glue", "tape", "scissors"
)

hangman = {0 : ("    ",
                "    ",
                "    "),
           1 : ("  O  ",
                "     ",
                "     "),
           2 : ("  O  ",
                "  |  ",
                "     "),
           3 : ("  O  ",
                " /|  ",
                "     "),
           4 : ("  O  ",
                " /|\\",
                "     "),
           5 : ("  O  ",
                " /|\\",
                " /    "),
           6 : ("  O  ",
                " /|\\",
                " / \\")}


def display_man(wrong_answer):
    print("*************")
    for i in hangman[wrong_answer]:
        print(i)
    print("*************")

def display_hint(hint):
    print(" ".join(hint))

def display_answer(answer):
    print(" ".join(answer))

def main():
    answer = random.choice(words)
    hint = ["_"] * len(answer)
    wrong_answer = 0
    guessed_letter = set()
    
    while True :
        display_man(wrong_answer)
        display_hint(hint)
        guess = input("Enter a letter : ").lower()

        if len(guess) > 1 or not guess.isalpha():
            print("Invalid input! Please enter a valid letter.")
            continue

        if guess in guessed_letter:
            print(f"The letter {guess} is already guessed.")
            continue

        guessed_letter.add(guess)

        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess

        else :
            wrong_answer += 1

        if "_" not in hint:
            display_man(wrong_answer)
            display_answer(answer)
            print("YOU WIN!!!")
            break

        elif wrong_answer >= len(hangman) - 1:
            display_man(wrong_answer)
            display_answer(answer)
            print("YOU LOSE!!!")
            break

if __name__ == "__main__":
    main()