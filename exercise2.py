import numpy as np

# Exercise 2: 1D NumPy array with 15 random floats between 1 and 10. Calculate median and round to nearest integer

random_floats = np.random.rand(15)

# Scale the floats to be between 1 and 10
scaled_floats = random_floats * 9 + 1  # Multiply by (10 - 1) and add 1

# Create the 1D NumPy array
my_array = np.array(scaled_floats)

print("Original array:")
print(my_array)
print()

median_value = np.median(my_array)
rounded_array = np.round(my_array)

print("Median value:")
print(median_value)
print()
print("Rounded array:")
print(rounded_array)