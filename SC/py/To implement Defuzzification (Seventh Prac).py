# Practical 7 : To implement Defuzzification (Max-membership principle, centroid method, weighted average method.)


# (Cell 1) 
import numpy as np
import matplotlib.pyplot as plt


# (Cell 2) Define Membership Functions
x = np.arange(0, 11, 0.1)

# First triangular membership function
mf1 = np.maximum(1 - np.abs(x - 3) / 3, 0)

# Second triangular membership function
mf2 = np.maximum(1 - np.abs(x - 7) / 3, 0)

# Combine membership functions
y1 = np.minimum(mf1, 0.5)
y2 = np.minimum(mf2, 0.8)

y = np.maximum(y1, y2)

plt.plot(x, y)
plt.xlabel("Output")
plt.ylabel("Membership Value")
plt.title("Combined Membership Function")
plt.grid()
plt.show()



# (Cell 3) Max-Membership Principle
max_value = np.max(y)

index = np.argmax(y)

result = x[index]

print("Maximum Membership Value:", max_value)
print("Defuzzified Output:", result)

plt.plot(x, y)
plt.axvline(result, color='red', linestyle='--')
plt.title("Max Membership Method")
plt.xlabel("Output")
plt.ylabel("Membership Value")
plt.grid()
plt.show()



# (Cell 4) Centroid Method
numerator = np.sum(x * y)
denominator = np.sum(y)

result = numerator / denominator

print("Defuzzified Output:", result)

plt.plot(x, y)
plt.axvline(result, color='red', linestyle='--')
plt.title("Centroid Method")
plt.xlabel("Output")
plt.ylabel("Membership Value")
plt.grid()
plt.show()


# (Cell 5) Weighted Average Method
# Maximum membership values
weights = [0.5, 0.8]

# Centre points of membership functions
values = [3, 7]

# Calculate weighted average
result = np.sum(np.array(weights) * np.array(values)) / np.sum(weights)

print("Defuzzified Output:", result)



# (Cell 6) Display All Results Together
print("Defuzzification Results")

print("------------------------------")

print("Max Membership:", x[np.argmax(y)])

print("Centroid Method:", np.sum(x * y) / np.sum(y))

print("Weighted Average:", result)