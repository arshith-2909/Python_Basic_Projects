questions = (("Who is the current Prime minister of India ?"),
             ("Who wrote Jana Gana Mana ? "),
             ("How many elements are there in a periodic table ?"),
             ("Who is the greatest footballer of all time ?"),
             ("Who is the first President of India ?"))

options = (("A. Narendra Modi","B. Draupadi Murmu","C. Rahul Gandhi","D. ManMohan Singh"),
           ("A. Arjit Singh","B. Sonu Nigam","C. Rabindranath Tagore","D. Bamkin Chandra Chatarji"),
           ("A. 106","B. 110","C. 115","D. 118"),
           ("A. Leonal Messi","B. Cristiano Ronaldo","C. Mbappe","D. Neymer Jr"),
           ("A. Ramanath Kovindh","B. Draupadhi Murmu","C. Dr Radha Krishna","D. Dr Ranjendra Prasad"))

answer = ['A','C','D','B','D']
guesses = []
score = 0
question_num = 0

for i,question in enumerate(questions):
    print("---------------------------------------------------")
    print(i+1,".",question)
    for option in options[question_num]:
        print(option)
    guess = input("Enter the option(A, B, C, D) : ").upper()
    guesses.append(guess)
    if guess == answer[question_num]:
        print("CORRECT!")
        score += 1
    else:
        print("INCORRECT!")
        print(f"The correct answer is {answer[question_num]}")
    question_num += 1

print("--------------------------------------------")
print("                   RESULT                   ")
print("--------------------------------------------")
print("ANSWER :",end=" ")
for ans in answer:
    print(f"{ans}",end=" ")
print()

print("GUESSES :",end=" ")
for guess in guesses:
    print(f"{guess}",end=" ")
print()

score = int(score/len(questions)*100)
print("Your Score is : ",score,"%")