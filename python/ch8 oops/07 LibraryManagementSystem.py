# #libmansystem

# class lib:
#     nofbooks =1
#     books = []

#     def check:
#     # no. of books == lenth of list of books
#     #error books doesn't much


class Library:
    numBooks = 5
    books = ["Business", "Economics", "Accounts", "Maths", "English"]

    def show(self):
        print(f"There are {self.numBooks} books are available in library :")
        for index, book in enumerate(self.books, start=1):
            print(f"    {index} : {book}")
        print("\n")

    def check(self):
        nbook = len(self.books)
        if self.numBooks == nbook:
            print("The Given length of books matches")
        else:
            print("The Given length of books does not matches")


def main():
    obj1 = Library()
    obj1.show()
    obj1.check()


if __name__ == "__main__":
    main()
