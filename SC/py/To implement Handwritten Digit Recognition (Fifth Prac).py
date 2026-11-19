# Practical 5 : To implement Handwritten Digit Recognition.   


# (Cell 1)
import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt
# Import MNIST dataset
from keras.datasets import mnist
# Load dataset
(x_train, y_train), (x_test, y_test) = mnist.load_data()
# Print number of training images
print("Number of training images:", len(x_train))
# Print number of testing images
print("Number of testing images:", len(x_test))
# Print shape of first training image
print("Shape of x_train[0]:", x_train[0].shape)


# (Cell 2)
plt.imshow(x_train[1])


# (Cell 3)
y_train[2]


# (Cell 4)
y_train[:5]


# (Cell 5)
x_train = x_train / 255
x_test = x_test / 255


# (Cell 6)
x_train_flattened = x_train.reshape(len(x_train), 28*28)
x_train_flattened.shape


# (Cell 7)
x_test_flattened = x_test.reshape(len(x_test), 28*28)
x_test_flattened.shape


# (Cell 8)
arr=np.array(x_train[0])


# (Cell 9)
x_train_flattened[0]


# (Cell 10)
model = keras.Sequential([
    keras.layers.Dense(10, input_shape=(784,), activation='sigmoid')
])
model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)
model.fit(
    x_train_flattened,
    y_train,
epochs=5
)


# (Cell 11)
model.evaluate(x_test_flattened, y_test)


# (Cell 12)
plt.matshow(x_test[0])


# (Cell 13)
y_pred = model.predict(x_test_flattened)
y_pred[0]


# (Cell 14)
y_pred_labels = [np.argmax(i) for i in y_pred]
y_pred_labels[:5]


# (Cell 15)
y_test[:5]


# (Cell 16)
import numpy as np
np.argmax(y_pred[10])


# (Cell 17)
conf_mat = tf.math.confusion_matrix(
labels=y_test,
predictions=y_pred_labels
)
conf_mat


# (Cell 18)
import seaborn as sn
import matplotlib.pyplot as plt
plt.figure(figsize=(10, 7))
sn.heatmap(conf_mat, annot=True, fmt='d')
plt.xlabel('Predicted')
plt.ylabel('Truth')
plt.show()


# (Cell 18)
model = keras.Sequential([
    keras.layers.Dense(100, input_shape=(784,), activation='relu'),
    keras.layers.Dense(10, activation='sigmoid')
])
model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)
model.fit(
    x_train_flattened,
    y_train,
    epochs=5
)


# (Cell 19)
model.evaluate(x_test_flattened, y_test)


# (Cell 20)
conf_mat = tf.math.confusion_matrix(
labels=y_test,
predictions=y_pred_labels
)
conf_mat


# (Cell 21)
import seaborn as sn
plt.figure(figsize=(10,7))
sn.heatmap(conf_mat, annot=True, fmt='d')
plt.xlabel('Predicted')
plt.ylabel('Truth')


# (Cell 22)
model = keras.Sequential([
keras.layers.Flatten(input_shape=(28, 28)),
keras.layers.Dense(100, activation='relu'),
keras.layers.Dense(10, activation='sigmoid')
])
model.compile(
optimizer='adam',
loss='sparse_categorical_crossentropy',
metrics=['accuracy']
)
model.fit(
x_train,
y_train,
epochs=5
)


