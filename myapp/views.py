from django.shortcuts import render, redirect

def home(request):
    return render(request, 'Home.html')

def level(request):
    # Reset session variables when starting a new quiz
    request.session['question_index'] = 0
    request.session['score'] = 0  # Reset score to 0
    return render(request, 'Level.html')

def easyQ(request):
    questions = [
        {
            "question": "What is Django?",
            "choices": ["Django is a database management system.", "Django is a Python tool for making websites.", "Django is a JavaScript library for front-end development.", "Django is a mobile app development framework."],
            "correct": "Django is a Python tool for making websites.",
        },
        {
            "question": "What is Django used for?",
            "choices": ["Django is used to design logos.", "Django is used to create video games.", "Django is used to create websites and web apps.", "Django is used for desktop applications."],
            "correct": "Django is used to create websites and web apps.",
        },
        {
            "question": "What does the models.py file do?",
            "choices": ["It defines URL routes for the website.", "It handles user authentication.", "It manages static files like images.", "It defines the database structure."],
            "correct": "It defines the database structure.",
        },
        {
            "question": "What is the settings.py file for?",
            "choices": ["It holds project settings.", "It processes form submissions.", "It manages the user interface design.", "It defines the database structure."],
            "correct": "It holds project settings.",
        },
    ]

    question_index = request.session.get('question_index', 0)
    
    # Check if the index is valid
    if question_index >= len(questions):
        # Retrieve the score from the session
        score = request.session.get('score', 0)
        return render(request, 'Finish.html', {
            'score': score,
            'questions': questions  # Pass the easy_questions list to the template
        })

    question_data = questions[question_index]

    if request.method == "POST":
        # Get the user's answer
        selected_answer = request.POST.get("answer")
        correct_answer = question_data["correct"]

        # You can store the result in the session if needed
        if selected_answer == correct_answer:
            request.session['score'] = request.session.get('score', 0) + 1

        # Move to the next question
        request.session['question_index'] += 1
        return redirect('easy_select')

    # Send question data to the template
    return render(request, 'EasyQ.html', {
        'question': question_data["question"],
        'choices': question_data["choices"]
    })


def medQ(request):   
    questions = [
        {
            "question": "How does Django handle URL routing?",
            "choices": [
                "By using `urls.py` to map URLs to views.",
                "By creating a separate file for each URL.",
                "By using HTML files to manage URL patterns.",
                "By defining all URL routes in the database."
            ],
            "correct": "By using `urls.py` to map URLs to views."
        },
        {
            "question": "What is Django’s ORM (Object-Relational Mapping)?",
            "choices": [
                "It allows Django to interact with a database using Python objects.",
                "It manages the authentication system.",
                "It defines static files for the web app.",
                "It provides front-end templates for the app."
            ],
            "correct": "It allows Django to interact with a database using Python objects."
        },
        {
            "question": "How does Django manage static files (like images, CSS, JavaScript)?",
            "choices": [
                "By storing them in the `static/` directory and linking them in the templates.",
                "By storing them directly in the database.",
                "By automatically creating new directories for each file.",
                "By using Django models to handle static files."
            ],
            "correct": "By storing them in the `static/` directory and linking them in the templates."
        },
        {
            "question": "What is the purpose of Django's `migrations`?",
            "choices": [
                "To keep track of changes to the database schema.",
                "To create new templates for the website.",
                "To manage user sessions.",
                "To handle background tasks in the app."
            ],
            "correct": "To keep track of changes to the database schema."
        }
    ]


    question_index = request.session.get('question_index', 0)
    
    # Check if the index is valid
    if question_index >= len(questions):
        # Retrieve the score from the session
        score = request.session.get('score', 0)
        return render(request, 'Finish.html', {
            'score': score,
            'questions': questions  # Pass the easy_questions list to the template
        })

    question_data = questions[question_index]

    if request.method == "POST":
        # Get the user's answer
        selected_answer = request.POST.get("answer")
        correct_answer = question_data["correct"]

        # You can store the result in the session if needed
        if selected_answer == correct_answer:
            request.session['score'] = request.session.get('score', 0) + 1

        # Move to the next question
        request.session['question_index'] += 1
        return redirect('medium_select')

    # Send question data to the template
    return render(request, 'MedQ.html', {
        'question': question_data["question"],
        'choices': question_data["choices"]
    })

def hardQ(request):
    questions = [
        {
            "question": "What's the difference between `ForeignKey` and `ManyToManyField`?",
            "choices": [
                "`ForeignKey` is one-to-many, `ManyToManyField` is many-to-many.",
                "`ForeignKey` creates one-to-one, `ManyToManyField` is one-to-many.",
                "`ForeignKey` is many-to-many, `ManyToManyField` is one-to-one.",
                "`ForeignKey` and `ManyToManyField` are the same."
            ],
            "correct": "`ForeignKey` is one-to-many, `ManyToManyField` is many-to-many."
        },
        {
            "question": "How do you filter records based on a related model’s attribute?",
            "choices": [
                "Use `.filter()` with model name and double underscores.",
                "Use `.select_related()` for filtering.",
                "Filter with the foreign key's ID.",
                "Query the related model directly."
            ],
            "correct": "Use `.filter()` with model name and double underscores."
        },
        {
            "question": "What are Django `signals` used for?",
            "choices": [
                "To run code on model events (save, delete).",
                "To manage request/response in views.",
                "To link views with static files.",
                "To map URLs to views."
            ],
            "correct": "To run code on model events (save, delete)."
        },
        {
            "question": "What are `atomic` transactions in Django?",
            "choices": [
                "Django commits changes after each query.",
                "`atomic` transactions group changes together.",
                "Django doesn’t support transactions.",
                "`atomic` transactions make queries independent."
            ],
            "correct": "`atomic` transactions group changes together."
        }
    ]

    question_index = request.session.get('question_index', 0)
    
    # Check if the index is valid
    if question_index >= len(questions):
        # Retrieve the score from the session
        score = request.session.get('score', 0)
        return render(request, 'Finish.html', {
            'score': score,
            'questions': questions  # Pass the easy_questions list to the template
        })

    question_data = questions[question_index]

    if request.method == "POST":
        # Get the user's answer
        selected_answer = request.POST.get("answer")
        correct_answer = question_data["correct"]

        # You can store the result in the session if needed
        if selected_answer == correct_answer:
            request.session['score'] = request.session.get('score', 0) + 1

        # Move to the next question
        request.session['question_index'] += 1
        return redirect('hard_select')

    # Send question data to the template
    return render(request, 'HardQ.html', {
        'question': question_data["question"],
        'choices': question_data["choices"]
    })