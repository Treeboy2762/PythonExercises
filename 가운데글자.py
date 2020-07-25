def solution(s):
    answer = ''
    length = len(s)
    print((length/2), (length/2+1))
    if length % 2 == 1:
        return s[int((length/2-0.5)):int((length/2+0.5))]
    else:
        return s[int(length/2-1):int(length/2+1)]
