def f(x, l=None):
    if l is None:
        l = []
    for i in range(x):
        l.append(i * i)
    #return l
    print(l)
f(2)
#[0, 1]
f(3, [0, 1, 2])
#[0, 1, 2, 0, 1, 4]
f(3)
#[0, 1, 4]