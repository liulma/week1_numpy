import numpy as np

# Exercise 8: 2D array with shape(3,4) containing random floats between 1 and 100. Find minimum and maximum values in the entire array. Round down to nearest integer

random_floats = np.random.rand(12)

# Scale the floats to be between 1 and 100
scaled_floats = random_floats * 99 + 1  # Multiply by (100 - 1) and add 1

random_2d = np.ndarray(shape=(3, 4), dtype=float, buffer=np.array(scaled_floats))

max_value = np.max(random_2d)
min_value = np.min(random_2d)
rounded_integers = np.floor(random_2d)

print("Original array:")
print(random_2d)
print()
print(f"Max value: {max_value}")
print(f"Min value: {min_value}")
print()
print("Array rounded down to integers:")
print(rounded_integers)