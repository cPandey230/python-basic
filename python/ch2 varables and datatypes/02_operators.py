from ast import operator
from platform import python_branch


a = 200 
b = 100

# Airthmetic opertaion in python
print("a+b=", a+b)
print("a-b=", a-b)
print("a*b=", a*b)
print("a/b=", a/b)

#assignment operators in python
print("Demonstring assignment opertors in python")
print("1.adding")
c = 5
d = 10

print(c,d)
c += 5
d += 5
print(c,d)

print("2.subtracting")
print(c,d)
c -= 5
d -=5
print(c,d)

# Comparision operator in python
print("demonstrating Comparison Operators in Python")
e = 6
f = 9

print(e==f)
print(e>f)
print(e<f)
print(e!=f)

# Logical Operators in python
print("Demonstrating Logical Operators in Python")

print(e==f and e<f)
print(e==f or e<f)
print(not(e>f))