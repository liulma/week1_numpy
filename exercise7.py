import numpy as np

# Exercise 7: 1D NumPy array with 10 random floats between -5 and 5. Calculate mean and round each float to two decimal places

random_floats = np.random.rand(10)

# Scale and shift to the range -5 to 5
scaled_floats = random_floats * 10 - 5  # Multiply by (5 - (-5)) and subtract 5

my_array = np.array(scaled_floats)
median_value = np.median(my_array)
rounded_decimals = np.round(my_array, decimals=2)

print("Original array:")
print(my_array)
print()
print("Median value of array:")
print(median_value)
print()
print("Array rounded down to two decimals:")
print(rounded_decimals)