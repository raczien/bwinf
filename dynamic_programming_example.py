#  Fibonacci Example
#  1,1,2,3,5,8....
#  bc of the picture :
#  The time it takes increases nearly exponentially
#  Order 2 to the Power of N
#  O(2^n)
#  --> Store all unique sub- Calculations
#  --> MEMOIZATION  ( NOT memorization)
import time


def fib(n):
    if n == 1 or n == 2:
        result = 1
    else:
        result = fib(n-1) + fib(n-2)
    return result


def better_fib(n, memo):
    if memo[n] is not None:
        return memo[n]
    if n == 1 or n == 2:
        result = 1
    else:
        result = better_fib(n-1, memo) + better_fib(n-2, memo)
    memo[n] = result
    return result


x = 39
start_time = time.time()
print(fib(x))
print("Program took ", time.time() - start_time, " to run.")

start_time2 = time.time()
memo = [None] * (x+1)
print(better_fib(x, memo))
print("Program took ", time.time() - start_time2, " to run.")