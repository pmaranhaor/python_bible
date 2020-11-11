a = 250

def f1():
    a = 100         #local scope
    print(a)

def f2():
    a = 50
    print(a)

f1()
f2()
print(a)
