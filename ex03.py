def f1():
    print("Executando f1")

def f2():
    print("Executando f2")
    f1()

def f3():
    print("Executando f3")
    f2()

f3()
