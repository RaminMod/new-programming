import random
import math
import matplotlib.pyplot as plt

def approximate_pi(n):
    nc = 0  # Counter for points inside the circle
    ns = 0  # Counter for points outside the circle

    points_in_circle = []  # List to store points inside the circle
    points_out_circle = []  # List to store points outside the circle

    for _ in range(n):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)

        if (x**2 + y**2) <= 1:
            nc += 1
            points_in_circle.append((x, y))
        else:
            ns += 1
            points_out_circle.append((x, y))

    pi_approx = 4 * nc / n

    # Create the scatter plot
    fig, ax = plt.subplots()
    ax.scatter(*zip(*points_in_circle), color='red', label='Inside Circle')
    ax.scatter(*zip(*points_out_circle), color='blue', label='Outside Circle')
    ax.set_aspect('equal')  # Set aspect ratio to maintain a circular shape
    ax.legend()

    # Set the title of the figure window to the filename
    plt.title(f"Figure: output_{n}.png")

    # Save the plot as a PNG file with the number of dots in the filename
    plt.savefig(f'output_{n}.png')
    plt.close()

    return nc, ns, pi_approx

# Test the program with different values of n
n_values = [1000, 10000, 100000]

approximations = []

for n in n_values:
    nc, ns, pi_approx = approximate_pi(n)
    approximations.append(pi_approx)
    error = abs(pi_approx - math.pi)
    print("-" * 50)
    print(f"Number of points = {n}")
    print(f"Approximation of π = {pi_approx}")
    print(f"Number of points inside the circle = {nc}")
    print(f"Number of points outside the circle = {ns}")
    print(f"Error = {error}")
    print("-" * 50)

print("Approximations of π:")
for i, n in enumerate(n_values):
    error = abs(approximations[i] - math.pi)
    print(f"n = {n}: pi = {approximations[i]}, Error = {error}")
print("-" * 50)
