import time


def f(weights, i, wanted, memo):
    if i >= len(weights):
        return 1 if wanted == 0 else 0

    if (i, wanted) not in memo:  # <-- Check if value has not been calculated.
        count = f(weights, i + 1, wanted, memo)
        count += f(weights, i + 1, wanted - weights[i], memo)
        memo[(i, wanted)] = count  # <-- Memoize calculated result.

    return memo[(i, wanted)]  # <-- Return memoized value.


def uu(weights, i, wanted, memo):
    print(i, " - ", wanted)
    print(memo)
    if i >= len(weights):
        return 1 if wanted == 0 else 0

    if (i, wanted) not in memo:  # <-- Check if value has not been calculated.
        count = f(weights, i + 1, wanted, memo)
        count += f(weights, i + 1, wanted - weights[i], memo)
        memo[(i, wanted)] = count  # <-- Memoize calculated result.

    return memo[(i, wanted)]  # <-- Return memoized value.


def g(weights, wanted, memo):
    print("v: ", weights)
    print("memo: ", memo)
    print(len(memo))
    subset = []
    for i, x in enumerate(weights):
        # Check if there is still a solution if we include v[i]
        if uu(weights, i + 1, wanted - x, memo) > 0:
            subset.append(x)
            wanted -= x
    return subset


start_time = time.time()
weights = [-10, -50, 10, 10, 10, 50, 50, 100, 100, 100, 500, 500, 500, 1000, 1000, 1000, 5000]
# -5000, -1000, -500, -100, -50, -10,
wanted = 1700  # 10
memo = dict()  # hashmap - comma-separated list of key: value pairs ex. {PAIR: i}
none = []

if f(weights, 0, wanted, memo) == 0:
    none.append(wanted)
else:
    print(g(weights, wanted, memo), " for: ", wanted)

#while wanted <= 10000:
#    if f(weights, 0, wanted, memo) == 0:
#        none.append(wanted)
#    else:
#        print(g(weights, wanted, memo), " for: ", wanted)
#    wanted += 10
print("No Sum for: ", none)
print("Ammount: ", len(none))
print("Program took ", time.time() - start_time, " to run.")
