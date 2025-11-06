class employee:
    name = "Null"
    ocupation = "Null"
    salary = 0

    def info(self):
        print(f"{self.name} is a {self.ocupation} his salary is {self.salary}")


def main():
    # creating object's instance
    harsh = employee()
    # setting variables values
    harsh.name = "Harsh"
    harsh.salary = 10000
    harsh.ocupation = "Junior developer"

    # invoking method of class
    print("called from info method")
    harsh.info()

    # calling varibles of class from main method
    print("called from main method")
    print(f"{harsh.name} is a {harsh.ocupation} his salary is {harsh.salary}")


main()
