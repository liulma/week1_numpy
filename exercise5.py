import numpy as np

# Exercise 5: 3x3 NumPy array with random integers between 1 and 100

arr_random = np.random.randint(1, 100, size=9)

arr_random_2d = np.ndarray(shape=(3, 3), dtype=np.int32, buffer=np.array(arr_random))

print(arr_random_2d)