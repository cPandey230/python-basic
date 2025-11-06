# private
# class Employee:
#     def __init__(self):
#         self.__name = "Hary"


# def main():
#     e = Employee()
#     # print(e.__name) cannot be access directly
#     print(e._Employee__name)
#     print(e.__dir__())


# if __name__ == "__main__":
#     main()


# protected
class Student:
    def __init__(self):
        self._name = "Harry"

    def _funName(self):
        return "CodeWithHarry"


class Subject(Student):
    pass


def main():
    obj1 = Student()
    obj2 = Subject()
    print(obj1._name)
    print(obj1._funName())

    print(obj2._name)
    print(obj2._funName())


if __name__ == "__main__":
    main()
