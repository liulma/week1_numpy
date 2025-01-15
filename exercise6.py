import numpy as np

# Exercise 6: 2D NumPy array with shape(4,5) and random integers between 10 and 50. Calculate median of array
arr_random = np.ndarray(shape=(4, 5), dtype=np.int32, buffer=np.random.randint(10, 51, size=20))

median_value = np.median(arr_random)

print("Random array:")
print(arr_random)
print("Median value:")
print(median_value)