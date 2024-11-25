

name = ""
while name != "your name":
    print("Please type your name (or type 'exit' to quit).")
    name = input()
    if name == "exit":
        print("Goodbye!")
        break
else:
    print("Thank you!")

