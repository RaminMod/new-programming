import random
import math


def is_inside(point):
    squared_sum = sum(x ** 2 for x in point)
    return squared_sum <= 1

def approximate_volume(n, d):
    points = [[random.uniform(-1, 1) for _ in range(d)] for _ in range(n)]
    inside_points = list(filter(is_inside, points))
    return (2 ** d) * (len(inside_points) / n)

def calculate_exact_volume(d):
    return math.pi ** (d/2) / math.gamma(d/2 + 1)

test_cases = [(100000, 2), (100000, 11)]

results = [(approximate_volume(n, d), calculate_exact_volume(d)) for n, d in test_cases]

for (approximation, exact), (n, d) in zip(results, test_cases):
    print("-" * 20)
    print(f"Approximation for V(1) with (n, d) = ({n}, {d}): {approximation}")
    print(f"Exact value for V(1) with d = {d}: {exact}")
    print("-" * 20)
