#Question 1
#This code defines a recursive function func that computes the nth number in the Fibonacci sequence. 
#The Fibonacci sequence is a series of numbers where a number is the addition of the last two numbers, starting with 0 and 1.

#Question 2
#This is not an example of a divide-and-conquer algorithm. 
#Divide-and-conquer algorithms work by recursively breaking down a problem into two or more sub-problems of the same or related type, until these become simple enough to be solved directly. 
#The solutions to the sub-problems are then combined to give a solution to the original problem. 
#In contrast, this function works by simply adding the results of two previous function calls, and does not divide the problem into independent sub-problems.

#Question 3
#The time complexity of this algorithm is exponential, specifically O(2^n), because each function call branches into two new calls (except for the base cases).
#This results in a binary tree of function calls, with a depth of n. The number of nodes in such a binary tree is proportional to 2^n.

#Question 4
#This code defines a recursive function func that computes the nth number in the Fibonacci sequence.

def fib_memo(n, memo={}):
    if n in memo:
        return memo[n]
    elif n <= 1:
        return n
    else:
        result = fib_memo(n-1, memo) + fib_memo(n-2, memo)
        memo[n] = result
        return result
    
#Question 5
#The time complexity of this optimized algorithm is O(n). This is because with memoization, each Fibonacci number is computed only once, and then stored in the memo dictionary for future reference.
    
#Question 6
import time
import matplotlib.pyplot as plt

def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib(n-1) + fib(n-2)

times_orig = []
times_memo = []

for i in range(36):
    start = time.time()
    fib(i)
    end = time.time()
    times_orig.append(end - start)

    start = time.time()
    fib_memo(i)
    end = time.time()
    times_memo.append(end - start)

plt.figure()
plt.plot(times_orig, label='Original')
plt.plot(times_memo, label='Memoized')
plt.legend()
plt.savefig('ex1.6.1.jpg')

plt.figure()
plt.plot(times_orig, label='Original')
plt.legend()
plt.savefig('ex1.6.2.jpg')