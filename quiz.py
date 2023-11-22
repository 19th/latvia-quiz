import random

# Questions about Latvia
questions = [
    # 1
    {
        "question": "Cik gadi ir pagājuši kopš Latvijas Republikas proklamēšanas?",
        "options": [95, 100, 105, 150],
        "correct_answer": 105
    },
    # 2
    {
        "question": "",
        "options": [""],
        "correct_answer": ""
    },
    # 3
    {
        "question": "",
        "options": [""],
        "correct_answer": ""
    },
    # 4
    {
        "question": "",
        "options": [""],
        "correct_answer": ""
    },
    # 5
    {
        "question": "",
        "options": [""],
        "correct_answer": ""
    },
    # 6
    {
        "question": "",
        "options": [""],
        "correct_answer": ""
    },
    # 7
    {
        "question": "",
        "options": [""],
        "correct_answer": ""
    },
    # 8
    {
        "question": "",
        "options": [""],
        "correct_answer": ""
    },
    # 9
    {
        "question": "",
        "options": [""],
        "correct_answer": ""
    },
    # 10
    {
        "question": "",
        "options": [""],
        "correct_answer": ""
    },
    # 11
    {
        "question": "",
        "options": [""],
        "correct_answer": ""
    },
    # 12
    {
        "question": "",
        "options": [""],
        "correct_answer": ""
    },
    # 13
    {
        "question": "",
        "options": [""],
        "correct_answer": ""
    },
    # 14
    {
        "question": "",
        "options": [""],
        "correct_answer": ""
    },
    # 15
    {
        "question": "",
        "options": [""],
        "correct_answer": ""
    },
    # 16
    {
        "question": "",
        "options": [""],
        "correct_answer": ""
    },
    # 17
    {
        "question": "",
        "options": [""],
        "correct_answer": ""
    },
    # 18
    {
        "question": "kāds ir Ventas rumbas apmēramais platums vidēji",
         "options": ["110-120 metri", "90-100 metri", "100-110 metri"],
        "correct_answer": "100-110 metri"
    },
    # 19
    {
        "question": "",
        "options": [""],
        "correct_answer": ""
    },
    # 20
    {
        "question": "",
        "options": [""],
        "correct_answer": ""
    },
]

def run_quiz():
    # Shuffle the questions
    random.shuffle(questions)

    # Initialize score
    score = 0

    # Iterate through questions
    for i, question_data in enumerate(questions, 1):
        print(f"Jautājums {i}: {question_data['question']}")
        for j, option in enumerate(question_data['options'], 1):
            print(f"  {j}. {option}")

        # Get user input
        user_answer = input("Atbilde (ieraksti varianta numuru): ")

        # Check if the answer is correct
        correct_answer = question_data['options'].index(question_data['correct_answer']) + 1
        if user_answer == str(correct_answer):
            print("Pareizi!\n")
            score += 1
        else:
            print(f"Kļūda! Pareizā atbilde ir {correct_answer}: {question_data['correct_answer']}\n")

    # Display final score
    print(f"Gala rezultāts: {score}/{len(questions)}")

# Run the quiz
run_quiz()