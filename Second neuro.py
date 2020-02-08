# Исправление ошибок : Горячо/Холодно
weight = 0.5
inp = 0.5
goal_pred = 0.8

step = 0.001

for i in range(1100):
    pred = inp * weight
    # Средняя квадратичная ошибки
    # Используеться, для показания промаха(положительна)
    # Как в футболе, промах на метр от ворот (не -1 метр)
    # Преуменьшение маленьких и увелечение больших ошибок
    error = (goal_pred - pred) ** 2

    print(f"{i + 1}; Error:{error} Prediction: {pred} Weight: {weight}")

    up_error = (goal_pred - inp * (weight + step)) ** 2
    down_error = (goal_pred - inp * (weight - step)) ** 2

    if up_error < down_error:
        weight = weight + step
    else:
        weight = weight - step
