# Q1. A profiler is a tool that helps in analyzing a program's performance.
# It does it by measuring the execution time of various parts of the code and making an execution profile for the given program

# Q2. Profiling's main purpose is to find the part of the code where a programs spends its most time by relative analysis of the whole program. 
# It uses modules like cProfile and profile.
# On the other hand, benchmarking is measuring the elapsed time for only a specific part of interest in the program.
#It uses timeit module. 

# Q3.
import timeit
import cProfile

def sub_function(n):
   #sub function that calculates the factorial of n
   if n == 0:
        return 1
   else:
        return n * sub_function(n-1)

def test_function():
    data = []
    for i in range(10):
        data.append(sub_function(i))
    return data

def third_function():
    # third function that calculates the square of the numbers from 0 to 999
   return [i**2 for i in range(100000000)]

test_function()
third_function()

if __name__ == "__main__":
    cProfile.run('test_function()', sort='cumulative')  # Profile the test_function
    cProfile.run('third_function()', sort='cumulative')  # Profile the third_function
    
    #using 'n' as 5 as an example for profiling
    n_value = 5  
    globals_dict = globals()
    locals_dict = {'n': n_value}
    cProfile.runctx('sub_function(n)', globals_dict, locals_dict, sort='cumulative')
    
# Q4.
# third_function takes the most amount of time. It has 1 ncall, however the range for i is 
# quite large. Therefore, it takes 5.916 seconds and the total time, percall and cumulative 
# time are all the same since its's only been called once



 
