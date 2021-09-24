import time

#  TODO: hier vll memo integrieren
def subsetsum(array, num, memo):
    if num == 0 or num < 1 or len(array) == 0:
        return None

    # if memo[num] is not None:
    #   return memo[n]

    else:
        if array[0] == num:
            r = [array[0]]
            return r
        else:
            with_v = subsetsum(array[1:], (num - array[0]), memo)
            if with_v:
                r = [array[0]] + with_v
                return r
            else:
                r = subsetsum(array[1:], num, memo)
                return r


memo = dict()
start_time = time.time()
set = [10, 10, 10, 50, 50, 100, 100, 100, 500, 500, 500, 1000, 1000, 1000, 5000]
#set = [11, 99480, 99511, 299836, 299836, 599761, 4497786, 4497786, 4497786, 1499171, 10499654, 10499654, 10499654, 41999427, 94499810, 94499810, 94499810, 283501867, 661499326, 661499326, 661499326, 1984505261]
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
