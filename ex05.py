def f(x):
    print("Em f: x =", x)

def g(y):
    print("Em g: y =", y)
    if y > 0:
        f(y - 1)

f(10)
g(12)
g(0)
