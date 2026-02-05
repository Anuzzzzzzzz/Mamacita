x = 1
def f():
    global x
    x+=2
    return x
x = x + f()
print(x)


