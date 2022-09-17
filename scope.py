a = [1,2,3]

def f1():
    a[0] = 5 #global scope
    print(a)

def f2():
    a = 50 #local scope
    print(a)

f1()
f2()
print(a)

#1)Two types of scope - Global & Local
#2)Python functions create local scopes
