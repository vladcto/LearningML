# Упрощенный градиентный спуск
weight = 0
inp = 1.1
goal_pred = 0.8

for i in range(100):
    pred = inp * weight
    error = (goal_pred - pred) ** 2
    # goal_pred - pred - называется чистой ошибка
    # Показывает разницу и направление в которую увеличть
    #
    # Масштабирование, обращаем знак и остановка
    # Остановка значит, что при inp = 0 не будет изменяться weight
    # Логично, ведь как ни крути , все равно error будет та же
    # Обращение знака нужно для коректности при inp < 0
    # Вес вверх - прогноз вниз , при inp < 0
    # Масштабировние - логично
    direction_change = (goal_pred - pred) * inp
    weight += direction_change
    print(f"{i + 1}; Error:{error} Prediction: {pred} Weight: {weight}")
