# Practical 3 : Implement Backpropagation Algorithm  

# (Cell 1)
import numpy as np 
# Input and output data 
X = np.array([[2, 9], [1, 5], [3, 6]], dtype=float) 
y = np.array([[92], [86], [89]], dtype=float)

# (Cell 2)
# Normalize data 
X = X / np.max(X, axis = 0) 
y = y / 100 

# (Cell 3)
# Sigmoid function 
def sigmoid(x): 
    return 1 / (1 + np.exp(-x)) 

# (Cell 4)
# Derivative of sigmoid 
def sigmoid_derivative(x): 
    return x * (1 - x) 

# (Cell 5)
# Parameters 
epochs = 7000 
lr = 0.1 

# (Cell 6)
# Weights and biases 
wh = np.random.uniform(size=(2, 3)) 
bh = np.random.uniform(size=(1, 3)) 
wo = np.random.uniform(size=(3, 1)) 
bo = np.random.uniform(size=(1, 1)) 

# (Cell 7)
# Backpropagation 
for i in range(epochs): 
    # Forward propagation 
    hidden = sigmoid(np.dot(X, wh) + bh) 
    output = sigmoid(np.dot(hidden, wo) + bo) 
    
    # Calculate error 
    error = y - output 
    
    # Output layer gradient 
    output_gradient = error * sigmoid_derivative(output) 
    
    # Hidden layer gradient 
    hidden_error = output_gradient.dot(wo.T) 
    hidden_gradient = hidden_error * sigmoid_derivative(hidden)
    # Update weights 
    wo += hidden.T.dot(output_gradient) * lr 
    wh += X.T.dot(hidden_gradient) * lr 

# (Cell 8)
# Display results 
print("Input:") 
print(X) 
print("\nActual Output:") 
print(y) 
print("\nPredicted Output:") 
print(output) 