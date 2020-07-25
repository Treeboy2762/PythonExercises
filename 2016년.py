def solution(a, b):
    answer = ''
    count = 0
    for i in range (1,a):
        print(i)
        if i in [1, 3, 5, 7, 8, 10, 12] :
            count = count + 31
        elif i in [4, 6, 9, 11]:
            count = count + 30
        elif i == 2:
            count = count + 29
    count = count + b
    print(count)
    count = (count-1)%7
    if count == 0:
        answer = 'FRI'
    elif count == 1:
        answer = 'SAT'
    elif count == 2:
        answer = 'SUN'
    elif count == 3:
        answer = 'MON'
    elif count == 4:
        answer = 'TUE'
    elif count == 5:
        answer = 'WED'
    elif count == 6:
        answer = 'THU'
    else:
        answer = "FRI"
    return answer
