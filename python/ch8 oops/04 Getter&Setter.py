class Maths:
    def __init__(self, num):
        self.num = num

    def display(self):
        print(f"number passed is {self.num}\n")

    @property
    def square(self):
        print("Inside Getter")
        return self.num * self.num

    @square.setter
    def square(self, newNum):
        print("Inside Setter")
        self.num = newNum


def main():
    obj = Maths(10)
    obj.display()

    # Using the setter method for square
    obj.square = 2  # Prints "Inside Setter" and sets self.num to 2

    # Using the getter method for square
    print(
        f"Square of {obj.num} is  {obj.square}"
    )  # Prints "Inside Getter" and then "Square of 2 is 4"


# Standard entry-point check
if __name__ == "__main__":
    main()
