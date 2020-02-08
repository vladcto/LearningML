def element_wise_multiplication(vec_a, vec_b):
    assert len(vec_a) == len(vec_b)
    result_vector = []
    for i in range(len(vec_a)):
        result_vector.append(vec_a * vec_b)
    return result_vector


def element_wise_addition(vec_a, vec_b):
    assert len(vec_a) == len(vec_b)
    result_vector = []
    for i in range(len(vec_a)):
        result_vector.append(vec_a + vec_b)
    return result_vector


def vector_sum(vec_a):
    result_vector = 0
    for i in range(len(vec_a)):
        result_vector += vec_a[i]
    return result_vector


def vector_average(vec_a):
    return vector_sum(vec_a) / len(vec_a)
