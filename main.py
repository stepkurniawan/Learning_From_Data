# This is a python script for Perceptron by Stephen Kurniawan
#     All right reserved

import numpy as np


# pseudo codes
# w0 = 0, b0 = 0, k0 = 0
w = []  # weight vector
b = []  # bias
k = 0  # how many repetition

w.append([0, 0])
print("w is ", w[0])

b.append(0)
print("b is ", b[0])

x = ((1, 1), (2, 3), (-1, -1), (-2, -2), (3, 4))  # using tuple for unchangeable data
# calling tuple is like calling list
print("x is ", x[0])
y = (1, 1, -1, -1, 1)
print("y0 is ", y[0])

# ---------------------------
# Using numpy
# --------------------------
x_np = np.array([[1, 2], [3, 2], [2, 1], [3, 3]])
print("x_np head is ", x_np[0], x_np[1])
y_np = np.array([-1, 1, -1, 1])
b_np = np.array(b)

R = 5
learning_rate = 1

x_np_length = len(x_np)

# repeat
while True:
    all_correct = True
    for i in range(x_np_length):
        # if there is a mistake
        print("wk", w[k])
        print("dot product", np.dot(w[k], x_np[i]))
        print("b", b[i])
        if y_np[i] * np.dot(w[k], x_np[i]) + b[i] <= 0:
            w.append(
                w[k] + learning_rate * y_np[i] * x_np[i]
            )
            b.append(
                b[k] + learning_rate * y_np[i] * R ^ 2
            )
            k = k + 1
            all_correct = False
        else:
            all_correct = True
    if all_correct:
        break

print("the weight vector is ", w[k])
