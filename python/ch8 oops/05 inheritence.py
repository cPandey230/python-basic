class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def showDetails(self):
        print(f"\nThe name of the employee is {self.name} whose id is {self.id} ")


class Programmer(Employee):
    def showLang(self):
        print(f"The default language of programmer is python ")


def main():
    e = Employee("Rohan Das", 400)
    e.showDetails()

    e1 = Programmer("Chandan", 100)
    e1.showDetails()
    e1.showLang()


if __name__ == "__main__":
    main()
