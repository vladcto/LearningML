# Градиетный спуск с нескольками входными данными и ожним выводом
def neural_network(_inp, _weights):
    assert (len(_inp) == len(_weights))
    sum = 0
    for i in range(0, len(_inp)):
        sum = sum + _inp[i] * _weights[i]
    return sum


inp = [8.5, 0.65, 1.2]
win_or_lose_binary = 1
weights = [0.2, 0.5, 0.5]
# Если изменить альфа-коэф. могут начаться сильные расхождения
alpha = 0.01

for iter in range(200):
    pred = neural_network(inp, weights)
    error = (pred - win_or_lose_binary) ** 2
    delta = (pred - win_or_lose_binary) * alpha
    print(f"{iter + 1}: Error: {error}  Pred:{pred}")

    for i in range(0, len(inp)):
        weights[i] = weights[i] - delta * inp[i]
        print(f"\tWeight[{i}] = {weights[i]}")
