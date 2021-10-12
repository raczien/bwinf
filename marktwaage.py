
def print_subset_sum(w, s, m):
    subset = []
    for i, x in enumerate(w):
        if calculate_sub_sums(w, i + 1, s - x, m) > 0:
            subset.append(x)
            s -= x
    return subset


def calculate_sub_sums(weights, i, sum, memo):
    if i >= len(weights):
        return 1 if sum == 0 else 0

    if (i, sum) not in memo:
        count = calculate_sub_sums(weights, i + 1, sum, memo)
        count += calculate_sub_sums(weights, i + 1, sum - weights[i], memo)
        memo[(i, sum)] = count
    return memo[(i, sum)]


def weight_balance(arr):
    counter = 0
    for i in range(len(arr)):
        temp = arr.copy()
        temp[i] *= -1
        for k in range(len(arr)):
            temp[k] *= -1
            print(temp)
            counter += 1
    print(counter)


def calculate(weight_object):
    weights = weight_object.all_weights
    wanted = 10
    memo = dict()
    none = []
    while wanted <= 10000:
        breaker = False
        if calculate_sub_sums(weight_object.all_weights, 0, wanted, memo) == 0:
            inverse_memo = dict()
            counter = 0
            for i in range(len(weights)):
                temp = weights.copy()
                temp[i] *= -1
                for k in range(len(weights)):
                    temp[k] *= -1
                    if print_subset_sum(temp, wanted, inverse_memo):
                        print(print_subset_sum(temp, wanted, inverse_memo), " for: ", wanted)
                        breaker = True
                        break
                    counter += 1
                if breaker:
                    break
            if not breaker:
                none.append(wanted)
        else:
            print(print_subset_sum(weights, wanted, memo), " for: ", wanted)
        wanted += 10

    print("No Sum for: ", none)
    print("Amount: ", len(none))
