def solution(board, moves):
    answer = 0
    baguni = []
    for i in moves:
        for j in board:
            if (j[i-1] != 0 & True):
                baguni.append(j[i-1])
                j[i-1] = 0
                break
    return calculate (baguni, 0)
def calculate(baguni, total):
    for i in range(1, baguni.__len__()):
        if i < baguni.__len__() and baguni[i-1] == baguni[i]:
            del baguni[i-1]
            del baguni[i-1]
            return calculate(baguni, total + 2)
    return total
