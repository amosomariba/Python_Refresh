# Grade calculation script
def calculate_grade(percentage):
    if percentage > 100 or percentage < 0:
        return "Invalid percentage. Please enter a value between 0 and 100."
    elif percentage >= 80:
        return "You got an A plain."
    elif percentage >= 75:
        return "You got an A-."
    elif percentage >= 70:
        return "You got a B+."
    elif percentage >= 65:
        return "You got a B plain."
    elif percentage >= 60:
        return "You got a B-."
    elif percentage >= 55:
        return "You got a C+."
    elif percentage >= 50:
        return "You got a C plain."
    elif percentage >= 45:
        return "You got a C-."
    elif percentage >= 40:
        return "You got a D plain."
    else:
        return "You got an E."


# Input from the user
try:

    percentage = float(input("Enter the percentage that you got from your exams: "))
    percentage = round(percentage)
    grade = calculate_grade(percentage)
    print(f"Rounded Percentage: {percentage}")
    print(grade)
except ValueError:
    print("Invalid input. Please enter a numerical value for the percentage.")
