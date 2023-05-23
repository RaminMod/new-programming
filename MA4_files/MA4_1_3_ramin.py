import random
import math
import concurrent.futures
import time

def is_inside(point):
    squared_sum = sum(x ** 2 for x in point)
    return squared_sum <= 1

def approximate_volume(n, d):
    points = [[random.uniform(-1, 1) for _ in range(d)] for _ in range(n)]
    inside_points = list(filter(is_inside, points))
    return (2 ** d) * (len(inside_points) / n)

def calculate_exact_volume(d):
    return math.pi ** (d/2) / math.gamma(d/2 + 1)

def run_sequential(n, d):
    start_time = time.perf_counter()
    volume = approximate_volume(n, d)
    end_time = time.perf_counter()
    execution_time = end_time - start_time
    return volume, execution_time

def run_parallel(n, d, num_processes):
    start_time = time.perf_counter()
    with concurrent.futures.ProcessPoolExecutor(max_workers=num_processes) as executor:
        volumes = executor.map(approximate_volume, [n // num_processes] * num_processes, [d] * num_processes)
        volume = sum(volumes)
    end_time = time.perf_counter()
    execution_time = end_time - start_time
    return volume, execution_time

test_cases = [
    (10000000, 11),
    (1000000, 11)
]
num_processes = 10

for test_case in test_cases:
    volume_sequential, execution_time_sequential = run_sequential(*test_case)
    volume_parallel, execution_time_parallel = run_parallel(*test_case, num_processes)

    print("-" * 20)
    print(f"Sequential execution time: {execution_time_sequential} seconds")
    print(f"Approximation for V(1) with (n, d) = {test_case}: {volume_sequential}")
    print(f"Parallel execution time: {execution_time_parallel} seconds")
    print(f"Approximation for V(1) with (n, d) = {test_case} and {num_processes} processes: {volume_parallel}")
    print("-" * 20)