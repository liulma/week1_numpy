import numpy as np

# Exercise 3: Random array of 25 integers between -100 and 100. Calculate mean

random_array = np.random.randint(-100, 100, size=25)

mean_value = np.mean(random_array)

print("Array:")
print(random_array)
print()
print("Mean of array:")
print(mean_value)