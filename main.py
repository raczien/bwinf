n = 6
w = [10, 50, 100, 500, 1000, 5000]
n_w = [3, 2, 3, 3, 3, 1]
arr = [10, 10, 10, 50, 50, 100, 100, 100, 500, 500, 500, 1000, 1000, 1000, 5000]


def test():
    i = 10
    while i <= 500:
        c = min(w, key=lambda x: abs(x-i))
        #print(c)
        if i in arr or (i % c <= n_w[w.index(c)]):
            print("Element: ", i, "(c = ", c, ")")
        else:
            print(i)
            closest = min(w, key=lambda x: abs(x-i))
            #check(closest, i)

        i += 10


def check(c, i):
    print(c, " - ", i)
    print(w.index(c))
    if (i % min(w, key=lambda x: abs(x-i)) <= n_w[w.index(c)]):
        print("NICE", c, " MIT ", i, "*********************")
    a = 1


if __name__ == '__main__':
    test()