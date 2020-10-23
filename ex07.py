def f(x):
    if x > 0:
        g(x - 1)
    print("Em f: x =", x)

def g(y):
    if y > 0:
        f(y - 1)
    print("Em g: y =", y)

f(8)
