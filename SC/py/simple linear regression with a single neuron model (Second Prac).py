# Practical 2
# Aim: To implement simple linear regression with a single neuron model.


# (Cell 1)
import sys
print(sys.executable)

# (Cell 2)
import sys
!{sys.executable} -m pip install scikit-learn



# (Cell 3)
import sklearn
print("scikit-learn installed successfully!")
print("Version:", sklearn.__version__)

# (Cell 4)
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# (Cell 5)
# Read CSV file
data = pd.read_csv(r"Salary_Data.csv")
# Display dataset
print(data)

# (Cell 6)
x = data.iloc[:, 0].values.reshape(-1, 1)
y = data.iloc[:, 1].values.reshape(-1, 1)
lin_reg = LinearRegression()
lin_reg.fit(X, y)
y_pred = lin_reg.predict(X)

# (Cell 7)
plt.scatter(X, y)
plt.plot(X, y_pred, color="red")
plt.show()

# (Cell 8)
# using single neuron model
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt

# (Cell 9)
np.random.seed(101)
tf.random.set_seed(101)

x = np.linspace(0, 25, 100)
y = np.linspace(0, 25, 100)
# adding noise to the random linear data
x += np.random.uniform(-4, 4, 100)
y += np.random.uniform(-4, 4, 100)
n = len(x)

# (Cell 10)
# plot of training data
plt.scatter(x, y)
plt.xlabel("x")
plt.ylabel("y")
plt.title("Training Data")
plt.show()

# (Cell 11)
import tensorflow as tf
import numpy as np
tf.compat.v1.disable_eager_execution()

# (Cell 12)
x = tf.compat.v1.placeholder("float")
y = tf.compat.v1.placeholder("float")

# (Cell 13)
w = tf.Variable(np.random.randn(), name="W")
b = tf.Variable(np.random.randn(), name="b")

# (Cell 14)
learning_rate = 0.01
training_epochs = 1000

# (Cell 15)
# Hypothesis
y_pred = tf.add(tf.multiply(x, w), b)
# Mean Squared Error cost function
cost = tf.reduce_sum(tf.pow(y_pred - y, 2)) / (2 * n)
# Gradient Descent optimizer
optimizer = tf.compat.v1.train.GradientDescentOptimizer(learning_rate).minimize(cost)
# Global variables initializer
init = tf.compat.v1.global_variables_initializer()

# (Cell 16)
import tensorflow as tf
import numpy as np
# Use tf.compat.v1 to maintain compatibility with older code
tf.compat.v1.disable_eager_execution()
# Input using tf.compat.v1.placeholder for compatibility
x = tf.compat.v1.placeholder("float")
y = tf.compat.v1.placeholder("float")
# Variables for weight and bias
w = tf.Variable(np.random.randn(), name="W")
b = tf.Variable(np.random.randn(), name="b")
# Learning rate and number of training epochs
learning_rate = 0.01
training_epochs = 1000
# Hypothesis
y_pred = tf.add(tf.multiply(x, w), b)
# Assuming 'n' is defined somewhere
n = 100  # You will need to define n
# Mean squared error cost function
cost = tf.reduce_sum(tf.pow(y_pred - y, 2)) / (2 * n)
# Gradient descent optimizer
optimizer = tf.compat.v1.train.GradientDescentOptimizer(learning_rate).minimize(cost)
# Global variables initializer
init = tf.compat.v1.global_variables_initializer()
# Sample training data

# (Cell 17)
# Replace this with your actual data
x_data = np.linspace(0, 10, 100)
y_data = 2 * x_data + 1 + np.random.randn(100)
# Starting the TensorFlow session
with tf.compat.v1.Session() as sess:
    # Initializing the variables
    sess.run(init)
    # Iterating through all the epochs
    for epoch in range(training_epochs):
        # Fitting the training data
        for (_x, _y) in zip(x_data, y_data):
            sess.run(optimizer, feed_dict={x: _x, y: _y})
        # Displaying the result after every 50 epochs
        if (epoch + 1) % 50 == 0:
            # Calculating the cost of every epoch
            c = sess.run(cost, feed_dict={x: x_data, y: y_data})
            print("Epoch", (epoch + 1), ": cost =", c, "w =", sess.run(w), "b =", sess.run(b))
    # Storing necessary values to be used outside the session
    training_cost = sess.run(cost, feed_dict={x: x_data, y: y_data})
    weight = sess.run(w)
    bias = sess.run(b)

# (Cell 18)
predictions = weight * x_data + bias
print("Training cost =", training_cost, "Weight =", weight, "bias =", bias, '\n')

# (Cell 19)
plt.plot(x_data, y_data, 'ro', label='Original data')
plt.plot(x_data, predictions, label='Fitted line')
plt.title('Linear Regression Result')
plt.legend()
plt.show()

