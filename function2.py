# global and local variable with the same name
x = 10


def change_x():
    x = 20
    print(x)


change_x()
print(x)
