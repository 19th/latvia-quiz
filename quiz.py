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
        "question": "Cik pilsetu ir Latvijā?",
        "options": [81, 87, 73, 79],
        "correct_answer": 81
    },
    # 3
    {
        "question": "Kāds ir Latvijas lielākā kalna Gaiziņkalna augstums?(metros)",
        "options": [400,350,250,300],
        "correct_answer": 300
    },
    # 4
    {
        "question": "Cik gara ir Latvijas jūras robeža kilometros?",
        "options": [500,450,400,550],
        "correct_answer": 500
    },
    # 5
    {
        "question": "Kurā gadā Latvija pievienojās Eiropas Savienībai?",
        "options": [1994, 2002, 2004, 2015],
        "correct_answer": 2004
    },
    # 6
    {
        "question": "Kāds ir Latvijas jūras robežas garums?",
        "options": [356, 498, 516, 245],
        "correct_answer": 498
    },
    # 7
    {
        "question": "Kāda ir Latvijas ceturtā pilsēta pēc iedzīvotāju skaita?",
        "options": ["Rīga", "Daugavpils", "Jelgava", "Liepāja"],
        "correct_answer": "Jelgava"
    },
    # 8
    {
        "question": "Kāds nobela prēmijas laureāts dzimis Latvijā?",
        "options": ["Vilhelms Ostvalds", "Valērijs Karklins", "Mikhail Kutuzov", "Ratmir Kutuzov"],
        "correct_answer": "Vilhelms Ostvalds"
    },
    # 9
    {
        "question": "Skeletonists, kurš 11 reizes izcīnījis Pasaules kausu?",
        "options": ["Egils Levits","Janis Lembergs", "Martins Cukurs", "Martins Dukurs"],
        "correct_answer": "Martins Dukurs"
    },
    # 10
    {
        "question": "Kuras no koordinātem ir Latvijā?",
        "options": ["34.0, -118.0", "53.0 -8.0", "57.0 24.0", "36.0, 138.0"],
        "correct_answer": "57.0 24.0"
    },
    # 11
    {
        "question": "Kad bija Baltijas ceļš? diena un mēnesis",
        "options": ["19 augusts", "Vakar", "11 septembris", "23 augusts"],
        "correct_answer": "23 augusts"
    },
    # 12
    {
        "question": "Kāda valsts platība?",
        "options": [">5cm", "666min", "15cm", "27582 km"],
        "correct_answer": ">5cm"
    },
    # 13
    {
        "question": "Izplatītākais koks Latvijas mežos",
        "options": ["Bērzs","Priede", "Ozols","Egle"],
        "correct_answer": "Bērzs"
    },
    # 14
    {
        "question": "Brīvības pieminekļa augstums",
        "options": [65,32,40,42],
        "correct_answer": 40
    },
    # 15
    {
        "question": "Policijas telefona numurs",
        "options": [112, 110, 911, 113],
        "correct_answer": 110
    },
    # 16
    {
        "question": "Latvijas naudas vienības",
        "options": ["lats", "dolarss", "eiro", "rubli", "vona"],
        "correct_answer": "eiro"
    },
    # 17
    {
        "question": "Kāds bija Latvijas iedzīvotāju skaits uz 2022 gadu?",
        "options": ["19", "1,876 miljoni", "1,609 miljoni", "739 miljoni"],
        "correct_answer": "1,876 miljoni"
    },
    # 18
    {
        "question": "Kāda ir ūdenskrituma Ventas Rumba īpatnība?",
        "options": ["Garākais", "Platākais", "Mitrākais", "Meow"],
        "correct_answer": "Platākais"
    },
    # 19
    {
        "question": "Kādas ir karoga krāsas?",
        "options": ["balts un sarkans", "balts un fuksija", "balts un karmīnsarkans", "balts un koši sarkans",],
        "correct_answer": "balts un karmīnsarkans"
    },
    # 20
    {
        "question": "Lielākais ezers",
        "options": ["sivers", "reznas", "lubāns", "engures"],
        "correct_answer": "lubāns"
    },
    # 21
    {
        "question": "Test 2",
        "options": ["0", "1", "2", "3"],
        "correct_answer": "1"
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
