import time

# set = [10, 50, 100, 100, 100, 500, 500, 500, 1000, 1000, 1000, 5000]
# 150
def subsetsum(array, num, memo):
    if num == 0 or num < 1 or len(array) == 0:
        return None

    else:
        if array[0] == num:
            result = [array[0]]
            return result

        else:
            new_start = subsetsum(array[1:], (num - array[0]), memo)
            if new_start:
                result = [array[0]] + new_start
                return result
            else:
                result = subsetsum(array[1:], num, memo)
                return result


memo = dict()
start_time = time.time()
set = sorted([-10, 10, 10, 50, 50, -100, 100, 100, 500, 500, 500, 1000, 1000, 1000, 5000])
i = 10
none = []

while i <= 10000:
    result = subsetsum(set, i, memo)
    if result is None:
        none.append(i)
    else:
        print(result, " for: ", i)
    i += 10

print(none)
print(len(none))
print(memo)
print("Program took ", time.time() - start_time, " to run.")