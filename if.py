percentage = float(input("Enter the percentage that you got from your exams:"))

if percentage > 100 or percentage < 0:
    print("Invalid percentage. Please enter a value between 0 and 100.")
elif percentage >= 80:
    print("You got an A plain.")
elif percentage >= 75:
    print("You got an A-.")
elif percentage >= 70:
    print("You got a B+.")
elif percentage >= 65:
    print("You got a B plain.")
elif percentage >= 60:
    print("You got a B-.")
elif percentage >= 55:
    print("You got a C+.")
elif percentage >= 50:
    print("You got a C plain.")
elif percentage >= 45:
    print("You got a C-.")
elif percentage >= 40:
    print("You got a D plain.")
else:
    print("You got an E.")
