def greet(fx):
    def mfx(*args, **kwargs):
        print("Good morning")
        fx(*args, **kwargs)
        print("Thanks for using this function\n")

    return mfx


@greet
def hello():
    print("Hello World")


# @greet()
def add(a, b):
    print(a + b)


def main():
    # hello()
    # same as above
    # greet(hello)()

    greet(add)(1, 2)


main()
