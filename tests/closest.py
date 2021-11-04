def closest_number(lst, num):
    return lst[min(range(len(lst)), key=lambda i: abs(lst[i]-num))]


lst = [3.64, 5.2, 9.42, 9.35, 8.5, 8]
K = 9.1
print(closest_number(lst, K))