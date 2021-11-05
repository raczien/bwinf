import initial_constants as const


# read values from the dictionary and returns the subset that sums up to the given number (for console output)
def get_subset_sum(w, s, m):
    subset = []
    for i, x in enumerate(w):
        if calculate_sub_sums(w, i + 1, s - x, m) > 0:
            subset.append(x)
            s -= x
    return subset


# calculates all possible calculations (permutations) from an array and saves all distinct calculations to a dictionary
def calculate_sub_sums(weights, index, sum, memo):
    if index >= len(weights):
        return 1 if sum == 0 else 0

    if (index, sum) not in memo:
        count = calculate_sub_sums(weights, index + 1, sum, memo)
        count += calculate_sub_sums(weights, index + 1, sum - weights[index], memo)
        memo[(index, sum)] = count
    return memo[(index, sum)]


# for beautified console printing - returns a substring with specific amount of blanks
def get_blanks_for_pretty_print(num):
    if num < 10:
        return "    :"
    elif num < 100:
        return "   :"
    elif num < 1000:
        return "  :"
    else:
        return " :"


# returns the closest value given in a dictionary compared to a given number
def closest_number(lst, num):
    return lst[min(range(len(lst)), key=lambda i: abs(lst[i]-num))]


# dynamic algorithm for the "Subset Sum - Problem"
def calculate(weight_object):
    weights = weight_object.all_weights
    wanted = 10
    memo = dict()
    not_found_values = []
    found_values = []
    while wanted <= 10000:
        if calculate_sub_sums(weight_object.all_weights, 0, wanted, memo) == 0:
            not_found_values.append(wanted)
        wanted += 10

    missing_dict = dict()

    # calculate missing values with permutation arrays, where all possible combinations have the times (-1) adaptation
    value_missing = False
    for k in range(10, 10000, 10):
        if not get_subset_sum(weights, k, memo):
            value_missing = True
        else:
            found_values.append(k)

    if const.search_for_missing_with_permutation:
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
                found_values.append(missing)

    # print all calculated values
    wanted_weight = 10
    while wanted_weight <= 10000:
        if wanted_weight in missing_dict:
            print(wanted_weight, get_blanks_for_pretty_print(wanted_weight), missing_dict[wanted_weight])
        elif not get_subset_sum(weights, wanted_weight, memo):
            print(wanted_weight, get_blanks_for_pretty_print(wanted_weight), "No value found. Closest value: ", closest_number(found_values, wanted_weight))
        else:
            print(wanted_weight, get_blanks_for_pretty_print(wanted_weight), get_subset_sum(weights, wanted_weight, memo))
        wanted_weight += 10

