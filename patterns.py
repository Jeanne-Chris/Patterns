def diamond(n):

    w = 0
    v = n

    for h in range(n):
        for i in range(n-h):
            print(end=" ")
        for j in range(h):
            print("+", end=" ")
        print()

    for q in range(v):
        for r in range(w):
            print(end=" ")
        for s in range(v):
            print("+", end=" ")
        print()
        
        w = w + 1
        v = v - 1


# end def diamond()
diamond(10)
