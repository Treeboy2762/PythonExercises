def solution(arr):
    answer = [arr[0]]
    for num, i in enumerate(arr[1:]):
        if i != arr[num]: answer.append(i)
    return answer
