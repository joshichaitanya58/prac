# Practical 4 : Implement and test RBF network   

# (Cell 1)
import numpy as np 
from scipy.spatial.distance import cdist 
from sklearn.cluster import KMeans 
from sklearn.metrics import mean_squared_error 


# (Cell 2)
# Generate sample data
np.random.seed(0)
X = np.random.rand(100, 2)
y = np.sin(X[:, 0]) + np.cos(X[:, 1])
print("Input shape:", X.shape)
print("Output shape:", y.shape)


# (Cell 3)
# Find RBF centers using K-Means
kmeans = KMeans(
    n_clusters=10,
    random_state=209,
    n_init=10
)
kmeans.fit(X)
centers = kmeans.cluster_centers_
print("RBF Centers:")
print(centers)


# (Cell 4)
# Calculate maximum distance between centers
d_max = np.max(cdist(centers, centers))
# Calculate sigma
sigma = d_max / np.sqrt(2 * len(centers))
print("Maximum distance (d_max):", d_max)
print("Sigma:", sigma)


# (Cell 5)
# Calculate RBF layer output
R = np.exp(
    -cdist(X, centers) ** 2 / (2 * sigma ** 2)
)
print("RBF Layer Output Shape:", R.shape)
print("\nFirst 5 rows:")
print(R[:5])


# (Cell 6)
# Calculate output weights
W = np.linalg.pinv(R).dot(y)
print("Output Weights:")
print(W)


# (Cell 7)
# Make predictions
y_pred = R.dot(W)
print("First 5 predicted values:")
print(y_pred[:5])


# (Cell 8)
# Display sample inputs and outputs
print("Sample Input        Actual Output        Predicted Output")
print("----------------------------------------------------------")
for i in range(5):
    print(
        X[i],
        "     ",
        round(y[i], 6),
        "          ",
        round(y_pred[i], 6)
    )


# (Cell 9)
# Calculate Mean Squared Error
mse = mean_squared_error(y, y_pred)
print("\nMean Squared Error:", mse)


# (Cell 10)
print("RBF Neural Network Results")
print("--------------------------")
print("Number of samples :", len(X))
print("Number of centers :", len(centers))
print("Sigma             :", sigma)
print("MSE               :", mse)