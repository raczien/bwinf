import time


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


def weight_balance(arr, wanted, m):
    counter = 0
    for i in range(len(arr)):
        temp = arr.copy()
        temp[i] *= -1
        for k in range(len(arr)):
            temp[k] *= -1
            print(temp)
            calculate_sub_sums(temp, 0, wanted, m)
            counter += 1
    print(counter)


if __name__ == '__main__':
    x1 = [10, 10, 10, 50, 50, 100, 100, 100, 500, 500, 500, 1000, 1000, 1000, 5000]
    y = 40
    z = dict()
    calculate_sub_sums(x1, 0, y, z)
    print(print_subset_sum(x1, y, z), " for: ", y)
    print(z)
    print(len(z))
    print(weight_balance(x1, y, z))


def calculate(weight_object):
    weights = weight_object.all_weights
    wanted = 10
    memo = dict()
    none = []
    while wanted <= 10000: #TODO: hier irgendwie balance reinbringen
        if calculate_sub_sums(weight_object.all_weights, 0, wanted, memo) == 0:
            none.append(wanted)
        else:
            print(print_subset_sum(weights, wanted, memo), " for: ", wanted)
        wanted += 10

    print("No Sum for: ", none)
    print("Ammount: ", len(none))
