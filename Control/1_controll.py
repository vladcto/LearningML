goal_pred = 0.8
input = 1
weight = 0.7
alpha = 0.1

for i in range(100):
    pred = input*weight
    error = (pred - goal_pred)**2
    delta_change =(pred - goal_pred)*input*alpha
    print(f"{i}: Error: {error}  Pred: {pred} Delta: {delta_change}")
    weight-=delta_change