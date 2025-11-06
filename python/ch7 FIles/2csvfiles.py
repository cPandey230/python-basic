import csv


def create():
    with open("example.csv", "w") as obj:
        fobj = csv.writer(obj)
        fobj.writerow(["ROLL", "NAME", "TOTAL MARKS"])
        while True:
            roll = int(input("Enter the Roll no. : "))
            name = input("Enter the name :")
            total = int(input("Enter the total marks : "))
            record = [roll, name, total]
            fobj.writerow(record)
            ch = int(input("1.Enter more records\n2.Exit\n3.Enter your choice"))
            if ch == 2:
                break


def display():
    with open("example.csv", "r") as obj:
        fobj = csv.reader(obj)
        for i in obj:
            print(i)


def search():
    with open("example.csv", "r") as obj:
        fobj = csv.reader(obj)
        next(fobj)
        for i in fobj:
            if i[2] >= 99:
                print(i)


# create()
display()
search()
