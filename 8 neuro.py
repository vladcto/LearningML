import numpy as np;

colors_lights = np.array([[1, 0, 1],
                          [0, 1, 1],
                          [0, 0, 1],
                          [1, 1, 1],
                          [0, 1, 1],
                          [1, 0, 1]])
go = np.array([0, 1, 0, 1, 1, 0])
weights = np.array([0.5, 0.2, 0.1])
alpha = 0.01

for iter in range(100):
    error_for_all_lights = 0

    for i in range(6):
        pred = colors_lights[i].dot(weights);
        delta = (pred - go[i]) * alpha
        weights = weights - delta * colors_lights[i]
        error_for_all_lights += delta ** 2

    print(error_for_all_lights)