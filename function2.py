# global and local variable with the same name
x = 10


def change_x():
    #global x
    x = 20
    print(x + 20)


change_x()
print(x)
