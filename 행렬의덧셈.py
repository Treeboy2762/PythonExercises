import numpy as np
def solution(arr1, arr2):
    answer = []
    for i, j in zip(arr1, arr2):
        answer.append(np.add(np.array(i), np.array(j)).tolist())
    return answer
