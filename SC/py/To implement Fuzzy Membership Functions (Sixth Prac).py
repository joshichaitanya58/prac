# Practical 6 : To implement Fuzzy Membership Functions (triangular, trapezoidal, gbell, PI, Gamma, Gaussian) 


# (Cell 1)
import numpy as np
import matplotlib.pyplot as plt


# (Cell 2) Triangular Membership Function
x = np.arange(0, 11, 1)

a = 3
b = 6
c = 10

y = np.maximum(np.minimum((x-a)/(b-a), (c-x)/(c-b)), 0)

plt.plot(x, y)
plt.xlabel("Triangular MF, p = [3, 6, 10]")
plt.ylabel("Fuzziness")
plt.ylim(-0.05, 1.05)
plt.title("Triangular Membership Function")
plt.grid()
plt.show()



# (Cell 3) Trapezoidal Membership Function
x = np.arange(0, 11, 1)

a = 1
b = 4
c = 6
d = 9

y = np.maximum(np.minimum(np.minimum((x-a)/(b-a), 1), (d-x)/(d-c)), 0)

plt.plot(x, y)
plt.xlabel("Trapezoidal MF, p = [1, 4, 6, 9]")
plt.ylabel("Fuzziness")
plt.ylim(-0.05, 1.05)
plt.title("Trapezoidal Membership Function")
plt.grid()
plt.show()



# (Cell 4) Gaussian Membership Function
x = np.arange(0, 10.1, 0.1)

sigma = 1
mean = 4

y = np.exp(-((x-mean)**2) / (2*sigma**2))

plt.plot(x, y)
plt.xlabel("Gaussian MF, p = [1, 4]")
plt.ylabel("Fuzziness")
plt.ylim(-0.05, 1.05)
plt.title("Gaussian Membership Function")
plt.grid()
plt.show()



# (Cell 5) Gaussian 2 Membership Function
x = np.arange(0, 10.1, 0.1)

sigma1 = 1
mean1 = 4

sigma2 = 5
mean2 = 7

y1 = np.exp(-((x-mean1)**2) / (2*sigma1**2))
y2 = np.exp(-((x-mean2)**2) / (2*sigma2**2))

y = np.where(x < mean1, y1,
             np.where(x > mean2, y2, 1))

plt.plot(x, y)
plt.xlabel("Gaussian 2 MF, p = [1, 4, 5, 7]")
plt.ylabel("Fuzziness")
plt.ylim(-0.05, 1.05)
plt.title("Gaussian 2 Membership Function")
plt.grid()
plt.show()



# (Cell 6) Bell Membership Function (GBell)
x = np.arange(0, 10.1, 0.1)

a = 1
b = 4
c = 7

y = 1 / (1 + np.abs((x-c)/a)**(2*b))

plt.plot(x, y)
plt.xlabel("Bell MF, p = [1, 4, 7]")
plt.ylabel("Fuzziness")
plt.ylim(-0.05, 1.05)
plt.title("Bell Membership Function")
plt.grid()
plt.show()



# (Cell 7) Sigmoidal Membership Function
x = np.arange(0, 10.1, 0.1)

a = 1
c = 4

y = 1 / (1 + np.exp(-a*(x-c)))

plt.plot(x, y)
plt.xlabel("Sigmoidal MF, p = [1, 4]")
plt.ylabel("Fuzziness")
plt.ylim(-0.05, 1.05)
plt.title("Sigmoidal Membership Function")
plt.grid()
plt.show()



# (Cell 8) Sigmoidal 2 Membership Function (SMF)
x = np.arange(0, 10.1, 0.1)

a = 1
b = 4

mid = (a+b)/2

y = np.zeros(len(x))

for i in range(len(x)):
    if x[i] <= a:
        y[i] = 0
    elif x[i] <= mid:
        y[i] = 2 * ((x[i]-a)/(b-a))**2
    elif x[i] < b:
        y[i] = 1 - 2 * ((x[i]-b)/(b-a))**2
    else:
        y[i] = 1

plt.plot(x, y)
plt.xlabel("Sigmoidal 2 MF, p = [1, 4]")
plt.ylabel("Fuzziness")
plt.ylim(-0.05, 1.05)
plt.title("Sigmoidal 2 Membership Function")
plt.grid()
plt.show()



# (Cell 9) PI Membership Function
x = np.arange(0, 10.1, 0.1)

a = 1
b = 4
c = 5
d = 7

def smf(x, a, b):
    mid = (a+b)/2

    if x <= a:
        return 0
    elif x <= mid:
        return 2 * ((x-a)/(b-a))**2
    elif x < b:
        return 1 - 2 * ((x-b)/(b-a))**2
    else:
        return 1

y = []

for value in x:
    left = smf(value, a, b)
    right = smf(value, c, d)

    y.append(left * (1-right))

plt.plot(x, y)
plt.xlabel("PI MF, p = [1, 4, 5, 7]")
plt.ylabel("Fuzziness")
plt.title("PI Membership Function")
plt.grid()
plt.show()

