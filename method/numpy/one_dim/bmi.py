import numpy as np

heights = np.array([1.83, 1.76, 1.69, 1.86, 1.77, 1.73])
weights = np.array([86, 74,  59, 95, 80, 68])

BMI1 = weights / heights**2
BMI2 = weights / pow(heights, 2)

print(BMI1)
print(BMI2)
print(BMI1.round(1))