# 과제 3번 코드란


def solution(array, commands):
    answer = []
    for a in range(len(commands)):
        b = array[commands[a][0]-1:commands[a][1]]
        b.sort()
        answer.append((b[commands[a][2]-1]))
    return answer

array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
print(solution(array, commands))