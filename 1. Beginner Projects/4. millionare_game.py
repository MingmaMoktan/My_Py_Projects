questions = [
    [
        "1. What is the capital of France?",
        "A) Paris",
        "B) London",
        "C) Rome",
        "D) Madrid",
        "A"
    ],
    [
        "2. Which planet is known as the Red Planet?",
        "A) Earth",
        "B) Mars",
        "C) Jupiter",
        "D) Venus",
        "B"
    ],
    [
        "3. Who wrote 'Romeo and Juliet'?",
        "A) Charles Dickens",
        "B) William Shakespeare",
        "C) Mark Twain",
        "D) Jane Austen",
        "B"
    ],
    [
        "4. What is the largest ocean on Earth?",
        "A) Atlantic Ocean",
        "B) Indian Ocean",
        "C) Arctic Ocean",
        "D) Pacific Ocean",
        "D"
    ],
    [
        "5. Which element has the chemical symbol 'O'?",
        "A) Gold",
        "B) Oxygen",
        "C) Osmium",
        "D) Iron",
        "B"
    ],
    [
        "6. What is the square root of 64?",
        "A) 6",
        "B) 7",
        "C) 8",
        "D) 9",
        "C"
    ],
    [
        "7. Which country hosted the 2016 Summer Olympics?",
        "A) China",
        "B) Brazil",
        "C) UK",
        "D) Russia",
        "B"
    ],
    [
        "8. Who painted the Mona Lisa?",
        "A) Vincent Van Gogh",
        "B) Pablo Picasso",
        "C) Leonardo da Vinci",
        "D) Claude Monet",
        "C"
    ],
    [
        "9. What is the hardest natural substance?",
        "A) Gold",
        "B) Iron",
        "C) Diamond",
        "D) Silver",
        "C"
    ],
    [
        "10. Which language is primarily spoken in Brazil?",
        "A) Spanish",
        "B) Portuguese",
        "C) French",
        "D) English",
        "B"
    ]
]

prize = [100, 200, 300, 400, 500, 6000, 70000, 80000, 900000, 1000000]
i = 0
for question in questions:
    """
    Here question is the element of the list inside the main list questions and all lists are iterated by this for loop.
    """
    print(question[0])
    print(question[1])
    print(question[2])
    print(question[3])
    print(question[4])
    
    # check your answer.
    ans = input("Enter your answer \"A,B,C,D\" ")
    if question[5]==ans.upper():
        print("You have selected the correct answer.")
        i+=1
        if i==len(questions):
            print(f"You are a millionare and you have won {prize[9]}")
    else:
        print(f"Your answer is incorrect.\nThe correct answer is{question[5]}")
        print("Better luck next time.")
        print(f"Your have won the prize {prize[i-1]} dollars.")
        break