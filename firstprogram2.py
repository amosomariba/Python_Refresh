# Questions to ask a newcomer in the university
questions = [
    "What is your name?",
    "Which course are you pursuing?",
    "Where are you from?",
    "What year of study are you in?",
    "Why did you choose this university?",
    "What hobbies or interests do you have?",
    "Have you joined any clubs or organizations yet?",
    "What are you looking forward to the most during your time here?",
    "Do you need any help settling in?",
    "What’s one goal you have for this semester?"
]

# Function to display the questions
def ask_questions():
    print("Here are 10 questions to get to know a newcomer:")
    for i, question in enumerate(questions, 1):
        print(f"{i}. {question}")

# Call the function to display questions
ask_questions()
