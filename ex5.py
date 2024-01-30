import random
import timeit
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

# Linear Search
def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

# Binary Search
def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0

    while low <= high:
        mid = (high + low) // 2
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid
    return -1

sizes = [1000, 2000, 4000, 8000, 16000, 32000]
linear_times = []
binary_times = []

for size in sizes:
    arr = sorted([random.randint(1, size) for _ in range(size)])
    x = random.choice(arr)

    start_time = timeit.default_timer()
    for _ in range(100):
        linear_search(arr, x)
    end_time = timeit.default_timer()
    linear_times.append((end_time - start_time) / 100)

    start_time = timeit.default_timer()
    for _ in range(100):
        binary_search(arr, x)
    end_time = timeit.default_timer()
    binary_times.append((end_time - start_time) / 100)


# Linear function for curve fitting
def linear_func(x, a, b):
    return a * x + b

# Logarithmic function for curve fitting
def log_func(x, a, b):
    return a * np.log(x) + b

# Fit the data
popt_linear, _ = curve_fit(linear_func, sizes, linear_times)
popt_log, _ = curve_fit(log_func, sizes, binary_times)

# Generate x values
x_values = np.linspace(min(sizes), max(sizes), 100)

# Generate y values for fitted functions
y_values_linear = linear_func(x_values, *popt_linear)
y_values_log = log_func(x_values, *popt_log)

# Plot the data
plt.figure(figsize=(10, 6))
plt.plot(sizes, linear_times, 'o', label='Linear Search')
plt.plot(x_values, y_values_linear, '-', label='Fit: a*x + b')
plt.plot(sizes, binary_times, 'o', label='Binary Search')
plt.plot(x_values, y_values_log, '-', label='Fit: a*log(x) + b')
plt.legend()
plt.show()

#The code is fitting two types of functions to some data points: a linear function and a logarithmic function. These functions are used to model the time complexity of linear search and binary search algorithms, respectively.

#The linear function is of the form y = a*x + b, where a and b are parameters that the curve_fit function is trying to optimize. a is the slope of the line, and b is the y-intercept. This function is used to model the time complexity of the linear search, which is O(n).

#The logarithmic function is of the form y = a*log(x) + b, where a and b are parameters that the curve_fit function is trying to optimize. a is the coefficient of the logarithm, and b is a constant term. This function is used to model the time complexity of the binary search, which is O(log n).

#The results are expected if the linear_times data shows a linear relationship with sizes, and binary_times data shows a logarithmic relationship with sizes. This is because linear search has a time complexity of O(n), and binary search has a time complexity of O(log n).

#The fitted functions should closely follow the data points if the data accurately represents the time complexities of these algorithms. Since the fitted functions closely follow the data points, we can conclude that the data accurately represents the time complexities of these algorithms.