# 과제 2번 코드란

def solution(intervals):
    inter_l = len(intervals)
    va = []

    for a in range(inter_l):

        if intervals[a][0] < intervals[a][1]:
            for b in range(intervals[a][0], intervals[a][1] + 1):
                va.append(b)

        else:
            for b in range(intervals[a][1], intervals[a][0] + 1):
                va.append(b)

    va = list(set(va))
    va.sort()

    d = va[len(va) - 1]
    mn = None

    data = []
    sub = []
    p = len(va) - 1  # va[] 안에 넣으면 오류 발생
    for i in range(va[0], va[p] + 1):

        if i in va:
            if mn == None:
                mn = i
                sub.append(i)
            else:
                continue

        else:
            if mn != None:
                sub.append(i - 1)
                mn = None
                data.append(sub)
                sub = []
            else:
                continue
    else:
        sub.append(va[p])
        data.append(sub)

    return data


intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
print(solution(intervals))