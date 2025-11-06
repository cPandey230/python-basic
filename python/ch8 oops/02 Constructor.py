class employee:

    # construtor
    def __init__(self, n, o):
        print("Hey i am employee")
        self.name = n
        self.occupation = o

    def info(self):
        print(f"{self.name} is a {self.occupation} \n")


def main():
    # creating object's instance
    harry = employee("harry", "Developer")
    harry.info()
    harsh = employee("harsh", "HR")
    harsh.info()


main()
