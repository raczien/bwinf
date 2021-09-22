import time


def subsetsum(array, num):
    if num == 0 or num < 1:
        return None
    elif len(array) == 0:
        return None
    else:
        if array[0] == num:
            return [array[0]]
        else:
            with_v = subsetsum(array[1:], (num - array[0]))
            if with_v:
                return [array[0]] + with_v
            else:
                return subsetsum(array[1:], num)


start_time = time.time()
set = [10, 10, 10, 50, 50, 100, 100, 100, 500, 500, 500, 1000, 1000, 1000, 5000]
#set = [11, 99480, 99511, 299836, 299836, 599761, 4497786, 4497786, 4497786, 1499171, 10499654, 10499654, 10499654, 41999427, 94499810, 94499810, 94499810, 283501867, 661499326, 661499326, 661499326, 1984505261]
i = 10
none = []

while i <= 10000:
    result = subsetsum(set, i)
    if result is None:
        none.append(i)
    else:
        print(result, " for: ", i)
    i += 10

print(none)
print(len(none))

print("Program took ", time.time() - start_time, " to run.")
