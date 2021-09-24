import time


def f(weights, i, wanted, memo):
    if i >= len(weights):
        #return 1 if wanted == 0 else 0

        if wanted == 0:
            return 1
        else:
            return 0

    if (i, wanted) not in memo:  # <-- Check if value has not been calculated.
        count = f(weights, i + 1, wanted, memo)
        count += f(weights, i + 1, wanted - weights[i], memo)
        memo[(i, wanted)] = count  # <-- Memoize calculated result.
        if memo[(i, wanted)] > 0:
            print("i = ", i, "wanted: ", wanted, "memo_count", memo[(i, wanted)])

    return memo[(i, wanted)]  # <-- Return memoized value.


def h(weights, i, wanted, memo):
    print(i, wanted)
    if i >= len(weights):
        if wanted == 0:
            return 1
        else:
            return 0
    return memo[(i, wanted)]  # <-- Return memoized value.


def solution(weights, wanted, memo):
    subset = []
    for i, x in enumerate(weights):
        print("i: ", i, "weight(x): ", x)
        if h(weights, i + 1, wanted - x, memo) > 0:
            print(h(weights, i + 1, wanted - x, memo))
            subset.append(x)
            wanted -= x
    return subset


start_time = time.time()
weights = [10, 10, 10, 50, 50, 100, 100, 100, 500, 500, 500, 1000, 1000, 1000, 5000]
# -5000, -1000, -500, -100, -50, -10,
wanted = 5730  # 10
memo = dict()
none = []

if f(weights, 0, wanted, memo) == 0:
    none.append(wanted)
else:
    print(solution(weights, wanted, memo), " for: ", wanted)

#while wanted <= 10000:
#    if f(weights, 0, wanted, memo) == 0:
#        none.append(wanted)
#    else:
#        print(g(weights, wanted, memo), " for: ", wanted)
#    wanted += 10
print("No Sum for: ", none)
print("Ammount: ", len(none))
print("Program took ", time.time() - start_time, " to run.")
