while True:
    print("What are your full names?")
    name = input("My name is, ")
    if name == name:
        print(f"Welcome back {name}.")
    # Enter your password
    print(f"Hello {name},What is your file password?")
    password = input("Please write your password here, ")
    print(f'Here is my password {password}')
    if password == "1234":
        print("Acess granted")
        break
    else:
        print("Incorrect password.Try again!!!")
