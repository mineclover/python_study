# 과제 3번 코드란

def solution(N, start, end, counts):
    answer = 0
    T = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    data = list(str(start))
    cur = 0
    for f in range(len(counts)):
        if f == 0:
            index = T.index(data[-1])
        dir = index + f

        if dir - cur >= N:
            cur += dir
            c = -2
            while True:
                try:
                    d = T.index(data[c])
                except IndexError:
                    data.insert(0, T[1])
                    d = T.index(str(data[c]))
                if d + 1 >= N:
                    data[c] = T[0]
                    c -= 1
                else:
                    d = T.index(data[c])
                    data[c] = T[d]
                    break
        data = data[:-1]
        data.append(T[dir - cur])

        if ''.join(data) == counts[f]:
            pass
        else:
            answer += 1
    return answer


N, start, end, counts = 14, 9, 'd', ['9', 'a', 'c', 'd', 'e']

print(solution(N, start, end, counts))

N, start, end, counts = 62, 'v', 'z', ['Z', 'y', 'x', 'z']

print(solution(N, start, end, counts))

#고작 36 줄쓰는데 2일 걸려..
