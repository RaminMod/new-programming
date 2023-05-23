#!/usr/bin/env python3.9

"""
Student: Ramin Modaresi
Mail: Ramin.modaresi.6800@student.uu.se
Reviewed by: 
Reviewed date:
"""

from person import Person  
from numba import njit  
from time import perf_counter as pc  
import matplotlib.pyplot as plt  

# Recursive Fibonacci function in pure Python
def fib_py(n):
    if n <= 1:
        return n
    else:
        return fib_py(n - 1) + fib_py(n - 2)

# Decorated Fibonacci function using Numba for performance optimization
@njit
def fib_numba(n):
    if n <= 1:
        return n
    else:
        return fib_numba(n - 1) + fib_numba(n - 2)

def main():
    # Lists to store timings for each function
    t_py = []
    t_numba = []
    t_cpp = []

    # Range of Fibonacci numbers to compute timings for
    x = range(30, 46)

    # Compute Fibonacci numbers and measure time for each function
    for n in x:
        # Compute time for pure Python function
        start = pc()
        fib_py(n)
        end = pc()
        t_py.append(end - start)

        # Compute time for Numba-optimized function
        start = pc()
        fib_numba(n)
        end = pc()
        t_numba.append(end - start)

        # Compute time for C++ function using Person class
        f = Person(n)
        start = pc()
        f.fib()
        end = pc()
        t_cpp.append(end - start)

    # Compute Fibonacci number for n = 47 using C++ code and Numba
    f = Person(47)
    start = pc()
    f.fib()
    end = pc()
    cpp_time = end - start

    start = pc()
    fib_numba(47)
    end = pc()
    numba_time = end - start

    # Plot the timings
    plt.plot(x, t_py, label="Python")
    plt.plot(x, t_numba, label="Numba")
    plt.plot(x, t_cpp, label="C++")
    plt.xlabel("n (Fibonacci Number)")
    plt.ylabel("Time (seconds)")
    plt.legend()
    plt.savefig("timings.png")
    plt.close()

    # Plot the timings for n = 20 to 30
    t_py_small = []
    t_numba_small = []
    x_small = range(20, 31)
    for n in x_small:
        start = pc()
        fib_py(n)
        end = pc()
        t_py_small.append(end - start)

        start = pc()
        fib_numba(n)
        end = pc()
        t_numba_small.append(end - start)

    plt.plot(x_small, t_py_small, label="Python")
    plt.plot(x_small, t_numba_small, label="Numba")
    plt.xlabel("n (Fibonacci Number)")
    plt.ylabel("Time (seconds)")
    plt.legend()
    plt.savefig("timings_small.png")
    plt.close()

    # Print the results for Fibonacci with n = 47
    print("Result for Fibonacci with n = 47:")
    print("C++ code (Person class):", cpp_time, "seconds")
    print("Numba:", numba_time, "seconds")

if __name__ == '__main__':
    main()
