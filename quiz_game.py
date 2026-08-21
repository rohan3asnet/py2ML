questions={
    'What is the capital of Nepal?':[
        'A. New Delhi',
        'B. Kathmandu',
        'C. Pokhara',
        'D. Chitwan'
    ],
    'What is the writer of War and Peace?':[
        'A. Leo Tolstoy',
        'B. Chekhov',
        'C. Dostoevsky',
        'D. Pushkin'
    ]

}

for question,answers in questions.items():
    print(f"{question}")
    for answer in answers:
        print(f"{answer}")
