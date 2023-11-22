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
        "question": "Cik liela ir Latvijas paltība?",
        "options": ["5 200 km²", "51 300 km²" , "18 705 km²", "64 589 km²"],
        "correct_answer": "64 589 km²"
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
        "question": "",
        "options": [""],
        "correct_answer": ""
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