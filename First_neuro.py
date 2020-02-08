# Пример нейронной сети
# Очень простой
# Учился по книге "Грокаем Глубокое Обучение"
import numpy as np

weihgts = np.array([0.1, 0.2, 0])


def neural_network(input, weights):
    pred = input.dot(weights)
    return pred


toes = np.array([8.5, 9.5, 9.9, 9])
wr = np.array([0.5, 1.5, 3.5, 6])
fans = np.array([1, 23, 4, 5])

inp = np.array([toes[0], wr[0], fans[0]])
pred = neural_network(inp, weihgts)
print(pred)
