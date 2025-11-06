f_name = "newfile1.text"
f_mode = "r"

f = open(f_name, f_mode)

data = f.read()
print(data)
print(f.tell())
# data = "this is lecture of jenny on file handling\n"
# f.write(data)
# print(f.tell())

f.close()
