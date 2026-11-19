# Practical 1
# Aim: To implement simple logic network using MP neuron model.


# Implement AND Gate (Cell 1)

x1 = [0, 0, 1, 1]
x2 = [0, 1, 0, 1]
w1 = [1, 1, 1, 1]
w2 = [1, 1, 1, 1]
t = 2
print("x1 x2 w1 w2 t Output")
for i in range(len(x1)):
    if (x1[i] * w1[i] + x2[i] * w2[i]) >= t:
        print(x1[i], x2[i], w1[i], w2[i], t, 1)
    else:
        print(x1[i], x2[i], w1[i], w2[i], t, 0)




# Implement OR Gate (Cell 2)
x1 = [0, 0, 1, 1]
x2 = [0, 1, 0, 1]
w1 = [1, 1, 1, 1]
w2 = [1, 1, 1, 1]
t = 1
print("x1 x2 w1 w2 t O")
for i in range(len(x1)):
    if (x1[i] * w1[i] + x2[i] * w2[i]) >= t:
        print(x1[i], x2[i], w1[i], w2[i], t, 1)
    else:
        print(x1[i], x2[i], w1[i], w2[i], t, 0)





# XOR Section (Cell 3)
x1 = [0, 0, 1, 1]
x2 = [0, 1, 0, 1]
w1 = [1, -1, -1, 1]
w2 = [1, 1, -1, -1]
t1 = 0
t2 = 1
print("x1 x2 w1 w2 t1 t2 Output")
for i in range(len(x1)):
    net1 = x1[i] * w1[i] + x2[i] * w2[i]
    o1 = 1 if net1 >= t1 else 0
    net2 = o1 * w1[i] + (1 - o1) * w2[i]
    o = 1 if net2 >= t2 else 0
    print(x1[i], x2[i], w1[i], w2[i], t1, t2, o)





# NOR Gate using MP Neuron (Cell 4)
x1 = [0, 0, 1, 1]
x2 = [0, 1, 0, 1]
w1 = [1, 1, 1, 1]
w2 = [1, 1, 1, 1]
t = -1
print("x1 x2 w1 w2 t Output")
for i in range(len(x1)):
	if (x1[i] * w1[i] + x2[i] * w2[i]) >= t:
		print(x1[i], x2[i], w1[i], w2[i], t, 1)
	else:
		print(x1[i], x2[i], w1[i], w2[i], t, 0)