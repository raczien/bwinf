import initial_constants as const


def get_subset_sum(w, s, m):
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


def get_blanks(num):
    if num < 10:
        return "    :"
    elif num < 100:
        return "   :"
    elif num < 1000:
        return "  :"
    else:
        return " :"


def calculate(weight_object):
    weights = weight_object.all_weights
    wanted = 10
    memo = dict()
    not_found_values = []
    while wanted <= 10000:
        if calculate_sub_sums(weight_object.all_weights, 0, wanted, memo) == 0:
            not_found_values.append(wanted)
        wanted += 10

    missing_dict = dict()

    if const.search_for_missing_with_permutation:
        value_missing = False
        for k in range(10, 10000, 10):
            if not get_subset_sum(weights, k, memo):
                value_missing = True
                break

        if value_missing:
            for value in not_found_values:
                breaker = False
                for i in range(len(weights)):
                    if not breaker:
                        temp = weights.copy()
                        temp[i] *= -1
                        for k in range(len(weights)):
                            temp[k] *= -1
                            memo_permut = dict()

                            if calculate_sub_sums(temp, 0, value, memo_permut) != 0:
                                missing_dict[value] = get_subset_sum(temp, value, memo_permut)
                                breaker = True
                                break

        for missing in missing_dict:
            if missing in not_found_values:
                not_found_values.remove(missing)

    wanted_weight = 10
    while wanted_weight <= 10000:
        if wanted_weight in missing_dict:
            print(wanted_weight, get_blanks(wanted_weight), missing_dict[wanted_weight]) ##print(missing_dict[wanted_weight], " for: ", wanted_weight)
        else:
            print(wanted_weight, get_blanks(wanted_weight), get_subset_sum(weights, wanted_weight, memo))  ##print(get_subset_sum(weights, wanted_weight, memo), " for: ", wanted_weight)
        wanted_weight += 10

    print("No Sum for: ", not_found_values)
    print("Amount: ", len(not_found_values))


