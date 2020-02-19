# Несколько входов и выходов
def scal_sum(matrix, matrix2):
    sum = 0
    for i in range(len(matrix)):
        sum = matrix[i] + matrix2[i]
    return sum


# Да здравствует Спагети КОД!!!!
input = [0.5, 0.3, 0.2]
goal_pred = [1, 0, 2]
weight = [[0.5, 2, 1],
          [0.3, 0.7, 2],
          [1, 4, 1]]
alpha = 0.1
alpha = 0.1
pred = [0, 0, 0]

for iter in range(0, 100):
    print(f"{iter}")

    pred[0] = scal_sum(input, weight[0])
    pred[1] = scal_sum(input, weight[1])
    pred[2] = scal_sum(input, weight[2])

    # Изменяю веса первого выхода
    delta = (pred[0] - goal_pred[0]) * alpha
    for i in range(0, 3):
        weight[0][i] = weight[0][i] - delta * input[0]

    delta = (pred[1] - goal_pred[1]) * alpha
    for i in range(0, 3):
        weight[1][i] = weight[1][i] - delta * input[1]

    delta = (pred[2] - goal_pred[2]) * alpha
    for i in range(0, 3):
        weight[2][i] = weight[2][i] - delta * input[2]

    print(f"\t 1: W1 :{weight[0][0]} W2 :{weight[0][1]} W3 :{weight[0][2]} Pred: {pred[0]} GoalPred: {goal_pred[0]}")
    print(f"\t 2: W1 :{weight[1][0]} W2 :{weight[1][1]} W3 :{weight[1][2]} Pred: {pred[1]} GoalPred: {goal_pred[1]}")
    print(f"\t 3: W1 :{weight[2][0]} W2 :{weight[2][1]} W3 :{weight[2][2]} Pred: {pred[2]} GoalPred: {goal_pred[2]}")
