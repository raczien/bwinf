def find_missing_number_with_subtraction(num_arr, pair_sum):
    for i in range(len(num_arr) - 1):
        for j in range(i + 1, len(num_arr)):
            if num_arr[i] - num_arr[j] == pair_sum:
                return num_arr[i], num_arr[j]



# Driver Code
num_arr = [100,80,70,60,50,30,20,10]
pair_sum = 40

# Function call inside print
a, b = find_missing_number_with_subtraction(num_arr, pair_sum)
print(a, b)