import numpy as np

# Exercise 1: 1D NumPy array with 12 random integers between 5 and 50. Find minimum and maximun values

random_in_arr = np.random.randint(5, 50, size=12)

min_value = np.min(random_in_arr)
max_value = np.max(random_in_arr)

print("Array:")
print(random_in_arr)
print("Minimum value in array:")
print(min_value)
print("Maximum value in array:")
print(max_value)