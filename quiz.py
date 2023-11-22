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
        "question": "Kāds ir Latvijas augstākā kalna garums(aptuveni)?",
        "options": [589, 312, 1246, 258],
        "correct_answer": 312
    },
    # 4
    {
        "question": "Cik gara ir Latvijas jūras robeža (km)?",
        "options": [289, 500, 498, 345],
        "correct_answer": 498
    },
    # 5
    {
        "question": "Kurā gadā Latvijas Republika iestājās Eiropas savienībā?",
        "options": [1995., 2002., 2004., 2007.],
        "correct_answer": 2004.
    },
    # 6
    {
        "question": "Cik garšs(km) ir Latvijas jūras robežas garums?",
        "options": [498, 515, 455, 321],
        "correct_answer": 498
    },
    # 7
    {
        "question": "Ceturtā pilsēta pēc iedzīvotāju skaita",
        "options": ["Ventspils", "Jūrmala", "Jelgava", "Liepāja"],
        "correct_answer": "Jelgava"
    },
    # 8
    {
        "question": "Cik gadi bija Vilhelmam Ostvaldam, Nobela prēmijas laureātam, kad viņš nomira?",
        "options": [76, 77, 78, 79],
        "correct_answer": 78
    },
    # 9
    {
        "question": "Skeletonists, kurš 11 reizes izcīnījis Pasaules kausu",
        "options": ["Ivo Šteinbergs", "Martins Dukurs", "Tomass Dukurs"],
        "correct_answer": "Martins Dukurs"
    },
    # 10
    {
    "question": "Kuras koordinātas ir Latvijā",
     "options": ["57.0° 24.0°, 56.0° 22.0°, 50.0° 30°, 60.0° 31.0°"],
        "correct_answer": "57.0° 24.0°"
    },
    # 11
    {
        "question": "Kurā datumā notika Baltijas ceļš?",
        "options": ["23.08.2023", "23.08.1989", "23.09.1989" , "23.08.1999"],
        "correct_answer": "23.08.1989"
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
        "question": "Kads ir policijas telefona numurs?",
        "options": ["111","110","119","004","056","11"],
        "correct_answer": "110"
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
        "question": "Cik krasas ir Latvijas karoga?",
        "options": [1, 2, 3, 4],
        "correct_answer": 2
    },
    # 20
    {
        "question": "Kāds ezers ir vislielākais Latgvijā?",
        "options": ["Rāznas ezers", "Babītes ezers", "Lubānas ezers", "Baltezers"],
        "correct_answer": "Lubānas ezers"
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
