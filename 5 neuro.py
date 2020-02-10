# Пример расхождения нейронного спуска.
# Так происходит из-за слишком большого inp, маленький вес корректируется слишком агресивно
# из-за огромного взодного значения.
# Следующим примером, я покажу как это исправить(по сути прошлым, alpha сглаживает).
weight = 0.5
inp = 2
goal_pred = 0.8

for i in range(20):
    pred = inp * weight
    error = (pred-goal_pred) ** 2
    delta = (pred-goal_pred) * inp
    weight -= delta
    print(f"{i + 1}; Error:{error} Prediction: {pred} Weight: {weight}")
