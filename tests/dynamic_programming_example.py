#  Fibonacci Example
#  1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987
#  bc of the picture :
#  The time it takes increases nearly exponentially
#  Order 2 to the Power of N
#  O(2^n)
#  --> Store all unique sub- Calculations
#  --> MEMOIZATION  ( NOT memorization)
import time

i = 0


def fib(n):
    global i
    i += 1
    if n == 1 or n == 2:
        result = 1
    else:
        result = fib(n-1) + fib(n-2)
    return result


def better_fib(n, memo):
    global i
    i += 1
    if memo[n] is not None:
        return memo[n]
    if n == 1 or n == 2:
        result = 1
    else:
        result = better_fib(n-1, memo) + better_fib(n-2, memo)
    memo[n] = result
    return result


x = 38
start_time = time.time()
print("Bad Function: ")
print("The", x, "-th fibonacci number is:", fib(x))
print("Called function:", i, "times.")
print("Program took ", time.time() - start_time, " to run.\n")
i = 0
start_time2 = time.time()
print("Optimized with memoization:")
memo = [None] * (x+1)
print("The", x, "-th fibonacci number is:", better_fib(x, memo))
print("Called function:", i, "times.")
print("Program took ", time.time() - start_time2, " to run.")
