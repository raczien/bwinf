from contextlib import redirect_stdout


def f(v, i, S, memo):
    if i >= len(v): return 1 if S == 0 else 0
    if (i, S) not in memo:  # <-- Check if value has not been calculated.
        count = f(v, i + 1, S, memo)
        count += f(v, i + 1, S - v[i], memo)
        memo[(i, S)] = count  # <-- Memoize calculated result.
    return memo[(i, S)]     # <-- Return memoized value.


def g(v, S, memo):
    subset = []
    for i, x in enumerate(v):
        # Check if there is still a solution if we include v[i]
        if f(v, i + 1, S - x, memo) > 0:
            subset.append(x)
            S -= x
    return subset


def test():
    v = [10, 10, 40, 40, 60, 70, 100, 200, 400, 800, 1000, 1000, 4000, 6000]
    #sum = 10
    memo = dict()
    for sum in range(10, 10000, 10):
        if f(v, 0, sum, memo) == 0:

            print("There are no valid subsets.")
        else:
            print(g(v, sum, memo))
    print(len(memo))


if __name__ == '__main__':
    test()
