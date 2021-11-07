import initial_constants as const


# read values from the dictionary and returns the subset that sums up to the given number (for console output)
def get_subset_sum(w, s, m):
    subset = []
    for i, x in enumerate(w):
        if s == 32000:
            print(calculate_sub_sums(w, i + 1, s - x, m))
        if calculate_sub_sums(w, i + 1, s - x, m) > 0:
            subset.append(x)
            s -= x
    return subset


# check if a difference of two found values exist (e.g. 40 not found, but 100 and 60 found, then return 100-60 if valid)
def find_missing_number_with_subtraction(found_weights, pair_sum, memo, weights, missing_dict):
    found_weights.sort(reverse=True)
    valid_arrays = []
    for i in range(len(found_weights) - 1):
        for j in range(i + 1, len(found_weights)):
            if found_weights[i] - found_weights[j] == pair_sum:
                #print("Pair: ", found_weights[i], found_weights[j])
                if found_weights[i] in missing_dict:
                    array1 = missing_dict[found_weights[i]]
                else:
                    array1 = get_subset_sum(weights, found_weights[i], memo)

                if found_weights[j] in missing_dict:
                    array2 = missing_dict[found_weights[j]]
                else:
                    array2 = get_subset_sum(weights, found_weights[j], memo)

                joined_arrays = array1 + array2
                joined_arrays.sort()
                is_valid = True
                for element in set(joined_arrays):
                    if joined_arrays.count(element) > weights.count(element):
                        is_valid = False
                        break

                if is_valid:
                    array2 = [-x for x in array2]
                    valid_array = array1 + array2
                    valid_array.sort()
                    valid_array_copy = valid_array.copy()
                    for index, x in enumerate(valid_array_copy):
                        if x < 0:
                            if -x in valid_array:
                                valid_array.remove(-x)
                                valid_array.remove(x)
                    if valid_array not in valid_arrays:
                        valid_arrays.append(valid_array)
    shortest_valid = min(valid_arrays, key=len, default=[])
    return shortest_valid


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
    return lst[min(range(len(lst)), key=lambda i: abs(lst[i]-num), default=[0])]


# dynamic algorithm for the "Subset Sum - Problem"
def calculate(weight_object):
    weights = weight_object.all_weights
    wanted = 10
    memo = dict()
    not_found_values = []
    found_values = []
    calculated_values = []
    while wanted <= const.end_value:
        if calculate_sub_sums(weight_object.all_weights, 0, wanted, memo) == 0:
            not_found_values.append(wanted)
        wanted += 10

    missing_dict = dict()

    for k in range(10, const.end_value+1, 10):
        if get_subset_sum(weights, k, memo):
            found_values.append(k)

    not_found_copy = not_found_values.copy()
    for v in not_found_copy:
        found = find_missing_number_with_subtraction(found_values, v, memo, weights, missing_dict)
        if found:
            missing_dict[v] = found
            not_found_values.remove(v)
            found_values.append(v)
            calculated_values.append(v)

    # print all calculated values
    wanted_weight = 10
    while wanted_weight <= const.end_value:
        if wanted_weight in not_found_values:
            print(wanted_weight, get_blanks_for_pretty_print(wanted_weight), "No value found. Closest value: ", closest_number(found_values, wanted_weight))
        elif wanted_weight in missing_dict:
            print(wanted_weight, get_blanks_for_pretty_print(wanted_weight), missing_dict[wanted_weight])
        else:
            print(wanted_weight, get_blanks_for_pretty_print(wanted_weight), get_subset_sum(weights, wanted_weight, memo))
        wanted_weight += 10

    print("Amount of not found values: ", len(not_found_values))
