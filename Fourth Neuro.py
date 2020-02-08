# Сеть очень схожа с 3 сетью
# Можно заметить её преимущества если посмотреть на вывод
weight = 0.5
inp = 0.5
goal_pred = 10000
# alpha "сглаживает" работу нейронной сети (задает ее работу)
# тем самым не будет слишком "агресивных" коректировок веса
alpha = 0.001

step = 0.001

for i in range(1001):
    pred = inp * weight
    error = (goal_pred - pred) ** 2
    delta = (goal_pred - pred) * inp
    weight += delta * alpha
    print(f"{i + 1}; Error:{error} Prediction: {pred} Weight: {weight}")
