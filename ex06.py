def f(x):
    print("Em f: x =", x)
    if x > 0:
        g(x - 1)

def g(y):
    print("Em g: y =", y)
    if y > 0:
        f(y - 1)

f(7)
